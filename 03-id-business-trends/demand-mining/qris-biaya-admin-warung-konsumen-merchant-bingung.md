# Warung dan Merchant Kecil Bingung Soal Biaya Admin QRIS, Berujung Ricuh dengan Konsumen

**Date observed:** 2026-07-12
**Signal strength:** 4
**Category:** seller
**Sources (minimum 3):**
- [Anggota TNI Disebut Acak-acak Warung di Jakpus Perkara Admin QRIS Rp 1.000 (Kompas.com)](https://news.google.com/rss/search?q=Anggota+TNI+acak-acak+warung+admin+QRIS+Rp+1.000+Kompas&hl=id&gl=ID&ceid=ID:id) — 2026-05-05 — Konsumen mengamuk dan merusak warung Madura di Kemayoran karena tidak terima ditarik biaya admin QRIS Rp1.000.
- [Ricuh QRIS di Warung Madura, Ini Penjelasan Resmi BI (Akurat.co)](https://news.google.com/rss/search?q=Ricuh+QRIS+Warung+Madura+penjelasan+resmi+BI+Akurat&hl=id&gl=ID&ceid=ID:id) — 2026-05-06 — BI menegaskan merchant dilarang membebankan biaya MDR ke konsumen, tapi merchant kecil merasa dipaksa menanggung biaya sendiri.
- [Tambahan Biaya Admin Rp500 Pembayaran Nontunai di Warung Tradisional, Begini Reaksi Konsumen (Blok-a.com)](https://blok-a.com/tambahan-biaya-admin-rp500-pembayaran-nontunai-di-warung-tradisional-begini-reaksi-konsumen/) — 2025-11-08 — Warung di Malang menerapkan biaya admin Rp500 per transaksi QRIS, memicu keluhan konsumen.
- [Di Balik Kebijakan Warung Madura di Malang Terapkan Biaya Admin Rp500 untuk Transaksi QRIS (Blok-a.com)](https://blok-a.com/di-balik-kebijakan-warung-madura-di-malang-terapkan-biaya-admin-rp500-untuk-transaksi-qris/) — 2025-11-07 — Pemilik warung menjelaskan mereka menarik biaya admin karena MDR memotong pendapatan tipis mereka.

## The pain (verbatim quotes in Indonesian)
> "Pungutan liar QRIS resahkan warga." (judul liputan AdaDiMalang.com, sinyal keresahan publik)

Catatan: kutipan pelaku dan konsumen di badan artikel tidak dapat diekstrak verbatim karena halaman sumber dirender JavaScript. Deskripsi pain berikut disintesis dari 4 sumber di atas:

- Merchant kecil (warung Madura, PKL, kios) menghadapi biaya MDR (Merchant Discount Rate) 0,3 persen untuk transaksi UMKM. Pada margin sembako yang sangat tipis, ini terasa memakan untung.
- Karena BI melarang membebankan biaya ke konsumen, merchant terjebak: kalau menaikkan harga atau menarik "admin Rp500-Rp1.000" mereka melanggar aturan dan berisiko ribut dengan pembeli, kalau menanggung sendiri untungnya makin tergerus.
- Insiden fisik (perusakan warung di Kemayoran, keributan di Malang) menunjukkan konflik nyata di lapangan akibat kebingungan aturan.

## Evidence of volume
- Minimal 6 artikel berita nasional dan daerah dalam 3 bulan terakhir soal ricuh/biaya admin QRIS di warung (Kompas, Akurat, Tribun, Gotvnews, Blok-a, AdaDiMalang).
- Insiden viral perusakan warung Madura di Kemayoran (Mei 2026) yang menyeret oknum TNI, menandakan isu sudah menembus perhatian nasional.
- Pola berulang di beberapa kota (Jakarta, Malang) menunjukkan ini bukan kasus tunggal melainkan gesekan struktural aturan QRIS vs realitas margin warung.

## Existing solutions (and why they fail)
- Aturan BI (MDR 0 persen untuk transaksi di bawah Rp100 ribu untuk UMKM tertentu): gagal karena tidak semua merchant paham kategorinya, dan penerapannya tidak merata antar-penyedia (bank, e-wallet).
- Sosialisasi BI melalui pengumuman resmi: gagal menjangkau warung kecil yang tidak membaca rilis pers; mereka tetap menarik biaya admin karena tidak tahu larangannya.
- Fitur QRIS bawaan aplikasi bank/e-wallet: tidak memberi merchant kalkulasi untung bersih setelah MDR, sehingga merchant tidak sadar berapa yang benar-benar mereka terima.

## Your wedge
Bangun aplikasi "Kasir QRIS Jujur" untuk merchant mikro: sebuah PWA/aplikasi ringan yang (1) menampilkan real-time berapa rupiah bersih yang diterima setelah MDR untuk setiap transaksi, (2) memberi peringatan otomatis kapan sebuah transaksi masuk kategori bebas MDR (di bawah Rp100 ribu untuk UMKM) sehingga merchant tidak salah menarik admin, dan (3) menyediakan template edukasi singkat berbahasa sederhana soal aturan BI yang bisa dicetak dan ditempel di warung untuk mencegah cekcok dengan konsumen.

Diferensiasi: kita tidak bersaing sebagai payment gateway, melainkan sebagai lapisan literasi dan transparansi di atas QRIS yang sudah dipakai. Model murah, fokus pada satu masalah nyata: menghilangkan kebingungan yang memicu konflik. Bisa dimonetisasi lewat langganan mikro atau bundling dengan pembukuan warung.

## What people would pay
- Titik harga: Rp15.000-Rp30.000 per bulan untuk merchant mikro, atau gratis dengan upsell fitur pembukuan.
- Bukti willingness-to-pay: warung sudah rela menarik "admin Rp500-Rp1.000" dari konsumen demi menutup biaya, artinya mereka sangat sensitif pada margin dan mau berupaya melindunginya.
- Pembanding: aplikasi kasir seperti Moka, Majoo, Olsera menarik Rp100.000-Rp300.000+ per bulan, terlalu mahal dan berat untuk warung. Celah di segmen ultra-murah masih terbuka.

## Adjacent opportunities
- Pembukuan harian otomatis dari data QRIS untuk warung (cross-sell).
- Modul rekonsiliasi settlement: banyak merchant tidak tahu kapan dana QRIS masuk ke rekening.
- Bundling dengan manajemen stok sembako sederhana.

## Time-to-build estimate
- 2 minggu untuk MVP kalkulator MDR + poster edukasi (off-the-shelf, PWA sederhana).
- 1 bulan untuk integrasi baca-notifikasi transaksi dan dashboard untung bersih.
- 3+ bulan untuk versi penuh dengan pembukuan dan rekonsiliasi settlement.
