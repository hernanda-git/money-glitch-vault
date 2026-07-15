# Aturan Baru Kontrol BPJS Kesehatan Bikin Pasien dan Lansia Bingung

**Date observed:** 2026-07-15
**Signal strength:** 4
**Category:** other
**Sources (minimum 3):**
- [Simak! Aturan Baru BPJS Kesehatan untuk Pasien Kontrol Mulai Juni 2026](https://news.detik.com/berita/d-8522630/simak-aturan-baru-bpjs-kesehatan-untuk-pasien-kontrol-mulai-juni-2026) — 2026-06-08 — per 1 Juni 2026 pasien wajib datang tepat tanggal surat kontrol
- [Aturan Baru BPJS Kesehatan untuk Pasien Kontrol per Juni 2026, Simak agar Tak Ditolak](https://www.suara.com/lifestyle/2026/06/08/165201/aturan-baru-bpjs-kesehatan-untuk-pasien-kontrol-per-juni-2026-simak-agar-tak-ditolak) — 2026-06-08 — datang lebih awal tidak dilayani, terlambat wajib reservasi online H-1
- [DPRD Kaltara Soroti Pendaftaran lewat Mobile JKN Online, Banyak Pasien Tua Tak Bisa Gunakan](https://kaltara.tribunnews.com/kaltara/121499/dprd-kaltara-soroti-pendaftaran-lewat-mobile-jkn-online-banyak-pasien-tua-tak-bisa-gunakan) — 2026 — DPRD soroti lansia gagal pakai Mobile JKN
- [Sistem BPJS Bermasalah, RSUD Soewandhie Tambah Dokter untuk Kurangi Antrean](https://www.jawapos.com/surabaya-raya/2503040005/sistem-bpjs-bermasalah-rsud-soewandhie-tambah-dokter-untuk-kurangi-antrean) — 2026 — RS tambah dokter karena antrean BPJS
- [DPRD Medan Soroti Sulitnya Akses Obat Pasien BPJS](https://medan.tribunnews.com/medan-terkini/1790111/dprd-medan-soroti-sulitnya-akses-obat-pasien-bpjs-desak-dinkes-dan-bpjs-kesehatan-segera-koordinasi) — 2026 — akses obat pasien BPJS sulit

## The pain (verbatim quotes in Indonesian)

> "Per 1 Juni 2026, pasien kini wajib datang tepat sesuai tanggal yang tertera pada surat kontrol dan tidak boleh mendahului." — Detik, 8/6/2026

> "Pasien yang datang lebih awal dari jadwal yang telah ditetapkan tidak akan mendapatkan layanan kontrol." — Suara.com

> "Banyak pasien tua tak bisa gunakan" aplikasi Mobile JKN untuk pendaftaran online. — DPRD Kaltara, Tribun

Sakitnya: pasien kontrol rutin (penyakit kronis, lansia, ibu hamil) sekarang harus datang pas di tanggal surat kontrol. Kalau datang lebih awal karena takut macet atau sudah ambil cuti, malah tidak dilayani. Kalau terlambat, wajib reservasi online H-1 lewat Mobile JKN, padahal banyak lansia dan warga desa yang tidak punya HP pintar atau tidak paham aplikasi. Ujungnya antrean panjang dan pelayanan tertunda.

## Evidence of volume

- Aturan berlaku nasional per 1 Juni 2026, menyangkut puluhan juta peserta BPJS kontrol rutin.
- DPRD di dua provinsi (Kaltara, Medan) sudah sidak dan soroti kendala lansia pakai Mobile JKN dan akses obat.
- RS daerah (RSUD Soewandhie Surabaya) terpaksa tambah dokter khusus untuk kurangi antrean BPJS, tanda beban sistem tinggi.
- Keluhan di medsos dan grup WA warga soal "surat kontrol tidak boleh maju" cukup banyak (sintesis dari berita + keluhan pengguna yang dikutip pers).

## Existing solutions (and why they fail)

- Mobile JKN (aplikasi resmi BPJS): gagal karena UI rumit, lansia dan warga desa tidak bisa pakai, sering error saat reservasi H-1.
- Loket manual di RS: berkurang karena dorong digitalisasi, antrean jadi panjang.
- Call center 165: sulit dihubungi di jam sibuk, tidak bisa bantu reservasi langsung.

## Your wedge

Buat asisten "Ingat Kontrol BPJS" berbasis WhatsApp: pasien kirim foto surat kontrol (atau ketik tanggal), bot ingatkan H-3 dan bantu buat reservasi Mobile JKN otomatis tanpa harus pahami aplikasi. Untuk lansia tanpa HP pintar, bisa diurus oleh anak/kerabat dari jarak jauh. Plus panduan "kalau datang lebih awal, ini opsi yang masih dilayani". Ini menjembatani kesenjangan digital lansia yang tidak bisa pakai Mobile JKN. Monetisasi lewat donasi atau langganan keluarga Rp 10.000 per bulan untuk ingatkan seluruh anggota keluarga.

## What people would pay

- Langganan keluarga Rp 10.000 sampai Rp 25.000 per bulan untuk reminder dan bantuan reservasi seluruh anggota.
- Evidence willingness to pay: keluarga rela bayar jasa panggil antar lansia ke RS (Rp 50.000 sampai Rp 100.000 sekali jalan). Tool digital jauh lebih murah.
- Comparable: aplikasi pengingat obat dan janji medis (Halodoc, Alodokter reminder) gratis tapi tidak terintegrasi reservasi BPJS.

## Adjacent opportunities

- Bantuan pendaftaran Mobile JKN untuk lansia (jasa kurir digital).
- Panduan akses obat BPJS (antrian farmasi RS sering kosong).
- Bundling dengan pengingat minum obat kronis (diabetes, hipertensi).

## Time-to-build estimate

- 2 minggu dengan off-the-shelf tools: bot WhatsApp (Twilio / WATI) + OCR tanggal surat kontrol + scheduler.
- 1 bulan dengan custom dev: integrasi API Mobile JKN (jika tersedia) dan multi-user keluarga.
- 3+ bulan untuk produk penuh dengan kemitraan klinik dan white-label untuk Dinas Kesehatan.
