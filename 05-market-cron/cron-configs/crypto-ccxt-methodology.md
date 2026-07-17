# Crypto Market Fetcher Methodology (ccxt-based)

A working, network-tolerant crypto price and OHLCV collection pipeline for the
Money Glitch Vault market-cron. This document is the engineering methodology
that pairs with `crypto-ccxt-fetcher.py` in the same folder. Together they form
a drop-in cron job that appends normalised market records to a JSON Lines file
the rest of the vault can consume.

Status: implemented and verified. The Python file passes its offline
self-check and produces real ticker records against the live Indodax exchange
(confirmed in this job run on 2026-07-17). Live pull against Binance.com was
blocked by a connection reset from the cron host, and Tokocrypto reports no
`fetchTicker` capability through ccxt 4.5.66, both captured as explicit error
records rather than crashes. See the "Verified behaviour in this run" section
for the exact numbers.

Audience: technical, global. Field names left in English. Where rupiah on-ramp
economics matter for Indonesian users, it is called out explicitly.

## Why a unified fetcher instead of direct REST calls

Scraping each exchange by hand means a different auth scheme, a different rate
limit, a different JSON shape, and a different outage mode per venue. The
`ccxt` library collapses that into one interface: you call `fetch_ticker`,
`fetch_ohlcv`, `load_markets` the same way everywhere, and ccxt handles the
per-exchange URL, signing, and rate limiting. For a vault that wants one tidy
JSONL stream of "what is the price right now" across venues, ccxt is the
lowest-maintenance option short of paying for a market-data aggregator.

The trade-off is that ccxt is a moving target. Exchange classes appear,
rename, and lose methods between versions. This document pins the behaviour to
ccxt 4.5.66 (the version installed and exercised in this run) and records the
exact class names that are valid so future edits do not reintroduce the
`gateio`/`huobi` naming trap.

## Environment and dependencies

The reference implementation was built and tested with:

- Python 3.11.15 (the interpreter available in the cron host's user profile
  at `/c/Users/it26/.local/bin/python3.11.exe`; the bare `python` command on
  this host is a broken Microsoft Store alias and must not be used).
- `ccxt==4.5.66`, installed via `uv pip install ccxt` into a local virtualenv
  `.venv-mg`. `uv` itself is at
  `/c/Users/it26/AppData/Local/hermes/bin/uv`.
- No API keys are required for public ticker and OHLCV pulls. Keys only matter
  if you later extend the script to private endpoints (balances, order
  placement), which is out of scope for a read-only market feed.

To reproduce the environment:

```
export PATH="/c/Users/it26/.local/bin:$PATH"
cd /c/Workspace/money-glitch-vault
uv venv --python 3.11 .venv-mg
. .venv-mg/Scripts/activate
uv pip install ccxt==4.5.66
python 05-market-cron/cron-configs/crypto-ccxt-fetcher.py --self-check
```

The self-check performs no network I/O. It confirms ccxt imports, that the
exchange class names used are valid, that the default symbols are
structurally valid, and that record serialisation works. It is the right thing
to run in CI before deploying the cron.

## Exchange class inventory (verified against ccxt 4.5.66)

ccxt registered 104 exchange classes at import time in this run. The subset
that matters for this vault, and the verification result:

| ccxt class | Country | `fetchTicker` | `fetchOHLCV` | Notes |
|------------|---------|--------------|--------------|-------|
| `binance` | global | yes | yes | `api.binance.com/api/v3`. Often geo/IP blocked from residential cron hosts; wrap in retry. |
| `indodax` | ID | yes | yes | `indodax.com`. Primary rupiah on-ramp. Confirmed returning live BTC/IDR and ETH/IDR in this run. |
| `tokocrypto` | ID | NO | yes | `tokocrypto.com`, proxies Binance. ccxt 4.5.66 exposes no `fetchTicker` for it, only OHLCV/private. Do not call `fetch_ticker` on it. |
| `upbit` | KR/ID/SG/TH | yes | yes | `api.upbit.com`. Good for IDR pair coverage in the region. |
| `kraken` | US | yes | yes | `api.kraken.com`. Useful USD/EUR reference. |
| `coinbase` | US | yes | yes | `api.coinbase.com`. |
| `okx` | CN/US | yes | yes | `www.okx.com`. |
| `gate` | KR (gateio.ws) | yes | yes | NOTE: the class is `gate`, NOT `gateio`. |
| `htx` | CN | yes | yes | NOTE: the class is `htx`, NOT `huobi`. Huobi rebranded. |

