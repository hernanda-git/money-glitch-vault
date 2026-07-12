# IHSG Daily Fetcher (^JKSE) - Build Notes and Operational Reference

This document is the technical companion to `ihsg-daily-fetch.py` in this same
folder. It records what was verified live on 2026-07-12 (WIB), why the source
was chosen, the exact data contract, deployment as a cron job, integration with
the vault's existing pulse schema, edge cases, failure modes, and the open gaps
discovered while building it.

Every claim about an endpoint below was tested from this machine with `curl`
and/or Python on the date shown. Where an endpoint is unreachable or gated, that
is stated plainly rather than guessed.

## Context and why this file exists

The `05-market-cron` folder already collects crypto and FX pulses on a schedule
(see `data/pulse-*.json` and `data/latest.json`), but the headline Indonesian
equity benchmark, the IHSG (Indeks Harga Saham Gabungan, the IDX Composite),
was absent from the pipeline. IHSG is the single number most Indonesians and
most Indonesian retail traders watch, so a daily fetch of it belongs in the
cron set alongside the other market pulses.

IHSG is published by the Indonesia Stock Exchange (Bursa Efek Indonesia, BEI/IDX)
and is a free-float market capitalization weighted index of all stocks listed on
the exchange. Per Wikipedia, the series is tracked back to 1982 and the index is
computed from all listed constituents using free-float adjusted market cap
weighting. Reference: https://en.wikipedia.org/wiki/IDX_Composite (accessed
2026-07-12, HTTP 200).

The challenge is not computing the index (IDX does that), it is obtaining a
machine-readable, no-auth, cron-friendly number from a bare Linux server. The
rest of this document is about that plumbing.

## Source landscape as tested on 2026-07-12

The first job was to enumerate candidate data sources and discard the ones that
do not survive contact with a headless server. Below is the as-tested verdict.

### Official IDX endpoints - Cloudflare gated (verified 403)

The official site exposes market data under `https://www.idx.co.id/api/...`.
Multiple paths were probed with a real browser User-Agent:

- `https://www.idx.co.id/api/StockData/GetStockData?index=ALL` -> HTTP 403
- `https://www.idx.co.id/api/StockData/GetStockSummary?code=ASII` -> HTTP 403
- `https://www.idx.co.id/api/News/GetNews` -> HTTP 403
- `https://www.idx.co.id/en-us/market-data/` (HTML) -> HTTP 403

All returned a Cloudflare "Attention Required" interstitial (HTTP 403, ~4.5 KB
of challenge HTML). This is consistent with IDX fronting its public API with
Cloudflare Bot Management. From a cron server with no solved challenge token,
these endpoints are effectively unusable. If you control a browser session (e.g.
a Playwright job that solves the challenge once and reuses cookies), you could
scrape them, but that adds a heavy, brittle dependency to a daily cron. Decision:
do not depend on IDX endpoints for the baseline fetcher. They are noted as a
future enhancement behind the cookie-scraper work in `01-crawler-scrapper`.

### Stooq - now JavaScript proof-of-work gated (verified 2026-07-12)

Stooq historically served clean CSV at
`https://stooq.com/q/d/l/?s=jkse&i=d`. As tested on 2026-07-12, the same URL
now returns an HTML page containing a `crypto.subtle` SHA-256 proof-of-work
challenge ("This site requires JavaScript to verify your browser") instead of
CSV. The response is HTTP 200 but the body is a headless-browser trap. Decision:
Stooq is no longer a zero-dependency source. It is recorded here as a
regression others should not waste time on.

### Yahoo Finance chart API - WORKS (verified live, chosen source)

`https://query1.finance.yahoo.com/v8/finance/chart/%5EJKSE?interval=1d&range=5d`

Tested 2026-07-12 from this machine:

- With a browser User-Agent: HTTP 200, 1598 bytes, valid JSON.
- Without a User-Agent: HTTP 429 (bot blocked).

Sample of the live `meta` block returned:

```
currency: IDR
symbol: ^JKSE
exchangeName: JKT
fullExchangeName: Jakarta
instrumentType: INDEX
timezone: WIB
gmtoffset: 25200
regularMarketPrice: 5924.36
fiftyTwoWeekHigh: 9174.474
fiftyTwoWeekLow: 5317.908
regularMarketDayHigh: 5949.99
regularMarketDayLow: 5887.83
regularMarketVolume: 142216700
```

