# Coretax Sering Error dan Sulit Diakses, Wajib Pajak Gagal Lapor SPT

**Date observed:** 2026-07-11
**Signal strength:** 4
**Category:** umkm
**Sources (minimum 3):**
- [Coretax Error di Hari Terakhir Lapor SPT, Ditjen Pajak Diminta Perpanjangan Tenggat](https://www.tribunnews.com/bisnis/7823857/coretax-error-di-hari-terakhir-lapor-spt-ditjen-pajak-diminta-perpanjangan-tenggat) — 2026-05-01 — Sistem Coretax lumpuh "502 Bad Gateway" persis di deadline SPT 30 April 2026.
- [Dinamika dan Tantangan Implementasi Coretax](https://news.detik.com/kolom/d-7787128/dinamika-dan-tantangan-implementasi-coretax) — 2025-02-20 — Kolom mengakui kegagalan koneksi, Faktur Pajak, Bukti Potong, dan verifikasi data jadi keluhan rutin WP.
- [9 Juta Wajib Pajak Punya Akun Coretax tapi Belum Lapor SPT](https://finance.detik.com/berita-ekonomi-bisnis/d-8386247/9-juta-wajib-pajak-punya-akun-coretax-tapi-belum-lapor-spt) — 2026 — 9 juta akun aktif tapi belum lapor, sinyal friction sistemik.
- [Coretax Sulit Diakses, Menkeu Bongkar Dugaan Bisnis Tersembunyi](https://www.beritasatu.com/ekonomi/2979392/coretax-sulit-diakses-menkeu-bongkar-dugaan-bisnis-tersembunyi) — 2026 — Menkeu sendiri akui Coretax sulit diakses (situs terblokir CloudFront saat diakses, tapi judul dan kutipan tersebar di berita lain).

## The pain (verbatim quotes in Indonesian)
> "Coretax mengalami gangguan pada Kamis sore dan saat diakses oleh wajib pajak, laman tersebut hanya menampilkan pesan '502 Bad Gateway'." (TribunNews, 1 Mei 2026)

> "Kegagalan koneksi, masalah dalam penerbitan Faktur Pajak dan pembuatan Bukti Potong pajak, kesulitan verifikasi dan otorisasi data melalui aplikasi Coretax adalah sebagian masalah yang sering dikeluhkan Wajib Pajak dalam satu bulan terakhir." (detik.com kolom, 20 Feb 2025)

> "Hari ini, 30 April, di hari terakhir batas lapor SPT, sistem malah error." (Said Abdullah, Anggota Komisi XI DPR, dikutip TribunNews)

## Evidence of volume
- 9 juta wajib pajak sudah punya akun Coretax tapi belum lapor SPT per data detikFinance 2026.
- Gangguan "502 Bad Gateway" terjadi tepat di hari terakhir pelaporan 30 April 2026 setelah perpanjangan dari 31 Maret.
- Anggota DPR Komisi XI secara terbuka minta DJP perpanjang tenggat karena error sistem.
- Keluhan Coretax rutin muncul di media sosial sejak peluncuran 1 Januari 2025 (Faktur Pajak, Bukti Potong, verifikasi NIK/NPWP).

## Existing solutions (and why they fail)
- Coretax Mobile (aplikasi resmi DJP): gagal menjawab root cause, server pusat tetap jadi bottleneck, sinyal buruk dan HP low-end warga Indonesia makin memperparah.
- Help desk dan layanan tatap muka KPP: hanya bisa membantu segelintir WP, antrean panjang, tidak skalabel untuk jutaan WP.
- Panduan video di YouTube/akun pajak: tidak menyelesaikan error server, hanya cara navigasi.

## Your wedge
Bangun layanan "pembantu lapor pajak" berbasis asisten (human-in-the-loop atau chatbot terlatih) yang mengambil alih proses Coretax untuk UMKM dan pekerja: mulai dari aktivasi akun, sinkronisasi NIK ke NPWP, input bukti potong, hingga submit SPT, lalu kirim bukti lapor ke WP. Bedanya dengan konsultan pajak mahal: pakai template otomatis dan antrean pintar di luar jam sibuk server. Produk kedua: alat monitor status Coretax (cek apakah sistem up) plus pengingat deadline dan draft SPT otomatis dari rekapan transaksi Shopee/Tokopedia. WP bayar karena mereka tak punya waktu dan takut denda (denda telat lapor Rp 100.000 per bulan untuk WP tertentu).

## What people would pay
- Paket "lapor SPT aman" satu kali: Rp 75.000 - Rp 150.000 per musim pajak.
- Langganan bulanan asisten pajak UMKM: Rp 50.000 - Rp 100.000 per bulan.
- Bukti willingness to pay: jasa jasa konsultan pajak konvensional mematok Rp 300.000 - Rp 1 juta per SPT; pasar lower-middle (UMKM, pekerja gig) belum terlayani.
- Comparable: aplikasi Klikpajak dan OnlinePajak mengenakan biaya per transaksi e-Faktur; ruang harga murah untuk WP orang pribadi masih kosong.

## Adjacent opportunities
- Template dan tracker pajak untuk freelancer penerima bayaran luar negeri (sudah ada file terpisah, bisa cross-sell).
- Alat rekonsiliasi bukti potong otomatis dari email dan PDF.
- Bundling dengan jasa pembuatan NPWP online dan EFIN terlupakan.

## Time-to-build estimate
- 2 minggu: bot status-check Coretax + pengingat deadline (no-code/low-code).
- 1 bulan: asisten lapor SPT semi-otomatis dengan template.
- 3+ bulan: produk pajak UMKM penuh dengan integrasi API dan rekonsiliasi transaksi marketplace.