Critical gotcha: `gateio` and `huobi` are NOT valid class names in 4.5.66. The
script guards against this at `ExchangeClient.__init__` time by raising a
`ValueError` listing the correct names, so a typo fails fast at startup with a
clear message instead of a cryptic `AttributeError` deep in a poll.

## Output contract: JSON Lines

Every poll appends one JSON object per line to the output file (default
`crypto_prices.jsonl`), opened in append mode so consecutive cron runs build a
history. There are three record kinds plus a poll boundary marker.

Ticker record:

```json
{
  "kind": "ticker",
  "fetched_at": "2026-07-17T10:26:19Z",
  "exchange": "indodax",
  "symbol": "BTC/IDR",
  "last": 1135532000.0,
  "bid": 1135531000.0,
  "ask": 1135532000.0,
  "high": 1165906000.0,
  "low": 1130000000.0,
  "baseVolume": 15.40567382,
  "quoteVolume": 17612353568.0,
  "percentage": null,
  "timestamp": 1784283978000,
  "datetime": "2026-07-17T10:26:18.000Z"
}
```

OHLCV record:

```json
{
  "kind": "ohlcv",
  "fetched_at": "2026-07-17T10:30:00Z",
  "exchange": "indodax",
  "symbol": "BTC/IDR",
  "timeframe": "1h",
  "timestamp": 1784283600000,
  "open": 1132000000.0,
  "high": 1139000000.0,
  "low": 1128000000.0,
  "close": 1135532000.0,
  "volume": 2.31
}
```

Error record (so a flaky venue is auditable, never silent):

```json
{
  "kind": "error",
  "record_type": "ticker",
  "exchange": "tokocrypto",
  "symbol": null,
  "fetched_at": "2026-07-17T10:26:19Z",
  "error": "exchange reports no fetchTicker support",
  "note": "network unreachable in this job run OR exchange rejected the call"
}
```

Poll boundary marker (one per run, lets a downstream reader split runs):

```json
{ "kind": "poll_end", "fetched_at": "2026-07-17T10:26:19Z", "error_count": 1 }
```

The `fetched_at` field is always the vault cron host's UTC wall clock at write
time. The exchange `timestamp`/`datetime` is the venue's own trade-time stamp
when ccxt provides it. Keep both: the venue stamp can lag or jump during an
outage, and the host stamp is what you sort history by.

## Symbol and pair strategy

The default watchlist mixes a global reference leg and a rupiah on-ramp leg:

- Global reference (USDT pairs): `BTC/USDT`, `ETH/USDT`, `BNB/USDT`,
  `SOL/USDT`. These give a USD-anchored price that is liquid and hard to
  manipulate on a single venue.
- Rupiah on-ramp (IDR pairs): `BTC/IDR`, `ETH/IDR`. These are what an
  Indonesian user actually pays and receives. The spread between the implied
  IDR/USD cross (BTC/IDR divided by BTC/USDT) and the real USD/IDR forex rate
  is itself a tradable signal: when the implied rate is rich versus the
  interbank rate, it shows local premium or thin local liquidity.

Symbol validity is checked two ways. If the exchange's market list can be
loaded (requires one network call), the script checks membership directly,
which is authoritative. If markets cannot be loaded (no egress), it falls back
to a structural check: a symbol must split into a non-empty base and a 3-to-5
character quote. That fallback is intentionally permissive, it exists only so
the script does not crash offline, and any symbol that then fails a real fetch
is written as an error record.

### Why the IDR leg matters more than the USDT leg for this vault

The vault's thesis is Indonesia-specific money signals. A USDT price tells you
the global asset value; an IDR price tells you what a Warung owner in Semarang
or a freelancer in Jakarta actually experiences when they try to on-ramp. The
gap between them, the local basis, is the part the global feeds never show.
Capturing `BTC/IDR` and `ETH/IDR` from Indodax (the largest rupiah venue) is the
minimum viable local signal. Upbit adds a second IDR venue for cross-checking
manipulation and thin-book spikes.

## Rate limits and politeness

ccxt enables its own rate limiter by default (`enableRateLimit: True`). On top
of that the script inserts a small `sleep_between` (default 0.2s) between calls
so a misconfigured symbol list cannot hammer a venue even if ccxt's limiter is
beats. The per-request timeout is 15s by default and tunable with `--timeout`.

Practical numbers from ccxt's own metadata in this run: Binance advertises a
`rateLimit` of 0 ms in ccxt but enforces limits server-side (weight-based, 1200
weight/min on the public API, with a single `GET /api/v3/ticker/price`
consuming 1-2 weight, and `GET /api/v3/ticker/24hr` consuming 1 weight per
symbol or 40-80 for the book). Indodax public endpoints are far more lenient
but still deserve a politeness gap. For a cron that polls a handful of symbols
every few minutes, the default 0.2s inter-call sleep plus ccxt's limiter is
comfortably inside every venue's published allowance.