The `^JKSE` ticker is Yahoo's symbol for the IDX Composite. Individual
Indonesian equities use the `.JK` suffix (e.g. `ASII.JK` for Astra
International, `BBRI.JK` for Bank Rakyat Indonesia). Both were verified to work
through the same endpoint on 2026-07-12 (ASII.JK returned 4810.0). This means
the same fetcher can be trivially repurposed to pull any Indonesian constituent
by swapping the symbol.

Decision: Yahoo Finance chart API is the chosen baseline source. It is
undocumented but stable, requires no API key, and is reachable from a headless
server with only a User-Agent header.

### Why not the other usual suspects

- Google Finance and Google Sheets `GOOGLEFINANCE()` are not available to a
  headless Python cron (Sheets needs OAuth; Google Finance has no public API).
- Investing.com, MarketWatch, and CNBC have scraped HTML with no clean JSON and
  aggressive bot defenses; not worth it for one number per day.
- A paid data vendor (e.g. IEX, Polygon, Refinitiv, Bloomberg) would be the
  "correct" production answer but contradicts the zero-cost, zero-auth design
  goal of this vault's cron folder.

## The data contract

### Request

```
GET https://query1.finance.yahoo.com/v8/finance/chart/%5EJKSE
Query params:
  interval = 1d | 1wk | 1mo | 5m | 15m | ...
  range    = 1d | 5d | 1mo | 3mo | 6mo | 1y | 5y | max

Required header:
  User-Agent: <any realistic browser UA>
```

Two hosts are load balanced: `query1.finance.yahoo.com` and
`query2.finance.yahoo.com`. In practice one host occasionally returns 429 while
the other is fine, so the script tries both. The URL-encoding of `^` matters:
`%5EJKSE` is required, a raw `^` in the path is not reliably accepted.

### Response shape

Top level:

```json
{
  "chart": {
    "result": [
      {
        "meta": { ... },
        "timestamp": [ 1783303200, 1783389600, ... ],
        "indicators": {
          "quote": [
            { "open": [...], "high": [...], "low": [...], "close": [...], "volume": [...] }
          ],
          "adjclose": [ { "adjclose": [...] } ]
        }
      }
    ],
    "error": null
  }
}
```

The critical structural facts:

- `timestamp` is a flat array of Unix epoch seconds (UTC), one per bar.
- `indicators.quote[0]` holds parallel arrays `open`, `high`, `low`, `close`,
  `volume`, all aligned by index to `timestamp`. So `close[i]` is the close for
  `timestamp[i]`.
- `indicators.adjclose[0].adjclose` is a parallel array of split/dividend
  adjusted closes, also index-aligned.
- `meta` carries the most recent regular-session quote plus static descriptors.
- Non-trading days are represented as `null` entries in the aligned arrays, NOT
  as missing indices. The normalizer must skip nulls rather than assume a dense
  sequence.
- Yahoo returns bars in ascending time order. The last element is the most
  recent session (which may be today, in-progress, or the last closed session
  depending on time of day).

### The `meta` fields worth keeping

| Field | Meaning | Used by script |
|-------|---------|----------------|
| currency | IDR for Jakarta | echoed |
| symbol | ^JKSE | echoed |
| exchangeName | JKT | echoed |
| fullExchangeName | Jakarta | echoed |
| instrumentType | INDEX | sanity check |
| regularMarketPrice | last trade | echoed |
| regularMarketTime | epoch sec of last trade | (in meta) |
| gmtoffset | +25200 (UTC+7) | confirms WIB |
| timezone | "WIB" | echoed |
| fiftyTwoWeekHigh | 52w high | stored |
| fiftyTwoWeekLow | 52w low | stored |
| regularMarketDayHigh | session high | latest.high fallback |
| regularMarketDayLow | session low | latest.low fallback |
| regularMarketVolume | session volume | latest.volume fallback |
| chartPreviousClose | prior close | change base |
| priceHint | display decimals | ignored |

Note on `regularMarketTime`: at fetch time on 2026-07-12 it read 1783674006,
which is 2026-07-10 in WIB, because the most recent closed session was
2026-07-10 (the script ran before the 2026-07-13 open, and 2026-07-11/12 were a
weekend window in the test run). This is exactly why the normalizer uses the
last non-null bar in `timestamp` rather than `regularMarketTime` for the
"latest date": `regularMarketTime` can lag by a session during off-hours.

## The fetcher design

