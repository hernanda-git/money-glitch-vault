#!/usr/bin/env python3
"""merge-ihsg-into-latest.py — D1 orchestrator: heal the dead IHSG leg.

PROBLEM
-------
`05-market-cron/data/latest.json` carries `sources.ihsg` and `sources.idx_movers`
that hit HTTP 429 (the old Yahoo v7 `quote` endpoint is bot-blocked), so the equity
leg of the pulse is permanently dead. Meanwhile `ihsg-daily-fetch.py` (the v8 `chart`
endpoint, browser UA, dual-host retry) works fine and writes a healthy standalone
`latest-ihsg.json`. Nothing merged the two — so the vault's own synthesis kept calling
the feed "dead".

WHAT THIS DOES
--------------
1. Runs `ihsg-daily-fetch.py --out data/latest-ihsg.json` (the WORKING fetcher).
2. If it succeeds and is fresh, splices its normalized payload into
   `latest.json.sources.ihsg`, replacing the `_error` node.
3. Re-runs `_meta/validate-pulse.py` and exits with its status.

Idempotent, safe to run every cron tick. If the fetcher fails, latest.json is left
untouched (the old `_error` stays — honest degradation, not a fake success).

USAGE
-----
    python merge-ihsg-into-latest.py
    python merge-ihsg-into-latest.py --data-dir 05-market-cron/data
"""
import argparse
import json
import os
import subprocess
import sys
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_DATA = os.path.join(HERE, "..", "data")


def run_fetcher(data_dir: str) -> dict | None:
    """Run the working v8 IHSG fetcher; return its parsed payload or None."""
    fetcher = os.path.join(HERE, "ihsg-daily-fetch.py")
    out = os.path.join(data_dir, "latest-ihsg.json")
    try:
        subprocess.run(
            [sys.executable, fetcher, "--out", out, "--quiet"],
            check=True, timeout=90, capture_output=True, text=True,
        )
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
        print(f"WARN: IHSG fetcher failed, leaving latest.json untouched: {e}",
              file=sys.stderr)
        return None
    try:
        with open(out, encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:  # noqa: BLE001
        print(f"WARN: cannot read fetcher output: {e}", file=sys.stderr)
        return None


def splice(latest_path: str, ihsg: dict) -> bool:
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
        "_healed_by": "merge-ihsg-into-latest.py",
        "_healed_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }
    tmp = latest_path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(latest, f, indent=2, ensure_ascii=False)
    os.replace(tmp, latest_path)
    close = (ihsg.get("latest") or {}).get("close")
    print(f"OK: spliced healthy IHSG (close={close}) into {latest_path}")
    return True


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description="Heal the dead IHSG leg of latest.json")
    p.add_argument("--data-dir", default=DEFAULT_DATA)
    args = p.parse_args(argv)
    data_dir = os.path.abspath(args.data_dir)
    latest_path = os.path.join(data_dir, "latest.json")

    ihsg = run_fetcher(data_dir)
    if ihsg is not None:
        splice(latest_path, ihsg)

    # Re-validate; propagate its exit code so cron sees true health.
    validator = os.path.join(HERE, "..", "..", "_meta", "validate-pulse.py")
    validator = os.path.abspath(validator)
    if os.path.isfile(validator):
        r = subprocess.run([sys.executable, validator, latest_path])
        return r.returncode
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
