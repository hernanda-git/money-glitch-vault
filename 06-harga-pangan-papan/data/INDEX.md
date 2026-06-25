# Indonesian Food Price Index

Daily snapshots from SP2KP (Sistem Pemantauan Pasar Kebutuhan Pokok), the official Kemendag (Ministry of Trade) price monitoring system.

Source: https://sp2kp.kemendag.go.id/
Update frequency: Daily (cron at 08:00 WIB)
Indicator: HNT (Harga Nasional Tertimbang) — weighted national price from 514 kab/kota using BPS SBH 2022 consumption weights.

## Files

- `sp2kp-YYYY-MM-DD.json` — daily snapshot, full record set
- `latest.json` — pointer to the most recent snapshot
- `INDEX.md` — chronological log of all captures

## Coverage

16 commodities × Nasional + Region A/B/C sub-prices = ~26 records per day.

- Beras Medium, Beras Premium, Beras SPHP Bulog
- Gula Pasir Curah
- Minyak Goreng Sawit Kemasan Premium, Curah, Minyakita
- Daging Sapi Paha Belakang, Daging Ayam Ras
- Telur Ayam Ras
- Tepung Terigu
- Kedelai Impor
- Cabai Merah Keriting, Cabai Rawit Merah, Cabai Merah Besar
- Bawang Merah, Bawang Putih Honan

## Region Codes

The site groups kab/kota into 3 buckets (A/B/C) for price stability analysis. The exact mapping is not publicly documented but is consistent day-over-day.

## INDEX

- [2026-06-19] SP2KP - 17 commodities x 4 regions (Nasional, A, B, C) = 26 records. Top movers: Cabai Rawit Merah -1.44%, Cabai Merah Besar -1.18%, Cabai Merah Keriting -0.61%
- [2026-06-16] SP2KP - 16 commodities x 10 region rows = 26 records total. Top movers: Cabai Merah Besar -2.21%, Cabai Merah Keriting -1.81%, Bawang Merah -1.71%
- [2026-06-15] SP2KP - 17 commodities x 4 regions (Nasional, A, B, C) = 26 records. Top movers: Cabai Merah Besar -2.21%, Cabai Merah Keriting -1.81%, Bawang Merah -1.71%
- [2026-06-19] SP2KP - 54 commodities x 1 region (Nasional)
- [2026-06-22] SP2KP - 54 commodities x 1 region (Nasional)
- [2026-06-23] SP2KP - 17 commodities x 26 rows
- [2026-06-23] SP2KP - 17 commodities x 26 rows. Top movers: Cabai Rawit Merah -2.21%, Cabai Merah Keriting -0.85%, Cabai Merah Besar -0.70%
- [2026-06-24] SP2KP - 54 commodities x 1 region (Nasional)
- [2026-06-25] SP2KP - 54 commodities x 1 region (Nasional)