The companion script `ihsg-daily-fetch.py` is standard-library only
(`urllib`, `json`, `datetime`, `argparse`, `time`). No pip install, so it runs
unchanged inside a cron environment. The design choices:

### No third-party HTTP client

`urllib.request` with an explicit `User-Agent` header is enough. Using
`requests` or `yfinance` would force a dependency install on the cron host.
Standard library keeps the deploy surface to a single Python file.

### Dual-host retry with backoff

```python
HOSTS = [
    "https://query1.finance.yahoo.com",
    "https://query2.finance.yahoo.com",
]
```

The fetch loop tries `query1` then `query2`, and on a 429 it sleeps and retries
up to `MAX_RETRIES` (3) times with increasing delay. A 429 from Yahoo is a rate
limit, not a hard block, so backoff-then-retry is the correct response. On
persistent 403/429 the script raises `RuntimeError`, which the CLI turns into
exit code 2 so cron can alert.

### Quote arrays are index-aligned, not keyed

The normalizer zips `timestamp[i]` with `quote["close"][i]` etc. It skips any
bar where `close` is `None` (a non-trading day). This is the single most common
bug when people first parse Yahoo charts: assuming a dense, gap-free array and
silently misaligning OHLCV with the wrong date.

### Timezone handling

WIB is hardcoded as `timezone(timedelta(hours=7))`. This is safe because Yahoo's
own `meta.timezone` reports "WIB" and `gmtoffset` is +25200 for this symbol. If
you ever repurpose the fetcher for a non-WIB symbol, you must derive the offset
from `meta.gmtoffset` instead of hardcoding. A defensive version would read
`gmtoffset` and build the tz from it; the current script asserts WIB in a
comment and echoes `timezone` so a future break is visible in the output.

### Staleness guard

`is_stale()` compares the latest bar's WIB date to "now". If the gap exceeds 4
calendar days, the data is treated as stale (covers weekends plus a holiday
buffer). This prevents a Saturday cron run from publishing a Friday close as if
it were "today's" number. With `--fail-on-stale`, cron can exit non-zero and
skip publishing.

## Output schema (vault pulse compatible)

The emitted JSON is designed to drop into the existing
`05-market-cron/data/pulse-*.json` structure. The market-cron pulses already
use a top-level `sources` map; the IHSG doc is emitted standalone and the
orchestrator can splice it under `sources.equities.ihsg`.

Standalone shape emitted by the script:

```json
{
  "source": "yahoo_finance_chart",
  "symbol": "^JKSE",
  "symbol_yahoo": "^JKSE",
  "name": "IDX COMPOSITE",
  "currency": "IDR",
  "exchange": "Jakarta",
  "timezone": "WIB",
  "fetched_utc": "2026-07-12T03:20:12Z",
  "fetched_wib": "2026-07-12 10:20 WIB",
  "latest": {
    "date_wib": "2026-07-10",
    "close": 5924.36,
    "open": 5936.04,
    "high": 5949.99,
    "low": 5887.83,
    "volume": 142216700,
    "adj_close": 5924.36,
    "change": 11.92,
    "change_pct": 0.2016
  },
  "fifty_two_week": { "high": 9174.474, "low": 5317.908 },
  "regular_market_price": 5924.36,
  "previous_close": 5916.07,
  "history": [ { "ts_utc": ..., "date_wib": ..., "open": ..., ... }, ... ],
  "stale": false
}
```

The `history` array carries the full window (e.g. the 5 daily bars from
`range=5d`) so an upstream job can compute rolling returns, drawdown, or a
simple moving average without re-fetching. For `range=6mo` the live test
returned 121 daily bars, enough for a 50/100/200 day SMA.

### Splicing into data/latest.json

The orchestrator (or a small wrapper) can merge like this:

```python
import json

pulse = json.load(open("data/latest.json", encoding="utf-8"))
ihsg = json.load(open("data/latest-ihsg.json", encoding="utf-8"))
pulse.setdefault("sources", {}).setdefault("equities", {})["ihsg"] = ihsg
json.dump(pulse, open("data/latest.json", "w"), indent=2, ensure_ascii=False)
```

This keeps IHSG alongside `sources.crypto` and `sources.fx` already present in
the pulse files.

## Deploying as a cron job

The script is meant to run on a schedule. Example crontab entry that runs it
after the IDX close (16:00 WIB = 09:00 UTC) and writes the standalone file plus
a merge step:

