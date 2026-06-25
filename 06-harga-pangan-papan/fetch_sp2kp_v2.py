#!/usr/bin/env python3
"""Fetch SP2KP daily food price data - uses API with proper date handling."""

import json
import os
import sys
from datetime import datetime, timedelta, timezone
from urllib.request import Request, urlopen
from urllib.parse import urlencode

API_BASE = "https://api-sp2kp.kemendag.go.id/report/api"
VAULT_BASE = "/mnt/c/Workspace/money-glitch-vault/06-harga-pangan-papan/data"
WIB = timezone(timedelta(hours=7))

def fetch_json(url, data=None):
    if data:
        encoded = urlencode(data).encode('utf-8')
        req = Request(url, data=encoded, method='POST')
        req.add_header('Content-Type', 'application/x-www-form-urlencoded')
    else:
        req = Request(url)
    try:
        with urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode('utf-8'))
    except Exception as e:
        print(f"Error fetching {url}: {e}", file=sys.stderr)
        return None

def find_latest_data_date():
    """Fetch data for recent dates and find the latest one with data."""
    today_wib = datetime.now(WIB)
    # Try last 7 days to find the latest date with data
    for days_back in range(1, 8):
        candidate = today_wib - timedelta(days=days_back)
        if candidate.weekday() >= 5:
            continue
        end = candidate.strftime("%Y-%m-%d")
        start = (candidate - timedelta(days=3)).strftime("%Y-%m-%d")
        data = fetch_json(
            f"{API_BASE}/average-price/export-area-daily-json",
            {"start_date": start, "end_date": end, "level": "nasional",
             "tipe_komoditas": "1", "skip_sat_sun": "true"}
        )
        if data and data.get("status") == "success":
            records = data.get("data", [])
            if records:
                # Check that candidate date has actual price data
                has_prices = 0
                for item in records:
                    for p in item.get("daftarHarga", []):
                        if p.get("date") == end and p.get("harga", 0) > 0:
                            has_prices += 1
                            break
                if has_prices >= 50:  # Most commodities have data
                    print(f"Found data for {end} ({has_prices}/{len(records)} commodities)")
                    return candidate, end
    return None, None

def get_previous_trading_day(date, days_back=3):
    result = date
    remaining = days_back
    while remaining > 0:
        result -= timedelta(days=1)
        if result.weekday() < 5:
            remaining -= 1
    return result

def fetch_commodity_prices(start_date, end_date, tipe_komoditas=1):
    url = f"{API_BASE}/average-price/export-area-daily-json"
    data = {
        "start_date": start_date,
        "end_date": end_date,
        "level": "nasional",
        "tipe_komoditas": str(tipe_komoditas),
        "skip_sat_sun": "true"
    }
    result = fetch_json(url, data)
    if result and result.get("status") == "success":
        return result.get("data", [])
    return None

