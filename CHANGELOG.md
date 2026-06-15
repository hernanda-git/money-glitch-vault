# Changelog — money-glitch-vault

## 2026-06-16 — Initial scaffold
- Repo created: `hernanda-git/money-glitch-vault` (private)
- 7 topic folders + README per folder
- `.gitignore` for secrets and raw data
- Folder layout modeled after `ai-knowledge-library`

## 2026-06-16 — Self-enriching cron pipeline (5 jobs)
- 3 no-agent data jobs: market-pulse, harga-pangan, auto-commit
- 2 LLM agents: id-miner, filler
- 1 weekly synthesizer
- All scripts tested end-to-end with real CoinGecko + Yahoo Finance data
- First market pulse captured: BTC $66,865, ETH $1,830, USD/IDR 16,848, IHSG pending Yahoo rate-limit recovery
- Data files (pulse-*.json, harga-*.json) committed and pushed

## 2026-06-16 — harga-pangan pipeline pivoted to SP2KP Kemendag
- Original PiJPS/Bapanas endpoints all dead (Cloudflare 522 on hargapangan.id, BPS firewall blocks, Bapanas subdomains unreachable)
- Discovered **SP2KP Kemendag** (https://sp2kp.kemendag.go.id/) is alive and serves live HNT (Harga Nasional Tertimbang) for 16 commodities × 514 kab/kota
- Converted `money-glitch-harga-pangan` cron from no_agent (HTTP scraper) to **agent-driven with browser MCP** (browser_navigate + browser_console extract)
- Deleted obsolete Python scraper + wrapper
- First successful capture: 26 records (16 commodities + 10 region sub-rows), top movers Cabai Merah Besar -2.21%, Bawang Merah -1.71%
- README updated to reflect SP2KP as primary source
- Data files: `sp2kp-2026-06-16.json`, `latest.json`, `INDEX.md`