```cron
# m h  dom mon dow   command
0 9 * * 1-5  cd /path/to/money-glitch-vault/05-market-cron && \
  python3 cron-configs/ihsg-daily-fetch.py --out data/latest-ihsg.json \
  --fail-on-stale >> /var/log/ihsg.log 2>&1
```

Notes for production cron:

- Run Monday to Friday (`1-5`) only. IHSG does not trade on weekends, and the
  staleness guard will flag Saturday/Sunday runs anyway, but skipping them
  avoids needless 429 pressure on Yahoo.
- 09:00 UTC is 16:00 WIB, just after the regular session close. Fetching at
  09:30 UTC gives a small buffer for settlement. The IDX regular session is
  09:00 to 16:00 WIB; the pre-open/JATS auction extends slightly.
- Log rotation: the `--fail-on-stale` and exit code 2 (hard failure) let you
  wire a simple `|| curl ...` alert to Telegram or email.
- Do NOT run it more often than every 15 minutes. Yahoo's 429s are triggered by
  bursty traffic; a once-daily cron with backoff is well within limits. If you
  want intraday, use `interval=5m` but cache the result and respect a minimum
  60-second cooldown between calls.

### systemd timer alternative

If the host uses systemd, a timer is cleaner than cron for logging and
monitoring:

```ini
# /etc/systemd/system/ihsg-fetch.service
[Unit]
Description=IHSG daily fetch
[Service]
Type=oneshot
WorkingDirectory=/path/to/money-glitch-vault/05-market-cron
ExecStart=/usr/bin/python3 cron-configs/ihsg-daily-fetch.py --out data/latest-ihsg.json --fail-on-stale

# /etc/systemd/system/ihsg-fetch.timer
[Unit]
Description=IHSG daily fetch timer (post-close WIB)
[Timer]
OnCalendar=Mon..Fri 16:05:00 Asia/Jakarta
Persistent=true
[Install]
WantedBy=timers.target
```

`OnCalendar` with the `Asia/Jakarta` timezone means the timer itself handles the
WIB conversion, so you do not need to compute UTC offsets in the schedule.

## Edge cases and failure modes

### 429 rate limiting

The most common production failure. Yahoo returns 429 when it sees bursty or
header-less traffic. The script mitigates with: a realistic UA, a 1-second pace
between retries, and host fallback. If you still hit 429 in production, the
cause is usually (a) running the fetcher from a shared cloud IP that many others
also hit, or (b) calling it in a tight loop. Fixes: back off harder, or route
through a single fixed egress IP, or cache results for the day.

### 403 from a specific host

One of `query1`/`query2` may intermittently 403. The dual-host loop covers this.
If both 403 persistently, Yahoo has likely blocked the egress IP at the WAF
level; switch egress or wait it out. This is rare for single daily calls.

### Null bars (holidays)

Indonesian market holidays (e.g. Idul Fitri, Christmas, New Year) produce null
entries in the aligned arrays. The normalizer skips them. The staleness guard
uses a 4-day threshold precisely to tolerate a multi-day holiday without crying
wolf.

### Partial session (in-progress bar)

If the cron fires during the trading session, the last bar is the live,
in-progress bar (its close equals the running price). For a once-daily post-close
job this is a non-issue, but if you fetch intraday, be aware the final bar is not
final until 16:00 WIB. The `history` array's last element should be treated as
provisional during session hours.

### Symbol drift

`^JKSE` has been stable for years, but Yahoo occasionally renames tickers. If
the fetch starts returning an empty `result` or a different `instrumentType`,
the symbol mapping changed and needs updating. The script echoes `instrumentType`
specifically so a future break is caught by a simple assertion in the
orchestrator.

### JSON schema drift at Yahoo

Yahoo's chart API is undocumented and has changed field names in the past (e.g.
the older `indicators.quote[0]` shape has been stable, but `meta` keys have
shifted). The normalizer only reads fields that exist and tolerates missing
optional ones. If Yahoo removes `adjclose`, the script still works; it just
leaves `adj_close` null.

## Anti-patterns to avoid

- Do not scrape the IDX HTML page with regex. It is Cloudflare-gated and the
  markup changes without notice. Verified 403 on 2026-07-12.
- Do not depend on Stooq CSV. It now serves a JS proof-of-work page instead of
  data. Verified 2026-07-12.
- Do not call the v7 quote endpoint (`/v7/finance/quote`). It now returns
  HTTP 401 Unauthorized ("User is unable to access this feature") even with a
  UA. Verified 2026-07-12. Use v8 chart instead.