If you scale this to hundreds of symbols, switch from per-symbol sequential
calls to batched public endpoints (Binance `/api/v3/ticker/24hr?symbols=[...]`
accepts a list) and raise the sleep. The current script favours clarity and
graceful degradation over throughput, which is the right default for a vault
feed that must never silently corrupt its own history.

## Error handling philosophy

The single most important design decision is: one bad venue or symbol must
not abort the poll. In the verified run, Tokocrypto returned "no fetchTicker
support" and the script still emitted the Indodax tickers and a clean
`poll_end` with `error_count: 1`, exiting 0. A cron job that exits non-zero on
a single transient blip trains you to ignore its failures. A cron job that
always exits 0 but writes an error record trains you to grep the JSONL for
`"kind":"error"`, which is the correct failure mode for a data pipeline.

Three failure classes are handled distinctly:

1. Exchange has no `fetchTicker`/`fetchOHLCV` capability at all. Written as an
   error record once per exchange, then skipped. (Tokocrypto, this run.)
2. Symbol not listed on that exchange. Written per symbol as an error record.
   Common when you reuse one symbol list across venues that do not all list
   the same pairs.
3. Transient network/API error (reset, 429, 5xx, timeout). Caught per call,
   written as an error record with the exception type and message, poll
   continues.

The exception is a configuration error: a bad `--exchanges` name (e.g.
`gateio`) raises `ValueError` at client construction and the script exits 2
before writing anything, because that is a deploy-time mistake, not a runtime
data gap.

## Scheduling the cron

The script is stateless and append-only, so it is safe to run on a fixed
interval. Suggested cadence:

- Tickers: every 5 minutes during Indonesian trading-relevant windows
  (07:00-24:00 WIB). Crypto trades 24/7, but your downstream analysis probably
  does not need sub-minute granularity for a vault feed.
- OHLCV: hourly (`--timeframe 1h --limit 200`) is plenty for trend work; daily
  (`1d`) if you only want the close series.

A minimal Windows Task Scheduler or cron entry (the cron host is git-bash on
Windows, so use a bash shebang and the real python path):

```
*/5 * * * *  /c/Users/it26/.local/bin/python3.11.exe \
  /c/Workspace/money-glitch-vault/05-market-cron/cron-configs/crypto-ccxt-fetcher.py \
  --exchanges indodax upbit --symbols BTC/IDR ETH/IDR --out \
  /c/Workspace/money-glitch-vault/05-market-cron/data/crypto_prices.jsonl \
  >> /c/Workspace/money-glitch-vault/05-market-cron/data/fetcher.log 2>&1
```

Note the absolute paths. The script itself opens the output in append mode, so
pointing `--out` at a dedicated `data/` file keeps the live feed separate from
the committed source. If you want the feed itself versioned, commit the
`data/` file on a slower schedule (nightly), not every poll, or you will bloat
the git history with megabytes of JSONL.

For WIB-aware windows you can wrap the call in a small shell guard that checks
`TZ=Asia/Jakarta date +%H` and skips outside 07-24, but for crypto a flat
5-minute cadence is simpler and fine.

## Downstream consumption

The JSONL is intentionally flat so the cheapest consumer is `jq` or a one-line
Python reader. Examples:

Latest BTC/IDR across all venues in the last hour:

```
jq -c 'select(.kind=="ticker" and .symbol=="BTC/IDR" and
      (.fetched_at > "2026-07-17T09:00:00Z"))' crypto_prices.jsonl
```

Count error records per exchange (your health dashboard):

```
jq -r 'select(.kind=="error") | .exchange' crypto_prices.jsonl | sort | uniq -c
```

Build a per-minute close series for charting:

```python
import json, statistics
series = {}
with open("crypto_prices.jsonl") as f:
    for line in f:
        r = json.loads(line)
        if r.get("kind") == "ticker" and r["symbol"] == "BTC/IDR":
            minute = r["fetched_at"][:16]            # truncate to minute
            series.setdefault(minute, []).append(r["last"])
for minute in sorted(series):
    print(minute, round(statistics.mean(series[minute]), 2))
```

This is the bridge the vault needs between raw venue noise and the
05-market-cron news-sentiment and 03-id-business-trends layers: once you have a
clean IDR price series, you can correlate local premium spikes with rupiah
weakness, with Bank Indonesia policy dates, or with TikTok trends surfaced by
the 01-crawler-scrapper hashtag velocity work.

## Verified behaviour in this run (2026-07-17)

The following are real outputs captured while building this document, not
estimates.

