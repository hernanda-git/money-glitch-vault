# BACKLOG.md — future works & auto-enrich pipeline

> **This is the curated "what to build / enrich next" queue.** It is the single source of
> truth for future work — not the weekly `07/*-weekly-gap-*.md` reports (those go stale and
> have contradicted reality; they feed *here*, a human curates *from* them).
>
> Status vocabulary: `proposed` (extracted from a report, unvetted) → `ready` (vetted,
> should be done) → `in-progress` → `done` → `dropped`. Update status inline as work moves.

---

## How this backlog is maintained

1. The weekly synthesizer writes `07-gaps-and-opportunities/*-weekly-gap-*.md` (leads only).
2. A human reads the report, promotes the real items here as `proposed`.
3. Items get vetted → `ready`, then assigned and worked → `in-progress` → `done`.
4. Every `done` item is reflected in `CHANGELOG.md` (one line).

---

## 🔴 READY — highest leverage

| # | Work | Type | Folder target | Status | Effort |
|---|------|------|---------------|--------|--------|
| R1 | **Regenerate the weekly synthesis cleanly** | process | `07` + this file | ✅ **done** | S |
| R2 | **`qris-settlement-mcp` spec** | build spec | `04-freelancer-ai-agent/mcp-servers/` | ✅ **done** | S |
| R3 | **`anchor-of-trust-registry`** | research | `03-id-business-trends/bottlenecks/` | ✅ **done** (cross-cutting `lookup_trust` registry) | M |
| R4 | **Scaffold `02/risk-management/` + `02/signals/`** | build | `02-trading-bot/` | ✅ **done** (Kelly sizing + sentiment scoring) | M |

---

## 🟡 PROPOSED — ✅ ALL DONE (2026-07-12 pass)

| # | Work | Type | Folder target | Status |
|---|------|------|---------------|--------|
| P1 | `settlement-float-convergence` | research | `03/.../bottlenecks/` | ✅ done |
| P2 | `warung-region-aware-stock` | spec | `03/.../bottlenecks/` | ✅ done |
| P3 | `micro-legaltech-engine` seed | spec | `07/inbox/` | ✅ done |
| P4 | `deadline-driven-saas-bundle` note | note | `07/inbox/` | ✅ done |
| P5 | `agri-input-mcp` | spec | `04/.../mcp-servers/` | ✅ done |
| P6 | `logistics-orchestrator-mcp` | spec | `04/.../mcp-servers/` | ✅ done |
| P7 | Promote 4 inbox → opportunities (MBG, net-margin, bills, desil/dormant) | promote | `07/opportunities/` | ✅ done |

---

## 🟠 DATA / INFRA — ✅ ALL DONE (tooling built + verified)

| # | Work | Status | Artifact |
|---|------|--------|----------|
| D1 | Harden `05` pulse + heal IHSG leg | ✅ done (verified: IHSG now live, close 5924.36) | `05-market-cron/cron-configs/merge-ihsg-into-latest.py` |
| D2 | Normalize `06` region column | ✅ done | `06-harga-pangan-papan/normalize_region.py` |
| D3 | Dedup/canonicalize `01`/`03` pains | ✅ done (verified: 81 canonical, 0 dupes) | `_meta/dedup_pains.py` |
| D4 | Redaction pre-commit check | ✅ done (verified: clean) | `_meta/check_secrets.py` |
| D5 | Archive stale `05` pulses >7d | ✅ done (dry-run verified) | `_meta/archive_pulses.py` |

---

## 🟢 AUTO-ENRICH — make the pipeline self-driving (the ask)

Concrete automation to bolt onto the existing cron jobs so enrichment compounds without
a human re-prompting each week:

1. **Self-healing synthesis (R1 hardening).** Add two guards to the synthesizer prompt
   (from the 2026-07-12 "self-evolution note"):
   - *Phantom-folder guard:* `ls` the 7 canonical folders; if one is missing, report it as
     a structural gap AND treat its intended function as a buildable opportunity — never
     cite a non-existent folder as a fulfilled dependency.
   - *Dead-feed guard:* diff `latest.json` against expected schema; if ≥1 source isn't
     live, mark DEGRADED, fall back to last-good, and say so in the report.
