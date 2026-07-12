#!/usr/bin/env python3
"""archive_pulses.py — D5: archive stale 05-market-cron pulse snapshots.

The `05-market-cron/data/` folder accumulates one `pulse-YYYYMMDD-HHMM.json` per tick.
Left unbounded it bloats the repo. This moves pulses older than N days (default 7)
into `08-research-archive/market-pulses/`, preserving history without cluttering the
live data folder. `latest.json` and `latest-ihsg.json` are NEVER archived.

USAGE
-----
    python archive_pulses.py                       # dry-run, 7-day cutoff
    python archive_pulses.py --apply               # actually move
    python archive_pulses.py --days 14 --apply
    python archive_pulses.py --apply --git         # use `git mv` to keep history
"""
import argparse
import os
import re
import subprocess
import sys
from datetime import datetime, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.normpath(os.path.join(HERE, "..", "05-market-cron", "data"))
ARCHIVE = os.path.normpath(os.path.join(HERE, "..", "08-research-archive", "market-pulses"))
PULSE_RE = re.compile(r"^pulse-(\d{8})-(\d{4})\.json$")


def pulse_date(name: str):
    m = PULSE_RE.match(name)
    if not m:
        return None
    try:
        return datetime.strptime(m.group(1) + m.group(2), "%Y%m%d%H%M")
    except ValueError:
        return None


def main(argv):
    p = argparse.ArgumentParser(description="Archive stale market pulses")
    p.add_argument("--days", type=int, default=7)
    p.add_argument("--apply", action="store_true", help="actually move (default dry-run)")
    p.add_argument("--git", action="store_true", help="use git mv to preserve history")
    p.add_argument("--now", default=None, help="override 'now' (YYYY-MM-DD) for testing")
    args = p.parse_args(argv[1:])

    now = datetime.strptime(args.now, "%Y-%m-%d") if args.now else datetime.now()
    cutoff = now - timedelta(days=args.days)

    if not os.path.isdir(DATA):
        print(f"no data dir: {DATA}", file=sys.stderr)
        return 2
    os.makedirs(ARCHIVE, exist_ok=True)

    moved = 0
    for name in sorted(os.listdir(DATA)):
        d = pulse_date(name)
        if d is None or d >= cutoff:
            continue
        src = os.path.join(DATA, name)
        dst = os.path.join(ARCHIVE, name)
        print(f"{'MOVE' if args.apply else 'DRY '} {name}  ({d.date()})")
        if args.apply:
            if args.git:
                subprocess.run(["git", "mv", src, dst], check=False)
            else:
                os.replace(src, dst)
        moved += 1
    print(f"{'archived' if args.apply else 'would archive'} {moved} pulse(s) "
          f"older than {args.days}d (cutoff {cutoff.date()})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
