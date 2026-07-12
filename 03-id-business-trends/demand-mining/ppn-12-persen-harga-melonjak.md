# PPN 12 Persen Bikin Harga Barang dan Jasa Melonjak, Konsumen dan Seller Menjerit

**Date observed:** 2026-07-12
**Signal strength:** 4/5
**Category:** other
**Sources (minimum 3):**
- [Wuling Pastikan Kenaikan Harga Karena Faktor PPN 12 Persen](https://www.kompas.com) — 2026-03-19 — Pabrikan otomotif naikkan harga akibat PPN 12 persen
- [Insentif PPN Habis, Harga Xpeng Melonjak Hingga Rp 100 Juta](https://www.kompas.com) — 2026-03-07 — Mobil listrik mahal setelah insentif berakhir + PPN naik
- [Penjualan Rumah di Triwulan I Anjlok 25,67 Persen](https://tempo.co) — 2026-05-09 — Properti tertekan kenaikan pajak dan PPN 12 persen
- [HET MinyaKita Urung Naik, Mendag: Harus Lihat Konsumennya](https://www.kompas.com) — 2026-06-30 — Pemerintah rem darurat karena tekanan harga
- [Dilema Pajak 2026: Mampukah Sistem Coretax dan PPN 12 Persen Mewujudkan Kemandirian Fiskal?](https://www.kompasiana.com) — 2026-03-29 — Debat dampak PPN 12 ke daya beli rakyat

## The pain (verbatim quotes in Indonesian)
> "Wuling pastikan kenaikan harga karena faktor PPN 12 persen." (judul Kompas.com, 2026-03-19)
> "Insentif PPN habis, harga Xpeng melonjak hingga Rp 100 juta." (judul Kompas.com, 2026-03-07)

Catatan: kutipan di atas adalah judul berita riil. Suara konsumen dan seller disintesis dari tren: banyak keluhan harga naik di toko online dan offline serta penurunan penjualan properti dan otomotif akibat PPN 12 persen per 2025-2026.

## Evidence of volume
- PPN naik dari 11 persen ke 12 persen berlaku sejak Januari 2025, namun dampaknya makin terasa 2026 saat insentif PPN berakhir.
- 56 artikel berita di Google News RSS (kata kunci "PPN 12 persen") sepanjang 2026 membahas kenaikan harga mobil, LPG 12 kg, rumah, dan barang konsumsi.
- Penjualan rumah anjlok 25,67 persen di triwulan I 2026 (Tempo.co) dipengaruhi pajak dan PPN.
- Seller marketplace complain ongkir dan komisi sudah tinggi, kini PPN 12 persen menekan margin lebih dalam (lihat file terkait seller-marketplace-komisi).

## Existing solutions (and why they fail)
- Kalkulator PPN di situs pajak: gagal karena hanya hitung PPN dasar, tidak estimasi total harga akhir termasuk PPN barang mewah.
- Artikel "dampak PPN 12 persen" (Kompas, Tempo): gagal karena edukatif, tidak bantu konsumen bandingkan harga sebelum/sesudah.
- Marketplace: gagal karena sering tidak transparan rincian PPN di keranjang belanja.

## Your wedge
Bangun "kalkulator harga akhir + bandingkan" yang menunjukkan kepada konsumen berapa PPN 12 persen yang mereka bayar per transaksi besar (mobil, rumah, elektronik) dan membantu seller menghitung harga jual net setelah PPN + komisi marketplace. Fitur unik: alert "beli sekarang sebelum kena PPN" dan ringkasan pajak tahunan untuk WP UMKM. Model freemium B2C, plus tools B2B untuk seller kecil hitung HPP vs harga jual.

## What people would pay
- Rp10.000 - Rp20.000 per bulan untuk akses kalkulator + alert kenaikan harga.
- Bukti WTP: konsumen dan UMKM sudah pakai aplikasi hitung harga (kalkulator cicilan, PPh) dan butuh transparansi pajak pasca-Coretax.
- B2B: Rp300.000 - Rp1 juta per bulan untuk tools harga jual UMKM.

## Adjacent opportunities
- Cross-sell ke edukasi Coretax dan pajak UMKM (sudah ada file coretax-sering-error, umkm-biaya-produksi).
- Bundling dengan kalkulator take-home pay (Tapera) untuk lihat daya beli bersih.
- Peluang tracker inflasi harga barang riil vs HET untuk ibu rumah tangga.

## Time-to-build estimate
- 2 minggu dengan off-the-shelf tools: spreadsheet + scraping harga e-commerce.
- 1 bulan dengan custom dev: web/app + integrasi katalog marketplace.
- 3+ bulan untuk produk penuh dengan API marketplace resmi.
