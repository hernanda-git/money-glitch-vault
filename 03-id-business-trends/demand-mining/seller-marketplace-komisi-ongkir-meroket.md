# Seller Marketplace Menjerit: Komisi TikTok Shop dan Ongkir Ditanggung Penjual Meroket

**Date observed:** 2026-07-11
**Signal strength:** 5/5
**Category:** seller
**Sources (minimum 3):**
- [TikTok Shop Naikkan Biaya Komisi Dinamis per 18 Mei, Seller Menjerit](https://teknologi.bisnis.com/read/20260515/84/1974040/tiktok-shop-naikkan-biaya-komisi-dinamis-per-18-mei-seller-menjerit) — 2026-05-15 — Komisi dinamis naik hingga 15 kali lipat, Menteri UMKM melarang
- [Komisi TikTok Shop Naik, Potongan ke Penjual Bisa Naik 16 Kali Lipat](https://www.cnbcindonesia.com/tech/20260518132932-37-735586/komisi-tiktok-shop-naik-potongan-ke-penjual-bisa-naik-16-kali-lipat) — 2026-05-18 — Hitungan potongan 16 kali lipat per kategori
- [Ditanggung Seller, Segini Ongkir di Toko Online](https://finance.detik.com/berita-ekonomi-bisnis/d-8477160/ditanggung-seller-segini-ongkir-di-toko-online) — 2026-05-06 — Biaya layanan logistik dibebankan ke penjual, tidak tampil di checkout pembeli
- [Nasib Afiliator TikTok Shop, Komisi Dibekukan Perkara Gratis Ongkir](https://www.cnbcindonesia.com/tech/20260707152842-37-748834/nasib-afiliator-tiktok-shop-komisi-dibekukan-perkara-gratis-ongkir/amp) — 2026-07-07 — Efek domino ke afiliator saat era gratis ongkir

## The pain (verbatim quotes in Indonesian)

> "TikTok Shop akan menaikkan biaya komisi dinamis hingga 15 kali lipat mulai 18 Mei 2026, menimbulkan keluhan dari penjual." (Bisnis.com, deskripsi artikel)

> "Saya sudah sampaikan tidak boleh ada dulu kenaikan-kenaikan, tidak boleh, sudah tegas itu," ujar Maman (Menteri UMKM) saat menanggapi kenaikan sepihak. (CNBC Indonesia)

> "Biaya ini ditanggung oleh penjual dan tidak akan ditampilkan kepada pembeli saat pembayaran (checkout)," tulis pengumuman TikTok Shop kepada penjual. (Detik Finance)

> "Platform e-commerce mulai memberlakukan biaya layanan logistik alias ongkos kirim (ongkir) yang dibebankan ke penjual (seller)." (Detik Finance)

Data ongkir baru: Jawa ke Jakarta Rp 690 - Rp 4.350 per pesanan, Jawa ke Kalimantan Rp 3.440 - Rp 5.060, Jawa ke Papua/Maluku Rp 3.540 - Rp 5.060. Gabung komisi baru + ongkir seller-paid, margin UMKM tinggal tipis.

## Evidence of volume

- TikTok Shop menaikkan komisi penjual hingga 16 kali lipat per 18 Mei 2026 (CNBC).
- Menteri UMKM turun tangan melarang kenaikan sepihak, tanda keluhan masif dari penjual.
- Hampir semua marketplace besar (Shopee, Tokopedia, Lazada, TikTok Shop) naikkan biaya admin dan komisi di 2026 (Sentrasoft).
- Afiliator TikTok Shop ikut terdampak (komisi dibekukan) saat era gratis ongkir, 7 Juli 2026.

## Existing solutions (and why they fail)

- Fitur hitung HPP bawaan marketplace: tidak akurat karena tidak memasukkan komisi dinamis per kategori + ongkir seller-paid secara real time.
- Sheet manual seller: rawan salah, butuh update tiap platform ganti tarif (terjadi berkali-kali di 2026).
- Agensi konsultan e-commerce: mahal, bukan untuk seller pemula dengan omset di bawah Rp 50 juta/bulan.

## Your wedge

Bikin kalkulator laba-bersih otomatis lintas marketplace yang selalu update tarif resmi (komisi dinamis + ongkir seller-paid + admin) dan ngasih alert "produk ini rugi di harga ini". Terus kasih rekomendasi harga jual minimum per SKU. Untuk seller yang kena gebuk komisi TikTok Shop, sediakan modul pindah ke Shopee/Tokopedia dengan bandingkan net margin. Underserved karena tool yang ada cuma hitung pajak, bukan net margin setelah semua potongan baru 2026.

## What people would pay

- Rp 25.000 - Rp 49.000/bulan per toko untuk kalkulator + monitor tarif + alert rugi.
- Evidence: seller rela bayar agen iklan Rp 100.000+/hari tapi nggak tahu produk mereka rugi di harga jual. Pain akut = takut tutup toko.
- Comparable: aplikasi manajemen toko lokal (Kasir Pintar, Mokapos) subscription Rp 50.000 - Rp 150.000/bulan.

## Adjacent opportunities

- Modul recomendasi pindah platform otomatis (Shopee ke TikTok atau sebaliknya).
- Bundling dengan jasa foto produk dan copywriting murah untuk naikkan konversi.
- Edukasi "cara harga agar nggak rugi" jadi lead magnet ke komunitas seller WhatsApp/Telegram.

## Time-to-build estimate

- 2 minggu dengan off-the-shelf tools (Google Sheet + Apps Script + scraper tarif publik).
- 1 bulan dengan custom app + webhook ke API marketplace (yang terbuka).
- 3+ bulan untuk full SaaS multi-toko dengan dashboard P&L real time.
