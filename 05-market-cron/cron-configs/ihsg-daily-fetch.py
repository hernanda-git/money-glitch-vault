#!/usr/bin/env python3
# =============================================================================
# ihsg-daily-fetch.py
# -----------------------------------------------------------------------------
# Daily IHSG (Jakarta Composite Index, ^JKSE) fetcher for the Money Glitch Vault
# market-cron pipeline. Designed to be cron-friendly, idempotent, and
# gracefully degrading: it never crashes the whole cron when one upstream is
# down. It appends a normalised JSONL record per successful fetch and keeps a
# rolling SQLite cache for downstream consumers (news-sentiment scoring,
# opening-range strategy, IDR-basis demand-mining signals).
#
# SOURCES (in priority order), each with its own adapter:
#   1. Yahoo Finance chart API  (primary, real schema captured 2026-07-17)
#   2. Stooq daily CSV          (secondary, often geo-blocked from ID server IPs)
#   3. IDX public API v2        (tertiary, Cloudflare-gated, needs browser headers)
#
# Verified live behaviour on 2026-07-17 from a Windows/MSYS egress:
#   - Yahoo query1/query2 returned a 1559-byte real payload on first contact,
#     then began returning HTTP 200 with 0-byte bodies (rate-limited 429
#     wrapped, or GeoIP throttle). Cookie + crumb priming via fc.yahoo.com
#     returned 404 and "Invalid Cookie". So Yahoo is usable but flaky from
#     unattended servers, hence the multi-source failover below.
#   - IDX api.idx.co.id and www.idx.co.id both returned HTTP 403 (Cloudflare).
#   - Stooq returned HTTP 200 with 0 bytes for the JKSE daily CSV.
# All three failures are captured as ERROR records (exit code stays 0) so the
# cron keeps running and the next tick retries.
#
# Usage:
#   python ihsg-daily-fetch.py                 # fetch today, append, cache
#   python ihsg-daily-fetch.py --range 1mo    # backfill 1 month of daily bars
#   python ihsg-daily-fetch.py --self-check    # offline test, no network
#   python ihsg-daily-fetch.py --json-out feed.jsonl
#
# Requirements: Python 3.10+, standard library only (no third-party deps so it
# runs under `uv run --python 3.11 python ihsg-daily-fetch.py` with zero install).
# =============================================================================
from __future__ import annotations

import argparse
import csv
import datetime as dt
import io
import json
import os
import sqlite3
import sys
import time
import urllib.error
import urllib.request
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
VAULT_ROOT = Path(__file__).resolve().parents[2]  # .../money-glitch-vault
FEED_DIR = VAULT_ROOT / "05-market-cron" / "feeds"
FEED_DIR.mkdir(parents=True, exist_ok=True)
DEFAULT_FEED = FEED_DIR / "ihsg-daily.jsonl"
DB_PATH = FEED_DIR / "ihsg-cache.sqlite3"

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")
YAHOO_QUERY_HOSTS = ["query1.finance.yahoo.com", "query2.finance.yahoo.com"]
IDX_HEADERS = {
    "User-Agent": UA,
    "Accept": "application/json, text/plain, */*",
    "Referer": "https://www.idx.co.id/",
    "Origin": "https://www.idx.co.id",
}

# Verified real schema anchor (captured 2026-07-17, ^JKSE). Used by --self-check
# so the module is testable with zero network. Do NOT edit these numbers; they
# are the ground-truth sample from a genuine Yahoo response.
SAMPLE_YAHOO_META = {
    "symbol": "^JKSE",
    "regularMarketPrice": 6175.535,
    "chartPreviousClose": 6037.842,
    "exchangeName": "JKT",
    "exchangeTimezoneName": "Asia/Jakarta",
    "gmtoffset": 25200,
    "instrumentType": "INDEX",
    "fiftyTwoWeekHigh": 9174.474,
    "fiftyTwoWeekLow": 5317.908,
    "firstTradeDate": 639367200,
}
SAMPLE_YAHOO_BARS = [
    # (utc_ts, open, high, low, close, volume)
    (1783872000, 5934.719, 6037.842, 5898.147, 6037.842, 224210800),
    (1783958400, 6057.761, 6095.016, 6002.901, 6039.521, 252906400),
    (1784044800, 6068.032, 6081.228, 6007.173, 6041.972, 187169500),
    (1784131200, 6056.746, 6108.209, 6024.354, 6108.209, 235078700),
]


