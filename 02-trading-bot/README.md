# 📈 02 — Trading Bot

Bot architectures, strategies, broker integrations, backtests. **Not financial advice — this is a research vault.**

## Asset classes tracked

- IHSG stocks (IDX via Ajaib / Stockbit / RTI)
- US stocks / ETFs
- Forex (OANDA, MT4/MT5)
- Crypto (Binance, Bybit, Indodax, Tokocrypto)
- Commodities (gold, crude palm oil, coal — relevant for ID)

## Sub-folders

- `architectures/` — event-driven, grid, DCA, mean-reversion, arbitrage, copy-trading
- `brokers-apis/` — per-broker notes, auth flow, rate limits, gotchas
- `strategies/` — entry/exit rules, parameters, edge thesis
- `backtests/` — historical results, walk-forward, monte carlo
- `live-deployments/` — running bots (configs, not secrets)
- `risk-management/` — position sizing, kill switches, drawdown caps
- `signals/` — incoming market calls (news, technical, on-chain)

## Strategy ideas to research

- [ ] IDX opening-range breakout (09:00-09:30 WIB)
- [ ] Crypto funding-rate arbitrage across CEX
- [ ] Palm-oil futures spread vs CPO global
- [ ] IDR/USD mean reversion on BI rate decision days
- [ ] X sentiment → next-day crypto pump prediction

## Tooling

- Python: `ccxt`, `pandas-ta`, `vectorbt`, `backtrader`
- Node: `binance`, `tulip`
- Brokers w/ API: Binance, Bybit, Indodax, Ajaib, Stockbit, Interactive Brokers