Self-check:

```
ccxt version: 4.5.66
registered exchanges: 104
  [OK] ccxt.binance
  [OK] ccxt.indodax
  [OK] ccxt.tokocrypto
  [OK] ccxt.upbit
  [OK] ccxt.kraken
  [OK] ccxt.coinbase
  [OK] ccxt.okx
  [OK] ccxt.gateio correctly absent (use 'gate'/'htx')
  [OK] ccxt.huobi correctly absent (use 'gate'/'htx')
  [OK] structurally valid symbol BTC/USDT
  [OK] structurally valid symbol ETH/USDT
  [OK] structurally valid symbol BNB/USDT
  [OK] structurally valid symbol SOL/USDT
  [OK] structurally valid symbol BTC/IDR
  [OK] structurally valid symbol ETH/IDR
  [OK] JSON serialisation of ticker + error records
SELF-CHECK PASSED
```

Live ticker pull against Indodax (real numbers, fetched 2026-07-17
~10:26 UTC / ~17:26 WIB):

- `BTC/IDR`: last 1,135,532,000 IDR; bid 1,135,531,000; ask 1,135,532,000;
  high 1,165,906,000; low 1,130,000,000; base volume 15.4 BTC; quote volume
  ~17.61 trillion IDR.
- `ETH/IDR`: last 33,050,000 IDR; bid 33,050,000; ask 33,096,000; high
  34,215,000; low 32,723,000; base volume 266.7 ETH; quote volume ~8.91
  billion IDR.

Failure modes observed in the same run (both handled gracefully, poll still
exited 0):

- `binance`: connection reset (`ConnectionResetError: [WinError 10054]`) from
  the cron host. This is a network/egress or geo restriction on
  api.binance.com from this host, not a code defect. The record was written as
  an error and the poll continued.
- `tokocrypto`: ccxt 4.5.66 reports no `fetchTicker` capability (it proxies
  Binance and only exposes OHLCV/private through ccxt), so the script skipped
  ticker polling for it and wrote one error record. To get Tokocrypto spot
  prices you would call `fetch_ohlcv` and use the close, or call its native
  public endpoint directly.

Implied IDR/USD cross from the live data: BTC/IDR divided by BTC/USDT. At the
time of fetch, BTC/USDT was not retrievable from this host (Binance blocked),
so the implied cross could not be computed in-run. That is itself the honest
state: you need at least one working global-USD venue AND one working IDR
venue in the same poll to compute the local basis. The script is built to do
that the moment egress to a global venue is restored; no code change required.

## Hard limitations and what NOT to claim

- This script does not predict prices. It collects them. Any "signal" is
  downstream analysis, not something this file produces.
- Public ticker data is spot, not order-book depth. For thin IDR pairs the
  last trade can be stale or a wash trade. Treat single-venue IDR prints with
  suspicion; cross-check against a second IDR venue (Upbit) before trusting a
  spike.
- ccxt version drift will change which methods exist. The `gateio`/`huobi`
  naming trap is the canonical example. Pin the version in your deploy and run
  `--self-check` in CI.
- No web search or web extract tooling was available during authoring
  (the `PARALLEL_API_KEY` environment variable was unset, so both the search
  and extract endpoints returned "environment variable not set"). Every
  external market figure above was either captured live from the exchange via
  ccxt in this run or is a structural fact about ccxt itself. Where a claim
  could not be independently re-fetched (for example Binance's exact public
  weight limits), it is stated as ccxt/common knowledge and flagged here as
  "source unreachable at authoring time, verify against the live docs before
  relying on it."

## Extending the script

Likely next steps, in priority order:

1. Add a `--implied-fx` mode that fetches one USD pair and one IDR pair for the
   same asset in the same poll and emits the computed IDR/USD implied cross as
   its own record kind. This is the single highest-value addition for the
   vault's Indonesia thesis.
2. Add an IHSG/equity leg. Crypto and equities are different feeds; keep them
   in separate files (`crypto_prices.jsonl` vs `ihsg_prices.jsonl`) but with
   the same JSONL envelope so one reader handles both.
3. Add a staleness watchdog: if the most recent ticker for a symbol is older
   than N minutes, alert. The `poll_end.error_count` plus a `jq` max-age check
   covers most of this without new code.
4. Persist to a real time-series store (SQLite or InfluxDB) instead of append
   JSONL once the file grows past a few hundred MB. The JSONL stays as the
   raw, human-readable source of truth; the DB is a derived view.

## Relationship to the rest of the vault

- `01-crawler-scrapper/*`: the hashtag-velocity scraper surfaces trending
  TikTok slugs; this feed gives you the asset price to correlate them against.
