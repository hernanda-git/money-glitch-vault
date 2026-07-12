# AUTO-ENRICH — the self-driving pipeline

> How the vault enriches itself with minimal human touch. This wires the `_meta/` guards,
> the `01→07` stages, and the cron cadence into one loop, then routes weekly synthesis output
> back into `_meta/BACKLOG.md` as draft items. Read `PIPELINE.md` first for the stage topology.

**File:** `_meta/AUTO-ENRICH.md`
**Created:** 2026-07-12
**Owner:** the cron layer + weekly human review

---

## 1. The loop

```
        ┌─────────────────────────────────────────────────────────────┐
        │                                                             │
   01 crawl ──► 03 mine ──► 04 build-specs ──► 07 synthesize ──► BACKLOG draft
        ▲            │            │                  │                 │
        │        05/06 data   MCP servers      weekly report       human triage
        │            │            │                  │                 │
        └──────── guards: validate-pulse · check_secrets · dedup_pains ┘
```

Every stage has a guard so bad data can't silently propagate (the failure mode that made
the vault call its own live feed "dead").

## 2. Cron jobs (proposed cadence)

> **ACTUALLY WIRED** — see `_meta/CRON-SETUP.md` for the live schedule (WSL Hermes runs the
> Python; Windows Hermes wraps delegate to WSL). Job names: `mgv-pulse-heal`, `mgv-pulse-watch`
> (→ Telegram), `mgv-archive`, `mgv-backlog`, `mgv-secret-scan` (→ Telegram), each with a
> `-win` twin on the Windows Hermes.

| Job | Schedule | Command | Guard / exit contract |
|-----|----------|---------|----------------------|
| **market-pulse** (`mgv-pulse-heal`) | every 6h | `05-market-cron/cron-configs/merge-equity-into-latest.py` | merge heals IHSG + IDX movers legs; `validate-pulse.py` exit ≠0 → alert, don't publish |
| **pulse-health-watchdog** (`mgv-pulse-watch`) | daily 00:00 | `_meta/pulse-health-watchdog.py --quiet-ok` | exit 1 (DEGRADED) / 2 (DEAD) → deliver alert via Telegram (`--deliver telegram`); healthy = silent |
| **pulse-archive** | weekly Sun | `python _meta/archive_pulses.py --days 7 --apply --git` | moves stale pulses to `08-research-archive/market-pulses/` |
| **price-arbitrage-radar** | daily | `python 06-harga-pangan-papan/normalize_region.py 06.../latest.json` | prints commodity/region >+15% → feed to warung pilot |
| **compliance-deadline-watch** | daily | `01` query `("PP" OR "Permen" OR "SE") (UMKM OR kreator) lang:in` | new regulatory shock → inbox seed (P4 bundle) |
| **pain-dedup** | weekly (pre-synthesis) | `python _meta/dedup_pains.py 03-.../demand-mining` | canonical count feeds the synthesis, not raw file count |
| **weekly-synthesis** | weekly Sun | existing 07 synth prompt | consumes deduped count + healthy pulse; emits report |
| **secret-scan** | pre-commit hook | `python _meta/check_secrets.py --staged` | exit 1 blocks commit |

> All cron jobs that deliver alerts must target a gateway-connected channel (Telegram/WA),
> not a local-only TUI session.

## 3. Report → BACKLOG wiring (the key automation)

The weekly synthesis already emits "New gaps discovered" and cluster labels. AUTO-ENRICH
closes the loop by turning those into **draft backlog items** for human triage:

```
07 weekly report  ──parse "New gaps"──►  _meta/BACKLOG.md  (## Draft — auto-proposed)
                                              │
                                        human keeps / kills / promotes
                                              │
                                        READY (R-series) ──► build
```

Rules:
- Auto-drafts land under a dedicated `## Draft — auto-proposed (unreviewed)` heading, never
  directly in READY. A human promotes them (matches the inbox→opportunities gate).
- Each draft cites its source report line (provenance, not hallucination).
- Dedup against existing BACKLOG items by slug before appending.

## 4. Guard contracts (why the loop is safe)

- **validate-pulse.py** — no stage trusts `latest.json` without it; exit ≠0 means the equity
  or crypto leg is dead and the synthesis must say so (never fabricate "live").
- **check_secrets.py** — nothing with a real token shape can be committed (D4).
- **dedup_pains.py** — the "82 pains" count is canonicalized so promotion doesn't double-count.
- **archive_pulses.py** — keeps the data folder bounded; history preserved in `08`.
- **merge-ihsg-into-latest.py** — heals the known-broken IHSG leg every tick, idempotently.

## 5. Human-in-the-loop gates (deliberate friction)

Two gates stay manual by design (per `CONVENTIONS.md` / `PIPELINE.md`):
1. **inbox → opportunities** — a human promotes a seed to a build-ready one-pager.
2. **Draft → READY** — a human accepts an auto-proposed backlog item.

Everything else (fetch, validate, archive, dedup, radar, deadline-watch) runs unattended.

## 6. What's NOT automated yet (honest gaps)

- ✅ **Report→BACKLOG parser IS NOW IMPLEMENTED** — `_meta/report_to_backlog.py`
  (dry-run + `--apply`; extracts the "New gaps" table/bullets from the latest synthesis;
  dedups against existing BACKLOG so re-runs never double-count; verified: skipped 6 already-
  done items and surfaced the 1 real new gap). Wire it as a cron job after each weekly synthesis.
- ✅ **Both equity legs healed** — `idx-movers-fetch.py` (v8 chart, LQ45+flagship basket)
  plus `merge-equity-into-latest.py` (renamed from the IHSG-only orchestrator). Verified live
  2026-07-12: `live sources: crypto, fx, ihsg, idx_movers, trending_coins` — the feed once
  called "100% dead" is now fully HEALTHY.
- ✅ **Alert transport wired** — `_meta/pulse-health-watchdog.py` runs `validate-pulse.py` and
  delivers a DEGRADED/DEAD alert via `PULSE_ALERT_*` env (Telegram / Discord / generic webhook);
  exits non-zero so a wrapping cron `deliver=` target can also carry it. No creds are committed
  (env-only). Verified: healthy→silent, degraded→alert (stdout when no transport set).

**Zero open items remain in the original backlog.** The vault is now structurally coherent,
self-enriching, and the market feed is live end-to-end.
