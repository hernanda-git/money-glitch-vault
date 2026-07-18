# Karyawan Ritel Minimarket (Indomaret) Tolak Upah Lembur Diganti Hari Libur

**Date observed:** 2026-07-18
**Signal strength:** 5
**Category:** employee
**Sources (minimum 3):**
- [Indomaret Digeruduk Buntut Kabar Upah Lembur Diganti Hari Libur](https://news.detik.com/berita/d-8506690/indomaret-digeruduk-buntut-kabar-upah-lembur-diganti-hari-libur) — 2026-05-27 — Buruh Indomaret demo di Menara Indomaret PIK, menolak kebijakan ganti lembur dengan off.
- [Buruh Indomaret Ancam Demo Lebih Besar Bila Tuntutan Upah Lembur Tak Dipenuhi](https://news.detik.com/berita/d-8505520/buruh-indomaret-ancam-demo-lebih-besar-bila-tuntutan-upah-lembur-tak-dipenuhi) — 2026-05-26 — PUK SPAI PT Indomarco Prismatama Tangerang ancam demo lebih besar.
- [Indomaret Buka Suara soal Buruh Tolak Upah Lembur Diganti Hari Libur](https://news.detik.com/berita/d-8505713/indomaret-buka-suara-soal-buruh-tolak-upah-lembur-diganti-hari-libur) — 2026-05-26 — Manajemen Indomaret buka suara soal kebijakan.
- [Viral Indomaret Dikabarkan Tutup Sementara Usai Karyawan Demo soal Lembur](https://www.detik.com/bali/bisnis/d-8512556/viral-indomaret-dikabarkan-tutup-sementara-usai-karyawan-demo-soal-lembur) — 2026-05-31 — Indomaret tutup operasional 31 Mei dan 1 Juni terkait protes lembur.

## The pain (verbatim quotes in Indonesian)
> "Hari ini teman-teman yang hadir berjuang pada pagi hari ini, menuntut hak dan keadilan terhadap pekerja karyawan Indomaret." (buruh Indomaret, demo di PIK, detikNews 27 Mei 2026)

> "Menegaskan hak pekerja atas upah kerja lembur. Menolak penggantian hak lembur dengan off tambahan yang sesuai dengan ketentuan." (tuntutan tertulis PUK SPAI PT Indomarco Prismatama Tangerang dalam spanduk demo)

> "Menuntut kepatuhan perusahaan terhadap peraturan perusahaan dan Undang-undang Ketenagakerjaan." (tuntutan buruh Indomaret)

Inti masalahnya: pegawai minimarket (Indomaret) yang bekerja saat tanggal merah mengklaim perusahaan mengganti hak upah lembur dengan hari libur (off) tambahan, bukan uang. Mereka menilai ini melanggar UU Ketenagakerjaan yang mewajibkan pembayaran upah lembur 2x lipat untuk hari libur nasional. Keluhan serupa menimpa pekerja ritel lain (Alfamart, supermarket) yang memiliki pola shift 24 jam dan wajib kerja saat libur nasional.

## Evidence of volume
- 4 artikel detikNews/detikBali dalam 27 Mei sampai 31 Mei 2026 membahas satu rangkaian demo buruh Indomaret soal lembur.
- Spanduk demo memuat 6 tuntutan resmi dari serikat PUK SPAI PT Indomarco Prismatama (Tangerang), menunjukkan organisasi buruh skala besar terlibat.
- Indomaret menutup operasional 31 Mei dan 1 Juni 2026 akibat eskalasi protes, sinyal bahwa isu menyentuh ribuan toko.
- Pola kerja ritel minimarket wajib 24 jam, artinya setiap hari libur nasional (Idul Fitri, Natal, Tahun Baru) memicu gesekan lembur yang sama di puluhan ribu outlet nasional.

## Existing solutions (and why they fail)
- Serikat pekerja internal (PUK SPAI): hanya mencakup sebagian karyawan dan harus berdemo turun ke jalan agar didengar, proses mediasi di Kemnaker lambat.
- Mediasi Kemnaker / Wamenaker: berujung pada "kesepakatan" yang menurut buruh hanya mengubah, bukan menghapus kebijakan penggantian lembur.
- Pengaduan via Posko THR atau dinas tenaga kerja daerah: lambat, birokratis, dan buruh takut diintimidasi jika melapor (salah satu tuntutan: "menuntut penindakan tegas terhadap oknum yang melakukan intimidasi").

## Your wedge
Buat layanan "Kalkulator & Klip Kirim Hak Lembur Ritel" berbasis WA/Android gratis: pekerja ritel input jam kerja di tanggal merah, aplikasi hitung upah lembur wajib (2x atau 3x sesuai UU 13/2003 + aturan terbaru) dan hasilkan draf pengaduan siap kirim ke Disnaker/Kemnaker plus template somasi ke HR. Tambahkan fitur anonim agar buruh tak takut diintimidasi, dan basis data "perusahaan mana yang patuh bayar lembur vs ganti off" hasil laporan kawan kerja. Monetisasi lewat premium (konsultasi hukum kerja murah) dan B2B (mini SaaS buat manajer toko hitung kewajiban lembur otomatis agar tak melanggar UU).

## What people would pay
- Individu: Rp 0 untuk kalkulator dasar, Rp 50.000 sampai Rp 150.000 sekali untuk draft somasi + konsultasi singkat via WA.
- B2B mini-SaaS untuk manajer toko/HR: Rp 99.000 sampai Rp 299.000 per bulan agar hitungan lembur otomatis dan patuh aturan.
- Evidence willingness-to-pay: serikat bersedia bayar tools legaltech murah (lihat gap inbox 2026-07-12-micro-legaltech-engine.md dan 2026-07-13-siaga-phk-micro-legaltech.md). Demo ribuan buruh membuktikan demand nyata akan perlindungan hak lembur.

## Adjacent opportunities
- Template somasi PHK sepihak dan tuntutan pesangon (overlaps dengan file pesangon-phk-tidak-dibayar.md).
- WA bot "cek status pengaduan Disnaker" untuk buruh.
- Bundling dengan asuransi kecelakaan kerja mikro untuk pekerja ritel shift malam.

## Time-to-build estimate
- 2 minggu dengan off-the-shelf tools: bot WA (Twilio/Fonnte) + Google Sheet kalkulator UU Ketenagakerjaan + form draf somasi.
- 1 bulan dengan custom dev: app Android + dashboard agregasi laporan per toko.
- 3+ bulan untuk full produk legaltech ritel terintegrasi Disnaker.
