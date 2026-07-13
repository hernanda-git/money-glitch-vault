#!/usr/bin/env python3
"""fetch_sp2kp.py — Money Glitch Harga Pangan fetcher.

Fetches SP2KP price comparison from api-sp2kp.kemendag.go.id (Source A REST API),
falls back from "today" to the latest non-zero date when today isn't loaded yet,
writes sp2kp-YYYY-MM-DD.json + latest.json, appends INDEX.md, commits/pushes,
and prints a machine-readable report to stdout.

Self-evolution notes (CHANGELOG 2026-07-11):
  - Homepage map / browser fallback yields nothing -> always use Source A REST API.
  - latest-price-dates may flip between 401 and 200; when 401, probe the
    comparison endpoint for successive dates to find the latest non-zero one.
  - Comparison date param is snake_case `tanggal_pembanding` (NOT camelCase).
  - Today's data is often not yet loaded -> returns all-zero rows / -100%.
    Fall back to the previous available non-zero date.
"""

import json
import subprocess
import sys
from datetime import date, timedelta

API = "https://api-sp2kp.kemendag.go.id"
DATA_DIR = "/mnt/c/Workspace/money-glitch-vault/06-harga-pangan-papan/data"
VAULT = "/mnt/c/Workspace/money-glitch-vault"


def curl_json(url, post_form=None, timeout=30):
    cmd = ["curl", "-s", "-m", str(timeout), url, "-w", "\n%{http_code}"]
    if post_form:
        cmd += ["-X", "POST", "-H", "Content-Type: multipart/form-data"]
        for k, v in post_form.items():
            cmd += ["-F", f"{k}={v}"]
    out = subprocess.run(cmd, capture_output=True, text=True).stdout
    body, _, code = out.rpartition("\n")
    return json.loads(body), code


def probe_date(d: str, cmp_d: str):
    """Return (status, data) for a comparison request. status: 'ok'|'zero'|'err'."""
    try:
        obj, code = curl_json(
            f"{API}/report/api/average-price/generate-perbandingan-harga",
            {"tanggal": d, "tanggal_pembanding": cmp_d},
        )
    except Exception as e:  # noqa
        return "err", None
    if not isinstance(obj, dict) or obj.get("status") != "success":
        return "err", obj
    data = obj.get("data") or []
    # Non-zero if any item has harga > 0
    nonzero = any((it.get("harga") or 0) > 0 for it in data)
    return ("ok" if nonzero else "zero"), data


def build_rows(data, d1: str, d2: str):
    rows = []
    for it in data:
        name = it.get("variant_nama")
        unit = it.get("satuan_display")
        # National row
        chg = round((it.get("persen_perubahan") or 0), 2)
        rows.append({
            "date": d1,
            "commodity_name": name,
            "unit": unit,
            "region": "Nasional",
            "previous_price": it.get("harga_pembanding") or None,
            "current_price": it.get("harga") or None,
            "change_percent": chg,
        })
        # Regional sub-rows
        for rg in (it.get("region") or []):
            rchg = round((rg.get("persen_perubahan") or 0), 2)
            rows.append({
                "date": d1,
                "commodity_name": name,
                "unit": rg.get("satuan_display") or unit,
                "region": rg.get("region"),
                "previous_price": rg.get("harga_pembanding") or None,
                "current_price": rg.get("harga") or None,
                "change_percent": rchg,
            })
    return rows


def find_latest_date():
    """Find the latest date with non-zero data, falling back from today."""
    # Try latest-price-dates first
    try:
        obj, code = curl_json(f"{API}/report/api/latest-price-dates?tipe_komoditas_id=1")
        if code == "200" and obj.get("status") == "success":
            td = obj["data"]["tanggal"]
            cd = obj["data"]["tanggal_pembanding"]
            status, data = probe_date(td, cd)
            if status == "ok":
                return td, cd, data, "latest-price-dates"
    except Exception:  # noqa
        pass
    # Fallback: probe today and walk backwards up to 7 days
    today = date.today()
    for back in range(0, 8):
        d = (today - timedelta(days=back)).isoformat()
        for cback in range(1, 4):
            cd = (today - timedelta(days=back + cback)).isoformat()
            status, data = probe_date(d, cd)
            if status == "ok":
                return d, cd, data, f"probe[{back}]"
    return None, None, None, "none"


def main():
    d1, d2, data, src = find_latest_date()
    if d1 is None:
        # Log failure
        from datetime import datetime, timezone
        ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        with open(f"{DATA_DIR}/last-failure.log", "a", encoding="utf-8") as f:
            f.write(f"[{ts}] FAIL: no non-zero SP2KP data found in last 7 days (src={src})\n")
        print(json.dumps({"status": "failure", "reason": "no data"}, indent=2))
        return 1

    rows = build_rows(data, d1, d2)
    commodity_names = []
    seen = set()
    for r in rows:
        if r["region"] == "Nasional" and r["commodity_name"] not in seen:
            seen.add(r["commodity_name"])
            commodity_names.append(r["commodity_name"])

    payload = {
        "source": "api-sp2kp.kemendag.go.id (REST: report/api/average-price/generate-perbandingan-harga)",
        "fetched_at_utc": __import__("datetime").datetime.now(__import__("datetime").timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "data_date": d1,
        "previous_date": d2,
        "commodity_count": len(commodity_names),
        "row_count": len(rows),
        "commodity_names": commodity_names,
        "rows": rows,
    }

    # Compare to existing file for this date
    import os
    path = f"{DATA_DIR}/sp2kp-{d1}.json"
    existing = None
    if os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            existing = json.load(f)

    def norm(p):
        return json.dumps(p, sort_keys=True, ensure_ascii=False)

    changed = (existing is None) or (norm(existing) != norm(payload))

    if not changed:
        print(json.dumps({
            "status": "noop", "date": d1, "commodities": len(commodity_names),
            "rows": len(rows), "note": "data already captured, identical; skipping write/commit",
        }, indent=2))
        return 0

    # Write files
    with open(path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
        f.write("\n")
    with open(f"{DATA_DIR}/latest.json", "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
        f.write("\n")

    # INDEX.md
    idx_line = f"- [{d1}] SP2KP - {len(commodity_names)} commodities x {len(set(r['region'] for r in rows))} regions"
    idx_path = f"{DATA_DIR}/INDEX.md"
    have = ""
    if os.path.exists(idx_path):
        with open(idx_path, encoding="utf-8") as f:
            have = f.read()
    if idx_line.split("]")[0] + "]" not in have:
        with open(idx_path, "a", encoding="utf-8") as f:
            f.write(idx_line + "\n")

    # Commit + push
    git = ["git", "-C", VAULT]
    subprocess.run(git + ["add", "06-harga-pangan-papan/"], check=False)
    res = subprocess.run(
        git + ["commit", "-m", f"enrich(06): SP2KP harga pangan {d1} - {len(commodity_names)} commodities"],
        capture_output=True, text=True,
    )
    pushed = False
    if res.returncode == 0:
        pr = subprocess.run(git + ["push", "origin", "main"], capture_output=True, text=True)
        pushed = pr.returncode == 0

    print(json.dumps({
        "status": "written", "date": d1, "previous_date": d2,
        "commodities": len(commodity_names), "rows": len(rows),
        "src": src, "committed": res.returncode == 0, "pushed": pushed,
        "path": path,
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
