# Relawan Dapur MBG/SPPG Kehilangan Penghasilan Mendadak

**Date observed:** 2026-07-19
**Signal strength:** 4/5
**Category:** employee
**Sources (minimum 3):**
- [Karyawan SPPG Banyumas Demo gegara Tak Bisa Kerja Imbas MBG Disetop Sementara](https://www.detik.com/jateng/berita/d-8549557/karyawan-sppg-banyumas-demo-gegara-tak-bisa-kerja-imbas-mbg-disetop-sementara) — 2026-06-27 — Relawan dapur MBG di Banyumas demo karena program dihentikan, puluhan ribu relawan kehilangan penghasilan harian.
- [Rincian Utang Badan Gizi Nasional Rp 1,6 Triliun](https://finance.detik.com/berita-ekonomi-bisnis/d-8579077/rincian-utang-badan-gizi-nasional-rp-1-6-triliun) — 2026-07-18 — BGN akui tunggakan Rp 1,6 T ke pihak ketiga, termasuk bantuan pemerintah MBG Rp 100 miliar dan pembangunan dapur Rp 1,04 triliun belum dibayar.
- [Prabowo Beri Waktu Sebulan Buat BGN Benahi MBG](https://finance.detik.com/berita-ekonomi-bisnis/d-8578819/prabowo-beri-waktu-sebulan-buat-bgn-benahi-mbg) — 2026-07-18 — Presiden beri tenggat satu bulan meski program sudah dihentikan sementara via SE Nomor 12 Tahun 2026.

## The pain (verbatim quotes in Indonesian)

> "Relawan sangat terbantu dengan program MBG. Awalnya mereka sulit mencari pekerjaan, sudah dapat pekerjaan ternyata dihentikan selama tiga minggu. Dampaknya luar biasa, baik bagi petani, UMKM, maupun relawan sendiri." , kata Koordinator Relawan SPPG Banyumas, Imam Muntofik, 27 Juni 2026.

> "Mereka benar-benar menjerit. Sebentar lagi anak-anak masuk sekolah, orang tua butuh biaya untuk beli buku, sepatu, seragam. Sementara program MBG tutup sehingga mereka tidak bisa bekerja." , ujar Imam.

> "Mereka mencari pekerjaan apa saja yang bisa dilakukan. Ada yang kerja bangunan dan pekerjaan lain untuk mencukupi kebutuhan sehari-hari." , jelasnya soal cara relawan bertahan.

> "Dalam juknis sudah jelas, relawan itu menerima Rp 100 ribu sampai Rp 200 ribu. Ada yang menerima Rp 115 ribu, Rp 120 ribu, tergantung SPPG masing-masing." , kata Imam soal honor harian yang kini terhenti.

## Evidence of volume

- Di Banyumas saja ada 200 lebih dapur MBG, masing-masing melibatkan sekitar 50 relawan , artinya hampir 10.000 sampai 11.000 relawan terdampak di satu kabupaten.
- Imam menyebut seluruh Jawa Timur APTRI menuntut hal serupa , mengindikasikan skala nasional karena MBG adalah program nasional.
- Aksi demo langsung turun ke jalan di Banyumas dengan massa sekitar setengah dari total relawan yang hadir , ditambah petani organisasi Tani Merdeka yang membawa gunungan hasil tani.
- BGN mencatat utang Rp 1,6 triliun ke pihak ketiga , sebagian besar adalah kewajiban ke dapur, vendor, dan pembangunan dapur yang berarti aliran penghasilan relawan mandek.

## Existing solutions (and why they fail)

- Bantuan sosial (PKH/BPNT) umum , gagal karena relawan MBG adalah pekerja harian informal yang tidak masuk data penerima bansos dan butuh income harian, bukan bantuan bulanan.
- Serikat pekerja / KSPI , gagal karena relawan MBG bukan karyawan tetap berbadan hukum, sehingga perlindungan PHI dan pesangon sulit menjangkau mereka.
- Pengalihan ke pekerjaan serabutan (bangunan, buruh harian) , gagal karena tidak menjamin pendapatan stabil mendekati Rp 100.000-200.000/hari dan bersifat musiman.

## Your wedge

Bangun layanan penghubung kerja harian terverifikasi khusus untuk relawan MBG/SPPG yang kehilangan shift: sebuah platform penyaluran tenaga harian (dapur, katering, gudang, agribisnis) yang terintegrasi dengan data SPPG sehingga mereka mendapatkan job harian pengganti dalam radius dekat. Bedanya dengan job board umum: verifikasi identitas pakai NIK + ID SPPG, pembayaran harian lewat QRIS ke e-wallet, dan modul "tagihan tertunda BGN" yang mencatat hak relawan agar bisa ditagih saat dana cair. Untuk pemda, jual dashboard "early warning relawan menganggur" berbasis jumlah dapur yang offline di wilayahnya. Ini bisa dijalankan dengan no-code (Spreadsheet + WhatsApp API + QRIS PPOB) dalam 2-3 minggu tanpa capex besar.

## What people would pay

- Relawan: Rp 0 di sisi pencari kerja , monetisasi dari potongan transaksi Rp 2.000-5.000 per shift yang dibayarkan penyedia kerja (katering/dapur).
- Pemda / Dinas Sosial: Rp 5-15 juta per bulan untuk dashboard early-warning per kabupaten , setara biaya satu konsultan lapangan.
- SPPG / dapur: Rp 1-3 juta per bulan untuk modul penagihan hak relawan ke BGN , karena mereka butuh bukti tagihan tertunda yang rapi.
- Bukti willingness to pay: dapur MBG sudah bayar honor Rp 100.000-200.000/hari per relawan , artinya ekosistem punya budget, hanya alirannya yang terputus.

## Adjacent opportunities

- Modul penagihan ke BGN untuk pihak ketiga (vendor, pembangun dapur) , lintas ke pain pemasok MBG.
- Pelatihan reskilling cepat (food handler, HACCP) untuk relawan agar bisa masuk katering swasta.
- Bundling dengan layanan HRIS mikro untuk dapur MBG yang kini kekurangan admin.

## Time-to-build estimate

- 2 minggu dengan no-code (WhatsApp bot + Google Sheet + QRIS PPOB) untuk MVP penyaluran kerja harian.
- 1 bulan dengan backend sederhana + verifikasi NIK via API Dukcapil sandbox.
- 3 bulan untuk versi enterprise dengan integrasi langsung ke sistem SPPG dan dashboard pemda.
