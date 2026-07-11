# Binance Spot & Futures API — Auth, Rate Limits & Common Pitfalls

> Folder: `02-trading-bot/brokers-apis/`
> Status: HIGH priority — the broker layer the trading-bot module is built on
> Author: Money Glitch Vault Filler (cron tick 2026-07-11)
> Audience: bot authors wiring `02-trading-bot` strategies to a real venue

---

## 0. Scope & honesty note

This document is a hands-on operator reference for building automated trading
bots against **Binance Spot** and **Binance USDⓈ-M Futures** (the perpetual and
dated futures venues). It covers authentication, the request-signing scheme,
rate limiting, the REST/WebSocket split, order-lifecycle pitfalls, and
production-hardening patterns.

> ⚠️ **Tool limitation note (2026-07-11 tick):** Live web verification was
> unavailable in the execution environment (`web_search`/`web_extract` returned
> `PARALLEL_API_KEY not set`). The API endpoints, signing algorithm (HMAC
> SHA256), and rate-limit structure described here are stable, long-lived public
> knowledge documented in Binance's official API docs and the `binance-connector`
> / `python-binance` libraries. **Always re-read the official docs before
> production:** `https://developers.binance.com` (Spot) and
> `https://binance-docs.github.io/apidocs/futures/en/` (USDⓈ-M). Numbers such as
> exact weight limits or endpoint paths can change; treat any specific threshold
> here as "approximately current, verify before launch."

---

## 1. Which Binance, and which API

| Product | Base host (REST) | Docs |
|---------|------------------|------|
| Spot | `https://api.binance.com` | developers.binance.com |
| Spot (backup) | `https://api1.binance.com`, `https://api2.binance.com`, `https://api3.binance.com`, `https://api4.binance.com` | — |
| USDⓈ-M Futures | `https://fapi.binance.com` | binance-docs.github.io/apidocs/futures/en |
| COIN-M Futures | `https://dapi.binance.com` | (delivery) |
| Spot WS | `wss://stream.binance.com:9443` | — |
| Futures WS | `wss://fstream.binance.com` | — |
| Testnet Spot | `https://testnet.binance.vision` | uses `@testnet` credentials |
| Testnet Futures | `https://testnet.binancefuture.com` | separate API keys |

**Rule #1:** Never develop against mainnet. Get testnet keys for both Spot
(`testnet.binance.vision`) and Futures (`testnet.binancefuture.com`). They use
**separate** key pairs — the Futures testnet is NOT the Spot testnet.

---

## 2. Authentication model

Binance uses **HMAC-SHA256** request signing for both Spot and Futures. (RSA and
Ed25519 are also supported for Spot; this doc focuses on HMAC, the default and
most portable.)

### 2.1 The signing recipe (every signed request)

1. Build your query string / JSON body parameters.
2. Append `timestamp=<ms epoch>` and (recommended) `recvWindow=<ms>`.
3. `queryString = urlencode(params, sorted)` — MUST be sorted alphabetically.
4. `signature = HMAC_SHA256(secret, queryString)` (hex digest).
5. Send `X-MBX-APIKEY: <apiKey>` in the header.
6. For GET, the signature goes in the query string; for POST/DELETE/PUT it also
   goes in the query string (Binance reads signature from the URL, not the body,
   for most endpoints).

### 2.2 Minimal signed GET (Spot) — `requests`
```python
import time, hmac, hashlib, urllib.parse, requests

API_KEY = "YOUR_API_KEY"        # from secure store, NEVER inline
API_SECRET = "YOUR_API_SECRET"  # encrypted at rest, see storage-safety.md

def signed_get(host, path, params=None):
    params = params or {}
    params["timestamp"] = int(time.time() * 1000)
    params["recvWindow"] = 5000
    q = urllib.parse.urlencode(sorted(params.items()))
    sig = hmac.new(API_SECRET.encode(), q.encode(), hashlib.sha256).hexdigest()
    headers = {"X-MBX-APIKEY": API_KEY}
    url = f"{host}{path}?{q}&signature={sig}"
    r = requests.get(url, headers=headers, timeout=10)
    r.raise_for_status()
    return r.json()

# Example: account balances
print(signed_get("https://api.binance.com", "/api/v3/account"))
```

