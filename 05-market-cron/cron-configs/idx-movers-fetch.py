#!/usr/bin/env python3
"""idx-movers-fetch.py — heal the last dead equity leg (IDX top movers).

WHY THIS EXISTS
---------------
`05-market-cron/data/latest.json` carries `sources.idx_movers` that hit HTTP 429 — the old
Yahoo v7 `quote` endpoint is bot-blocked. The proven fix (see `ihsg-daily-fetch.py`) is the
**v8 chart API** with a browser User-Agent and dual-host retry. This script reuses that exact
pattern to compute IDX top movers (biggest % gainers / losers) across a fixed LQ45 + flagship
basket, and emits a pulse-compatible JSON the merge orchestrator splices into `latest.json`.

Verified live 2026-07-12 (WIB): emitted gainers/losers with real % moves.

USAGE
-----
    python idx-movers-fetch.py                 # prints JSON to stdout
    python idx-movers-fetch.py --out data/latest-idx-movers.json
    python idx-movers-fetch.py --quiet

SOURCE (same as ihsg-daily-fetch.py, cite this):
    https://query1.finance.yahoo.com/v8/finance/chart/<TICKER.JK>?interval=1d&range=5d
"""
import argparse
import json
import sys
import time
import urllib.request
import urllib.error
import urllib.parse
from datetime import datetime, timezone, timedelta

HOSTS = ["https://query1.finance.yahoo.com", "https://query2.finance.yahoo.com"]
USER_AGENT = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
              "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36")
WIB = timezone(timedelta(hours=7))
REQUEST_DELAY = 1.0
MAX_RETRIES = 3

# LQ45 + flagship IDX basket. ".JK" is the Yahoo suffix for Indonesian equities.
# Kept intentionally small & liquid so cron stays fast and 429-safe. Add tickers as needed.
BASKET = [
    "BBRI.JK", "BBCA.JK", "TLKM.JK", "ASII.JK", "BBNI.JK", "BMRI.JK",
    "UNVR.JK", "GOTO.JK", "ADRO.JK", "ANTM.JK", "PGAS.JK", "ICBP.JK",
    "INDF.JK", "KLBF.JK", "SMGR.JK", "TPIA.JK", "UNTR.JK", "AKRA.JK",
    "CPIN.JK", "ERAA.JK",
]
NAMES = {  # human-readable labels for the pulse (Yahoo shortName is sometimes null)
    "BBRI.JK": "Bank Rakyat Indonesia", "BBCA.JK": "Bank Central Asia",
    "TLKM.JK": "Telkom Indonesia", "ASII.JK": "Astra International",
    "BBNI.JK": "Bank Negara Indonesia", "BMRI.JK": "Bank Mandiri",
    "UNVR.JK": "Unilever Indonesia", "GOTO.JK": "GoTo Gojek Tokopedia",
    "ADRO.JK": "Adaro Energy", "ANTM.JK": "Aneka Tambang",
    "PGAS.JK": "Perusahaan Gas Negara", "ICBP.JK": "Indofood CBP",
    "INDF.JK": "Indofood Sukses Makmur", "KLBF.JK": "Kalbe Farma",
    "SMGR.JK": "Semen Indonesia", "TPIA.JK": "Chandra Asri Pacific",
    "UNTR.JK": "United Tractors", "AKRA.JK": "AKR Corporindo",
    "CPIN.JK": "Charoen Pokphand Indonesia", "ERAA.JK": "Erajaya Swasembada",
}


def fetch_chart(symbol: str) -> dict:
    last_err = None
    for attempt in range(MAX_RETRIES):
        for host in HOSTS:
            url = f"{host}/v8/finance/chart/{urllib.parse.quote(symbol)}?interval=1d&range=5d"
            req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            try:
                with urllib.request.urlopen(req, timeout=20) as resp:
                    raw = resp.read().decode("utf-8")
                payload = json.loads(raw)
                if payload.get("chart", {}).get("error") is not None:
                    raise ValueError(str(payload["chart"]["error"]))
                return payload["chart"]["result"][0]
            except urllib.error.HTTPError as e:
                last_err = f"{host} {symbol} HTTP {e.code}"
                if e.code == 429:
                    time.sleep(REQUEST_DELAY * (attempt + 2))
                    continue
            except (urllib.error.URLError, ValueError, KeyError, json.JSONDecodeError) as e:
                last_err = f"{host} {symbol} {type(e).__name__}: {e}"
        time.sleep(REQUEST_DELAY * (attempt + 1))
    raise RuntimeError(f"Failed {symbol}: {last_err}")


def pct_change(result: dict) -> float | None:
    ts = result.get("timestamp", []) or []
    quote = (result.get("indicators", {}).get("quote", [{}])[0]) if result.get("indicators") else {}
    closes = quote.get("close", []) or []
    # last two non-null closes
    vals = [c for i, c in enumerate(closes) if ts and c is not None][-2:]
    if len(vals) < 2 or not vals[-2]:
        return None
    return round(((vals[-1] - vals[-2]) / vals[-2]) * 100.0, 2)


def collect(basket: list[str]) -> list[dict]:
    rows = []
    for sym in basket:
        try:
            r = fetch_chart(sym)
            pct = pct_change(r)
            if pct is None:
                continue
            meta = r.get("meta", {})
            price = meta.get("regularMarketPrice")
            rows.append({
                "symbol": sym, "name": NAMES.get(sym, meta.get("shortName")),
                "price": price, "change_pct": pct,
            })
        except RuntimeError as e:
            print(f"WARN: {e}", file=sys.stderr)
    return rows


def build(basket: list[str]) -> dict:
    rows = collect(basket)
    rows.sort(key=lambda x: x["change_pct"], reverse=True)
    gainers = [r for r in rows if r["change_pct"] > 0][:5]
    losers = [r for r in rows if r["change_pct"] < 0][-5:][::-1]
    return {
        "source": "yahoo_finance_chart",
        "market": "IDX",
        "fetched_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "fetched_wib": datetime.now(WIB).strftime("%Y-%m-%d %H:%M WIB"),
        "count_scanned": len(basket),
        "count_priced": len(rows),
        "top_gainers": gainers,
        "top_losers": losers,
    }


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description="Compute IDX top movers via Yahoo v8 chart API.")
    p.add_argument("--out", default=None, help="Write JSON here (else stdout)")
    p.add_argument("--quiet", action="store_true")
    p.add_argument("--basket", nargs="*", default=BASKET)
    args = p.parse_args(argv)
    try:
        doc = build(args.basket)
    except RuntimeError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 2
    text = json.dumps(doc, indent=2, ensure_ascii=False)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(text + "\n")
    if not args.quiet:
        print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
