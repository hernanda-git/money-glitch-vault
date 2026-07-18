#!/usr/bin/env python3
"""Build sp2kp-2026-07-17.json from browser-extracted DOM rows.

Matches the established schema in sp2kp-2026-07-16.json:
  - header rows => region "Nasional"
  - 3 rice items (Beras Medium/Premium/SPHP Bulog) also have Region A/B/C sub-rows
  - empty national cells (Beras SPHP Bulog) => null
Prices parsed from "Rp 13.837" -> 13837 (integer rupiah).
"""
import json, os
from datetime import datetime, timezone

DATA_DIR = os.path.dirname(os.path.abspath(__file__))

# Raw DOM extraction (headers: Komoditas, Unit, 16 Jul, 17 Jul, Perubahan)
RAW_ROWS = [
    ["Beras Medium", "kg", "Rp 13.837", "Rp 13.839", "0.01 %"],
    ["Region A", "kg", "Rp 13.938", "Rp 13.942", "0.03 %"],
    ["Region B", "kg", "Rp 14.675", "Rp 14.675", "0.00 %"],
    ["Region C", "kg", "Rp 17.031", "Rp 17.031", "0.00 %"],
    ["Beras Premium", "kg", "Rp 15.527", "Rp 15.529", "0.01 %"],
    ["Region A", "kg", "Rp 15.326", "Rp 15.333", "0.04 %"],
    ["Region B", "kg", "Rp 16.635", "Rp 16.635", "0.00 %"],
    ["Region C", "kg", "Rp 19.254", "Rp 19.254", "0.00 %"],
    ["Beras SPHP Bulog", "kg", "", "", ""],
    ["Region A", "kg", "Rp 12.158", "Rp 12.158", "0.00 %"],
    ["Region B", "kg", "Rp 12.671", "Rp 12.671", "0.00 %"],
    ["Region C", "kg", "Rp 13.321", "Rp 13.321", "0.00 %"],
    ["Gula Pasir Curah", "kg", "Rp 18.270", "Rp 18.270", "0.00 %"],
    ["Minyak Goreng Sawit Kemasan Premium", "lt", "Rp 22.453", "Rp 22.464", "0.05 %"],
    ["Minyak Goreng Sawit Curah", "lt", "Rp 19.483", "Rp 19.492", "0.05 %"],
    ["Minyakita", "lt", "Rp 15.870", "Rp 15.862", "-0.05 %"],
    ["Daging Sapi Paha Belakang", "kg", "Rp 141.672", "Rp 141.625", "-0.03 %"],
    ["Daging Ayam Ras", "kg", "Rp 36.625", "Rp 36.787", "0.44 %"],
    ["Telur Ayam Ras", "kg", "Rp 26.345", "Rp 26.445", "0.38 %"],
    ["Tepung Terigu", "kg", "Rp 12.569", "Rp 12.568", "-0.01 %"],
    ["Kedelai Impor", "kg", "Rp 13.740", "Rp 13.725", "-0.11 %"],
    ["Cabai Merah Keriting", "kg", "Rp 39.880", "Rp 39.524", "-0.89 %"],
    ["Cabai Rawit Merah", "kg", "Rp 50.783", "Rp 50.078", "-1.39 %"],
    ["Cabai Merah Besar", "kg", "Rp 41.582", "Rp 41.295", "-0.69 %"],
    ["Bawang Merah", "kg", "Rp 39.580", "Rp 39.274", "-0.77 %"],
    ["Bawang Putih Honan", "kg", "Rp 38.964", "Rp 38.858", "-0.27 %"],
]

DATA_DATE = "2026-07-17"
PREV_DATE = "2026-07-16"
RICE = {"Beras Medium", "Beras Premium", "Beras SPHP Bulog"}

def to_int(s):
    s = (s or "").strip()
    if not s:
        return None
    # "Rp 13.837" -> 13837
    digits = s.replace("Rp", "").replace(".", "").replace(",", ".").strip()
    try:
        return int(float(digits))
    except ValueError:
        return None

def to_pct(s):
    s = (s or "").strip()
    if not s:
        return None
    try:
        # "0.01 %" or "-0.05 %"
        return round(float(s.replace("%", "").strip()), 2)
    except ValueError:
        return None

rows = []
commodity_names = []
for r in RAW_ROWS:
    name, unit, prev, cur, chg = r
    region = "Nasional" if name not in ("Region A", "Region B", "Region C") else name
    commodity = name if region == "Nasional" else None
    # For sub-rows, attach to the most recent rice commodity header
    if region != "Nasional":
        commodity = commodity_names[-1]
    entry = {
        "date": DATA_DATE,
        "commodity_name": commodity,
        "unit": unit,
        "region": region,
        "previous_price": to_int(prev),
        "current_price": to_int(cur),
        "change_percent": to_pct(chg),
    }
    rows.append(entry)
    if region == "Nasional" and commodity not in commodity_names:
        commodity_names.append(commodity)

payload = {
    "source": "sp2kp.kemendag.go.id homepage table (browser-rendered, region sub-rows for 3 rice items)",
    "fetched_at_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    "data_date": DATA_DATE,
    "previous_date": PREV_DATE,
    "commodity_count": len(commodity_names),
    "row_count": len(rows),
    "commodity_names": commodity_names,
    "rows": rows,
}

path = os.path.join(DATA_DIR, f"sp2kp-{DATA_DATE}.json")
with open(path, "w", encoding="utf-8") as f:
    json.dump(payload, f, ensure_ascii=False, indent=2)
    f.write("\n")
with open(os.path.join(DATA_DIR, "latest.json"), "w", encoding="utf-8") as f:
    json.dump(payload, f, ensure_ascii=False, indent=2)
    f.write("\n")

# INDEX.md
idx_line = f"- [{DATA_DATE}] SP2KP - {len(commodity_names)} commodities x {len(set(r['region'] for r in rows))} regions"
idx_path = os.path.join(DATA_DIR, "INDEX.md")
have = ""
if os.path.exists(idx_path):
    with open(idx_path, encoding="utf-8") as f:
        have = f.read()
if idx_line.split("]")[0] + "]" not in have:
    with open(idx_path, "a", encoding="utf-8") as f:
        f.write(idx_line + "\n")

print("WROTE", path)
print("commodities:", len(commodity_names), "rows:", len(rows))
print("Beras SPHP Bulog Nasional current_price:",
      [r for r in rows if r["commodity_name"] == "Beras SPHP Bulog" and r["region"] == "Nasional"][0]["current_price"])
