#!/usr/bin/env python3
"""Fetch SP2KP daily food price data and save to the vault."""

import json
import os
import sys
from datetime import datetime, timedelta, timezone
from urllib.request import Request, urlopen
from urllib.parse import urlencode
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# --- Configuration ---
API_BASE = "https://api-sp2kp.kemendag.go.id/report/api"
VAULT_BASE = "/mnt/c/Workspace/money-glitch-vault/06-harga-pangan-papan/data"

# WIB is UTC+7
WIB = timezone(timedelta(hours=7))

def fetch_json(url, data=None):
    """Fetch JSON from URL with POST form data if provided."""
    if data:
        # Encode as form data (multipart is not needed for simple form fields)
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

def get_latest_trading_day():
    """Get the latest trading day (weekdays only, exclude weekends)."""
    now_utc = datetime.now(timezone.utc)
    now_wib = now_utc.astimezone(WIB)
    
    # If today is weekend, go back to Friday
    current = now_wib
    while current.weekday() >= 5:  # Saturday=5, Sunday=6
        current -= timedelta(days=1)
    
    # SP2KP data usually lags by 1-2 days. Let's try the most recent weekday
    # that has data. We'll try yesterday first, then go back.
    for i in range(1, 5):
        candidate = current - timedelta(days=i)
        if candidate.weekday() < 5:  # Weekday
            return candidate
    
    return current - timedelta(days=1)

def get_previous_trading_day(date, days_back=3):
    """Get a trading day N weekdays before the given date."""
    result = date
    remaining = days_back
    while remaining > 0:
        result -= timedelta(days=1)
        if result.weekday() < 5:  # Weekday
            remaining -= 1
    return result

def fetch_commodity_prices(start_date, end_date, tipe_komoditas=1):
    """Fetch daily price data from the API."""
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
    # Get the latest data date
    today_date = get_latest_trading_day()
    
    # Try multiple recent dates to find the latest data
    date_str = today_date.strftime("%Y-%m-%d")
    print(f"Target date: {date_str}")
    
    # Get data for current period (last 5 trading days)
    # We want the 3 trading days before the latest
    current_date = today_date
    previous_date = get_previous_trading_day(current_date, 3)
    
    start = previous_date.strftime("%Y-%m-%d")
    end = current_date.strftime("%Y-%m-%d")
    
    print(f"Fetching data from {start} to {end}")
    
    # Fetch all commodity types (1 = Barang Kebutuhan Pokok)
    commodities = fetch_commodity_prices(start, end, tipe_komoditas=1)
    
    if not commodities:
        # Try without specifying a date range
        print("No data returned, trying broader range...")
        end = current_date.strftime("%Y-%m-%d")
        start = (current_date - timedelta(days=10)).strftime("%Y-%m-%d")
        commodities = fetch_commodity_prices(start, end, tipe_komoditas=1)
    
    if not commodities:
        print("ERROR: Could not fetch any price data from SP2KP API", file=sys.stderr)
        sys.exit(1)
    
    print(f"Fetched {len(commodities)} commodities")
    
    # Build the dataset
    rows = []
    for item in commodities:
        variant = item.get("variant", "")
        satuan = item.get("satuan", "")
        daftar_harga = item.get("daftarHarga", [])
        
        # Find current (latest) price and previous price
        # Sort by date
        daftar_harga.sort(key=lambda x: x.get("date", ""))
        
        current_price = None
        previous_price = None
        
        for entry in daftar_harga:
            price = entry.get("harga", 0)
            if price and price > 0:
                if previous_price is None:
                    previous_price = price
                else:
                    previous_price = current_price or previous_price
                    current_price = price
        
        # If we only got one price, use it as current
        if current_price is None and previous_price is not None:
            current_price = previous_price
        
        # Calculate change
        change_percent = None
        if current_price and previous_price and previous_price > 0:
            change_percent = round(((current_price - previous_price) / previous_price) * 100, 2)
        
        row = {
            "date": end,
            "commodity_name": variant,
            "unit": satuan,
            "region": "Nasional",
            "previous_price": previous_price,
            "current_price": current_price,
            "change_percent": change_percent
        }
        rows.append(row)
    
    # Sort by order number from the API
    # Re-fetch with order info
    ordered_commodities = fetch_commodity_prices(end, end, tipe_komoditas=1)
    
    if ordered_commodities:
        ordered_names = [c.get("variant", "") for c in ordered_commodities]
        row_map = {r["commodity_name"]: r for r in rows}
        rows = []
        for name in ordered_names:
            if name in row_map:
                rows.append(row_map[name])
            # Skip if not found (shouldn't happen)
    
    # Build output
    output = {
        "date": end,
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "source": "SP2KP Kemendag - API",
        "commodity_type": "Barang Kebutuhan Pokok",
        "total_commodities": len(rows),
        "data": rows
    }
    
    # Ensure directory exists
    os.makedirs(f"{VAULT_BASE}", exist_ok=True)
    
    # Save daily file
    daily_path = f"{VAULT_BASE}/sp2kp-{end}.json"
    with open(daily_path, 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)
    print(f"Saved: {daily_path}")
    
    # Save latest.json
    latest_path = f"{VAULT_BASE}/latest.json"
    with open(latest_path, 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)
    print(f"Saved: {latest_path}")
    
    # Update INDEX.md
    index_path = f"{VAULT_BASE}/INDEX.md"
    index_line = f"- [{end}] SP2KP - {len(rows)} commodities x 1 region (Nasional)"
    
    # Check if line already exists
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
    
    # Print summary for report
    print(f"\n=== SUMMARY ===")
    print(f"Date: {end}")
    print(f"Commodities: {len(rows)}")
    
    # Top movers
    with_price = [r for r in rows if r["change_percent"] is not None]
    with_price.sort(key=lambda x: abs(x["change_percent"]), reverse=True)
    
    print(f"\nTop movers (biggest change):")
    for r in with_price[:5]:
        direction = "UP" if r["change_percent"] > 0 else "DOWN"
        print(f"  {r['commodity_name']}: {r['previous_price']} -> {r['current_price']} ({r['change_percent']:+.2f}%) {direction}")
    
    high_movers = [r for r in with_price if abs(r["change_percent"]) > 5]
    if high_movers:
        print(f"\nCommodities with >5% change (potential business opportunity):")
        for r in high_movers:
            print(f"  ** {r['commodity_name']}: {r['change_percent']:+.2f}%")
    
    # Output JSON for the report
    report = {
        "date": end,
        "commodity_count": len(rows),
        "file_path": daily_path,
        "top_movers": [
            {
                "commodity_name": r["commodity_name"],
                "previous_price": r["previous_price"],
                "current_price": r["current_price"],
                "change_percent": r["change_percent"]
            }
            for r in with_price[:5]
        ],
        "high_change_commodities": [
            {
                "commodity_name": r["commodity_name"],
                "change_percent": r["change_percent"]
            }
            for r in high_movers
        ]
    }
    
    print(f"\n=== REPORT JSON ===")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    
    return report

if __name__ == "__main__":
    report = main()
