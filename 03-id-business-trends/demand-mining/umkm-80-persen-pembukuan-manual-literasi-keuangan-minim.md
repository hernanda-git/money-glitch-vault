# 80% UMKM Indonesia Masih Catat Keuangan Secara Manual

**Date observed:** 2026-06-29
**Signal strength:** 5/5
**Category:** umkm
**Sources (minimum 3):**
- [80% UMKM RI Masih Catat Keuangan Manual, Pahami Digitalisasi](https://www.fortuneidn.com/finance/80-umkm-ri-masih-catat-keuangan-manual-pahami-fungsi-digitalisasi-00-ccw2k-3cjmgn) — 2024-01-08 — Riset OCBC Indonesia Business Fitness Index: 80% pelaku usaha masih catat keuangan manual
- [80% Pelaku UMKM Indonesia Catat Keuangan Secara Manual, Masih Zaman di 2024?](https://mediaasuransinews.co.id/perbankan/80-pelaku-umkm-indonesia-catat-keuangan-secara-manual-masih-zaman-di-2024/) — 2024-01-08 — Kutipan langsung dari riset OCBC: 80 persen pelaku usaha Indonesia masih melakukan pencatatan keuangan dan stok usaha mereka secara manual
- [Kesulitan Catat Keuangan? Mahasiswa KKN UNDIP ajarkan SIAPIK](https://www.goodnewsfromindonesia.id/2024/08/03/kesulitan-catat-keuangan-mahasiswa-kkn-undip-ajarkan-siapik-solusi-mudah-digitalisasi-laporan-keuangan-bagi-umkm) — 2024-08-03 — Kutipan langsung dari pemilik UMKM Mama Laundry di Desa Kemusu, Boyolali
- [Genjot Pemanfaatan Teknologi di UMKM, Bisa Tumbuh Kolaborasi dengan Rumah BUMN](https://regional.kontan.co.id/news/genjot-pemanfaatan-teknologi-di-umkm-bisa-tumbuh-kolaborasi-dengan-rumah-bumn) — 2024-12-05 — Hanya 32% dari 64 juta UMKM yang sudah memanfaatkan digital

## The pain (verbatim quotes in Indonesian)
> "Sebelumnya saya mencatat keuangan usaha laundry hanya di buku mas, seadanya, jelek, kas masuk keluar saya catat. Kepingin banget bisa yang nyatat by sistem. Jadi, mau kalau diajari sistem itu." — Pemilik UMKM Mama Laundry, Desa Kemusu, Boyolali (kutipan dari Good News From Indonesia, Agustus 2024)

> "Masih banyak UMKM yang belum terbiasa menyusun laporan keuangan, bahkan tidak mengerti manfaat pencatatan keuangan dalam keberlanjutan aktivitas usaha." — Artikel GNFI KKN UNDIP, 2024

> "Sebanyak 80 persen pelaku usaha Indonesia masih melakukan pencatatan keuangan dan stok usaha mereka secara manual." — Riset OCBC Indonesia Business Fitness Index 2023, dikutip Fortune IDN dan Media Asuransi

## Evidence of volume
- 80% dari 64 juta UMKM Indonesia (sekitar 51 juta pelaku usaha) masih catat keuangan manual (OCBC Business Fitness Index 2023)
- Hanya 32% atau sekitar 21 juta UMKM dari total 64 juta yang sudah memanfaatkan teknologi digital (Kontan, data 2024)
- Riset ResearchGate (2025) menunjukkan sebagian besar UMKM tidak memiliki sistem manajemen arus kas yang jelas
- Mahasiswa KKN UNDIP harus turun langsung ke desa untuk mengajarkan pencatatan keuangan digital, menunjukkan kesenjangan literasi yang masif
- DPR RI menerbitkan kajian singkat tentang kendala UMKM termasuk keterbatasan akses perbankan dan pencatatan keuangan (Info Singkat P3DI, Desember 2023)

## Existing solutions (and why they fail)
- Solution A: Aplikasi pembukuan seperti Jurnal.id, Accurate, atau Wave — gagal karena terlalu kompleks untuk UMKM mikro, membutuhkan literasi digital yang belum dimiliki, dan berbayar
- Solution B: SIAPIK (Bank Indonesia) — gratis dan mudah, tetapi sosialisasinya masih sangat terbatas, hanya bisa diakses oleh UMKM yang sudah melek digital
- Solution C: Catatan manual di buku — masih menjadi pilihan utama karena tidak membutuhkan teknologi, tetapi menyebabkan data hilang, kesalahan hitung, dan tidak bisa diakses untuk pengajuan kredit

## Your wedge
Buat aplikasi pencatatan keuangan UMKM ultra-sederhana berbasis WhatsApp chatbot atau SMS. UMKM tinggal kirim pesan "jual gorengan 50rb" atau "beli minyak 30rb" dan sistem otomatis mencatat transaksi, menghitung laba rugi, dan menghasilkan laporan keuangan bulanan. Tidak perlu install aplikasi, tidak perlu login, tidak perlu belajar interface baru. Cukup kirim pesan seperti biasa. Laporan keuangan bisa langsung dikirim ke bank untuk pengajuan KUR atau kredit. Ini menjembatani 51 juta UMKM yang masih di buku tulis ke dunia digital tanpa friction.

## What people would pay
- Rp 15.000-25.000/bulan untuk UMKM mikro (warung, pedagang kaki lima, usaha rumahan)
- Bukti willingness-to-pay: UMKM rela bayar Rp 50.000-100.000/bulan untuk jasa pembukuan manual yang sering tidak akurat
- Komparasi: Jurnal.id mulai Rp 199.000/bulan (terlalu mahal untuk UMKM mikro), SIAPIK gratis tapi kurang dikenal, buku kas manual gratis tapi tidak efisien

## Adjacent opportunities
- Laporan keuangan digital otomatis bisa menjadi dasar credit scoring untuk pengajuan KUR
- Cross-sell: integrasi dengan QRIS untuk otomatisasi pencatatan transaksi digital
- Bundling dengan layanan perpajakan sederhana untuk pelaporan PPN atau pajak final UMKM

## Time-to-build estimate
- 2 minggu dengan WhatsApp Business API + spreadsheet sederhana
- 1 bulan dengan custom dev (chatbot + dashboard laporan)
- 3+ bulan untuk full product dengan fitur credit scoring dan integrasi perbankan
