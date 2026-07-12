# PIPELINE.md — Money Glitch Vault enrichment pipeline

This document is the operating manual for the vault. It defines the 7 stages, what each
produces, the folder contract for every stage, the gates between stages, the cron cadence,
and the canonical templates. **New enrich/mine work should follow this, not improvise.**

The vault's purpose: turn **raw Indonesian market/social signal** into **build-ready
opportunity one-pagers** with verifiable evidence and explicit willingness-to-pay. Every
stage is a pure-ish transform: it reads upstream artifacts and writes downstream artifacts
in a fixed folder, with no side effects on other stages' files.

---

## 1. Topology

```
01-crawler-scrapper   ──queries──▶  03-id-business-trends (demand-mining)
        │                              │
        │ (social sentiment)          │ (pains → bottlenecks → competitors)
        ▼                              ▼
05-market-cron ──feed──▶ 04-freelancer-ai-agent (MCP/delivery)   07-gaps-and-opportunities
        │                    ▲   │                                  (inbox → opportunities)
        ▼                    │   └── consumes 01+05 ──▶ 02-trading-bot (strategies)
06-harga-pangan-papan ──region data──▶ 03 / 07
```

- **Inputs (external):** X/Twitter, news (Kompas/Bisnis/BPS), CoinGecko, Yahoo/Stooq
  (IHSG), SP2KP pangan & papan API, Binance.
- **Output (internal):** `07/opportunities/*.md` one-pagers + `05`/`06` live data +
  reusable build specs in `02`/`04`.

---

## 2. The 7 stages

### Stage 01 · Crawl / scrape playbooks — `01-crawler-scrapper/`
- **Purpose:** the *firehose grammar*. Defines how to mine raw signal (X advanced-search
  operators, twscrape/snscrape wiring, query patterns per module).
- **Produces:** `x/search-operators-playbook.md` and any per-source scraper notes.
- **Contract:** query patterns are copy-pasteable and tagged by target module
  (e.g. `regulatory-shock`, `early-panic`, `arbitrage`, `competitor-gap`).
- **Gate → 03:** a query is "done" when it has (a) a working operator string and
  (b) a documented target folder it feeds.

### Stage 02 · Trading / execution infra — `02-trading-bot/`
- **Purpose:** execution plumbing for the trading wedge (broker APIs, auth, rate limits,
  strategies, risk engine).
- **Folder contract:**
  - `brokers-apis/` — exchange/API references (e.g. `binance-spot-futures.md`)
  - `strategies/` — strategy docs (e.g. `idx-opening-range-breakout.md`)
  - `risk-management/` *(planned)* — position-sizing / Kelly / drawdown caps
  - `signals/` *(planned)* — sentiment/news scoring
- **Gate → 04:** a strategy is "consumable" when it documents the event-driven baseline
  (queue + state machine + idempotent handlers) the agent layer reuses.

### Stage 03 · Demand mining — `03-id-business-trends/`
- **Purpose:** the pain reservoir. Raw mined pains → deep bottleneck analyses → competitor
  teardowns.
- **Folder contract:**
  - `demand-mining/` — one file per pain, `kebab-case-slug.md`, **uses
    [`_templates/demand-mining.md`](_templates/demand-mining.md)**. Must have ≥3 sources,
    signal strength, and a wedge. Logged in `demand-mining/INDEX.md`.
  - `bottlenecks/` — deep (600–1500 line) structural analyses with code/SQL schemas.
  - `competitors/` — competitor gap teardowns.
- **Gate → 07:** a pain graduates to `07/inbox/` when it carries a concrete wedge +
  willingness-to-pay. A cluster of related pains graduates to a `bottlenecks/` doc.

### Stage 04 · Agent / delivery — `04-freelancer-ai-agent/`
- **Purpose:** the "signal-to-action" layer. MCP server specs + agent code that consume
  `01` (sentiment) + `05` (feed) and push to WhatsApp/Telegram.
- **Folder contract:** `mcp-servers/` (specs), `signal-agent/` *(planned)*, etc.
- **Gate:** a spec is "build-ready" when it has endpoints, auth model, tool surface, and
  reference code (see `fastwork-mcp-spec.md` as the template).

### Stage 05 · Market pulse (live feed) — `05-market-cron/`
- **Purpose:** scheduled fetch of crypto / fx / IHSG / movers into `data/`.
- **Folder contract:**
  - `cron-configs/` — fetcher scripts + deploy notes (`ihsg-daily-fetch.{py,md}`)
  - `data/` — `latest.json` (current), `pulse-YYYYMMDD-HHMM.json` (snapshots)
- **Data contract (`latest.json`):** each source key is either a data object **or**
  `{"_error": "...", "_source": "..."}`. **Consumers MUST special-case `_error`** — a
  naive parser will crash on the IHSG/idx_movers leg (frequently 429).
