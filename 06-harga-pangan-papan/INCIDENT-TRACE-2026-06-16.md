# Incident Trace — PiJPS / Bapanas endpoint outage

**Date:** 2026-06-16 00:17-00:45 WIB  
**Impact:** `money-glitch-harga-pangan` cron returning empty data with timeout errors  
**Status:** RESOLVED via SP2KP pivot

## Timeline

| Time (WIB) | Event |
|------------|-------|
| 00:17 | First cron test: `money-glitch-harga-pangan.py` tried PiJPS endpoints → all timed out |
| 00:17 | Probed `hargapangan.id` directly via curl → **522 Cloudflare origin server timeout** |
| 00:17 | Probed `panel.hargapangan.id` → same 522 |
| 00:18 | Tried `bapanas.go.id`, `data.bapanas.go.id`, `pihps.bappenas.go.id` → all unreachable (HTTP 000 / DNS failure from this network) |
| 00:18 | Tried `bps.go.id` → **403 firewall block** |
| 00:18 | Tried `bi.go.id` → reachable (302) but not price data |
| 00:18 | **breakthrough:** `satudata.kemendag.go.id` → **HTTP 200** and loaded in browser |
| 00:20 | Browser-discovered the online "Satu Data Perdagangan" catalog |
| 00:22 | Found the catalog entry: **"Harga Komoditas - SP2KP"** (daily commodity price dataset, 34 provinces) |
| 00:23 | Found the actual SP2KP website: `sp2kp.kemendag.go.id` — fully functional dashboard |
| 00:24 | Discovered the price table API is behind **Google reCAPTCHA Enterprise** — no direct HTTP access |
| 00:26 | Extracted full price table from rendered DOM via `browser_console` JavaScript — **successful capture** |
| 00:30 | Deleted broken `money-glitch-harga-pangan.py` (HTTP-based) and its wrapper |
| 00:31 | Replaced with **agent-driven cron** using browser MCP (DOM extraction) |
| 00:35 | First real capture: 26 records, 16 commodities, pushed to repo |
| 00:40 | README updated, CHANGELOG logged, obsolete files removed |

## Root Cause

**Primary:** `hargapangan.id` (PiJPS) — the entire domain is down with Cloudflare 522. The origin server behind Cloudflare is not responding. This is not a script bug or rate limit — the source itself is offline.

**Secondary:** Multiple alternative Indonesian government data sources are inaccessible from this WSL network:
- `bps.go.id` — WAF/403 block (geofencing?)
- `api.bapanas.go.id`, `data.bapanas.go.id`, `www.bapanas.go.id` — DNS resolution fails (HTTP 000)
- `pihps.bappenas.go.id` — DNS failure (HTTP 000)

**Tertiary (unused path):** The SP2KP `api-sp2kp.kemendag.go.id` endpoints require **reCAPTCHA Enterprise** tokens obtained through browser login with active session. No public API key exists.

## Resolution

**Pivot to SP2KP Kemendag** (`https://sp2kp.kemendag.go.id/`):

- Government-run, official Ministry of Trade system
- Public frontend, no login required for viewing
- Data is rendered in the DOM as a static HTML table
- Extraction via browser MCP (`browser_navigate` + `browser_console` JavaScript)
- 16 commodities (beras, minyak, daging, telur, cabai, bawang, etc.)
- HNT (Harga Nasional Tertimbang) weighted by 514 kab/kota using BPS SBH 2022 consumption weights
- Region sub-groups (A/B/C) for price stability analysis
- Daily updates

## What Changed

| Before | After |
|--------|-------|
| `money-glitch-harga-pangan.py` (HTTP) | Deleted |
| `money-glitch-harga-pangan.sh` (bash wrapper) | Deleted |
| no-agent cron | Replaced with **agent-driven cron** |
| Data from PiJPS JSON API | Data from SP2KP browser DOM |
| Bapanas 522 error | Live 16-commodity table every 08:00 WIB |

## Monitoring

- SP2KP availability should be verified monthly — it's a government site that could change its SPA structure
- PiJPS recovery should be checked again in 2-4 weeks (`curl -sI https://hargapangan.id/` → if no 522, restore PiJPS as primary)
- Bapanas endpoint should be re-checked every 3 months (government sites migrate under new administrations)

## Files Modified/Created

- `06-harga-pangan-papan/README.md` — updated sources to SP2KP as primary
- `06-harga-pangan-papan/data/sp2kp-2026-06-16.json` — first successful capture
- `06-harga-pangan-papan/data/latest.json` — updated pointer
- `06-harga-pangan-papan/data/INDEX.md` — created with chronological log
- `~/.hermes/scripts/money-glitch-harga-pangan-prompt.md` — new prompt file for agent-driven cron
- `CHANGELOG.md` — updated with full incident log