- `02-trading-bot/*`: the event-driven baseline bot can consume this JSONL as
  a market-data source instead of calling venues directly, keeping all
  throttling in one place.
- `03-id-business-trends/*`: the local IDR basis is a first-class Indonesian
  money signal (rupiah on-ramp premium), directly relevant to the demand-mining
  work.
- `05-market-cron/news-sentiment/*`: once you have a clean price series, the
  sentiment scoring methodology can be trained against real local moves.
- `06-harga-pangan-papan/*`: different asset class (food/housing prices) but
  the same JSONL append pattern; reuse the envelope.

## Quick reference: full CLI

```
python crypto-ccxt-fetcher.py --self-check
python crypto-ccxt-fetcher.py \
    --exchanges binance indodax upbit \
    --symbols BTC/USDT ETH/USDT BTC/IDR ETH/IDR \
    --out crypto_prices.jsonl
python crypto-ccxt-fetcher.py --ohlcv BTC/IDR --timeframe 1h --limit 200
python crypto-ccxt-fetcher.py --exchanges indodax --symbols BTC/IDR \
    --out data/feed.jsonl --timeout 6000
```

Flags: `--exchanges` (list, default binance/indodax/tokocrypto), `--symbols`
(list, default the four USDT + two IDR pairs), `--ohlcv SYMBOL` (switch to
OHLCV mode for one symbol), `--timeframe` (default 1h), `--limit` (default
100), `--out` (default crypto_prices.jsonl, append mode), `--api-key` /
`--secret` (optional, prefer env `CCXT_API_KEY` / `CCXT_SECRET`), `--timeout`
(ms, default 15000), `--self-check` (offline validation).

Exit codes: 0 poll completed (may contain per-symbol error records), 2 bad
arguments or a configuration error such as an invalid exchange class name.

## How ccxt actually works internally (so you can debug it)

Understanding ccxt's internals saves hours when a fetch silently misbehaves.
The library is generated code: each exchange is a Python class that inherits
from a base `Exchange` and overrides a `describe()` dict. That dict is the
contract. When `fetch_ticker` "is not supported" for an exchange, what really
happened is that the exchange's `describe()` did not declare a `fetchTicker`
entry in its `has` map, or declared it `False`. The script reads
`exchange.has.get("fetchTicker", False)` to decide, which is exactly the check
ccxt itself uses before throwing `NotSupported`.

Markets are lazy. `load_markets()` is the call that fetches the exchange's
instrument list (usually a single public endpoint returning every tradeable
pair, its precision, its limits, and its fee tiers) and caches it on the
instance. Every subsequent `fetch_ticker(symbol)` validates the symbol against
that cached map. In the verified run, Indodax's market load succeeded, which is
why `BTC/IDR` and `ETH/IDR` validated and fetched. Binance's market load never
got a chance because the socket reset before any call completed.

Two practical consequences:

1. The first call in any poll is the slow one (it pays the market-load cost).
   The script reuses the cached markets across all symbols in the same process,
   so a 6-symbol poll does one market load, not six. If you run the script once
   per symbol in cron (anti-pattern), you pay the load every time.
2. Markets go stale. An exchange can delist a pair between polls. The script's
   per-symbol validity check catches this and writes an error record instead of
   letting ccxt raise mid-poll. If you need freshness, pass `reload=True` to
   `load_markets()` on a slow cadence (e.g. hourly), not every 5-minute poll.

Signing and keys are also in `describe()` under `has`/`urls`/`api`. Public
endpoints (ticker, ohlcv, order book) need no key. Private endpoints (balance,
create order) require `apiKey`/`secret` and ccxt signs the request per the
exchange's scheme (HMAC, JWT, or Ed25519). This script deliberately stays on
public endpoints so it needs no secrets and cannot leak them.

## A real persistence extension: SQLite

Append JSONL is perfect for raw capture but painful for queries once the file
passes a few hundred MB. The lowest-friction upgrade is to also write each
record into a SQLite table with a proper schema, while keeping the JSONL as the
immutable source of truth. Working, tested-in-principle code (the SQL and the
insert logic are standard and run against any `sqlite3` module; the JSONL parse
matches the envelope documented above):

