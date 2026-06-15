# 🛒 06 — Harga Pangan & Papan

Daily/weekly prices for food staples and housing across Indonesian regions. Inflation edge lives in **regional deltas** — Jakarta trend ≠ Makassar trend.

## Coverage

### Pangan (food staples)
- Beras (premium, medium, SPHP)
- Minyak goreng (curah, kemasan)
- Gula pasir
- Telur ayam
- Daging ayam, daging sapi
- Bawang merah, bawang putih
- Cabai (rawit, merah)
- Gas elpiji 3kg
- Minyakita

### Papan (housing)
- Sewa kos (per kota, per tier)
- Harga rumah subsidi
- Cicilan KPR simulasi
- Harga tanah (per kabupaten, per kecamatan)
- Harga bahan bangunan (semen, besi, kayu)

## Sub-folders

- `data/` — daily CSV/JSON dumps
- `regional/` — per-province / per-kabupaten breakdowns
- `sources/` — scrapers + manual entry sources
- `analysis/` — weekly delta reports, anomaly detection
- `alerts/` — spikes >X% auto-flagged

## Sources to mine

- Bapanas / Panel Harga Bapanas
- PiJPS (hargapangan.id)
- BPS (Statistics Indonesia)
- Bank Indonesia (IHK / inflation)
- Tokopedia/Shopee price scrapes (regional sellers)
- Properti: Rumah123, OLX, Pinhome, Lamudi

## Cadence

- Daily snapshot at 08:00 WIB (Bapanas publish time)
- Weekly regional delta digest on Sunday
- Monthly trend writeup with macro overlay (BI rate, harvest season, Lebaran, etc.)
