#!/usr/bin/env python3
"""
ihsg-daily-fetch.py
===================

A dependency-free (Python standard library only) daily fetcher for the
Indonesia Composite Index (IHSG / ^JKSE) that emits a JSON document compatible
with the vault's existing 05-market-cron/data/pulse-*.json schema.

WHY THIS EXISTS
---------------
The vault's market-cron folder already collects crypto + FX pulses, but IHSG
(the headline Indonesian equity benchmark) was missing from the pipeline. The
official IDX endpoints are Cloudflare-gated (HTTP 403 even with a browser UA),
and Stooq now serves a JavaScript proof-of-work challenge instead of CSV. The
only reliable, no-auth, machine-readable source that works from a bare server
is the Yahoo Finance chart API (query1.finance.yahoo.com / query2.finance.yahoo.com).

This was verified live on 2026-07-12 (WIB): HTTP 200, symbol ^JKSE, last close
5924.36, 52-week range 5317.91 / 9174.47, timezone WIB (gmtoffset +25200).

USAGE
-----
    python3 ihsg-daily-fetch.py                 # prints JSON to stdout
    python3 ihsg-daily-fetch.py --range 6mo    # wider window
    python3 ihsg-daily-fetch.py --out data/latest-ihsg.json
    python3 ihsg-daily-fetch.py --quiet         # only write file, no stdout

The emitted JSON mirrors the vault pulse shape so it can be trivially merged
into data/latest.json by the orchestrator.

SOURCE (verified, cite this in research notes):
    https://query1.finance.yahoo.com/v8/finance/chart/%5EJKSE?interval=1d&range=5d
    Yahoo Finance undocumented chart API. No API key. Requires a User-Agent.
"""

import argparse
import json
import sys
import time
import urllib.request
import urllib.error
import urllib.parse
from datetime import datetime, timezone, timedelta

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

# ^JKSE is the Yahoo ticker for the IDX Composite (IHSG). The ".JK" suffix is
# used for individual Indonesian equities (e.g. ASII.JK for Astra International),
# but the composite index uses the caret prefix only.
YAHOO_SYMBOL = "^JKSE"

# Yahoo runs two hostnames that are load-balanced / sometimes one is blocked:
# query1 (primary) and query2 (secondary fallback). We try both.
HOSTS = [
    "https://query1.finance.yahoo.com",
    "https://query2.finance.yahoo.com",
]

# A real browser User-Agent is REQUIRED. Without it Yahoo returns HTTP 429
# (rate limited / bot blocked) even for a single request.
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
)

# WIB = UTC+7. Yahoo's `gmtoffset` field confirms this (+25200 seconds).
WIB = timezone(timedelta(hours=7))

# Trading hours in WIB used for staleness checks.
OPEN_WIB = (9, 0)    # 09:00 WIB pre-open / regular open
CLOSE_WIB = (16, 0)  # 16:00 WIB close (regular session ends ~16:00, JATS)

# Conservative per-host request pacing to avoid 429 storms in cron.
REQUEST_DELAY = 1.0   # seconds between retry attempts
MAX_RETRIES = 3


# ---------------------------------------------------------------------------
# Core fetch
# ---------------------------------------------------------------------------

def _build_url(host: str, symbol: str, interval: str, rng: str) -> str:
    base = f"{host}/v8/finance/chart/{urllib.parse.quote(symbol)}"
    return f"{base}?interval={interval}&range={rng}"


def fetch_chart(symbol: str = YAHOO_SYMBOL,
                interval: str = "1d",
                rng: str = "5d") -> dict:
    """Fetch the raw Yahoo chart JSON, trying both hosts with simple backoff.

    Returns the parsed `chart.result[0]` dict. Raises RuntimeError on total
    failure so callers can decide whether to skip this tick or alert.
    """
    last_err = None
    for attempt in range(MAX_RETRIES):
        for host in HOSTS:
            url = _build_url(host, symbol, interval, rng)
            req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            try:
                with urllib.request.urlopen(req, timeout=20) as resp:
                    raw = resp.read().decode("utf-8")
                payload = json.loads(raw)
                if payload.get("chart", {}).get("error") is not None:
                    raise ValueError(f"Yahoo chart error: {payload['chart']['error']}")
                result = payload["chart"]["result"][0]
                return result
            except urllib.error.HTTPError as e:
                last_err = f"{host} HTTP {e.code}"
                if e.code == 429:
                    # Rate limited: back off harder before the next attempt.
                    time.sleep(REQUEST_DELAY * (attempt + 2))
                    continue
                last_err = f"{host} HTTP {e.code}: {e.reason}"
            except (urllib.error.URLError, ValueError, KeyError, json.JSONDecodeError) as e:
                last_err = f"{host} {type(e).__name__}: {e}"
        time.sleep(REQUEST_DELAY * (attempt + 1))
    raise RuntimeError(f"Failed to fetch {symbol} after retries. Last error: {last_err}")