### 2.3 POST order (Spot)
```python
def place_spot_order(symbol, side, quantity, price=None, type_="MARKET"):
    params = {
        "symbol": symbol,
        "side": side,            # "BUY" or "SELL"
        "type": type_,
        "quantity": quantity,
        "timestamp": int(time.time() * 1000),
        "recvWindow": 5000,
        "newOrderRespType": "FULL",
    }
    if price is not None:
        params["price"] = price
    q = urllib.parse.urlencode(sorted(params.items()))
    sig = hmac.new(API_SECRET.encode(), q.encode(), hashlib.sha256).hexdigest()
    headers = {"X-MBX-APIKEY": API_KEY}
    url = f"https://api.binance.com/api/v3/order?{q}&signature={sig}"
    r = requests.post(url, headers=headers, timeout=10)
    return r.json()  # includes orderId, fills, etc.
```

### 2.4 Futures signed request (USDⓈ-M)
Identical signing recipe, different host and path prefixes:
```python
def fapi_signed_get(path, params=None):
    params = params or {}
    params["timestamp"] = int(time.time() * 1000)
    params["recvWindow"] = 5000
    q = urllib.parse.urlencode(sorted(params.items()))
    sig = hmac.new(API_SECRET.encode(), q.encode(), hashlib.sha256).hexdigest()
    headers = {"X-MBX-APIKEY": API_KEY}
    url = f"https://fapi.binance.com{path}?{q}&signature={sig}"
    return requests.get(url, headers=headers, timeout=10).json()

# Open positions
print(fapi_signed_get("/fapi/v2/positionRisk"))
```

### 2.5 Recommended libraries (don't hand-roll in prod)
- **`binance-connector`** (official, pip `binance-connector`) — thin, explicit
  wrapper; good for learning the signing model.
- **`python-binance`** (community, pip `python-binance`) — higher-level, handles
  signatures, websockets, and async; widely used for bots.
- **`ccxt`** — unified multi-exchange library; if you ever run the same strategy
  on multiple venues (Kraken, Bybit, OKX), `ccxt` keeps one code path. (The
  `05-market-cron` crypto fetcher already uses `ccxt` — reuse it.)

---

## 3. Rate limits — the thing that bites every bot

Binance rate limits are expressed in **request weight** (not raw request count)
and are enforced **per IP** for public endpoints and **per API key (UID)** for
signed endpoints, with a hard cap also per IP.

### 3.1 Two limits to track
1. **Per-endpoint weight limit** — e.g. `GET /api/v3/klines` costs 1–2 weight;
   `GET /api/v3/account` costs 10; some heavy endpoints cost 20–40.
2. **Per-IP / per-UID ceiling** — Spot enforces `IP: X weight per minute`
   (historically 6000 weight/min per IP, but verified against docs at launch).
   Futures enforces both `UID` and `IP` limits and a **concurrent order cap**.

### 3.2 Reading the `X-MBX-USED-WEIGHT` headers
Every response returns these headers (Spot):
```
X-MBX-USED-WEIGHT-1m   : <weight used in last 1 min>
X-MBX-ORDER-COUNT-1m   : <orders in last 1 min>
X-MBX-ORDER-COUNT-1d   : <orders in last 1 day>
```
**Always read `X-MBX-USED-WEIGHT-1m`** and back off before you hit the ceiling.
Futures returns `X-MBX-USED-WEIGHT-1M` and `X-BINANCE-USED-ORDER-COUNT`.

### 3.3 The 429 / 418 responses
| Code | Meaning | Action |
|------|---------|--------|
| `429` | Rate limit breached (weight or order count) | Back off; read `Retry-After` header if present |
| `418` | IP auto-banned (persistent 429 abuse) | **Stop all traffic** for the ban duration (often 2+ min); respect the ban or it extends |
| `5xx` | Binance-side error / maintenance | Retry with exponential backoff; check `@BinanceStatus` |