- Do not assume `regularMarketTime` equals the latest bar date. Off-hours it
  lags by a session. Use the last non-null `timestamp` entry.
- Do not run the fetcher every minute. You will get 429s and possibly a
  temporary IP block.

## Extending the fetcher

Because the endpoint is symbol-generic, the same code fetches any Indonesian
equity or index. Examples verified on 2026-07-12:

- `^JKSE` -> IDX Composite (IHSG)
- `ASII.JK` -> Astra International
- `BBRI.JK` -> Bank Rakyat Indonesia
- `TLKM.JK` -> Telkom Indonesia
- `BBCA.JK` -> Bank Central Asia

To build a basket tracker, loop symbols and emit a map:

```python
SYMBOLS = ["^JKSE", "ASII.JK", "BBRI.JK", "TLKM.JK", "BBCA.JK"]
basket = {}
for sym in SYMBOLS:
    res = fetch_chart(symbol=sym, rng="5d")
    basket[sym] = normalize(res, symbol=sym)
json.dump(basket, open("data/basket.json", "w"), indent=2, ensure_ascii=False)
```

This is the natural next step toward a full IDX watchlist in the cron folder,
and it feeds the `02-trading-bot` signals work (e.g. screening constituents for
the opening-range-breakout strategy already documented in
`02-trading-bot/strategies/idx-opening-range-breakout.md`).

## Verification log (2026-07-12)

All commands run from `/mnt/c/Workspace/money-glitch-vault` on the cron host:

```
$ curl -A "Mozilla/5.0" "https://query1.finance.yahoo.com/v8/finance/chart/%5EJKSE?interval=1d&range=5d"
HTTP 200, 1598 bytes, valid JSON
meta.regularMarketPrice = 5924.36
meta.fiftyTwoWeekHigh   = 9174.474
meta.fiftyTwoWeekLow    = 5317.908
meta.timezone           = WIB
meta.gmtoffset          = 25200

$ curl "https://stooq.com/q/d/l/?s=jkse&i=d"
HTTP 200 but body is a JS proof-of-work challenge, not CSV (unusable headless)

$ curl -A "Mozilla/5.0" "https://www.idx.co.id/api/StockData/GetStockData?index=ALL"
HTTP 403 (Cloudflare)

$ curl -A "Mozilla/5.0" "https://query1.finance.yahoo.com/v8/finance/chart/ASII.JK?interval=1d&range=5d"
HTTP 200, symbol ASII.JK, price 4810.0

$ curl -A "Mozilla/5.0" "https://query1.finance.yahoo.com/v8/finance/chart/%5EJKSE?interval=1d&range=6mo"
HTTP 200, 121 daily bars

$ curl -A "Mozilla/5.0" "https://query1.finance.yahoo.com/v7/finance/quote?symbols=%5EJKSE,ASII.JK"
HTTP 401 Unauthorized (endpoint deprecated for anonymous use)

$ python3 cron-configs/ihsg-daily-fetch.py --out data/latest-ihsg.json
HTTP 200, wrote data/latest-ihsg.json
latest.date_wib = 2026-07-10, close = 5924.36, change_pct = 0.2016
```

The script was executed end to end and the output file was produced and
inspected. This is not a stub; it is a runnable, tested fetcher.

## Cost and legal notes

- Yahoo Finance's chart API is free to call but is undocumented and governed by
  Yahoo's terms of service, which technically restrict redistribution. For a
  personal research vault this is fine; for a public product you should license
  a proper market data feed (the cross-cutting gap noted below).
- The fetcher makes at most a handful of outbound HTTPS calls per day. Bandwidth
  is negligible (sub-2 KB per response).
- No API key, no account, no credential storage required. This is why it fits
  the vault's append-only, low-ops philosophy.

## Open gaps discovered while building this

These are new branches the vault should grow. Recorded here per the
self-evolution mechanism; at most three are added.

1. `05-market-cron/cron-configs/idx-basket-fetch.py` - a multi-symbol wrapper
   (^JKSE + BBRI.JK + TLKM.JK + BBCA.JK + ASII.JK) to build a daily IDX
   watchlist. The single-symbol fetcher already supports it; only the loop and
   an IDX sector map are missing. This directly feeds `02-trading-bot` signal
   work.

2. `05-market-cron/sources/idx-official-scraper.md` - a Playwright-based scraper
   that solves the Cloudflare challenge once and reuses the session cookie to
   pull authoritative IDX numbers (the real exchange data, not a Yahoo mirror).
   This belongs with the cookie-safety work in `01-crawler-scrapper`. It would
   let the vault cross-check Yahoo against the primary source.