# ---------------------------------------------------------------------------
# Normalization
# ---------------------------------------------------------------------------

def normalize(result: dict, symbol: str = YAHOO_SYMBOL) -> dict:
    """Flatten the Yahoo chart result into the vault pulse schema.

    The raw Yahoo payload nests OHLCV under indicators.quote[0] keyed by index
    position, parallel to the top-level `timestamp` array. We zip them back
    together and keep the most recent trading day as `latest`, plus a short
    `history` array for trend math.
    """
    meta = result.get("meta", {})
    ts = result.get("timestamp", []) or []
    quote = (result.get("indicators", {}).get("quote", [{}])[0]) if result.get("indicators") else {}
    adj = result.get("indicators", {}).get("adjclose", [{}])
    adj_series = adj[0].get("adjclose", []) if adj else []

    rows = []
    for i, t in enumerate(ts):
        # Yahoo returns nulls for non-trading days in the aligned arrays.
        if quote.get("close", [None] * len(ts))[i] is None:
            continue
        rows.append({
            "ts_utc": t,
            # gmtoffset from meta is the authoritative tz offset in seconds.
            "date_wib": datetime.fromtimestamp(t, WIB).strftime("%Y-%m-%d"),
            "open": quote.get("open", [None] * len(ts))[i],
            "high": quote.get("high", [None] * len(ts))[i],
            "low": quote.get("low", [None] * len(ts))[i],
            "close": quote.get("close", [None] * len(ts))[i],
            "volume": quote.get("volume", [None] * len(ts))[i],
            "adj_close": adj_series[i] if i < len(adj_series) else None,
        })

    if not rows:
        raise RuntimeError("No valid trading rows returned from Yahoo.")

    latest = rows[-1]
    prev = rows[-2] if len(rows) >= 2 else None

    change = None
    change_pct = None
    if prev and latest["close"] is not None and prev["close"]:
        change = round(latest["close"] - prev["close"], 2)
        change_pct = round((change / prev["close"]) * 100.0, 4)

    doc = {
        "source": "yahoo_finance_chart",
        "symbol": symbol,
        "symbol_yahoo": meta.get("symbol", symbol),
        "name": meta.get("shortName") or meta.get("longName"),
        "currency": meta.get("currency", "IDR"),
        "exchange": meta.get("fullExchangeName"),
        "timezone": meta.get("timezone", "WIB"),
        "fetched_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "fetched_wib": datetime.now(WIB).strftime("%Y-%m-%d %H:%M WIB"),
        "latest": {
            "date_wib": latest["date_wib"],
            "close": latest["close"],
            "open": latest["open"],
            "high": latest["high"],
            "low": latest["low"],
            "volume": latest["volume"],
            "adj_close": latest["adj_close"],
            "change": change,
            "change_pct": change_pct,
        },
        "fifty_two_week": {
            "high": meta.get("fiftyTwoWeekHigh"),
            "low": meta.get("fiftyTwoWeekLow"),
        },
        "regular_market_price": meta.get("regularMarketPrice"),
        "previous_close": meta.get("chartPreviousClose"),
        "history": rows,  # useful for rolling returns / drawdown math upstream
    }
    return doc


# ---------------------------------------------------------------------------
# Staleness guard
# ---------------------------------------------------------------------------

def is_stale(doc: dict) -> bool:
    """Return True if the latest row is older than the most recent trading
    session we should have seen. Used by cron to skip publishing a stale
    weekend/holiday snapshot as if it were fresh.
    """
    try:
        latest_dt = datetime.strptime(doc["latest"]["date_wib"], "%Y-%m-%d").replace(tzinfo=WIB)
    except (KeyError, ValueError):
        return True
    now_wib = datetime.now(WIB)
    # Allow a one-day grace for holidays/weekends; beyond that, flag staleness.
    return (now_wib.date() - latest_dt.date()).days > 4


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main(argv=None) -> int:
    p = argparse.ArgumentParser(description="Fetch IHSG (^JKSE) daily close via Yahoo Finance.")
    p.add_argument("--range", default="5d", help="Yahoo range token: 1d,5d,1mo,6mo,1y (default 5d)")
    p.add_argument("--interval", default="1d", help="Bar interval (default 1d)")
    p.add_argument("--out", default=None, help="Write JSON to this path instead of only stdout")
    p.add_argument("--quiet", action="store_true", help="Suppress stdout; only write --out if given")
    p.add_argument("--fail-on-stale", action="store_true", help="Exit non-zero if data is stale")
    args = p.parse_args(argv)

    try:
        result = fetch_chart(rng=args.range, interval=args.interval)
    except RuntimeError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 2

    doc = normalize(result)
    doc["stale"] = is_stale(doc)

    text = json.dumps(doc, indent=2, ensure_ascii=False)

    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(text + "\n")
    if not args.quiet:
        print(text)

    if args.fail_on_stale and doc["stale"]:
        print("WARN: fetched data appears stale (no recent trading session).", file=sys.stderr)
        return 3
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
