#!/usr/bin/env python3
"""validate-pulse.py — health check for the 05-market-cron live feed.

Guards against the "dead-feed" failure mode: a cron that reports success while
returning 100% errors. Run it in the synthesizer and in a daily watchdog:

    python _meta/validate-pulse.py 05-market-cron/data/latest.json

Exit codes:
    0  HEALTHY   -> at least one source live, file fresh
    1  DEGRADED  -> no source live OR file stale OR schema broken
    2  USAGE/IO  -> bad args / unreadable file

It prints a per-source table so a human (or the synthesis prompt) can see *which* leg
is broken (usually IHSG / idx_movers hitting 429). The real schema nests all sources
under a top-level "sources" key; this script handles both that and a flat layout.
"""
import json
import sys
import os
from datetime import datetime, timezone

STALENESS_HOURS = 24
KNOWN_SOURCES = ("crypto", "fx", "ihsg", "idx_movers", "trending_coins")


def parse_generated_iso(path):
    try:
        with open(path, "r", encoding="utf-8") as fh:
            data = json.load(fh)
        iso = data.get("generated_iso")
        if iso:
            return datetime.fromisoformat(iso)
    except Exception:
        pass
    return None


def is_error(obj):
    return isinstance(obj, dict) and "_error" in obj


def main(argv):
    if len(argv) != 2:
        print("usage: validate-pulse.py <path-to-latest.json>", file=sys.stderr)
        return 2
    path = argv[1]
    if not os.path.isfile(path):
        print(f"USAGE: file not found: {path}", file=sys.stderr)
        return 2

    try:
        with open(path, "r", encoding="utf-8") as fh:
            data = json.load(fh)
    except Exception as exc:  # noqa: BLE001
        print(f"DEGRADED: cannot parse JSON: {exc}")
        return 1

    # The real feed nests sources under "sources"; fall back to flat.
    root = data.get("sources", data) if isinstance(data, dict) else data

    # Freshness check
    gen = parse_generated_iso(path)
    now = datetime.now(timezone.utc)
    stale = gen is None or (now - gen).total_seconds() > STALENESS_HOURS * 3600

    # Walk every leaf; collect error leaves.
    def walk(prefix, obj):
        if isinstance(obj, dict):
            if is_error(obj):
                yield prefix or "(root)", obj.get("_error", "unknown")
                return
            for k, v in obj.items():
                yield from walk(f"{prefix}.{k}" if prefix else k, v)
        elif isinstance(obj, list):
            for i, v in enumerate(obj):
                yield from walk(f"{prefix}[{i}]", v)

    error_leaves = dict(walk("", root))

    # Known-source liveness.
    live_sources = []
    dead_sources = []
    for key in KNOWN_SOURCES:
        node = root.get(key) if isinstance(root, dict) else None
        if node is None:
            continue
        if is_error(node):
            dead_sources.append((key, node.get("_error", "unknown")))
        else:
            live_sources.append(key)

    # Report
    print(f"PULSE: {path}")
    print(f"generated_iso: {gen.isoformat() if gen else 'MISSING'}"
          f"  -> {'STALE' if stale else 'fresh'}")
    print(f"live sources : {', '.join(live_sources) or 'NONE'}")
    for key, err in dead_sources:
        print(f"dead source  : {key} -> {err}")
    # Any other error leaves not in the known set (e.g. nested under crypto).
    known = {k for k, _ in dead_sources}
    for leaf, err in error_leaves.items():
        top = leaf.split(".")[0].split("[")[0]
        if top not in known and top not in live_sources:
            print(f"error leaf   : {leaf} -> {err}")

    healthy = (len(live_sources) > 0) and not stale
    print("STATUS: " + ("HEALTHY" if healthy else "DEGRADED"))
    return 0 if healthy else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
