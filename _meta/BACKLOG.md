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

## 🔴 READY — highest leverage, do these next

| # | Work | Type | Folder target | Why now | Effort |
|---|------|------|---------------|---------|--------|
| R1 | **Regenerate the weekly synthesis cleanly** | process | `07` + this file | Current `07` reports call `04` and `02/strategies` "phantom" — both now exist. Reports are stale/contradictory. See `PIPELINE.md §6`. | S |
| R2 | **`qris-settlement-mcp` spec** | build spec | `04-freelancer-ai-agent/mcp-servers/` | Explicitly requested in `qris-settlement-speed-arbitrage.md §19`, never built. The connective tissue for the settlement cluster. Reuse `fastwork-mcp-spec.md` pattern. | S |
| R3 | **`anchor-of-trust-registry`** | research | `03-id-business-trends/bottlenecks/` | The cross-cutting insight: judol, scam-detection, desil/dormant, MBG compliance all need one `lookup_trust(entity)` registry. Write it before the 4 products diverge. | M |
| R4 | **Scaffold `02/risk-management/` + `02/signals/`** | build | `02-trading-bot/` | `binance-spot-futures.md` references these layers; they're absent. The ORB strategy needs a risk engine (Kelly / drawdown) the `04` agent consumes. | M |

---

## 🟡 PROPOSED — vetted from 2026-07-12 synthesis, not yet started

| # | Work | Type | Folder target | Source | Effort |
|---|------|------|---------------|--------|--------|
| P1 | `settlement-float-convergence` — unify COD+QRIS+logistics float thesis | research | `03/.../bottlenecks/` | synthesis Cluster A | M |
| P2 | `warung-region-aware-stock` — close 07↔06 loop via normalized region | spec | `03/.../bottlenecks/` | synthesis Cluster B | S |
| P3 | `micro-legaltech-engine` — promote 2026-07-09 seed to build-ready | spec | `07/inbox/` | synthesis Cluster D | S |
| P4 | `deadline-driven-saas-bundle` — shared GTM note (MBG+halal+margin+bills) | note | `07/inbox/` | synthesis Cluster E | S |
| P5 | `agri-input-mcp` — sawit/pupuk price+MCP mirroring Fastwork | spec | `04/.../mcp-servers/` | synthesis Cluster F | S |
| P6 | `logistics-orchestrator-mcp` — B2B last-mile sibling (ref'd but missing) | spec | `04/.../mcp-servers/` | lalamove teardown Gap 5 | S |
| P7 | **Promote inbox → opportunities:** MBG compliance, marketplace net-margin, household bills tracker, desil/dormant checker | promote | `07/opportunities/` | synthesis §5 | S |

---

## 🟠 DATA / INFRA — non-product gaps that block downstream enrich

| # | Work | Why it matters | Effort |
|---|------|----------------|--------|
| D1 | **Harden `05` pulse parser** against `_error` objects + add IHSG retry/backoff | Current feed returns 100% errors some weeks; synthesis analyzes nothing. Run `python _meta/validate-pulse.py` as a guard. | S |
| D2 | **Normalize `06` region column** (Nasional/Region A/B/C → province/kabupaten taxonomy) | Unblocks region-aware restock/arbitrage alerts (warung one-pager phase-2). | M |
| D3 | **Add dedup/canonicalization layer for `01` pains** | Same pain surfaces 5×/week in different phrasings; needed before any trust registry works. | M |
| D4 | **Redact Fastwork `config.json` creds** before any push | `fastwork-mcp-spec.md` references JWT/access_token/user_id by name — ensure never committed. `.gitignore` already blocks `config.json`. | S |
| D5 | **Archive stale `05` pulses** older than 7 days once feed is healthy | Noise reduction. | S |

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
