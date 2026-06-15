# 📊 05 — Market Cron Jobs

Scheduled intelligence on markets that matter. All cron jobs write to this folder, version-controlled so you can diff sentiment week-over-week.

## Sub-folders

- `ihsg/` — IDX composite, sector indices, top movers
- `forex/` — USD/IDR, major pairs, BI rate calendar
- `crypto/` — BTC, ETH, IDR pairs, on-chain flows
- `stocks-id/` — watchlist of ID-listed names
- `stocks-us/` — watchlist US names
- `news-sentiment/` — scored headlines per ticker
- `forecasts/` — weekly outlook notes
- `cron-configs/` — actual cron / systemd / GitHub Actions YAML

## Data sources

- IHSG: RTI Business, Stockbit, Ajaib, Yahoo Finance `.JK`
- Forex: openexchangerates, BI, OANDA
- Crypto: CoinGecko, Binance, Coinglass (funding/OI), Glassnode
- News: Google News RSS, Kontan, Bloomberg, CoinDesk

## Cron schedule (WIB)

- `05:50` — pre-market ID briefing
- `09:30` — IHSG opening summary
- `12:00` — crypto + US pre-market
- `16:00` — IHSG close recap
- `22:00` — US mid-session + crypto funding
- `06:00 Sunday` — weekly forecast digest

## Setup (to do)

- [ ] Pick scheduler: `cronjob` (Hermes) vs GitHub Actions vs VPS crontab
- [ ] Wire each into a stable script under `cron-configs/`
- [ ] Auto-commit outputs so the vault history is the audit trail
- [ ] Add Telegram digest summarizer