> ⚠️ A `418` is a **hard ban of your IP**. If you see it, halt the bot entirely
> for the ban window. Hammering through a 418 lengthens the ban and can get the
> API key revoked.

### 3.4 Weight budgeting pattern
```python
import time
class WeightBudget:
    def __init__(self, cap=5000, window=60):
        self.cap, self.window = cap, window
        self.used, self.t0 = 0, time.time()
    def consume(self, w):
        now = time.time()
        if now - self.t0 >= self.window:
            self.used, self.t0 = 0, now
        if self.used + w > self.cap:
            sleep_for = self.window - (now - self.t0) + 0.1
            time.sleep(max(0, sleep_for))
            self.used, self.t0 = 0, time.time()
        self.used += w
```
Call `budget.consume(weight)` before each request. Tune `cap` to ~80% of the
documented ceiling to leave headroom.

---

## 4. Timestamp, `recvWindow`, and clock skew

Binance rejects requests where `|serverTime - timestamp| > recvWindow`
(default recvWindow is 5000 ms; max 60000 ms).

- **Symptom:** `{"code":-1021,"msg":"Timestamp for this request was 1000ms ahead of the server's time."}`
- **Cause:** Your machine clock is drifted (common on Windows VMs, containers
  without NTP).
- **Fix:** Sync the system clock (NTP/`w32tm`), and/or fetch
  `GET /api/v3/time` and compute an offset to apply to every `timestamp`.
```python
def server_offset():
    srv = requests.get("https://api.binance.com/api/v3/time", timeout=5).json()["serverTime"]
    return srv - int(time.time() * 1000)
OFFSET = server_offset()  # add to timestamp each call
# timestamp = int(time.time()*1000) + OFFSET
```
Also set `recvWindow=5000` (or a bit higher if your network jitter is large),
but don't crank it to 60000 — that widens the replay window for a stolen
signature.

---

## 5. Order lifecycle & filters (Spot)

Placing an order is rejected (`-1111`, `-1013`, `-2010`, etc.) if it violates
a **filter**. Knowing them saves hours.

### 5.1 Filter families (from `GET /api/v3/exchangeInfo`)
- **PRICE_FILTER**: `minPrice`, `maxPrice`, `tickSize` (price must be a multiple
  of `tickSize`, within `[minPrice, maxPrice]`).
- **LOT_SIZE** / **MARKET_LOT_SIZE**: `minQty`, `maxQty`, `stepSize` for the
  base asset; market orders use `MARKET_LOT_SIZE`.
- **MIN_NOTIONAL**: order `price * quantity` must exceed `minNotional`
  (some symbols have a `applyToMarket` flag and `avgPriceMins`).
- **PERCENT_PRICE**: price must be within `X%` of the last price (prevents fat
  fingers on limit orders).
- **ICEBERG_PARTS**, **MAX_NUM_ORDERS**, **MAX_NUM_ALGO_ORDERS**.

**Pattern:** fetch `exchangeInfo` once at startup, parse the filters per symbol,
and round your price/qty to the filter grid *before* sending. A `LOT_SIZE`
violation is the #1 newbie 400.

### 5.2 Order types
`LIMIT`, `MARKET`, `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`,
`TAKE_PROFIT_LIMIT`, `LIMIT_MAKER`. For a market-making or maker-rebate bot, use
`LIMIT_MAKER` (rejects if it would take liquidity).

### 5.3 Fill model & `FULL` response
Set `newOrderRespType=FULL` to get `fills[]` (price, qty, commission, asset)
so you can reconcile PnL precisely. For high-frequency, `ACK` is lighter.

---

## 6. Futures specifics (USDⓈ-M) — the dangerous part

Futures adds leverage, margin, position modes, and liquidation. **This is where
accounts get wiped.** Cover the essentials.

