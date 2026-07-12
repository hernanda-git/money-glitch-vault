#!/usr/bin/env python3
"""check_secrets.py — D4: pre-commit redaction guard.

Scans staged (or all) files for leaked credential shapes before they hit git. The
vault previously carried Fastwork credentials in a committed MCP spec; this guard
plus `.gitignore` prevents a repeat. Wire it as a git pre-commit hook:

    ln -sf ../../_meta/check_secrets.py .git/hooks/pre-commit  # (make executable)

or run manually:

    python _meta/check_secrets.py            # scan tracked files
    python _meta/check_secrets.py --staged   # scan only staged (hook mode)

Exit 0 = clean, 1 = secrets found (blocks commit), 2 = usage error.

It looks for JWTs, Bearer tokens, AWS keys, private keys, and known field names
(access_token, api_key, secret, password) with a real-looking value. Markdown specs
may DESCRIBE these fields; a value of ***, <...>, [REDACTED], or a placeholder is OK.
"""
import argparse
import re
import subprocess
import sys

PLACEHOLDER = re.compile(r"(\*{3,}|<[^>]+>|\[REDACTED\]|xxx+|your[_-]?\w+|example|dummy|changeme)",
                         re.I)

PATTERNS = [
    ("JWT", re.compile(r"eyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}")),
    ("AWS access key", re.compile(r"AKIA[0-9A-Z]{16}")),
    ("Private key", re.compile(r"-----BEGIN (?:RSA |EC )?PRIVATE KEY-----")),
    ("Bearer token", re.compile(r"[Bb]earer\s+[A-Za-z0-9._-]{20,}")),
    ("Slack token", re.compile(r"xox[baprs]-[A-Za-z0-9-]{10,}")),
    ("Generic secret assignment",
     re.compile(r"(?i)(access_token|api[_-]?key|secret|password|token)\s*[:=]\s*"
                r"['\"]?([A-Za-z0-9._/+-]{16,})['\"]?")),
]


def tracked_files(staged: bool):
    cmd = ["git", "diff", "--cached", "--name-only"] if staged else ["git", "ls-files"]
    out = subprocess.run(cmd, capture_output=True, text=True)
    return [f for f in out.stdout.splitlines() if f.strip()]


def scan_file(path: str):
    hits = []
    try:
        with open(path, encoding="utf-8", errors="ignore") as f:
            for lineno, line in enumerate(f, 1):
                for label, pat in PATTERNS:
                    m = pat.search(line)
                    if not m:
                        continue
                    val = m.group(len(m.groups())) if m.groups() else m.group(0)
                    if PLACEHOLDER.search(val):
                        continue  # redacted/placeholder is fine
                    hits.append((lineno, label, line.strip()[:100]))
    except (OSError, UnicodeError):
        pass
    return hits


def main(argv):
    p = argparse.ArgumentParser(description="Scan for leaked secrets")
    p.add_argument("--staged", action="store_true", help="scan only git-staged files")
    p.add_argument("paths", nargs="*", help="explicit paths (default: tracked files)")
    args = p.parse_args(argv[1:])

    files = args.paths or tracked_files(args.staged)
    total = 0
    for path in files:
        for lineno, label, snippet in scan_file(path):
            total += 1
            print(f"LEAK {path}:{lineno} [{label}] {snippet}")
    if total:
        print(f"\nBLOCKED: {total} potential secret(s) found. Redact before commit.",
              file=sys.stderr)
        return 1
    print("clean: no secrets detected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