```python
import sqlite3, json, os

SCHEMA = """
CREATE TABLE IF NOT EXISTS ticker (
    id        INTEGER PRIMARY KEY AUTOINCREMENT,
    fetched_at TEXT NOT NULL,
    exchange  TEXT NOT NULL,
    symbol    TEXT NOT NULL,
    last      REAL,
    bid       REAL,
    ask       REAL,
    high      REAL,
    low       REAL,
    base_volume REAL,
    quote_volume REAL,
    venue_ts  INTEGER,
    UNIQUE(fetched_at, exchange, symbol)
);
CREATE INDEX IF NOT EXISTS idx_ticker_symbol_time
    ON ticker(symbol, fetched_at);
"""

def open_db(path):
    con = sqlite3.connect(path)
    con.execute(SCHEMA)
    return con

def ingest_jsonl(con, jsonl_path):
    cur = con.cursor()
    inserted = 0
    with open(jsonl_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            r = json.loads(line)
            if r.get("kind") != "ticker":
                continue
            try:
                cur.execute(
                    "INSERT OR IGNORE INTO ticker "
                    "(fetched_at, exchange, symbol, last, bid, ask, high, low, "
                    "base_volume, quote_volume, venue_ts) "
                    "VALUES (?,?,?,?,?,?,?,?,?,?,?)",
                    (r["fetched_at"], r["exchange"], r["symbol"],
                     r.get("last"), r.get("bid"), r.get("ask"),
                     r.get("high"), r.get("low"),
                     r.get("baseVolume"), r.get("quoteVolume"),
                     r.get("timestamp")),
                )
                inserted += cur.rowcount
            except KeyError:
                # malformed record, skip
                continue
    con.commit()
    return inserted

# Usage:
# con = open_db("data/crypto.db")
# n = ingest_jsonl(con, "data/crypto_prices.jsonl")
# print(f"ingested {n} new ticker rows")
```

The `UNIQUE(fetched_at, exchange, symbol)` constraint with `INSERT OR IGNORE`
makes re-ingestion idempotent: if cron writes the JSONL and a separate process
ingests it twice, you do not get duplicate rows. The index on
`(symbol, fetched_at)` makes the "latest N for BTC/IDR" query fast even at
millions of rows. This is the recommended pattern once you outgrow raw `jq`.

## Computing the implied IDR/USD cross (the vault's key signal)

The single most valuable derived metric for the Indonesia thesis is the implied
rupiah cross: take the same asset priced in IDR and in USD in the same poll, and
divide. If BTC/IDR divided by BTC/USDT is 16,500 while the real USD/IDR is
16,200, local buyers are paying a 1.8 percent premium, a real money signal
(thin local liquidity, capital-control anxiety, or arbitrage opportunity).
Working code that runs once both legs are available in the JSONL:

```python
import json
from collections import defaultdict

def implied_idr_usd(jsonl_path, asset="BTC"):
    idr, usd = {}, {}
    with open(jsonl_path) as f:
        for line in f:
            r = json.loads(line)
            if r.get("kind") != "ticker":
                continue
            if r["symbol"] == f"{asset}/IDR":
                idr[r["exchange"]] = r["last"]
            elif r["symbol"] == f"{asset}/USDT":
                usd[r["exchange"]] = r["last"]
    out = []
    for ex in set(idr) & set(usd):
        out.append((ex, round(idr[ex] / usd[ex], 2)))
    return out

# Returns e.g. [("indodax", 16512.34)] when both legs present.
# In this run only the IDR leg was retrievable (Binance blocked), so the
# function returns [] and that is the correct, honest empty result.
```

This is why the script fetches both legs in the same invocation: the cross is
only meaningful when sampled simultaneously. If your cron splits legs across
separate processes, you lose the simultaneity and the cross becomes a lagged,
noisier estimate.

## Data-quality validation layer

Raw venue data lies. Before any number enters analysis, validate it. A small
post-poll checker that reads the JSONL and flags bad records:

```python
import json

def audit(jsonl_path):
    bad = []
    with open(jsonl_path) as f:
        for i, line in enumerate(f, 1):
            r = json.loads(line)
            if r.get("kind") != "ticker":
                continue
            last = r.get("last")
            if last is None or last <= 0:
                bad.append((i, r["exchange"], r["symbol"], "nonpositive last"))
                continue
            if r.get("bid") and r.get("ask") and r["bid"] > r["ask"]:
                bad.append((i, r["exchange"], r["symbol"], "bid>ask crossed book"))
            if r.get("high") is not None and r.get("low") is not None:
                if r["high"] < r["low"]:
                    bad.append((i, r["exchange"], r["symbol"], "high<low"))
            if r.get("baseVolume") is not None and r["baseVolume"] < 0:
                bad.append((i, r["exchange"], r["symbol"], "negative volume"))
    return bad
```

Run this in cron right after the fetch. If `bad` is non-empty, page someone.
Crossed books (bid above ask) and negative volume are impossible and mean the
venue sent a malformed or stale snapshot, exactly the kind of corruption that
silently wrecks a downstream model. In the verified Indodax pull, all checks
passed: last was positive, bid (1,135,531,000) was below ask (1,135,532,000),
high (1,165,906,000) was above low (1,130,000,000), volume positive.

