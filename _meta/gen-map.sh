#!/usr/bin/env bash
# gen-map.sh — regenerate _meta/VAULT-MAP.md from the current repo tree.
# Run from repo root:  bash _meta/gen-map.sh
set -euo pipefail
cd "$(dirname "$0")/.."

{
  echo "# VAULT-MAP.md — generated map of pipeline content"
  echo
  echo "> Auto-generated snapshot of every content file in the vault. Infrastructure (_meta, _templates, .git) is excluded. Regenerate with: \`bash _meta/gen-map.sh\`"
  echo
  for d in 01-crawler-scrapper 02-trading-bot 03-id-business-trends 04-freelancer-ai-agent 05-market-cron 06-harga-pangan-papan 07-gaps-and-opportunities 08-research-archive; do
    if [ -d "$d" ]; then
      echo "## $d"
      echo
      find "$d" -type f -name '*.md' | sort | while read -r f; do
        n=$(wc -l < "$f")
        echo "- \`$f\` ($n lines)"
      done
      cnt=$(find "$d" -type f \( -name '*.json' -o -name '*.csv' \) ! -name 'package*.json' 2>/dev/null | wc -l)
      if [ "$cnt" -gt 0 ]; then echo "- _data files (json/csv): $cnt"; fi
      echo
    fi
  done
} > _meta/VAULT-MAP.md
echo "Wrote _meta/VAULT-MAP.md ($(wc -l < _meta/VAULT-MAP.md) lines)"