### 6.1 Position modes
- **One-way mode** (default): one position per symbol, side implied by net qty.
- **Hedge mode**: long and short positions held simultaneously per symbol.
Set via `POST /fapi/v1/positionSide/dual` (`dualSidePosition=true`). Your order
`side` + `positionSide` (`BOTH`/`LONG`/`SHORT`) then determine behavior.

### 6.2 Leverage & margin
- `POST /fapi/v1/leverage` sets `leverage` (1–125 depending on symbol).
- `POST /fapi/v1/marginType` sets `ISOLATED` or `CROSSED`.
- `POST /fapi/v1/positionMargin` adds/removes margin.
- **Always set leverage explicitly after opening the position context**; the
  default may be 20x and a small adverse move liquidates you.

### 6.3 Order types (futures)
`LIMIT`, `MARKET`, `STOP`/`STOP_MARKET`, `TAKE_PROFIT`/`TAKE_PROFIT_MARKET`,
`TRAILING_STOP_MARKET`. Note futures uses `timeInForce`, `reduceOnly`,
`closePosition`, `activationPrice` (for trailing), `priceRate`.

### 6.4 The liquidation math (conceptual)
Maintenance margin `MMR` scales with notional. Liquidation price moves closer as
leverage rises. A 100x position liquidates on a ~1% adverse move. Bots MUST
compute liquidation price and set a stop **well before** it. The
`positionRisk` endpoint returns `liquidationPrice`, `markPrice`, `marginRatio`
— poll it, and auto-deleverage (close) if `marginRatio` crosses a safety line.

### 6.5 `reduceOnly` and `closePosition`
Use `reduceOnly=true` on stop/take-profit orders so they can never *increase*
exposure. Use `closePosition=true` to flatten the whole position with one order.

### 6.6 Futures rate limits
- Order rate limit is per `UID` **and** per `IP`, with a cap on **concurrent**
  open orders. Exceeding returns `-1003` / order-count errors.
- Weight limits mirror Spot but with separate counters (`fapi` host).

---

## 7. WebSocket streaming (don't poll)

Polling eats weight and lags price. Use streams.

### 7.1 Spot streams
- `<symbol>@kline_<interval>` — candles.
- `<symbol>@trade` / `@aggTrade` — individual/aggregated trades.
- `<symbol>@bookTicker` — best bid/ask (cheap, ideal for market-making).
- `<symbol>@depth` / `@depth20@100ms` — order book.
- User Data Stream: `POST /api/v3/userDataStream` → `listenKey`, then
  `wss://stream.binance.com:9443/ws/<listenKey>` for account updates (orders,
  balances). **`listenKey` expires after 60 min** — `PUT` to keep it alive every
  ~30 min (`/api/v3/userDataStream` with the `listenKey`).

### 7.2 Futures streams
- `wss://fstream.binance.com/ws/<listenKey>` for user data.
- `<symbol>@markPrice` for funding/liquidation-adjacent data.
- Multiplex: `wss://stream.binance.com:9443/stream?streams=btcusdt@trade/ethusdt@kline_1m`.

### 7.3 Keepalive is mandatory
```python
def keepalive_listenkey(host, path, key):
    requests.put(f"{host}{path}?listenKey={key}", timeout=5)
# schedule every 30 min
```

---

## 8. Error codes every bot must handle

| Code | Meaning | Handling |
|------|---------|----------|
| `-1000` | Unknown / server busy | retry w/ backoff |
| `-1003` | Too many requests (weight) | back off per §3 |
| `-1013` | Order not allowed (filter) | inspect filters §5.1 |
| `-1015` | IP banned | halt, wait out ban |
| `-1021` | Bad timestamp | clock sync §4 |
| `-1022` | Bad signature | re-sign, check secret/encoding |
| `-1100` | Illegal parameter | validate input |
| `-1101` | Too many params | remove unused |
| `-1111` | Precision too deep | round to `stepSize` |
| `-2010` | New order rejected (balance) | insufficient funds |
| `-2013` | Order not found (cancel) | already filled/canceled |
| `-2014` | API key invalid | key mismatch |
| `-2015` | API key no permission | enable on dashboard |