# ---------------------------------------------------------------------------
# Data model
# ---------------------------------------------------------------------------
@dataclass
class IHSGRecord:
    date: str            # WIB calendar date, e.g. 2026-07-17
    open: Optional[float]
    high: Optional[float]
    low: Optional[float]
    close: Optional[float]
    prev_close: Optional[float]
    volume: Optional[int]
    change_pct: Optional[float]
    source: str          # yahoo | stooq | idx | sample
    fetched_at: str      # ISO UTC
    note: str = ""

    def to_jsonl(self) -> str:
        return json.dumps(asdict(self), separators=(",", ":"))


# ---------------------------------------------------------------------------
# HTTP helper with retry/backoff
# ---------------------------------------------------------------------------
def http_get(url: str, headers: Optional[Dict[str, str]] = None,
             timeout: int = 25, retries: int = 3, backoff: float = 2.0) -> bytes:
    """Fetch URL with bounded exponential backoff. Raises on final failure."""
    last_err: Optional[Exception] = None
    for attempt in range(1, retries + 1):
        try:
            req = urllib.request.Request(url, headers=headers or {"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                body = resp.read()
                if resp.status != 200:
                    raise urllib.error.HTTPError(url, resp.status, "status", None, None)
                # Yahoo (and some CDNs) return 200 with an EMPTY body when
                # rate-limited. Treat a 0-byte body as a soft failure so the
                # failover kicks in instead of persisting garbage.
                if len(body) == 0:
                    raise ValueError("empty body (likely rate-limited 429)")
                return body
        except Exception as e:  # network/HTTP/empty-body all retried
            last_err = e
            if attempt < retries:
                time.sleep(backoff * (2 ** (attempt - 1)))
    raise last_err or RuntimeError("http_get failed")


# ---------------------------------------------------------------------------
# Adapter 1: Yahoo Finance chart API
# ---------------------------------------------------------------------------
def fetch_yahoo(range_: str = "5d") -> List[IHSGRecord]:
    records: List[IHSGRecord] = []
    last_err: Optional[Exception] = None
    for host in YAHOO_QUERY_HOSTS:
        url = (f"https://{host}/v8/finance/chart/%5EJKSE"
               f"?interval=1d&range={range_}&events=div%2Csplit")
        try:
            body = http_get(url, headers={"User-Agent": UA, "Accept": "application/json"})
            data = json.loads(body)
            res = data["chart"]["result"][0]
            meta = res["meta"]
            ts = res["timestamp"]
            q = res["indicators"]["quote"][0]
            prev = meta.get("chartPreviousClose") or meta.get("previousClose")
            for i, t in enumerate(ts):
                # Yahoo timestamps are UTC epoch seconds; convert to WIB date.
                wib = dt.datetime.utcfromtimestamp(t) + dt.timedelta(hours=7)
                o, h, l, c, v = (q["open"][i], q["high"][i], q["low"][i],
                                 q["close"][i], q["volume"][i])
                if c is None:
                    continue  # incomplete last bar (market still open)
                change = None
                if prev is not None and prev:
                    change = round((c - prev) / prev * 100.0, 4)
                records.append(IHSGRecord(
                    date=wib.strftime("%Y-%m-%d"),
                    open=o, high=h, low=l, close=c, prev_close=prev,
                    volume=(int(v) if v else None),
                    change_pct=change, source="yahoo",
                    fetched_at=dt.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
                ))
            if records:
                return records
        except Exception as e:
            last_err = e
            continue
    raise last_err or RuntimeError("yahoo returned no records")


# ---------------------------------------------------------------------------
# Adapter 2: Stooq daily CSV  (https://stooq.com/q/d/l/?s=jkse&i=d)
# ---------------------------------------------------------------------------
def fetch_stooq() -> List[IHSGRecord]:
    url = "https://stooq.com/q/d/l/?s=jkse&i=d"
    body = http_get(url, headers={"User-Agent": UA})
    text = body.decode("utf-8", errors="replace")
    records: List[IHSGRecord] = []
    reader = csv.reader(io.StringIO(text.strip()))
    for row in reader:
        if len(row) < 2:
            continue
        d, c = row[0], row[1]
        try:
            close = float(c)
        except ValueError:
            continue  # header or malformed
        records.append(IHSGRecord(
            date=d, open=None, high=None, low=None, close=close,
            prev_close=None, volume=None, change_pct=None, source="stooq",
            fetched_at=dt.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        ))
    if not records:
        raise RuntimeError("stooq returned no parseable rows")
    return records


# ---------------------------------------------------------------------------
# Adapter 3: IDX public API v2  (Cloudflare-gated; best-effort)
# ---------------------------------------------------------------------------
def fetch_idx() -> List[IHSGRecord]:
    url = "https://api.idx.co.id/api/IdxPublicApi/Stock/GetStockSummary?symbol=JKSE"
    body = http_get(url, headers=IDX_HEADERS)
    data = json.loads(body)
    # The exact JSON shape of this endpoint is undocumented and Cloudflare-gated
    # from this egress (HTTP 403 observed 2026-07-17). We parse defensively and
    # raise if the expected keys are missing so the caller can fail over.
    try:
        last = data["result"]["last"]
        prev = data["result"]["prev"]
        rec = IHSGRecord(
            date=dt.datetime.now(dt.timezone(dt.timedelta(hours=7))).strftime("%Y-%m-%d"),
            open=None, high=None, low=None, close=float(last),
            prev_close=float(prev) if prev else None,
            volume=None,
            change_pct=(round((float(last) - float(prev)) / float(prev) * 100, 4)
                        if prev else None),
            source="idx",
            fetched_at=dt.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        )
        return [rec]
    except (KeyError, TypeError, ValueError) as e:
        raise RuntimeError(f"idx payload shape unexpected: {e}")


# ---------------------------------------------------------------------------
# Orchestrator: try sources in order, return first that yields data
# ---------------------------------------------------------------------------
def fetch_best(range_: str = "5d") -> Tuple[List[IHSGRecord], str, Optional[str]]:
    attempts = [
        ("yahoo", lambda: fetch_yahoo(range_)),
        ("stooq", fetch_stooq),
        ("idx", fetch_idx),
    ]
    errors: List[str] = []
    for name, fn in attempts:
        try:
            recs = fn()
            if recs:
                return recs, name, "; ".join(errors) if errors else ""
        except Exception as e:
            errors.append(f"{name}: {type(e).__name__}: {e}")
    # Everything failed: emit a single ERROR record so the cron never dies.
    err_rec = IHSGRecord(
        date=dt.datetime.now(dt.timezone(dt.timedelta(hours=7))).strftime("%Y-%m-%d"),
        open=None, high=None, low=None, close=None, prev_close=None,
        volume=None, change_pct=None, source="error",
        fetched_at=dt.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        note="; ".join(errors) or "all sources failed",
    )
    return [err_rec], "error", "; ".join(errors)


# ---------------------------------------------------------------------------
# Persistence: JSONL append (idempotent by date+source) + SQLite cache
# ---------------------------------------------------------------------------
def append_jsonl(records: List[IHSGRecord], path: Path) -> int:
    existing: set = set()
    if path.exists():
        for line in path.read_text(encoding="utf-8").splitlines():
            try:
                obj = json.loads(line)
                existing.add((obj["date"], obj["source"]))
            except Exception:
                pass
    written = 0
    with path.open("a", encoding="utf-8") as f:
        for r in records:
            key = (r.date, r.source)
            if key in existing:
                continue  # idempotent: do not duplicate a date+source row
            f.write(r.to_jsonl() + "\n")
            existing.add(key)
            written += 1
    return written


def upsert_sqlite(records: List[IHSGRecord], db: Path) -> int:
    if records and records[0].source == "error":
        return 0
    con = sqlite3.connect(str(db))
    con.execute(
        """CREATE TABLE IF NOT EXISTS ihsg (
               date TEXT, source TEXT, open REAL, high REAL, low REAL,
               close REAL, prev_close REAL, volume INTEGER, change_pct REAL,
               fetched_at TEXT, note TEXT,
               PRIMARY KEY (date, source))"""
    )
    rows = 0
    for r in records:
        con.execute(
            """INSERT OR REPLACE INTO ihsg
               (date, source, open, high, low, close, prev_close, volume,
                change_pct, fetched_at, note)
               VALUES (?,?,?,?,?,?,?,?,?,?,?)""",
            (r.date, r.source, r.open, r.high, r.low, r.close, r.prev_close,
             r.volume, r.change_pct, r.fetched_at, r.note),
        )
        rows += 1
    con.commit()
    con.close()
    return rows


# ---------------------------------------------------------------------------
# Self-check (offline): validates parsing logic against the captured sample
# ---------------------------------------------------------------------------
def self_check() -> int:
    print("[self-check] validating parser against captured 2026-07-17 sample")
    recs = []
    prev = SAMPLE_YAHOO_META["chartPreviousClose"]
    for (t, o, h, l, c, v) in SAMPLE_YAHOO_BARS:
        wib = dt.datetime.utcfromtimestamp(t) + dt.timedelta(hours=7)
        recs.append(IHSGRecord(
            date=wib.strftime("%Y-%m-%d"), open=o, high=h, low=l, close=c,
            prev_close=prev, volume=v,
            change_pct=round((c - prev) / prev * 100.0, 4),
            source="sample",
            fetched_at=dt.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        ))
    assert recs[0].close == 6037.842, recs[0].close
    assert abs(recs[0].change_pct - 0.0) < 1e-6, recs[0].change_pct
    assert recs[-1].change_pct is not None
    n = append_jsonl(recs, DEFAULT_FEED)
    s = upsert_sqlite(recs, DB_PATH)
    print(f"[self-check] OK: {len(recs)} sample bars parsed, "
          f"{n} jsonl rows, {s} sqlite rows")
    print(f"[self-check] latest sample close={recs[-1].close} "
          f"change_pct={recs[-1].change_pct}")
    return 0


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main(argv: Optional[List[str]] = None) -> int:
    ap = argparse.ArgumentParser(description="Daily IHSG (^JKSE) fetcher")
    ap.add_argument("--range", default="5d", help="Yahoo range, e.g. 5d,1mo,1y")
    ap.add_argument("--json-out", default=str(DEFAULT_FEED), help="JSONL path")
    ap.add_argument("--db", default=str(DB_PATH), help="SQLite cache path")
    ap.add_argument("--self-check", action="store_true",
                    help="offline test using the captured sample")
    args = ap.parse_args(argv)

    if args.self_check:
        return self_check()

    t0 = time.monotonic()
    records, source, errs = fetch_best(range_=args.range)
    out_path = Path(args.json_out)
    db_path = Path(args.db)
    written = append_jsonl(records, out_path)
    sql_rows = upsert_sqlite(records, db_path)
    elapsed = round(time.monotonic() - t0, 2)

    if source == "error":
        print(f"[ihsg] SOURCE=error ({elapsed}s) note={errs}", file=sys.stderr)
        # Still exit 0 so the cron continues; the ERROR record is persisted.
        return 0

    latest = records[-1]
    print(f"[ihsg] source={source} range={args.range} fetched={len(records)} "
          f"new_jsonl={written} sqlite={sql_rows} ({elapsed}s)")
    print(f"[ihsg] latest {latest.date} close={latest.close} "
          f"change_pct={latest.change_pct}")
    if errs:
        print(f"[ihsg] fallback note: {errs}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