def main():
    # Step 1: Find the latest data date
    latest_date_obj, latest_date_str = find_latest_data_date()
    if not latest_date_obj or not latest_date_str:
        print("ERROR: Could not find any data in the last 7 days", file=sys.stderr)
        # Log failure
        os.makedirs(VAULT_BASE, exist_ok=True)
        with open(f"{VAULT_BASE}/last-failure.log", "a") as f:
            f.write(f"{datetime.now(WIB).isoformat()} | No data found in last 7 days\n")
        sys.exit(1)
    
    # Step 2: Find the comparison date (3 trading days before)
    prev_date_obj = get_previous_trading_day(latest_date_obj, 3)
    prev_date_str = prev_date_obj.strftime("%Y-%m-%d")
    
    print(f"Data date: {latest_date_str}, Comparison date: {prev_date_str}")
    
    # Step 3: Fetch full dataset including comparison date
    commodities = fetch_commodity_prices(prev_date_str, latest_date_str, tipe_komoditas=1)
    if not commodities:
        print("ERROR: Could not fetch price data", file=sys.stderr)
        sys.exit(1)
    
    print(f"Fetched {len(commodities)} commodities")
    
    # Step 4: Build rows
    rows = []
    for item in commodities:
        variant = item.get("variant", "")
        satuan = item.get("satuan", "")
        order = item.get("order", 999)
        daftar_harga = item.get("daftarHarga", [])
        
        # Find price for latest date and comparison date
        current_price = None
        previous_price = None
        for entry in daftar_harga:
            if entry.get("date") == latest_date_str:
                current_price = entry.get("harga", 0) or None
            if entry.get("date") == prev_date_str:
                previous_price = entry.get("harga", 0) or None
        
        # Calculate change
        change_percent = None
        if current_price and previous_price and previous_price > 0:
            change_percent = round(((current_price - previous_price) / previous_price) * 100, 2)
        
        # Determine status
        status = None
        if change_percent is not None:
            if change_percent > 0:
                status = "Naik"
            elif change_percent < 0:
                status = "Turun"
            else:
                status = "Tidak Berubah"
        
        row = {
            "date": latest_date_str,
            "commodity_name": variant,
            "unit": satuan,
            "region": "Nasional",
            "previous_price": previous_price,
            "current_price": current_price,
            "change_percent": change_percent,
            "status": status
        }
        rows.append(row)
    
    # Sort by order number from API
    rows.sort(key=lambda r: [item.get("order", 999) for item in commodities if item.get("variant") == r["commodity_name"]][0] if any(item.get("variant") == r["commodity_name"] for item in commodities) else 999)
    
    # Actually, let's just use the original API order
    ordered_commodities = fetch_commodity_prices(latest_date_str, latest_date_str, tipe_komoditas=1)
    if ordered_commodities:
        ordered_names = [c.get("variant", "") for c in ordered_commodities]
        row_map = {r["commodity_name"]: r for r in rows}
        sorted_rows = []
        for name in ordered_names:
            if name in row_map:
                sorted_rows.append(row_map[name])
        if sorted_rows:
            rows = sorted_rows
    
    # Build output
    output = {
        "date": latest_date_str,
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "source": "SP2KP Kemendag - API",
        "commodity_type": "Barang Kebutuhan Pokok",
        "total_commodities": len(rows),
        "data": rows
    }
    
    # Save files
    os.makedirs(VAULT_BASE, exist_ok=True)
    
    daily_path = f"{VAULT_BASE}/sp2kp-{latest_date_str}.json"
    with open(daily_path, 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)
    print(f"Saved: {daily_path}")
    
    latest_path = f"{VAULT_BASE}/latest.json"
    with open(latest_path, 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)
    print(f"Saved: {latest_path}")
    
    # Update INDEX.md
    index_path = f"{VAULT_BASE}/INDEX.md"
    index_line = f"- [{latest_date_str}] SP2KP - {len(rows)} commodities x 1 region (Nasional)"
    
    already_exists = False
    try:
        with open(index_path, 'r', encoding='utf-8') as f:
            content = f.read()
            if index_line in content:
                already_exists = True
    except FileNotFoundError:
        pass
    
    if not already_exists:
        with open(index_path, 'a', encoding='utf-8') as f:
            f.write(index_line + "\n")
        print(f"Updated: {index_path}")
    
    # Compute top movers
    with_price = [r for r in rows if r["change_percent"] is not None]
    with_price.sort(key=lambda x: abs(x["change_percent"]), reverse=True)
    
    top3 = with_price[:3]
    
    high_movers = [r for r in with_price if abs(r["change_percent"]) > 5]
    
    # Prepare report data
    report_data = {
        "date": latest_date_str,
        "commodity_count": len(rows),
        "file_path": daily_path,
        "top_movers": [
            {"commodity_name": r["commodity_name"], "previous_price": r["previous_price"],
             "current_price": r["current_price"], "change_percent": r["change_percent"]}
            for r in top3
        ],
        "high_change_commodities": [
            {"commodity_name": r["commodity_name"], "change_percent": r["change_percent"]}
            for r in high_movers
        ],
        "all_above_1pct": [r for r in with_price if abs(r["change_percent"]) >= 1.0]
    }
    
    # Print report
    print(f"\n=== REPORT ===")
    print(f"Date: {latest_date_str}")
    print(f"Commodities: {len(rows)}")
    print(f"Top movers:")
    for r in top3:
        d = "UP" if r["change_percent"] > 0 else "DOWN"
        print(f"  {r['commodity_name']}: {r['previous_price']} -> {r['current_price']} ({r['change_percent']:+.2f}%) {d}")
    if high_movers:
        print(f"Commodities with >5% change:")
        for r in high_movers:
            print(f"  ** {r['commodity_name']}: {r['change_percent']:+.2f}%")
    
    return report_data

if __name__ == "__main__":
    report = main()
    # Output JSON for pipeline
    print(f"\n===REPORT_JSON===")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    print(f"===END_REPORT_JSON===")