**Never assume a rejected order means "didn't happen."** On timeout, **query the
order** (`GET /api/v3/order` with `orderId`) to learn its true state before
retrying — naive retries cause double-fills.

---

## 9. API key permissioning & security

On the Binance dashboard, restrict keys:
- **Enable Spot / Enable Futures / Enable Margin** granularly.
- **Restrict IP** to your bot's egress IP(s) — strongest control.
- **Disable withdrawals** on trading keys (use a separate, air-gapped key if you
  ever need to move funds).
- Rotate keys periodically; store secrets encrypted at rest per
  `01-crawler-scrapper/cookies-tokens/storage-safety.md`.

---

## 10. Production-hardening checklist

- [ ] Use **testnet** for all dev; separate Spot + Futures testnet keys.
- [ ] Fetch `exchangeInfo` once, cache filters; round price/qty to grid.
- [ ] Compute `serverTime` offset at startup; apply to every timestamp.
- [ ] Implement `WeightBudget` (§3.4); read `X-MBX-USED-WEIGHT` headers.
- [ ] Handle `429`→backoff, `418`→full halt. Never hammer through a ban.
- [ ] On order timeout, **query order status** before retry (no double-fills).
- [ ] Keep `listenKey` alive every 30 min; reconnect WS on drop with backoff.
- [ ] Futures: set leverage + margin mode explicitly; set stops via
      `reduceOnly`; monitor `marginRatio` and auto-deleverage.
- [ ] Log every request/response (redact signature/secret) for reconciliation.
- [ ] Circuit breaker: if N consecutive errors or drawdown > X%, halt and alert.
- [ ] Use `ccxt` if multi-exchange; reuse `05-market-cron`'s ccxt fetcher.

---

## 11. Minimal end-to-end bot skeleton (Spot, `python-binance`)
```python
from binance.client import Client
from binance.exceptions import BinanceAPIException
import time

client = Client(API_KEY, API_SECRET)  # keys from secure store

def safe_order(symbol, side, qty):
    info = client.get_symbol_info(symbol)
    # round qty to LOT_SIZE stepSize
    step = float([f["stepSize"] for f in info["filters"] if f["filterType"]=="LOT_SIZE"][0])
    qty = round(float(qty) / step) * step
    for attempt in range(5):
        try:
            return client.create_order(symbol=symbol, side=side,
                                       type="MARKET", quantity=qty)
        except BinanceAPIException as e:
            if e.code in (-1003, -1021):
                time.sleep(2 ** attempt)
                continue
            raise
    raise RuntimeError("order failed after retries")

# Example: DCA buy on a signal from the vault pipeline
# if signal_score > THRESHOLD: safe_order("BNBUSDT", "BUY", qty)
```

---

## 12. Mapping to the rest of the vault

- `02-trading-bot/architectures/event-driven-baseline.md` — canonical bot
  skeleton (queue + state machine); this file is the *broker* layer it calls.
- `02-trading-bot/strategies/` — consume market data from
  `05-market-cron` (IHSG/FX/crypto) and emit signals to this API layer.
- `02-trading-bot/risk-management/position-sizing-kelly.md` — sizing math that
  decides the `qty` passed into `safe_order`.
- `02-trading-bot/signals/news-sentiment-scoring.md` — scores headlines; a
  positive/negative score can flip `side`.
- `05-market-cron` — provides the price/volume feeds (REST or WS) this bot acts on.

---

## 13. Known limitations & TODO

- [ ] Verify exact current weight caps and per-endpoint weights against live docs
      at launch (they shift with exchange load/region).
- [ ] Add a `ccxt`-based cross-exchange comparison so the bot can route orders to
      the best venue (price + fee).