- **Health gate:** before any synthesis consumes `05`, assert ≥1 source is live and
  `latest.json` is newer than 24h. If 100% errors → mark feed DEGRADED, alert, fall back
  to last-good snapshot. Do **not** report success on empty data ("dead-feed" pattern).

### Stage 06 · Pangan & papan (live feed) — `06-harga-pangan-papan/`
- **Purpose:** SP2KP commodity price boards (food staples + property) per region.
- **Folder contract:** `data/` — `sp2kp-YYYY-MM-DD.json` per day, `latest.json`, `INDEX.md`.
- **Data contract:** region column is a **raw string** needing normalization (Nasional /
  Region A/B/C). The 30–40% province/kabupaten taxonomy from the warung/COD docs is **not**
  yet applied — normalize before using region data to power restock/arbitrage alerts.
- **Gotcha:** the homepage map is Highcharts (no `<table>`); Tabulasi Harga is a Tableau
  iframe (not scrapable). **Always use Source A REST API.** `latest-price-dates` is
  auth-gated (HTTP 401) as of 2026-07-11 — find the latest date by probing
  `generate-perbandingan-harga` and picking the first date with non-zero `harga`.

### Stage 07 · Gaps & opportunities — `07-gaps-and-opportunities/`
- **Purpose:** the build layer. Seeds in `inbox/` → curated one-pagers in `opportunities/`
  → weekly synthesis reports.
- **Folder contract:**
  - `inbox/` — seed-stage ideas (`YYYY-MM-DD-slug.md`), short but with a wedge.
  - `opportunities/` — full one-pagers (800+ lines, build-ready), **uses
    [`_templates/opportunity.md`](_templates/opportunity.md)**.
  - `*weekly-gap-report-*.md`, `*-weekly-gap-synthesis.md` — **cron-generated, STALE by
    design**. Read for leads, then curate into `_meta/BACKLOG.md`.
- **Promotion gate (inbox → opportunities):** promote when the seed has (1) proven WTP,
  (2) a clear GTM motion, (3) a buildable architecture. Keep the inbox file as the
  origination log (don't delete; don't duplicate — e.g. halal inbox copy is now redundant
  with the `opportunities/` one-pager).

---

## 3. The enrichment loop (what cron runs)

| Cron job | Stage(s) | Cadence | Action |
|----------|----------|---------|--------|
| `id-miner` | 01→03 | daily | Run `01` queries, write new `demand-mining/*.md` + INDEX rows |
| `filler` | 03 | daily | Backfill competitor/bottleneck docs from accumulated pains |
| `market-pulse` | 05 | every 6h | Fetch crypto/fx/IHSG → `05/data/` (with health gate) |
| `harga-pangan` | 06 | daily | Fetch SP2KP → `06/data/` |
| `synthesizer` | 03+07 | weekly | Cross-read all folders → write `07` reports + new-gap backlog |

**Cadence note:** the synthesizer should `ls` the 7 canonical folders first and report any
missing ("phantom folder" pattern), then diff each live feed against expected schema before
analyzing ("dead-feed" pattern). These two guards prevent the stale/contradictory reports
seen in the 2026-07-12 run.

---

## 4. Stage-to-stage gates (quality bar)

1. **Mine → Enrich:** a pain needs ≥3 sources + signal strength + verbatim evidence.
2. **Enrich → Bottleneck:** ≥3 related pains + a quantified root cause + a wedge.
3. **Bottleneck/Inbox → Opportunity:** proven WTP + GTM + architecture.
4. **Report → Backlog:** a human curates synthesis output into `_meta/BACKLOG.md`. Reports
   are never the source of truth.
5. **Build spec → Implement:** spec has endpoints + auth + tool surface + reference code.

---

## 5. Templates & conventions

- All canonical file shapes live in [`_templates/`](_templates/): `demand-mining.md`,
  `bottleneck.md`, `competitor.md`, `opportunity.md`, `inbox-seed.md`, `mcp-spec.md`,
  `pulse-data.json`.
- Every file starts with a header block (file path, created date, category, related files).
- Numbers tagged `verify-live` in any doc are **unverified this run** — never present them
  as fact. Live web verification requires `PARALLEL_API_KEY` in the agent env.
- Credential hygiene: reference `config.json` / JWT / access_token by **name only**.
  `.gitignore` blocks the actual files. See [`_meta/CONVENTIONS.md`](_meta/CONVENTIONS.md).

---

## 6. Regenerating the synthesis (clean run)

1. `ls` `01`–`07` (+ `_meta`); record any missing folder → structural gap.
2. Health-check `05/data/latest.json` and `06/data/latest.json`; fall back to last-good if
   degraded; note it in the report.
3. Cross-read folders, build clusters, emit `07/*-weekly-gap-*.md`.
4. Extract new gaps → `_meta/BACKLOG.md` as `proposed` (not `ready`).
5. A human reviews BACKLOG, promotes items to `ready`/`in-progress`, and assigns owners.