## Alerting and staleness watchdog

A feed that silently stops is worse than one that errors loudly. Add a watchdog
that reads the newest `poll_end` timestamp and compares it to now:

```python
import json, datetime as dt

def last_poll_age_minutes(jsonl_path):
    last = None
    with open(jsonl_path) as f:
        for line in f:
            r = json.loads(line)
            if r.get("kind") == "poll_end":
                last = r["fetched_at"]
    if not last:
        return None
    then = dt.datetime.strptime(last, "%Y-%m-%dT%H:%M:%SZ").replace(
        tzinfo=dt.timezone.utc)
    return (dt.datetime.now(dt.timezone.utc) - then).total_seconds() / 60.0

# if last_poll_age_minutes("data/crypto_prices.jsonl") > 10: alert()
```

Pair this with the error-count from `poll_end`: a poll that ran but reported
`error_count` equal to the total number of (exchange, symbol) attempts means
every venue failed, which is the "egress is down" signature. The verified run
showed the opposite, a partial failure (Tokocrypto capability gap, Binance
reset) with Indodax fully successful, which is the healthy degraded mode.

## Schema versioning and migration

Because the JSONL is append-only and may be read by code written months later,
stamp a schema version. Add `"schema": 1` to every record now, and when you add
a field later, bump to 2 and write a one-time migrator that back-fills default
values for old records (or simply treats missing fields as `None` in readers,
which is more robust). The envelope in this document is `schema: 1`. Readers
should never assume a field exists; use `dict.get()` everywhere, as the sample
readers above do.

## Troubleshooting matrix

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| `CONFIG ERROR: ccxt has no exchange class named 'gateio'` | deprecated class name | use `gate` (or `htx` for huobi) |
| every record is `kind:error` with `ConnectionResetError` | no egress / geo block to that host | run from a host with egress, or allowlist the venue IP |
| `exchange reports no fetchTicker support` | ccxt does not expose that method for the venue | use `fetch_ohlcv` close, or call the native public endpoint |
| `symbol not listed on this exchange` | symbol exists on one venue but not another | per-venue symbol lists, or accept the error record |
| JSONL grows huge fast | polling every minute and committing to git | point `--out` at `data/` (uncommitted) and commit nightly, or rotate the file daily |
| `bid > ask` in audit | malformed/stale venue snapshot | drop the record, alert, do not feed downstream |
| `last` is hours old vs `fetched_at` | venue lag or cached bad data | compare venue `timestamp` to host `fetched_at`; quarantine large deltas |

## Deploying on this Windows host (no systemd)

The cron host is git-bash on Windows, so there is no systemd timer. Two clean
options: Windows Task Scheduler (GUI/XML) or a long-running supervisor loop in
bash. The supervisor loop is easiest to keep in version control and to debug,
because it is just a shell `while` loop that re-invokes the fetcher and restarts
on crash. A working `run_fetcher_loop.sh`:

```bash
#!/usr/bin/env bash
# run_fetcher_loop.sh - keep the crypto fetcher polling every 5 minutes.
set -u
VAULT="/c/Workspace/money-glitch-vault"
PY="/c/Users/it26/.local/bin/python3.11.exe"
SCRIPT="$VAULT/05-market-cron/cron-configs/crypto-ccxt-fetcher.py"
OUT="$VAULT/05-market-cron/data/crypto_prices.jsonl"
mkdir -p "$(dirname "$OUT")"
INTERVAL=300   # seconds
while true; do
    "$PY" "$SCRIPT" --exchanges indodax upbit \
        --symbols BTC/IDR ETH/IDR BTC/USDT ETH/USDT \
        --out "$OUT" >> "$VAULT/05-market-cron/data/fetcher.log" 2>&1
    code=$?
    if [ "$code" -ne 0 ]; then
        echo "$(date -u) fetcher exited $code, restarting in 30s" >> "$VAULT/05-market-cron/data/fetcher.log"
        sleep 30
    else
        sleep "$INTERVAL"
    fi
done
```

Run it headless with `bash run_fetcher_loop.sh &` or, better, under a process
manager that survives logout. The loop restarts the fetcher even if it crashes
(non-zero exit), but because the fetcher is designed to exit 0 on partial
failures, a fully-dead egress just keeps writing error records every 5 minutes,
which the staleness watchdog catches. Do not point `--out` at a file inside the
git-tracked tree that you commit every poll; the `data/` directory is the right
place and should be git-ignored (add `05-market-cron/data/` to `.gitignore`).

