#!/usr/bin/env python3
"""normalize_region.py — D2: map 06 price-data region strings to a province taxonomy.

The `06-harga-pangan-papan` feed carries region as a raw string ("Nasional",
"Region A/B/C"). Region-aware warung restock (see
`03-id-business-trends/bottlenecks/warung-region-aware-stock.md`) and the fair-price
arbitrage radar both need province/kabupaten resolution. This module normalizes a
06 data row and computes the premium-vs-Nasional that drives the arbitrage signal.

USAGE
-----
    python normalize_region.py 06-harga-pangan-papan/data/latest.json
    # prints normalized rows + any commodity with >15% regional premium

The province lists below are a STARTER taxonomy. Expand from the province/kabupaten
mapping already used in the warung / COD bottleneck docs before production use.
"""
import json
import sys

# Starter region -> province taxonomy. Region C is the persistent +24% rice premium zone.
REGION_MAP = {
    "Nasional": {"scope": "national", "provinces": []},
    "Region A": {"scope": "region", "provinces": ["DKI Jakarta", "Jawa Barat", "Banten"]},
    "Region B": {"scope": "region", "provinces": ["Jawa Tengah", "Jawa Timur", "DI Yogyakarta"]},
    "Region C": {"scope": "region", "provinces": ["Papua", "Papua Barat", "Maluku", "NTT"]},
}

PREMIUM_THRESHOLD = 0.15  # >15% vs Nasional = actionable arbitrage


def normalize_row(row: dict) -> dict:
    r = row.get("region") or row.get("wilayah") or "Nasional"
    mapped = REGION_MAP.get(r, {"scope": "unknown", "provinces": []})
    return {**row, "region_normalized": mapped, "region_raw": r}


def premium_vs_nasional(rows: list[dict]) -> list[dict]:
    """Flag any (commodity, region) whose price exceeds the Nasional price by >15%."""
    nat = {}
    for row in rows:
        if (row.get("region") or "Nasional") == "Nasional":
            c = row.get("commodity") or row.get("komoditas")
            price = row.get("price") or row.get("harga")
            if c and price:
                nat[c] = price
    flags = []
    for row in rows:
        region = row.get("region") or "Nasional"
        if region == "Nasional":
            continue
        c = row.get("commodity") or row.get("komoditas")
        price = row.get("price") or row.get("harga")
        base = nat.get(c)
        if c and price and base:
            prem = (price - base) / base
            if prem > PREMIUM_THRESHOLD:
                flags.append({"commodity": c, "region": region,
                              "premium_pct": round(prem * 100, 1),
                              "price": price, "nasional": base})
    return flags


def _extract_rows(data):
    if isinstance(data, list):
        return data
    for key in ("rows", "data", "prices", "items"):
        if isinstance(data, dict) and isinstance(data.get(key), list):
            return data[key]
    return []


def main(argv):
    if len(argv) != 2:
        print("usage: normalize_region.py <06-latest.json>", file=sys.stderr)
        return 2
    with open(argv[1], encoding="utf-8") as f:
        data = json.load(f)
    rows = _extract_rows(data)
    if not rows:
        print("WARN: no rows found (schema mismatch); adjust _extract_rows.",
              file=sys.stderr)
        return 1
    norm = [normalize_row(r) for r in rows]
    flags = premium_vs_nasional(rows)
    print(f"normalized {len(norm)} rows")
    if flags:
        print(f"ARBITRAGE ({len(flags)} commodity/region > +{int(PREMIUM_THRESHOLD*100)}%):")
        for fl in flags:
            print(f"  {fl['commodity']} @ {fl['region']}: +{fl['premium_pct']}% "
                  f"(Rp {fl['price']} vs Nasional Rp {fl['nasional']})")
    else:
        print("no regional premium above threshold")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