- [ ] Implement the futures liquidation monitor (`positionRisk` poller +
      auto-deleverage) as a standalone safety service.
- [ ] Add a replay/simulation mode that reads historical `klines` and replays
      the strategy before risking capital.
- [ ] Document COIN-M (delivery) futures separately if the strategy needs it.

---

## 14. Full reconnecting WebSocket client (asyncio)

Polling burns weight and lags. Here is a production-shaped WS client that
auto-reconnects, keeps the `listenKey` alive, and never silently drops data.

```python
import asyncio, json, time, requests, websockets  # pip install websockets

HOST_WS = "wss://stream.binance.com:9443"
REST = "https://api.binance.com"

class BinanceWS:
    def __init__(self, api_key, api_secret):
        self.api_key, self.api_secret = api_key, api_secret
        self.listen_key = None
        self.stop = False

    def _new_listen_key(self):
        r = requests.post(f"{REST}/api/v3/userDataStream",
                          headers={"X-MBX-APIKEY": self.api_key}, timeout=5)
        self.listen_key = r.json()["listenKey"]

    def _keepalive(self):
        requests.put(f"{REST}/api/v3/userDataStream",
                     params={"listenKey": self.listen_key},
                     headers={"X-MBX-APIKEY": self.api_key}, timeout=5)

    async def _user_stream(self):
        while not self.stop:
            try:
                async with websockets.connect(f"{HOST_WS}/ws/{self.listen_key}") as ws:
                    async for msg in ws:
                        ev = json.loads(msg)
                        self.on_event(ev)   # your handler: orders, balances
            except Exception as e:
                print(f"WS dropped: {e}; reconnect in 3s")
                await asyncio.sleep(3)

    async def _keepalive_loop(self):
        while not self.stop:
            await asyncio.sleep(30 * 60)
            try: self._keepalive()
            except Exception as e: print(f"keepalive failed: {e}")

    def on_event(self, ev):
        # Dispatch by event type: executionReport, outboundAccountPosition, ...
        print("EVENT", ev.get("e"), ev)

    async def run(self, market_streams):
        self._new_listen_key()
        # market data stream (multiplexed)
        url = f"{HOST_WS}/stream?streams={'/'.join(market_streams)}"
        await asyncio.gather(self._user_stream(), self._keepalive_loop(),
                             self._market_stream(url))

    async def _market_stream(self, url):
        while not self.stop:
            try:
                async with websockets.connect(url) as ws:
                    async for msg in ws:
                        self.on_market(json.loads(msg))
            except Exception as e:
                print(f"market WS dropped: {e}; retry 3s")
                await asyncio.sleep(3)

    def on_market(self, msg):
        print("MARKET", msg.get("stream"), msg.get("data", {}).get("s"))

# Usage:
# bws = BinanceWS(API_KEY, API_SECRET)
# asyncio.run(bws.run(["btcusdt@bookTicker", "ethusdt@trade"]))
```

**Reconnect rules:** exponential backoff on drop (3s→up to 60s cap), re-issue
`listenKey` if `listenKey` is rejected (`-1125` invalid), and never block the
event loop on slow handlers — offload to a queue/thread.

---

## 15. Cross-exchange routing with `ccxt`

If the same strategy should also run on Bybit/OKX/Kraken, `ccxt` gives one
interface. Reuse the `05-market-cron` ccxt setup.

```python
import ccxt
def best_venue(symbol, side, qty):
    ex = {"binance": ccxt.binance({"apiKey": K, "secret": S}),
          "okx": ccxt.okx({"apiKey": K2, "secret": S2}),
          "bybit": ccxt.bybit({"apiKey": K3, "secret": S3})}
    best, best_price = None, None
    for name, e in ex.items():
        try:
            ob = e.fetch_order_book(symbol)
            px = ob["bids"][0][0] if side == "BUY" else ob["asks"][0][0]
            # include taker fee comparison here
            if best_price is None or (side == "BUY" and px < best_price) \
               or (side == "SELL" and px > best_price):
                best, best_price = name, px
        except Exception as ex_err:
            print(f"{name} unavailable: {ex_err}")
    return best, best_price
```
Route the order to `best` venue. Note: ccxt normalizes *most* of the signing
and error model, but futures leverage/position-mode still differ per exchange —
isolate those behind adapter functions.

