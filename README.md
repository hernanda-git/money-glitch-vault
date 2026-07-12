# Money Glitch Vault 🐉

> A self-enriching knowledge base of **financial opportunity gaps in Indonesia** — business
> pain points, settlement/logistics bottlenecks, buildable product one-pagers, and live
> market/pangan data — mined and enriched autonomously by Hermes cron jobs.

The vault is a **pipeline**, not a wiki. Raw signal flows through 7 stages
(`01` → `07`) and gets progressively enriched until a pain becomes a build-ready
opportunity. This README is the map. **[PIPELINE.md](PIPELINE.md)** is the operating
manual. **[`_templates/`](_templates/)** are the canonical file shapes. **[`_meta/`](_meta/)**
holds the living backlog and conventions.

---

## ⚠️ Read this before you trust the reports

The two synthesis reports in `07-gaps-and-opportunities/` (`weekly-gap-report-*.md`,
`*-weekly-gap-synthesis.md`) are **cron-generated snapshots** and go **stale**:

- They were written when `04-freelancer-ai-agent/` and `02-trading-bot/strategies/` did
  **not exist**. Both folders now exist. The reports calling them "phantom" are **wrong**
  and should be regenerated, not quoted as ground truth.
- The `05-market-cron` feed degrades often (rate-limits / 429s / dead endpoints). Reports
  run on an empty feed will confidently analyze nothing. Always check a feed's `latest.json`
  health before acting on a synthesis claim.

Treat reports as **leads to verify**, not conclusions. The single source of truth for
"what should I build next" is **[`_meta/BACKLOG.md`](_meta/BACKLOG.md)**, which is curated
by a human after reading the reports.

---

## The pipeline (one line per stage)

| Stage | Folder | What it holds | Output → |
|-------|--------|---------------|----------|
| **01 · Crawl** | `01-crawler-scrapper/` | X/Twitter advanced-search playbooks & query grammar (the firehose) | signal queries → `03` |
| **02 · Trade infra** | `02-trading-bot/` | Broker/API refs + strategies (Binance, IDX ORB) — execution plumbing | → `04` brain |
| **03 · Demand mine** | `03-id-business-trends/` | `demand-mining/` (82 pains), `bottlenecks/` (7 deep analyses), `competitors/` (2 teardowns) | pains → `07` |
| **04 · Agent/Delivery** | `04-freelancer-ai-agent/` | MCP server specs (Fastwork) — the "signal-to-action" delivery layer | consumes `01`+`05` |
| **05 · Market pulse** | `05-market-cron/` | Cron configs + live `data/` (crypto/fx/IHSG pulse JSON) | feed → `02`/`04` |
| **06 · Pangan & papan** | `06-harga-pangan-papan/` | SP2KP commodity price boards (17 commodities × regions) | region data → `03`/`07` |
| **07 · Gaps & opps** | `07-gaps-and-opportunities/` | `inbox/` (14 seeds), `opportunities/` (5 one-pagers), weekly synthesis reports | → build |

Plus: `08-research-archive/` (one-off recaps, see below) and `_meta/` / `_templates/`
(infrastructure, not pipeline content).

---

## Live inventory (as of this commit)

| Metric | Count |
|--------|-------|
| Demand-mining pains (`03/.../demand-mining`) | 82 |
| Bottleneck analyses (`03/.../bottlenecks`) | 7 |
| Competitor teardowns (`03/.../competitors`) | 2 |
| Build specs / MCP servers (`04`) | 1 |
| Opportunity one-pagers (`07/opportunities`) | 5 |
| Inbox seeds (`07/inbox`) | 14 |
| Live data feeds (05 pulse + 06 SP2KP) | 2 |

Full per-file map → **[`_meta/VAULT-MAP.md`](_meta/VAULT-MAP.md)**.

---

## Where to start

- **"What do I build next?"** → [`_meta/BACKLOG.md`](_meta/BACKLOG.md) (curated future-works queue)
- **"How does enrich work?"** → [`PIPELINE.md`](PIPELINE.md)
- **"What shape should a new file be?"** → [`_templates/`](_templates/)
- **"Is my new file on-convention?"** → [`_meta/CONVENTIONS.md`](_meta/CONVENTIONS.md)
- **"Regenerate the synthesis, but right this time."** → run the weekly synthesizer per
  `PIPELINE.md §Stage 7`, then curate the output into `BACKLOG.md`.

---

## Repo hygiene

- Root-level recap artifacts (`recap-*.md`, `recap-regulasi-*.{md,html}`,
  `rekap-regulasi-*.pdf`) are **one-off research exports**, not pipeline content. They
  live in [`08-research-archive/`](08-research-archive/) so the root stays a clean map.
- No credentials are committed (secrets live in agent env / local-only). `.gitignore`
  blocks `config.json`, `.env`, `*.token`. **Never** paste JWT/access tokens into docs —
  reference them by name only.
- `CHANGELOG.md` is append-only, one line per enrich/mine/agent action.
