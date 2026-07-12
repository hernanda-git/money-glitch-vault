# Warung Region-Aware Stock — closing the 07↔06 loop

> A short spec on why warung restock / smart-stock **must** be province/kabupaten-aware, and
> how `06-harga-pangan-papan` `latest.json` (once its region column is normalized) feeds it.
> Closes the loop between the warung collective-buying one-pager (`07/opportunities/...`) and
> the `06` price data. Flagged as New gap #3 in the 2026-07-12 synthesis.

**File:** `03-id-business-trends/bottlenecks/warung-region-aware-stock.md`
**Created:** 2026-07-12
**Category:** Bottleneck analysis (spec)
**Priority:** MED
**Related files:**
- `07-gaps-and-opportunities/opportunities/warung-collective-buying-loyalty-toolkit.md` (phase-2 smart stock "must be region-aware")
- `06-harga-pangan-papan/data/latest.json` (the data source)
- `03-id-business-trends/bottlenecks/warung-micro-fulfillment.md`

---

## 1. The gap

The warung one-pager's phase-2 "smart stock" explicitly says restock logic must be
**region-aware**. But `06/data/latest.json` carries region as a **raw string**
(`Nasional` / `Region A` / `Region B` / `Region C`) with no province/kabupaten mapping. So
today the data *cannot* drive a region-aware alert — the loop is open.

## 2. Why region-awareness is non-negotiable

From `06`'s own snapshots (2026-07-08 → 07-10), the **Region-C rice premium is +23–24%**
vs Nasional and **has not moved in 3 daily snapshots**. That persistent premium *is* the
arbitrage margin — but only if the restock engine knows which warungs sit in Region C and
which suppliers sit in Region A/B (where rice is 8–23% cheaper). Without province mapping,
every warung gets the Nasional average and the premium is invisible.

This is the exact hook the `fair-price regional arbitrage` opportunity (weekly report Q2)
needs: match Region-C buyers (> +15% vs Nasional) with Region-A/B suppliers.

## 3. The normalization step (prerequisite — see D2)

`06` region strings must be mapped to the **30–40% province/kabupaten taxonomy** already used
in the warung/COD docs. Concretely:

```python
# D2 module: 06-harga-pangan-papan/normalize_region.py
REGION_MAP = {
    "Nasional": {"scope": "national"},
    "Region A": {"scope": "region", provinces": ["DKI Jakarta", "Jawa Barat", ...]},
    "Region B": {"scope": "region", "provinces": [...]},
    "Region C": {"scope": "region", "provinces": [...]},  # the +24% premium zone
}

def normalize(row: dict) -> dict:
    r = row.get("region") or row.get("wilayah") or "Nasional"
    mapped = REGION_MAP.get(r, {"scope": "unknown"})
    return {**row, "region_normalized": mapped}
```

Until this runs, `06` data is descriptive, not actionable.

## 4. The region-aware restock rule

```
for warung in kelurahan:
    region = normalize(warung.province)          # via D2
    staples = 06.latest(commodity="beras", region=region)
    if staples.premium_vs_nasional > 0.15:        # > +15%
        suggest_group_buy_from(cheaper_region)    # pooled buy (warung one-pager)
        alert_koperasi(staples.spread)
```

This wires `06` → `07/opportunities/warung-collective-buying` directly: the one-pager's
pooled-buy spread becomes *provably* larger in Region C.

## 5. New gaps

- **D2** (data infra): build + run the `normalize_region` module on `06` daily.
- A **regional mispricing radar** (weekly report Q2): 30-line diff script flagging any
  commodity > +15% vs Nasional per region, pushed to a pilot koperasi WA group.

## 6. References

`06/data/latest.json` (Region C +23–24% rice premium, stable 3 days); warung one-pager
phase-2 note; `warung-micro-fulfillment.md`.