2. **Report → Backlog auto-draft.** After each synthesis, have the cron append any "new
   gaps" it finds into a `proposed` section of *this* file (not committed as truth — a
   human flips `proposed` → `ready`). This keeps the backlog from rotting between reviews.
3. **Promotion nudge.** When an `inbox` seed hits 3+ related `demand-mining` pains or a
   proven-WTP signal, the synthesizer should flag it in the report as a promotion
   candidate (feeds P7).
4. **Pulse health cron.** A daily check that runs `validate-pulse.py` and posts DEGRADED to
   the same channel the synthesis reads, so R1/D1 close the loop automatically.

---

## Done (this structuring pass)
- ✅ Root `README.md` (vault map + pipeline overview + stale-report warning)
- ✅ `PIPELINE.md` (7-stage manual, gates, cadence, template refs)
- ✅ `_meta/` (VAULT-MAP, this BACKLOG, CONVENTIONS, validate-pulse.py, gen-map.sh)
- ✅ `_templates/` (7 canonical templates)
- ✅ Relocated 4 orphaned root recaps → `08-research-archive/`
- ✅ `.gitignore` (secrets/scratch)
- ✅ **R1 — Regenerated the synthesis cleanly:** corrected `weekly-gap-report-2026-07-12.md` (false "phantom" claims about `04`/`02`, and "100% dead feed" → actually crypto/fx live, equity 429) and `*-weekly-gap-synthesis.md` (stale 50→82 pain count), added in-place correction notes, and fixed README's overclaim.
- ✅ **R2** — `qris-settlement-mcp.md` (advance/get_float/reconcile, netting engine, reuse map).
- ✅ **R4** — `02/risk-management/position-sizing-kelly.md` + `02/signals/news-sentiment-scoring.md` (Kelly sizing, drawdown cap, sentiment→win-prob prior).
- ✅ **P1** — `settlement-float-convergence.md` (unifies COD+QRIS+logistics float thesis).
- ✅ **P2** — `warung-region-aware-stock.md` (closes 07↔06 loop).
- ✅ **P3** — `2026-07-12-micro-legaltech-engine.md` inbox seed (5 use-cases).
- ✅ **P4** — `2026-07-12-deadline-driven-saas-bundle.md` inbox note (shared GTM).
- ✅ **P5** — `agri-input-mcp.md` (sawit/pupuk price + subsidy MCP).
- ✅ **P6** — `logistics-orchestrator-mcp.md` (B2B multi-carrier orchestration MCP).
- ✅ **P7** — promoted 4 inbox seeds → `07/opportunities/` (MBG compliance, marketplace net-margin, household bills tracker, desil/dormant checker).
- ✅ **D1–D5** — runnable + verified tooling: `merge-ihsg-into-latest.py` (heals IHSG leg, verified close 5924.36), `normalize_region.py`, `dedup_pains.py` (81 canonical), `check_secrets.py` (clean), `archive_pulses.py`.
- ✅ **AUTO-ENRICH** — `_meta/AUTO-ENRICH.md` self-driving pipeline (cron cadence, guard contracts, report→BACKLOG wiring, human gates, honest gaps).
- ✅ **R3** — `anchor-of-trust-registry.md` (cross-cutting `lookup_trust(entity)` registry for judol/scam/desil/dormant/MBG; reference interface + 5 anchor sources).
- ✅ **report→BACKLOG parser** — `_meta/report_to_backlog.py` (dry-run + `--apply`; table/bullet extraction; dedup against existing BACKLOG; verified: skipped 6 done items, surfaced the 1 real new gap).

## Still open
- `idx_movers` still 429 (needs a v8-based movers fetcher); alert transport not wired to a gateway channel.
