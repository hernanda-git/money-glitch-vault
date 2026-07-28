import subprocess, json, os, sys
from datetime import datetime, timezone

API = "https://api-sp2kp.kemendag.go.id"
VAULT = r"C:\Users\it26\money-glitch-vault"
DATA_DIR = os.path.join(VAULT, "06-harga-pangan-papan", "data")

def curl_json(url, post_form=None, timeout=60):
    cmd = ["curl", "-s", "-m", str(timeout), url, "-w", "\n%{http_code}"]
    if post_form:
        cmd += ["-X", "POST", "-H", "Content-Type: multipart/form-data"]
        for k, v in post_form.items():
            cmd += ["-F", f"{k}={v}"]
    out = subprocess.run(cmd, capture_output=True, text=True).stdout
    body, _, code = out.rpartition("\n")
    return json.loads(body), code

def build_rows(data, td, cd):
    rows = []
    for it in data:
        name = it.get("variant_nama")
        unit = it.get("satuan_display")
        chg = it.get("persen_perubahan")
        rows.append({
            "date": td,
            "commodity_name": name,
            "unit": unit,
            "region": "Nasional",
            "previous_price": it.get("harga_pembanding") or None,
            "current_price": it.get("harga") or None,
            "change_percent": round(chg, 2) if chg is not None else None,
        })
        for rg in (it.get("region") or []):
            rchg = rg.get("persen_perubahan")
            rows.append({
                "date": td,
                "commodity_name": name,
                "unit": rg.get("satuan_display") or unit,
                "region": rg.get("region"),
                "previous_price": rg.get("harga_pembanding") or None,
                "current_price": rg.get("harga") or None,
                "change_percent": round(rchg, 2) if rchg is not None else None,
            })
    return rows

def main():
    # Get latest date
    obj, code = curl_json(f"{API}/report/api/latest-price-dates?tipe_komoditas_id=1")
    if code != "200" or obj.get("status") != "success":
        report = {"status": "failure", "reason": "latest-price-dates endpoint failed"}
        print(json.dumps(report, indent=2))
        return 1

    td = obj["data"]["tanggal"]
    cd = obj["data"]["tanggal_pembanding"]

    # Fetch comparison data
    obj2, code2 = curl_json(
        f"{API}/report/api/average-price/generate-perbandingan-harga",
        {"tanggal": td, "tanggal_pembanding": cd},
    )
    if code2 != "200" or obj2.get("status") != "success":
        report = {"status": "failure", "reason": "comparison endpoint failed", "detail": str(obj2)[:500]}
        print(json.dumps(report, indent=2))
        return 1

    data = obj2.get("data") or []
    if not data:
        report = {"status": "failure", "reason": "empty data"}
        print(json.dumps(report, indent=2))
        return 1

    rows = build_rows(data, td, cd)
    commodity_names = []
    seen = set()
    for r in rows:
        if r["region"] == "Nasional" and r["commodity_name"] not in seen:
            seen.add(r["commodity_name"])
            commodity_names.append(r["commodity_name"])

    regions = sorted(set(r["region"] for r in rows))

    payload = {
        "source": f"{API} (REST: report/api/average-price/generate-perbandingan-harga)",
        "fetched_at_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "data_date": td,
        "previous_date": cd,
        "commodity_count": len(commodity_names),
        "row_count": len(rows),
        "commodity_names": commodity_names,
        "rows": rows,
    }

    os.makedirs(DATA_DIR, exist_ok=True)
    path = os.path.join(DATA_DIR, f"sp2kp-{td}.json")

    with open(path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
        f.write("\n")
    with open(os.path.join(DATA_DIR, "latest.json"), "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
        f.write("\n")

    # INDEX.md
    idx_line = f"- [{td}] SP2KP - {len(commodity_names)} commodities x {len(regions)} regions"
    idx_path = os.path.join(DATA_DIR, "INDEX.md")
    have = ""
    if os.path.exists(idx_path):
        with open(idx_path, encoding="utf-8") as f:
            have = f.read()
    if idx_line.split("]")[0] + "]" not in have:
        with open(idx_path, "a", encoding="utf-8") as f:
            f.write(idx_line + "\n")

    # Big movers
    national_rows = [r for r in rows if r["region"] == "Nasional" and r["change_percent"] is not None]
    movers = sorted(national_rows, key=lambda r: abs(r["change_percent"]), reverse=True)
    top3 = movers[:3]
    big_movers = [r for r in national_rows if abs(r["change_percent"]) > 5]

    report = {
        "status": "success",
        "date": td,
        "previous_date": cd,
        "commodities": len(commodity_names),
        "rows": len(rows),
        "regions": regions,
        "commodity_names": commodity_names,
        "top_movers": [{"name": r["commodity_name"], "change": r["change_percent"]} for r in top3],
        "big_movers": [{"name": r["commodity_name"], "change": r["change_percent"]} for r in big_movers],
        "path": path,
    }
    print(json.dumps(report, indent=2))

    # Git commit + push
    git = ["git", "-C", VAULT]
    subprocess.run(git + ["add", "06-harga-pangan-papan/"], check=False)
    res = subprocess.run(
        git + ["commit", "-m", f"enrich(06): SP2KP harga pangan {td} - {len(commodity_names)} commodities"],
        capture_output=True, text=True,
    )
    if res.returncode == 0:
        subprocess.run(git + ["push", "origin", "main"], capture_output=True, text=True)

    return 0

if __name__ == "__main__":
    raise SystemExit(main())