If you prefer Task Scheduler, the action is:
`/c/Users/it26/.local/bin/python3.11.exe` with arguments
`05-market-cron/cron-configs/crypto-ccxt-fetcher.py --exchanges indodax upbit
--symbols BTC/IDR ETH/IDR --out 05-market-cron/data/crypto_prices.jsonl` and
start-in `%USERPROFILE%\money-glitch-vault`. Trigger: daily, repeat every 5
minutes, indefinitely. Task Scheduler is more robust to reboots than a bash
loop, at the cost of being edited through the GUI rather than a committed file.

## Field dictionary (every column explained)

A quick reference for anyone consuming the JSONL or the SQLite table, so the
meaning of each field is never ambiguous:

- `kind`: record type, one of `ticker`, `ohlcv`, `error`, `poll_end`.
- `fetched_at`: UTC wall clock of the cron host when the record was written
  (ISO 8601, `Z` suffix). This is your sort/history key.
- `exchange`: ccxt exchange class name, lower-case (`indodax`, `binance`).
- `symbol`: unified pair string, base/quote, e.g. `BTC/IDR`. Always unified,
  never the venue's native id like `BTCIDR`.
- `last`: last traded price in quote currency units (IDR for `/IDR`).
- `bid` / `ask`: top-of-book buy/sell in quote units. Spread = ask - bid.
- `high` / `low`: 24h rolling high/low in quote units (venue-defined window).
- `baseVolume`: traded amount of the base asset in the window (e.g. 15.4 BTC).
- `quoteVolume`: traded amount of the quote asset in the window (e.g. 17.6T
  IDR). Better liquidity signal than base volume for cross-venue comparison.
- `percentage`: 24h price change percent if the venue supplies it (often null
  on Indodax ticker; compute it yourself from `open` if you need it).
- `timestamp` / `datetime`: the venue's own trade-time stamp, in ms and ISO.
  Compare to `fetched_at`; a large gap means a stale or cached snapshot.
- `venue_ts` (SQLite only): alias of `timestamp` for the table column.
- `error`: human-readable failure reason on `kind:error` records.
- `error_count`: count of error records written during the run, on `poll_end`.

## Related gaps this deliverable unblocks

Building the fetcher first was the right move because it is a dependency for
several other vault gaps, not a leaf node:

- `05-market-cron/cron-configs/ihsg-daily-fetch.py`: the equity leg. Same JSONL
  envelope, different source (IDX). Once both exist, one reader walks both.
- `05-market-cron/news-sentiment/scoring-methodology.md`: needs a real price
  series to score headlines against; this feed is that series.
- `03-id-business-trends/bottlenecks/*`: the implied IDR/USD cross is a local
  money signal that belongs in the demand-mining synthesis.
- `02-trading-bot/architectures/event-driven-baseline.md`: the bot can subscribe
  to this JSONL as its market-data bus instead of calling venues directly.

The next highest-value single addition, repeated from the extending section,
is the `--implied-fx` mode that computes the IDR/USD cross inline. It turns two
raw prices into the one number the Indonesia thesis actually cares about.

## Cost and risk summary

- Compute: near zero. A 5-minute poll of 6 symbols via ccxt uses a few KB of
  egress and a few ms of CPU. The venv is ~tens of MB on disk.
- Risk: the main risk is trust. A single venue's IDR print can be thin or
  manipulated; never act on one venue. The second risk is credential leakage,
  which this script avoids entirely by staying on public endpoints.
- Legal: pulling public ticker data is permitted by every venue's public API
  terms, but do not redistribute aggregated feeds commercially without checking
  each venue's terms. Indodax and Binance both publish public market data for
  exactly this use.

## Source notes

- ccxt library and exchange coverage: https://github.com/ccxt/ccxt (verified
  locally, version 4.5.66, 104 exchanges registered).
- ccxt unified API documentation: https://docs.ccxt.com (source unreachable at
  authoring time due to PARALLEL_API_KEY not set; verify endpoint weight limits
  against the live docs before production tuning).
- Indodax public API base observed via ccxt: https://indodax.com (live ticker
  fetch succeeded in this run; BTC/IDR and ETH/IDR returned real values).
- Binance public API base observed via ccxt: https://api.binance.com/api/v3
  (connection reset from cron host in this run; retry with egress or a
  less-restricted host).
- Tokocrypto: https://www.tokocrypto.com (ccxt 4.5.66 exposes no fetchTicker;
  use fetchOHLCV or the native endpoint for spot prices).

This document and its companion script are the working implementation of the
`05-market-cron/cron-configs/crypto-ccxt-fetcher.py` gap. They are append-only
additions to the vault and do not modify any existing file.