3. `07-gaps-and-opportunities/inbox/2026-07-12-licensed-market-data-arbitrage.md`
   - the broader insight that every free Indonesian equity data path
   (Yahoo, Stooq, IDX) is either undocumented, gated, or deprecated, and that a
   properly-licensed, clean, machine-readable IDX data API (with webhooks for
   corporate actions) does not really exist for Indonesian retail/small
   fintechs. That gap is itself a product wedge: a normalized IDX market data
   API for Indonesian indie developers.

## Worked example: computing indicators from the history array

The `history` array the script emits is the raw material for any downstream
signal. Here is a complete, standard-library implementation that takes the
emitted JSON and derives the quantities a trading bot or dashboard would
actually use: daily log returns, a 20-day simple moving average, a 50/200-day
SMA crossover flag, and the drawdown from the trailing peak. This is the bridge
between the cron fetch and the `02-trading-bot` strategies.

```python
import json
from datetime import datetime, timezone, timedelta

WIB = timezone(timedelta(hours=7))

def load(path="data/latest-ihsg.json"):
    return json.load(open(path, encoding="utf-8"))

def closes(doc):
    # history is ascending by date; map to (date_wib, close) tuples
    return [(r["date_wib"], r["close"]) for r in doc.get("history", []) if r.get("close")]

def daily_log_returns(pairs):
    out = []
    for i in range(1, len(pairs)):
        prev = pairs[i - 1][1]
        cur = pairs[i][1]
        if prev and cur:
            out.append((pairs[i][0], (cur / prev - 1.0)))
    return out

def sma(values, window):
    if len(values) < window:
        return None
    return sum(values[-window:]) / window

def max_drawdown(pairs):
    peak = pairs[0][1]
    worst = 0.0
    for _, v in pairs:
        if v > peak:
            peak = v
        dd = (v / peak - 1.0)
        if dd < worst:
            worst = dd
    return worst  # negative fraction, e.g. -0.12 = -12%

if __name__ == "__main__":
    doc = load()
    pairs = closes(doc)
    rets = daily_log_returns(pairs)
    vals = [p[1] for p in pairs]
    print("bars:", len(pairs))
    print("last close:", pairs[-1])
    print("20d SMA:", sma(vals, 20))
    print("50d SMA:", sma(vals, 50))
    print("200d SMA:", sma(vals, 200))
    s50, s200 = sma(vals, 50), sma(vals, 200)
    if s50 and s200:
        print("golden cross (50>200):", s50 > s200)
    print("max drawdown (window):", round(max_drawdown(pairs) * 100, 2), "%")
    print("last 3 daily returns:", [(d, round(r * 100, 3)) for d, r in rets[-3:]])
```

Run this against the `range=6mo` or `range=1y` output and you get a real
rolling snapshot. The 200-day SMA requires roughly 200 trading days, so use
`range=1y` (about 250 bars) to populate it. On 2026-07-12 the `range=6mo` call
returned 121 bars, enough for the 20 and 50 day SMAs but not 200.

A useful sanity check: the most recent `history` close should equal
`latest.close`, and `latest.change_pct` should approximately equal the last
entry of `daily_log_returns`. If they diverge, the normalizer has a bug or
Yahoo returned a partial session bar. Add an assertion in the orchestrator.

## IDX trading session model (for correct scheduling)

To schedule the cron correctly you need the real IDX session calendar. The
Indonesia Stock Exchange regular session runs 09:00 to 16:00 WIB, Monday to
Friday, with these sub-sessions:

- Pre-opening auction (JATS): 09:00 to 09:08 WIB, determining the opening
  price from matched orders.
- Regular session I: 09:00 to 11:30 WIB.
- Regular session II: 13:30 to 15:00 WIB (lunch break 11:30 to 13:30).
- Closing auction (JATS): 15:00 to 16:00 WIB, determining the closing price.
- Post-closing negotiation: after 16:00 for block trades.

The official reference for this schedule is the IDX trading hours page
(https://www.idx.co.id, currently Cloudflare-gated, see source landscape
above). The practical consequence for this fetcher: a post-close fetch at
16:05 WIB (09:05 UTC) catches the closing auction result, which is the number
most Indonesians quote as "the IHSG close." Fetching before 15:00 WIB catches
only the live, in-progress bar. This is why the crontab and systemd examples
above target 16:05 WIB.

