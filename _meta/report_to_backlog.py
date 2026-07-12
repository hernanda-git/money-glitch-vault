#!/usr/bin/env python3
"""report_to_backlog.py — AUTO-ENRICH §6: turn weekly synthesis into draft backlog items.

The vault's weekly synthesis (`07/*-weekly-gap-synthesis.md` or `*weekly-gap-report-*.md`)
ends with a "New gaps identified" / "New Gaps Discovered" section listing actionable items.
This script parses that section, emits one draft backlog row per item, and appends them to
`_meta/BACKLOG.md` under a dedicated `## Draft — auto-proposed` heading (NEVER directly into
READY — a human flips draft -> ready, per `AUTO-ENRICH.md` human gates).

Dedup: skips any item whose slug already appears anywhere in BACKLOG (proposed, ready, done,
or a prior draft), so re-running never double-counts.

USAGE
-----
    python report_to_backlog.py                         # dry-run, prints what it would add
    python report_to_backlog.py --apply                 # append drafts to BACKLOG.md
    python report_to_backlog.py --report 07/.../xxx.md  # point at a specific report

Exit 0 = nothing to add (or applied cleanly); 1 = usage / parse error.
"""
import argparse
import os
import re
import sys
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, ".."))
REPORTS_DIR = os.path.join(ROOT, "07-gaps-and-opportunities")
BACKLOG = os.path.join(HERE, "BACKLOG.md")
DRAFT_HEADING = "## Draft — auto-proposed (unreviewed)"

NEW_GAP_RE = re.compile(r"^#{2,4}\s+.*new\s+gaps?\b", re.I)
ITEM_RE = re.compile(r"^[-*]\s+(.*)$")
WRITE_REF_RE = re.compile(r"`?([0-9A-Za-z_-]+\.md)`?|(?:write|build)\s+`?([0-9A-Za-z_/-]+\.md)`?", re.I)


def find_latest_report() -> str | None:
    """Prefer the synthesis (it carries the 'New gaps' backlog section); fall back
    to the most-recently-named gap report."""
    files = [n for n in os.listdir(REPORTS_DIR)
             if "weekly-gap" in n and n.endswith(".md")]
    if not files:
        return None
    synth = [f for f in files if f.endswith("synthesis.md")]
    if synth:
        return os.path.join(REPORTS_DIR, synth[0])
    files.sort()
    return os.path.join(REPORTS_DIR, files[-1])


TABLE_ROW_RE = re.compile(r"^\|\s*\d+\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*$")
REF_IN_CELL_RE = re.compile(r"`([^`]+\.md)`")


def extract_new_gaps(path: str) -> list[str]:
    """Return actionable items under the first 'New gaps' heading.

    Handles BOTH bullet lists (`- item`) and markdown tables
    (`| n | `file.md` | cluster | why | effort |` — the format the synthesis actually uses).
    """
    with open(path, encoding="utf-8") as f:
        lines = f.read().splitlines()
    items: list[str] = []
    in_section = False
    for line in lines:
        if NEW_GAP_RE.match(line):
            in_section = True
            continue
        if in_section:
            if re.match(r"^#{1,4}\s", line) and not NEW_GAP_RE.match(line):
                break
            m = ITEM_RE.match(line)
            if m:
                items.append(m.group(1).strip())
                continue
            t = TABLE_ROW_RE.match(line)
            if t:
                cell1 = t.group(1).strip()
                refs = REF_IN_CELL_RE.findall(line)
                label = refs[0] if refs else cell1
                why = t.group(3).strip()
                items.append(f"{label} — {why}" if why else label)
    return items


def slugify(item: str) -> str:
    """Derive a stable slug from an item: prefer a `path.md` ref, else kebab the text."""
    m = WRITE_REF_RE.search(item)
    if m:
        ref = m.group(1) or m.group(2)
        if ref:
            return ref.lower().replace("/", "-").replace(".md", "")
    words = re.findall(r"[a-z0-9]+", item.lower())
    return "-".join(words[:6])


def main(argv):
    p = argparse.ArgumentParser(description="Weekly report -> draft backlog items")
    p.add_argument("--report", default=None, help="explicit report path")
    p.add_argument("--apply", action="store_true", help="append (default dry-run)")
    args = p.parse_args(argv[1:])

    report = args.report or find_latest_report()
    if not report or not os.path.isfile(report):
        print(f"no weekly report found (looked in {REPORTS_DIR})", file=sys.stderr)
        return 1
    items = extract_new_gaps(report)
    if not items:
        print(f"no 'New gaps' items found in {os.path.basename(report)}")
        return 0

    # load existing BACKLOG to dedup
    existing = set()
    if os.path.isfile(BACKLOG):
        with open(BACKLOG, encoding="utf-8") as f:
            bl = f.read().lower()
        for token in re.findall(r"[0-9a-z_-]+\.md", bl):
            existing.add(token.lower().replace("/", "-").replace(".md", ""))

    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    drafts = []
    seen = set()
    for it in items:
        slug = slugify(it)
        if slug in existing or slug in seen:
            print(f"SKIP (dup): {slug}")
            continue
        seen.add(slug)
        drafts.append((slug, it.strip()))

    if not drafts:
        print("nothing new to add (all items already in BACKLOG)")
        return 0

    print(f"=== {len(drafts)} new draft item(s) from {os.path.basename(report)} ===")
    for slug, text in drafts:
        print(f"  + [{slug}] {text[:90]}")

    if not args.apply:
        print("\n(dry-run — rerun with --apply to append)")
        return 0

    with open(BACKLOG, encoding="utf-8") as f:
        cur = f.read()
    if DRAFT_HEADING not in cur:
        cur = cur.rstrip() + f"\n\n{DRAFT_HEADING}\n"
    rows = "\n".join(f"- [draft] {text}  _(slug: `{slug}`, proposed {today})_"
                     for slug, text in drafts)
    new_block = cur.rstrip() + "\n" + rows + "\n"
    with open(BACKLOG, "w", encoding="utf-8") as f:
        f.write(new_block)
    print(f"\nappended {len(drafts)} draft item(s) to {os.path.basename(BACKLOG)}")
    return 0


def _draft_heading_present() -> bool:
    if not os.path.isfile(BACKLOG):
        return False
    with open(BACKLOG, encoding="utf-8") as f:
        return DRAFT_HEADING in f.read()


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
