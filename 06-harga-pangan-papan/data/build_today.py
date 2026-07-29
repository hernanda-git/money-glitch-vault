#!/usr/bin/env python3
import json
import time
from datetime import datetime, timezone

# Data extracted from SP2KP page on 2026-07-28
# Columns: Komoditas, Unit, 27 Jul, 28 Jul, Perubahan
# The page date picker shows 2026-07-28

DATA_DATE = "2026-07-28"
PREVIOUS_DATE = "2026-07-27"
FETCHED_AT = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

# Raw rows from the page
raw_rows = [
    ("Beras Medium", "kg", "Rp 13.862", "Rp 13.856", "-0.04 %", True),
    ("Region A", "kg", "Rp 13.946", "Rp 13.946", "0.00 %", False),
    ("Region B", "kg", "Rp 14.728", "Rp 14.727", "-0.01 %", False),
    ("Region C", "kg", "Rp 17.031", "Rp 17.031", "0.00 %", False),
    ("Beras Premium", "kg", "Rp 15.536", "Rp 15.543", "0.05 %", True),
    ("Region A", "kg", "Rp 15.311", "Rp 15.321", "0.06 %", False),
    ("Region B", "kg", "Rp 16.668", "Rp 16.673", "0.03 %", False),
    ("Region C", "kg", "Rp 19.237", "Rp 19.237", "0.00 %", False),
    ("Beras SPHP Bulog", "kg", "", "", "", True),
    ("Region A", "kg", "Rp 12.165", "Rp 12.165", "-0.00 %", False),
    ("Region B", "kg", "Rp 12.671", "Rp 12.669", "-0.01 %", False),
    ("Region C", "kg", "Rp 13.321", "Rp 13.321", "0.00 %", False),
    ("Gula Pasir Curah", "kg", "Rp 18.249", "Rp 18.246", "-0.02 %", True),
    ("Minyak Goreng Sawit Kemasan Premium", "lt", "Rp 22.435", "Rp 22.435", "0.00 %", True),
    ("Minyak Goreng Sawit Curah", "lt", "Rp 19.482", "Rp 19.473", "-0.05 %", True),
    ("Minyakita", "lt", "Rp 15.866", "Rp 15.864", "-0.01 %", True),
    ("Daging Sapi Paha Belakang", "kg", "Rp 141.940", "Rp 141.953", "0.01 %", True),
    ("Daging Ayam Ras", "kg", "Rp 37.448", "Rp 37.548", "0.27 %", True),
    ("Telur Ayam Ras", "kg", "Rp 27.284", "Rp 27.227", "-0.21 %", True),
    ("Tepung Terigu", "kg", "Rp 12.542", "Rp 12.523", "-0.15 %", True),
    ("Kedelai Impor", "kg", "Rp 13.706", "Rp 13.733", "0.20 %", True),
    ("Cabai Merah Keriting", "kg", "Rp 40.790", "Rp 41.049", "0.63 %", True),
    ("Cabai Rawit Merah", "kg", "Rp 46.961", "Rp 47.322", "0.77 %", True),
    ("Cabai Merah Besar", "kg", "Rp 43.561", "Rp 43.468", "-0.21 %", True),
    ("Bawang Merah", "kg", "Rp 36.569", "Rp 36.109", "-1.26 %", True),
    ("Bawang Putih Honan", "kg", "Rp 37.350", "Rp 37.104", "-0.66 %", True),
]

def parse_price(s):
    """Parse Indonesian price string like 'Rp 13.862' to int 13862"""
    s = s.strip()
    if not s:
        return None
    # Remove "Rp " prefix
    if s.startswith("Rp "):
        s = s[3:]
    # Remove thousands separator (period in Indonesian format)
    s = s.replace(".", "")
    try:
        return int(s)
    except ValueError:
        return None

def parse_change(s):
    """Parse change string like '-0.04 %' to float -0.04"""
    s = s.strip()
    if not s:
        return None
    # Remove "%" and spaces
    s = s.replace("%", "").strip()
    try:
        return float(s)
    except ValueError:
        return None

commodity_names_set = set()
rows_out = []
current_commodity = None
current_unit = None

for name, unit, prev_str, curr_str, change_str, is_header in raw_rows:
    if is_header:
        current_commodity = name
        current_unit = unit
        region = "Nasional"
        commodity_names_set.add(name)
    else:
        # Region sub-row — use the parent commodity name
        region = name  # name is like "Region A"
    
    prev_price = parse_price(prev_str)
    curr_price = parse_price(curr_str)
    change_pct = parse_change(change_str)
    
    row = {
        "date": DATA_DATE,
        "commodity_name": current_commodity,
        "unit": current_unit,
        "region": region,
        "previous_price": prev_price,
        "current_price": curr_price,
        "change_percent": change_pct
    }
    rows_out.append(row)

commodity_names = sorted(commodity_names_set)

output = {
    "source": "https://sp2kp.kemendag.go.id (browser scrape via DOM table)",
    "fetched_at_utc": FETCHED_AT,
    "data_date": DATA_DATE,
    "previous_date": PREVIOUS_DATE,
    "commodity_count": len(commodity_names),
    "row_count": len(rows_out),
    "commodity_names": commodity_names,
    "rows": rows_out
}

print(json.dumps(output, indent=2, ensure_ascii=False))