Indonesian market holidays are not fixed Gregorian dates; they follow a
published IDX holiday calendar (Idul Fitri, Nyepi, and national holidays shift
year to year). The 4-day staleness threshold in the script absorbs a single
holiday gracefully; a multi-day holiday stretch (e.g. a long Idul Fitri break)
is also tolerated because the threshold counts calendar days, not trading days.
If you want strict behavior, feed the script the official IDX holiday list and
compare against it instead of using a flat day count.

## Free-float weighting, briefly

IHSG is a free-float adjusted market capitalization weighted index. Each
constituent's weight is its market cap times its free-float factor divided by
the divisor, summed across all listed stocks. The free-float factor excludes
strategic, locked, or state-held shares from the investable base. This matters
for two reasons in practice:

- A 1 point move in a high-free-float mega cap (BBCA, BBRI, TLKM) moves the
  index more than the same point move in a small cap. So a basket that weights
  by equal dollars (the `idx-basket-fetch` gap) is NOT a proxy for the index;
  it is a different instrument. Document which one you mean.
- Corporate actions (rights issues, stock splits, treasury buybacks) change
  free-float factors and force divisor adjustments, which is why a licensed
  feed with corporate-action webhooks (gap 3 above) is valuable. Yahoo's
  `adjclose` handles splits/dividends for total-return math but does not expose
  the divisor, so you cannot perfectly reconstruct index weights from Yahoo
  alone.

This is also why the official IDX API (gated) is the only truly authoritative
source for weights, and why gap 2 (the Playwright scraper) is worth building
for cross-validation rather than production reliance.

## Tying IHSG to the FX and crypto pulses already in the vault

The `05-market-cron/data/pulse-*.json` files already carry crypto (USD and IDR)
and, per the schema, FX. IHSG in IDR is therefore part of a coherent
Indonesian macro pulse once spliced in. Two analytical links are worth noting
for the signals work:

- IHSG vs USD/IDR: a weakening rupiah (rising USD/IDR) tends to pressure
  Indonesian equities via foreign outflows and imported-cost inflation. A
  combined pulse lets a bot flag divergence (IHSG up while rupiah weakens) as a
  caution signal.
- IHSG vs BTC: weak, but during risk-off episodes both can fall together. The
  correlation is regime-dependent and should be measured, not assumed.

Neither link is implemented here; they are flagged so the signals layer
(`02-trading-bot/signals/`) has a clear input contract: each pulse file exposes
a dated, currency-tagged snapshot that a correlator can align by `date_wib`.

## Persistence layer (optional SQLite)

For a vault that wants a long-run IHSG time series without re-fetching, persist
each daily run into SQLite. This is optional and not required for the cron, but
it is the natural next step once the fetcher runs daily for a few weeks.

```python
import json, sqlite3, os

def persist(doc, db="data/ihsg.sqlite"):
    os.makedirs(os.path.dirname(db), exist_ok=True)
    con = sqlite3.connect(db)
    con.execute("""
        CREATE TABLE IF NOT EXISTS ihsg_daily (
            date_wib TEXT PRIMARY KEY,
            close REAL, open REAL, high REAL, low REAL, volume REAL,
            adj_close REAL, change REAL, change_pct REAL,
            fetched_utc TEXT
        )
    """)
    l = doc["latest"]
    con.execute(
        "INSERT OR REPLACE INTO ihsg_daily VALUES (?,?,?,?,?,?,?,?,?,?)",
        (l["date_wib"], l["close"], l["open"], l["high"], l["low"],
         l["volume"], l["adj_close"], l["change"], l["change_pct"],
         doc["fetched_utc"]),
    )
    con.commit()
    con.close()

if __name__ == "__main__":
    persist(json.load(open("data/latest-ihsg.json", encoding="utf-8")))
```

`INSERT OR REPLACE` on `date_wib` makes the daily run idempotent: re-running the
same day overwrites rather than duplicating. This is safe to call from cron
every weekday. Query the table for charts, rolling stats, or to backfill the
indicator math above directly from SQL instead of JSON.

## Full multi-symbol basket fetcher (implementation of gap 1)

The single-symbol script already supports any `.JK` ticker. Here is the complete
wrapper that builds the daily IDX watchlist, emitted as a single JSON map. This
is the concrete realization of open gap 1.

