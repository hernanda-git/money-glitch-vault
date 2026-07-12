# CONVENTIONS.md — vault-wide rules

Enforced so the vault stays machine-readable and the enrichment pipeline can run unattended.

## File naming
- **Slugs:** `kebab-case`, Indonesian-phrase where possible (e.g. `harga-beras-di-atas-het-ibu-rt.md`).
- **Dates:** `YYYY-MM-DD` in filenames and INDEX rows. `YYYYMMDD-HHMM` for pulse snapshots.
- **No spaces, no caps** in filenames.

## Folder contract (see PIPELINE.md for detail)
- `01` crawl playbooks · `02` trade infra (`brokers-apis/`, `strategies/`, `risk-management/`, `signals/`)
  · `03` pains (`demand-mining/`, `bottlenecks/`, `competitors/`) · `04` agent (`mcp-servers/`)
  · `05` market (`cron-configs/`, `data/`) · `06` pangan (`data/`) · `07` gaps (`inbox/`, `opportunities/`)
  · `08` research-archive (one-off recaps) · `_meta` + `_templates` (infra, not pipeline content).
- **Never** put one-off recaps/exports at the repo root (that's how `recap-*.md` / `rekap-*.pdf`
  got orphaned). They go in `08-research-archive/`.

## Document header (every content file)
```
# <Title>
**File:** `<path>`        (bottlenecks/opportunities also: **Created:**, **Category:**, **Priority:**, **Related files:**)
**Date observed:** YYYY-MM-DD   (demand-mining)
**Signal strength:** N   (demand-mining, 1–5)
**Category:** <parent|seller|umkm|farmer|employee|freelancer|student|other>
**Sources (minimum 3):**  (demand-mining)
```

## Demand-mining minimum bar
- ≥3 sources with URLs + dates.
- A `## The pain` section with verbatim Indonesian quotes.
- `## Evidence of volume`, `## Existing solutions (and why they fail)`, `## Your wedge`,
  `## What people would pay`, `## Adjacent opportunities`, `## Time-to-build estimate`.
- Logged as one line in `demand-mining/INDEX.md`.

## Data contracts
- **`05/data/latest.json`:** each source key is data **or** `{"_error": "...", "_source": "..."}`.
  **Always special-case `_error`.**
- **`06/data/sp2kp-*.json`:** region is a raw string (Nasional / Region A/B/C). Normalize
  before region-aware use.
- **Pulses older than 7 days** are archived once the feed is healthy.

## Verification etiquette
- Figures not confirmed this run are tagged **`verify-live`**. Never present them as fact.
- Live web verify needs `PARALLEL_API_KEY` in the agent env; if absent, say so in the doc.
- **No data invented.** If a source is unreachable, annotate — do not fill with plausible numbers.

## Credential hygiene (security)
- Reference `config.json` / JWT / `access_token` / `user_id` **by name only**. Never paste values.
- `.gitignore` blocks: `config.json`, `.env`, `*.token`, `*.secret`, `__pycache__/`, `node_modules/`.
- Before any push: `git status` + check no token-looking string is staged. Run
  `grep -rniE 'Bearer |access_token *: *"|"jwt"' --include=*.md .` as a sanity check.

## CHANGELOG
- Append-only, one line per action, format:
  `## YYYY-MM-DD -- <verb>(<stage>): <what> — <note>`
  verbs: `mine`, `enrich`, `agent`, `fix`, `doc`, `synthesis`.
- Keep the root `CHANGELOG.md` as the canonical log (the uncommitted 2-line local edit should
  be folded into a commit, not left dirty).

## Synthesis reports are not truth
- `07/*-weekly-gap-*.md` are cron snapshots. Read for leads; curate into `_meta/BACKLOG.md`.
- Regenerate per `PIPELINE.md §6` (phantom-folder + dead-feed guards) before trusting.
