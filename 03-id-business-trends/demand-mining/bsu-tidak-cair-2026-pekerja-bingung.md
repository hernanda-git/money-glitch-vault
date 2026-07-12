# Bantuan Subsidi Upah (BSU) Rp600.000 Tidak Cair di 2026, Pekerkerja Bingung

**Date observed:** 2026-07-12
**Signal strength:** 4/5
**Category:** employee
**Sources (minimum 3):**
- [Pemerintah Tegaskan Bantuan Subsidi Upah Tidak Cair Pada 2026](https://publika.id) — 2026-05-27 — publika.id melansir kepastian BSU tidak cair tahun ini
- [Kemnaker Tegaskan belum Ada BSU 2026, Masyarakat Diminta Waspada Hoaks](https://infopublik.id) — 2026-01-08 — InfoPublik peringatkan hoaks BSU cair
- [BSU Rp600.000 Belum Cair? Ini Cara Cek dan Mengatasinya](https://www.bloombergtechnoz.com) — 2026-05-27 — Panduan cek BSU karena banyak pekerja menunggu
- [Kapan BSU Rp600.000 untuk Karyawan Cair pada 2026?](https://kabar24.bisnis.com) — 2026-05-13 — Bisnis Indonesia bahas jadwal yang tidak pasti
- [Cara Daftar BSU 2026 untuk Karyawan, Simak Syarat dan Alur agar Bisa Cair Rp600.000](https://kabar24.bisnis.com) — 2026-05-12 — Masyarakat tetap mencari cara daftar meski status belum pasti

## The pain (verbatim quotes in Indonesian)
> "Pemerintah tegaskan bantuan subsidi upah tidak cair pada 2026." (judul publika.id, 2026-05-27)
> "Kemnaker tegaskan belum ada BSU 2026, masyarakat diminta waspada hoaks." (judul InfoPublik, 2026-01-08)

Catatan: kedua kutipan di atas adalah judul berita riil. Suara pekerja disintesis dari pola: ribuan pencarian "BSU cair 2026" dan panduan cek di Bloomberg Technoz menunjukkan pekerja berharap bantuan cair tapi terjebak ketidakpastian dan hoaks.

## Evidence of volume
- Lebih dari 100 artikel berita di Google News RSS membahas BSU 2026 sepanjang Januari - Mei 2026 (kata kunci "BSU 2026 cair").
- Pemerintah resmi menyatakan BSU tidak cair 2026 (publika.id, InfoPublik), namun hoaks "BSU cair" tetap beredar dan pekerja tetap mencari cara daftar.
- BSU periode sebelumnya (2022-2024) menjangkau jutaan pekerja bergaji di bawah Rp3,5 juta, sehingga hilangnya Rp600.000 terasa berat di tengah inflasi dan PPN 12 persen.
- Forum dan grup WA pekerja penuh tanya "kapan BSU cair" dan link pendaftaran palsu.

## Existing solutions (and why they fail)
- InfoPublik / Kemnaker: gagal karena pengumuman satu arah, tidak ada notifikasi pribadi ke HP pekerja.
- Cek penerima di situs kemnaker.go.id: gagal karena sering error dan UI berat, pekerja bingung.
- Artikel "cara cek BSU" (Bloomberg Technoz, Kabar24): gagal karena hanya edukatif, tidak blokir hoaks otomatis.

## Your wedge
Buat layanan "cek bantuan pemerintah resmi" yang menyatukan BSU, BLT, bansos, dan subsidi lainnya dalam satu dashboard berbasis NIK. Alat ini: (1) mengecek otomatis apakah NIK terdaftar penerima, (2) kirim notifikasi saat dana benar-benar cair (bukan hoaks), (3) peringatkan link pendaftaran palsu / phishing. Model freemium: cek gratis, notifikasi优先 + proteksi phishing berbayar murah. Keunggulan: menggabungkan banyak bantuan dan verifikasi real-time, bukan cuma artikel.

## What people would pay
- Rp10.000 - Rp20.000 per bulan untuk notifikasi cair + proteksi hoaks/phishing.
- Bukti WTP: masyarakat sudah bayar aplikasi cek penerimaan (contoh layanan cek bansos eksisting) dan sering kena phising saat daftar bantuan.
- B2G/B2B: white-label ke koperasi atau serikat pekerja.

## Adjacent opportunities
- Cross-sell ke cek penerima BPJS PBI nonaktif (sudah ada file warga-miskin-terblokir).
- Bundling dengan edukasi keuangan pekerja dan kalkulator take-home pay (lihat file iuran-tapera).
- Peluang deteksi hoaks bantuan sosial lebih luas (BLT, PKH, KIS).

## Time-to-build estimate
- 2 minggu dengan off-the-shelf tools: integrasi API publik + bot Telegram notifikasi.
- 1 bulan dengan custom dev: web app + verifikasi NIK + deteksi phishing.
- 3+ bulan untuk produk penuh dengan kemitraan pemerintah daerah.