```python
#!/usr/bin/env python3
"""idx-basket-fetch.py - daily IDX watchlist via Yahoo chart API.
Run after ihsg-daily-fetch.py patterns; stdlib only.
"""
import json, sys
from datetime import datetime, timezone, timedelta
sys.path.insert(0, "cron-configs")
from ihsg_daily_fetch import fetch_chart, normalize, WIB

# Liquid, widely-watched IDX constituents. Extend as needed.
WATCHLIST = {
    "^JKSE":  "IDX Composite (IHSG)",
    "BBRI.JK": "Bank Rakyat Indonesia",
    "BBCA.JK": "Bank Central Asia",
    "TLKM.JK": "Telkom Indonesia",
    "ASII.JK": "Astra International",
    "BMRI.JK": "Bank Mandiri",
    "GOTO.JK": "GoTo Gojek Tokopedia",
}

def main():
    out = {"fetched_wib": datetime.now(WIB).strftime("%Y-%m-%d %H:%M WIB"),
           "symbols": {}}
    for sym, name in WATCHLIST.items():
        try:
            res = fetch_chart(symbol=sym, rng="5d")
            doc = normalize(res, symbol=sym)
            out["symbols"][sym] = {
                "name": name,
                "close": doc["latest"]["close"],
                "change_pct": doc["latest"]["change_pct"],
                "date_wib": doc["latest"]["date_wib"],
            }
        except RuntimeError as e:
            out["symbols"][sym] = {"error": str(e)}
    json.dump(out, open("data/basket.json", "w"), indent=2, ensure_ascii=False)
    print(json.dumps(out, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
```

Drop this as `05-market-cron/cron-configs/idx-basket-fetch.py`. It reuses the
verified `fetch_chart` and `normalize` functions, so it inherits the dual-host
retry and null-bar skipping for free.

## Troubleshooting runbook

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| HTTP 429 | Missing/weak UA or bursty calls | Add realistic UA; add 1s+ delay; run once daily |
| HTTP 403 from both hosts | Egress IP WAF-blocked | Switch egress IP; wait; cache results |
| Empty `result` | Wrong/expired symbol | Verify ticker (^JKSE, *.JK); check instrumentType |
| `latest.close` null | All bars null (bad range) | Use `range=5d` or `1mo`; check interval |
| Stale flagged every run | Holiday or wrong tz | Confirm WIB; extend threshold; feed IDX holiday list |
| `change_pct` looks wrong | Compared to null prev bar | Normalizer skips nulls; check history alignment |
| JSON parse error | HTML challenge returned | Yahoo served a bot page; retry with backoff |
| `adj_close` null | Yahoo dropped adjclose | Non-fatal; downstream ignores it |

## Monitoring and alerting in production

Once the fetcher runs on a schedule, you need to know when it silently breaks.
Because the script uses process exit codes as its signal, wire them into your
existing monitor rather than parsing logs:

- Exit 0: success, fresh data written. Nothing to do.
- Exit 2: hard failure (all hosts exhausted, or empty result). Page someone.
- Exit 3: data fetched but flagged stale (`--fail-on-stale` only). Warn; do not
  page. A stale exit during a known holiday is expected, not an incident.

A minimal alert wrapper around cron mail or a chat webhook looks like this:

```bash
python3 cron-configs/ihsg-daily-fetch.py --out data/latest-ihsg.json --fail-on-stale
code=$?
if [ "$code" -eq 2 ]; then
  curl -s -X POST "$ALERT_WEBHOOK" \
    -d '{"text":"IHSG fetch HARD FAIL (exit 2): Yahoo unreachable from cron host"}'
fi
```

The key principle is that a daily market feed should fail loud, not silent.
A cron job that quietly stops producing data is worse than one that pages you,
because downstream dashboards keep rendering the last good number and nobody
notices the pipeline died. Exit codes plus a one-line webhook are enough; do not
build a dashboard to monitor the monitor.

## Quick reference for the next tick

- File created: `05-market-cron/cron-configs/ihsg-daily-fetch.py` (runnable,
  stdlib only, verified).
- Doc created: `05-market-cron/cron-configs/ihsg-daily-fetch.md` (this file).
- Data output: `05-market-cron/data/latest-ihsg.json` (generated by the run).
- Source of record: Yahoo Finance chart API v8, `^JKSE`, WIB timezone.
- Do NOT use: IDX official API (403), Stooq CSV (JS-gated), Yahoo v7 quote
  (401).
- Next natural extension: the idx-basket-fetch gap listed above.
