#!/usr/bin/env python3
"""Build today's SP2KP data from raw browser-extracted rows."""
import json, re
from datetime import datetime, timezone

# Raw data from browser_console extraction
# Each row: [name_or_region, unit, prev_price_str, curr_price_str, change_str]
# date columns: 29 Jul (previous), 30 Jul (current)

rows = [
    ["Beras Medium", "kg", "Rp 13.860", "Rp 13.862", "0.01 %"],
    ["Region A", "kg", "Rp 13.942", "Rp 13.943", "0.00 %"],
    ["Region B", "kg", "Rp 14.727", "Rp 14.727", "0.00 %"],
    ["Region C", "kg", "Rp 17.031", "Rp 17.031", "0.00 %"],
    ["Beras Premium", "kg", "Rp 15.547", "Rp 15.544", "-0.02 %"],
    ["Region A", "kg", "Rp 15.317", "Rp 15.318", "0.01 %"],
    ["Region B", "kg", "Rp 16.670", "Rp 16.673", "0.02 %"],
    ["Region C", "kg", "Rp 19.237", "Rp 19.254", "0.09 %"],
    ["Beras SPHP Bulog", "kg", "", "", ""],
    ["Region A", "kg", "Rp 12.165", "Rp 12.165", "0.00 %"],
    ["Region B", "kg", "Rp 12.666", "Rp 12.666", "0.00 %"],
    ["Region C", "kg", "Rp 13.321", "Rp 13.321", "0.00 %"],
    ["Gula Pasir Curah", "kg", "Rp 18.248", "Rp 18.254", "0.03 %"],
    ["Minyak Goreng Sawit Kemasan Premium", "lt", "Rp 22.435", "Rp 22.438", "0.01 %"],
    ["Minyak Goreng Sawit Curah", "lt", "Rp 19.470", "Rp 19.481", "0.06 %"],
    ["Minyakita", "lt", "Rp 15.863", "Rp 15.864", "0.01 %"],
    ["Daging Sapi Paha Belakang", "kg", "Rp 141.956", "Rp 142.123", "0.12 %"],
    ["Daging Ayam Ras", "kg", "Rp 37.719", "Rp 37.933", "0.57 %"],
    ["Telur Ayam Ras", "kg", "Rp 27.145", "Rp 27.093", "-0.19 %"],
    ["Tepung Terigu", "kg", "Rp 12.524", "Rp 12.526", "0.02 %"],
    ["Kedelai Impor", "kg", "Rp 13.735", "Rp 13.735", "0.00 %"],
    ["Cabai Merah Keriting", "kg", "Rp 41.644", "Rp 42.003", "0.86 %"],
    ["Cabai Rawit Merah", "kg", "Rp 48.015", "Rp 48.751", "1.53 %"],
    ["Cabai Merah Besar", "kg", "Rp 43.555", "Rp 43.736", "0.42 %"],
    ["Bawang Merah", "kg", "Rp 36.007", "Rp 35.884", "-0.34 %"],
    ["Bawang Putih Honan", "kg", "Rp 36.995", "Rp 36.814", "-0.49 %"],
]

def parse_price(s):
    """Parse 'Rp 13.860' -> 13860, '' -> None"""
    s = s.strip()
    if not s:
        return None
    s = s.replace("Rp ", "").replace(".", "").strip()
    return int(s)

def parse_change(s):
    """Parse '0.01 %' -> 0.01, '' -> None"""
    s = s.strip()
    if not s:
        return None
    s = s.replace("%", "").strip()
    return float(s)

data_date = "2026-07-30"
previous_date = "2026-07-29"
fetched_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

output_rows = []
current_commodity = None
current_unit = None

for row in rows:
    name = row[0].strip()
    unit = row[1].strip()
    prev_raw = row[2]
    curr_raw = row[3]
    change_raw = row[4]
    
    # Determine if this is a commodity header or a region sub-row
    if name in ["Region A", "Region B", "Region C"]:
        region = name
        commodity_name = current_commodity
        commodity_unit = current_unit
    else:
        current_commodity = name
        current_unit = unit
        region = "Nasional"
        commodity_name = name
        commodity_unit = unit
    
    prev_price = parse_price(prev_raw)
    curr_price = parse_price(curr_raw)
    change_percent = parse_change(change_raw)
    
    output_rows.append({
        "date": data_date,
        "commodity_name": commodity_name,
        "unit": commodity_unit,
        "region": region,
        "previous_price": prev_price,
        "current_price": curr_price,
        "change_percent": change_percent
    })

# Build the full JSON
commodity_names = []
seen = set()
for r in output_rows:
    if r["commodity_name"] not in seen:
        seen.add(r["commodity_name"])
        commodity_names.append(r["commodity_name"])

full = {
    "source": "https://sp2kp.kemendag.go.id (browser scrape via DOM table)",
    "fetched_at_utc": fetched_at,
    "data_date": data_date,
    "previous_date": previous_date,
    "commodity_count": len(commodity_names),
    "row_count": len(output_rows),
    "commodity_names": commodity_names,
    "rows": output_rows
}

print(json.dumps(full, indent=2, ensure_ascii=False))
