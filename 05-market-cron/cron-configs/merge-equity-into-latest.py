#!/usr/bin/env python3
"""merge-equity-into-latest.py — D1 orchestrator: heal the DEAD equity legs.

PROBLEM
-------
`05-market-cron/data/latest.json` carries `sources.ihsg` and `sources.idx_movers`
that hit HTTP 429 (the old Yahoo v7 `quote` endpoint is bot-blocked), so the equity
leg of the pulse was permanently dead. Meanwhile `ihsg-daily-fetch.py` and the new
`idx-movers-fetch.py` (both v8 `chart` endpoint, browser UA, dual-host retry) work
fine and write healthy standalone JSON. Nothing merged them — so the vault's own
synthesis kept calling the feed "dead".

WHAT THIS DOES
--------------
1. Runs `ihsg-daily-fetch.py --out data/latest-ihsg.json` (the WORKING fetcher).
2. Runs `idx-movers-fetch.py --out data/latest-idx-movers.json` (WORKING, see D1b).
3. If each succeeds and is fresh, splices its payload into `latest.json.sources.<leg>`,
   replacing the `_error` node.
4. Re-runs `_meta/validate-pulse.py` and exits with its status.

Idempotent, safe to run every cron tick. If a fetcher fails, that leg is left untouched
(the old `_error` stays — honest degradation, not a fake success).

USAGE
-----
    python merge-equity-into-latest.py
    python merge-equity-into-latest.py --data-dir 05-market-cron/data
"""
import argparse
import json
import os
import subprocess
import sys
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_DATA = os.path.join(HERE, "..", "data")


def run_fetcher(script: str, out_name: str, data_dir: str) -> dict | None:
    """Run a v8 fetcher script; return its parsed payload or None on failure."""
    fetcher = os.path.join(HERE, script)
    out = os.path.join(data_dir, out_name)
    try:
        subprocess.run(
            [sys.executable, fetcher, "--out", out, "--quiet"],
            check=True, timeout=120, capture_output=True, text=True,
        )
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
        print(f"WARN: {script} failed, leaving latest.json leg untouched: {e}",
              file=sys.stderr)
        return None
    try:
        with open(out, encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:  # noqa: BLE001
        print(f"WARN: cannot read {out}: {e}", file=sys.stderr)
        return None


def splice_ihsg(latest_path: str, ihsg: dict) -> bool:
    """Splice the healthy ihsg payload into latest.json.sources.ihsg."""
    try:
        with open(latest_path, encoding="utf-8") as f:
            latest = json.load(f)
    except Exception as e:  # noqa: BLE001
        print(f"ERROR: cannot read {latest_path}: {e}", file=sys.stderr)
        return False

    if ihsg.get("stale"):
        print("WARN: IHSG data is stale; not splicing (keeping prior node).",
              file=sys.stderr)
        return False

    sources = latest.setdefault("sources", {})
    # Compact node compatible with the pulse schema (drop the long history array).
    sources["ihsg"] = {
        "source": ihsg.get("source"),
        "symbol": ihsg.get("symbol"),
        "name": ihsg.get("name"),
        "latest": ihsg.get("latest"),
        "fifty_two_week": ihsg.get("fifty_two_week"),
        "fetched_utc": ihsg.get("fetched_utc"),
        "_healed_by": "merge-equity-into-latest.py",
        "_healed_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }
    _write(latest_path, latest)
    close = (ihsg.get("latest") or {}).get("close")
    print(f"OK: spliced healthy IHSG (close={close}) into {latest_path}")
    return True


def splice_movers(latest_path: str, movers: dict) -> bool:
    """Splice the healthy idx_movers payload into latest.json.sources.idx_movers."""
    try:
        with open(latest_path, encoding="utf-8") as f:
            latest = json.load(f)
    except Exception as e:  # noqa: BLE001
        print(f"ERROR: cannot read {latest_path}: {e}", file=sys.stderr)
        return False

    if not movers.get("top_gainers") and not movers.get("top_losers"):
        print("WARN: movers empty; not splicing.", file=sys.stderr)
        return False

    sources = latest.setdefault("sources", {})
    sources["idx_movers"] = {
        "source": movers.get("source"),
        "market": movers.get("market"),
        "fetched_utc": movers.get("fetched_utc"),
        "count_scanned": movers.get("count_scanned"),
        "count_priced": movers.get("count_priced"),
        "top_gainers": movers.get("top_gainers"),
        "top_losers": movers.get("top_losers"),
        "_healed_by": "merge-equity-into-latest.py",
        "_healed_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }
    _write(latest_path, latest)
    print(f"OK: spliced IDX movers (gainers={len(movers.get('top_gainers', []))}, "
          f"losers={len(movers.get('top_losers', []))}) into {latest_path}")
    return True


def _write(latest_path: str, latest: dict) -> None:
    tmp = latest_path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(latest, f, indent=2, ensure_ascii=False)
    os.replace(tmp, latest_path)


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description="Heal the dead IDX equity legs of latest.json")
    p.add_argument("--data-dir", default=DEFAULT_DATA)
    args = p.parse_args(argv)
    data_dir = os.path.abspath(args.data_dir)
    latest_path = os.path.join(data_dir, "latest.json")

    ihsg = run_fetcher("ihsg-daily-fetch.py", "latest-ihsg.json", data_dir)
    if ihsg is not None:
        splice_ihsg(latest_path, ihsg)

    movers = run_fetcher("idx-movers-fetch.py", "latest-idx-movers.json", data_dir)
    if movers is not None:
        splice_movers(latest_path, movers)

    # Re-validate; propagate its exit code so cron sees true health.
    validator = os.path.join(HERE, "..", "..", "_meta", "validate-pulse.py")
    validator = os.path.abspath(validator)
    if os.path.isfile(validator):
        r = subprocess.run([sys.executable, validator, latest_path])
        return r.returncode
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
