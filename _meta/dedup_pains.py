#!/usr/bin/env python3
"""dedup_pains.py — D3: canonicalize & dedup demand-mining pains.

The `03-id-business-trends/demand-mining/` folder has 82 pain files mined over many
runs. Some describe the SAME underlying pain with different slugs (e.g. a PLN spike
logged twice). This module clusters near-duplicate pains so the synthesis counts a
canonical set, not raw file count, and so promotion doesn't double-count.

Approach: dependency-free. Tokenize each file's title + first paragraph, compute
Jaccard similarity on token sets, cluster anything >= THRESHOLD.

USAGE
-----
    python dedup_pains.py 03-id-business-trends/demand-mining
    python dedup_pains.py 03-id-business-trends/demand-mining --threshold 0.6
"""
import argparse
import os
import re
import sys

STOP = set("dan di ke yang untuk dari the a an of to in is are itu ini pada "
           "atau juga akan bisa tidak ada saya kita mereka".split())
THRESHOLD = 0.55


def tokens(text: str) -> set:
    words = re.findall(r"[a-z0-9]+", text.lower())
    return {w for w in words if w not in STOP and len(w) > 2}


def load_docs(folder: str) -> dict:
    docs = {}
    for name in os.listdir(folder):
        if not name.endswith(".md") or name.upper().startswith("INDEX"):
            continue
        path = os.path.join(folder, name)
        try:
            with open(path, encoding="utf-8") as f:
                # title + first ~600 chars is enough signal
                text = f.read(800)
        except Exception:  # noqa: BLE001
            continue
        docs[name] = tokens(text)
    return docs


def jaccard(a: set, b: set) -> float:
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def cluster(docs: dict, threshold: float) -> list:
    names = list(docs)
    seen = set()
    clusters = []
    for i, n in enumerate(names):
        if n in seen:
            continue
        group = [n]
        seen.add(n)
        for m in names[i + 1:]:
            if m in seen:
                continue
            if jaccard(docs[n], docs[m]) >= threshold:
                group.append(m)
                seen.add(m)
        clusters.append(group)
    return clusters


def main(argv):
    p = argparse.ArgumentParser(description="Dedup demand-mining pains")
    p.add_argument("folder")
    p.add_argument("--threshold", type=float, default=THRESHOLD)
    args = p.parse_args(argv[1:])
    if not os.path.isdir(args.folder):
        print(f"not a folder: {args.folder}", file=sys.stderr)
        return 2
    docs = load_docs(args.folder)
    clusters = cluster(docs, args.threshold)
    dupes = [c for c in clusters if len(c) > 1]
    print(f"files: {len(docs)}  canonical clusters: {len(clusters)}  "
          f"duplicate groups: {len(dupes)}")
    for g in dupes:
        print("  DUP:")
        for name in g:
            print(f"    - {name}")
    if not dupes:
        print("no near-duplicates above threshold")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
