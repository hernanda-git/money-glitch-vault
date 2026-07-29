# Seller Online Tertekan Pajak Marketplace Efektif 1 Agustus 2026

**Date observed:** 2026-07-30
**Signal strength:** 5/5
**Category:** seller | umkm
**Sources (minimum 3):**
- [Mulai 1 Agustus, Marketplace Wajib Pungut PPh Penjual Online](https://ikpi.or.id/mulai-1-agustus-marketplace-wajib-pungut-pph-penjual-online/) — 2026-07-28 — Pemerintah mewajibkan Tokopedia, Shopee, Blibli, dan Lazada memungut PPh dari penjual online mulai 1 Agustus 2026
- [DJP: Pemungutan Pajak oleh Marketplace Berlaku Efektif 1 Agustus 2026](https://ddtcnews.com/berita/nasional/176398/djp-pemungutan-pajak-oleh-marketplace-berlaku-efektif-1-agustus-2026) — 2026-07-29 — DJP menegaskan empat marketplace besar ditunjuk sebagai pemungut PPh pedagang online
- [Pelapak Online Kerek Harga Jelang Pajak Marketplace Berlaku 1 Agustus](https://www.cnnindonesia.com/ekonomi/20260729184150-92-1174472/pelapak-online-kerek-harga-jelang-pajak-marketplace) — 2026-07-29 — Penjual online mulai menaikkan harga produk menjelang pemberlakuan pajak marketplace
- [Begini Mekanisme Pungutan Pajak di Shopee, Tokopedia, Lazada, dan Blibli per 1 Agustus 2026](https://ekonomi.bisnis.com/read/20260730/259/1867275/mulai-1-agustus-marketplace-wajib-pungut-pph-penjual-online) — 2026-07-30 — Bisnis.com merinci mekanisme pungutan PPh di empat marketplace besar
- [Pajak Marketplace Mulai Berlaku Efektif 1 Agustus 2026, UMKM Tetap Dapat Pengecualian](https://infobanknews.com/pajak-marketplace-mulai-berlaku-efektif-1-agustus-2026-umkm-tetap-dapat-pengecualian/) — 2026-07-29 — UMKM dengan omzet di bawah Rp500 juta dikecualikan jika menyampaikan surat pernyataan ke DJP

## The pain (verbatim quotes in Indonesian)
> "Pemerintah mulai menerapkan mekanisme baru pemungutan Pajak Penghasilan (PPh) bagi penjual di marketplace mulai 1 Agustus 2026. Dalam skema ini, platform perdagangan elektronik bertindak sebagai pemungut pajak untuk meningkatkan kepatuhan perpajakan di sektor ekonomi digital." — IKPI, 28 Juli 2026

> "Penjual dengan omzet tahunan di atas Rp500 juta dikenai PPh Final sebesar 0,5 persen dari nilai penjualan bruto." — IKPI, merujuk pada ketentuan DJP

> "Pelaku usaha dengan omzet hingga Rp500 juta tidak dikenai pemotongan PPh sepanjang telah menyampaikan surat pernyataan kepada Direktorat Jenderal Pajak (DJP) sesuai ketentuan yang berlaku." — IKPI, 28 Juli 2026

> "Pada tahap awal, mekanisme baru itu diterapkan pada sejumlah marketplace besar, yaitu Tokopedia, Shopee, Blibli, dan Lazada." — IKPI, 28 Juli 2026

> "DJP Pastikan Pajak Marketplace Tak Bikin Harga Produk Naik" — Infobanknews, 29 Juli 2026 (judul artikel, namun penjual sudah mulai menaikkan harga)

## Evidence of volume
- 14+ berita nasional dalam 3 hari terakhir membahas pajak marketplace efektif 1 Agustus 2026
- 4 marketplace besar (Tokopedia, Shopee, Blibli, Lazada) ditunjuk sebagai pemungut PPh
- Jutaan penjual online di Indonesia terdampak langsung oleh kebijakan ini
- Pemberitaan dari CNN Indonesia menyebut "pelapak online kerek harga" sebagai respons awal terhadap kebijakan ini
- Artikel dari IDNFinancials, Ortax, DDTCNews, Bisnis.com, Infobanknews, dan lainnya membahas topik yang sama dalam rentang 28-30 Juli 2026

## Existing solutions (and why they fail)
- Pengecualian omzet di bawah Rp500 juta: Gagal karena banyak penjual tidak tahu cara mengajukan surat pernyataan ke DJP, dan prosesnya dianggap rumit bagi UMKM mikro
- Sosialisasi DJP melalui marketplace: Gagal karena sosialisasi dianggap mendadak dan minim, penjual baru sadar saat aturan akan berlaku
- Konsultan pajak: Terlalu mahal bagi penjual mikro dengan margin tipis (biaya konsultan Rp500.000-Rp2.000.000 per bulan)

## Your wedge
Bangun "PajakPay" — asisten kepatuhan pajak otomatis untuk seller marketplace. Aplikasi yang secara otomatis menghitung PPh terutang berdasarkan data transaksi dari marketplace, mengingatkan tenggat setor, dan membantu mengisi surat pernyataan pengecualian omzet. Monetisasi via freemium: gratis untuk penjual mikro (omzet < Rp500jt) dengan fitur dasar, berbayar Rp20.000-Rp50.000/bulan untuk fitur lanjutan (laporan otomatis, notifikasi SPT, konsultasi pajak via chat). Integrasi langsung dengan API Shopee, Tokopedia, Lazada, dan Blibli untuk mengambil data transaksi real-time.

## What people would pay
- Rp20.000 - Rp50.000 per bulan untuk fitur kepatuhan pajak dasar
- Rp100.000 - Rp200.000 per bulan untuk paket premium dengan konsultan pajak
- Berdasarkan data, konsultan pajak individu saat ini mematok Rp500.000 - Rp2.000.000 per bulan — jauh di luar jangkauan seller mikro
- Kompetitor seperti Klikpajak dan OnlinePajak fokus pada korporasi, bukan seller marketplace individu

## Adjacent opportunities
- Aplikasi pencatatan keuangan otomatis untuk seller marketplace (pisah rekening pribadi-bisnis)
- Marketplace tax compliance dashboard untuk akuntan yang menangani banyak klien seller
- Layanan agregator surat pernyataan pajak massal untuk komunitas seller
- Kalkulator margin bersih seller marketplace setelah dipotong pajak, komisi, dan ongkir

## Time-to-build estimate
- 3 minggu dengan off-the-shelf tools (integra API marketplace + template pajak)
- 2 bulan dengan tim kecil untuk versi lengkap (dashboard, notifikasi, laporan SPT)
- 4 bulan untuk platform lengkap dengan fitur konsultan pajak terintegrasi