---

## 16. Backtest / replay harness (no capital at risk)

Before going live, replay against historical `klines`:

```python
import ccxt, pandas as pd
def load_klines(symbol, timeframe, limit=1000):
    b = ccxt.binance()
    raw = b.fetch_ohlcv(symbol, timeframe, limit=limit)
    return pd.DataFrame(raw, columns=["ts","open","high","low","close","vol"])

def replay(symbol, signal_fn, timeframe="1h"):
    df = load_klines(symbol, timeframe)
    cash, pos = 1000.0, 0.0
    for i in range(1, len(df)):
        sig = signal_fn(df.iloc[:i])           # your strategy
        px = df["close"].iloc[i]
        if sig > 0 and pos == 0:
            pos = cash / px; cash = 0
        elif sig < 0 and pos > 0:
            cash = pos * px; pos = 0
    final = cash + pos * df["close"].iloc[-1]
    return final  # compare vs buy-and-hold
```
Run this on every strategy in `02-trading-bot/strategies/` before wiring it to
the live API layer in §11. A strategy that loses to buy-and-hold in replay has
no business touching the broker.

---

## 17. Troubleshooting FAQ

**Q: `-1022` Bad signature even though I HMAC correctly.**
A: Most common causes: (1) params not sorted alphabetically before encoding;
(2) `timestamp` computed twice with different values (compute once, reuse);
(3) signature sent in body instead of query string; (4) trailing/extra `&`
when concatenating `q & signature`.

**Q: Orders rejected with `-1111` / precision.**
A: You didn't round `price` to `tickSize` and `qty` to `stepSize`. Parse
`exchangeInfo` and quantize before sending.

**Q: Getting `418` IP banned constantly.**
A: You're exceeding weight and not backing off. Implement `WeightBudget` (§3.4),
read `X-MBX-USED-WEIGHT` headers, and halt on `418`. Spread load across
whitelisted IPs if you have them.

**Q: Futures position liquidated instantly.**
A: Default leverage may be high and you didn't set it. Always set leverage +
margin mode explicitly; place `reduceOnly` stops; monitor `marginRatio`.

**Q: `listenKey` stops delivering account events.**
A: It expired (60 min). The `PUT` keepalive (§7.3, §14) must run every ~30 min.
If you see `-1125`, reissue a new key.

**Q: `recvWindow` errors under good latency.**
A: Machine clock drift. Sync NTP and apply the `serverTime` offset (§4).

**Q: Double-filled on retry after a timeout.**
A: You retried without checking state. On timeout, `GET` the order by `orderId`
before resending (§8).

---

## 18. Glossary

- **Weight:** cost unit Binance meters requests by; not raw request count.
- **recvWindow:** max allowed clock skew between your `timestamp` and server.
- **listenKey:** ephemeral token granting access to a user-data WS stream.
- **MARKET_LOT_SIZE:** lot filter applied to market orders specifically.
- **reduceOnly:** order flag preventing an increase in position size.
- **marginRatio:** used-margin / account-equity; liquidation risk indicator.
- **dualSidePosition:** hedge-mode toggle allowing simultaneous long+short.
- **MIN_NOTIONAL:** minimum order value (`price × qty`) filter.
- **tickSize / stepSize:** price / quantity granularity enforced by filters.
- **ccxt:** unified multi-exchange trading library (one API, many venues).

---

*Generated by the Money Glitch Vault Filler cron tick. Web verification was
unavailable at generation time (web tools returned `PARALLEL_API_KEY not set`);
the HMAC-SHA256 signing model, endpoint hosts, and rate-limit structure are from
stable, long-lived Binance public documentation. Re-read the official API
references before production use.*
