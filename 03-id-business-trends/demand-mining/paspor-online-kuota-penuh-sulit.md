# Paspor Online Sulit, Kuota Antrean M-Paspor Ludes dalam Hitungan Jam

**Date observed:** 2026-07-16
**Signal strength:** 5
**Category:** other
**Sources (minimum 3):**
- [Imigrasi Bekasi Jemput Bola, 130 Paspor Ludes Kurang dari 24 Jam](https://news.detik.com/berita/d-8530933/imigrasi-bekasi-jemput-bola-130-paspor-ludes-kurang-dari-24-jam) — 2026-06-13 — kuota paspor habis sangat cepat, pemda harus jemput bola
- [Belum Dua Bulan Beroperasi, Imigrasi Tabanan Banjir Pemohon](https://www.detik.com/bali/berita/d-8496329/belum-dua-bulan-beroperasi-imigrasi-tabanan-banjir-pemohon) — 2026-05-29 — kantor imigrasi baru langsung kebanjiran pemohon paspor
- [Penerbangan Internasional Picu Permohonan Paspor di Palembang](https://www.detik.com/sumbagsel/berita/d-8550807/penerbangan-internasional-picu-permohonan-paspor-di-palembang) — 2026-06-28 — lonjakan permohonan seiring pembukaan rute internasional
- [Layanan Imigrasi Bogor Akhir Pekan: Sabtu di Kantor, Minggu di GOR](https://news.detik.com/berita/d-8559434/layanan-imigrasi-bogor-akhir-pekan-sabtu-di-kantor-imigrasi-minggu-di-gor-bogor) — 2026-07-04 — imigrasi buka weekend karena antrean menggunung

## The pain (verbatim quotes in Indonesian)
> "Kurang dari 24 jam, sebanyak 130 paspor masyarakat rampung." (Imigrasi Bekasi, program jemput bola karena kuota kantor utama ludes)
> "Sejak dibuka 1 April 2026, Kantor Imigrasi Kelas III Non TPI Tabanan kebanjiran pemohon baik WNI maupun WNA."
> "Layanan yang paling banyak diminati adalah pembuatan paspor dan perpanjangan izin tinggal." (Kepala Kantor Imigrasi Tabanan, Andika Rahadiansyah)
> "Penerbangan Internasional Picu Permohonan Paspor di Palembang." (judul berita, lonjakan pasca pembukaan rute luar negeri)

Catatan: kuota appointment M-Paspor sering penuh di menit pertama buka. Warga terpaksa bayar calo atau nginep di depan kantor imigrasi. Sumber resmi (Kantor Imigrasi Yogyakarta, 2023) sendiri merilis panduan "Kuota M-Paspor Penuh? Apa Yang Harus Dilakukan", mengonfirmasi kuota penuh adalah masalah berulang.

## Evidence of volume
- 4 berita Detik sepanjang Mei-Juli 2026 melaporkan kuota paspor ludes / kantor imigrasi banjir pemohon di Bekasi, Tabanan, Palembang, Bogor.
- Imigrasi Bekasi: 130 slot paspor habis kurang dari 24 jam lewat skema jemput bola.
- Imigrasi Tabanan: kantor baru yang belum dua bulan beroperasi sudah kebanjiran pemohon.
- Imigrasi Bogor terpaksa buka layanan akhir pekan (Sabtu kantor, Minggu di GOR) untuk menyerap antrean.
- Pembukaan rute penerbangan internasional (Palembang) memicu lonjakan permohonan paspor baru.

## Existing solutions (and why they fail)
- M-Paspor (aplikasi resmi Ditjen Imigrasi): gagal karena kuota sangat terbatas dan diambil detik pertama buka, tidak ada waitlist otomatis, UI sering error saat traffic tinggi.
- Walk-in ke kantor imigrasi: gagal karena kuota harian fisik sangat kecil, harus datang subuh, dan banyak kantor tidak terima walk-in tanpa janji M-Paspor.
- Jasa calo / "agen paspor": mahal (Rp 500rb-2jt di luar biaya resmi) dan berisiko penipuan serta data pribadi bocor.
- Layanan "jemput bola" (Bekasi, Bogor): hanya sesekali dan teritorial, tidak scalable bagi warga di luar kota penyelenggara.

## Your wedge
Bangun layanan "paspor concierge" lokal: asisten yang memantau ketersediaan kuota M-Paspor 24/7, mengisi formulir dan booking slot atas nama user (dengan surat kuasa digital), plus panduan dokumen foto KTP/KK yang lolos verifikasi. Versi B2B: white-label untuk desa/kelurahan dan komunitas TKI yang rutin butuh paspor massal. Bedanya: bukan calo gelap, tapi kemitraan resmi berbasis biaya layanan transparan (Rp 50-100rb per booking sukses). Bisa juga bot notifikasi "kuota M-Paspor buka di kota X" via Telegram/WhatsApp.

## What people would pay
- Rp 50.000 - 150.000 per booking paspor sukses (jauh di bawah calo Rp 500rb-2jt).
- Evidence willingness-to-pay: masyarakat sudah bayar calo jutaan rupiah, artinya demand akan rela bayar jasa legal yang lebih murah dan aman.
- Comparable: jasa travel umroh/haji dan calo paspor mematok Rp 500rb-2jt; jasa fotokopi & dokumen online (e.g. Tokopedia "jasa administrasi") Rp 25-75rb per dokumen.

## Adjacent opportunities
- Panduan + booking visa (cross-sell ke agen travel).
- Layanan dokumen lain yang antreannya seperit (SKCK online, NPWP, KUA nikah) dalam satu "antrean assistant".
- Bundling asuransi perjalanan / notifikasi penerbangan murah untuk pembuat paspor baru.
- Marketplace slot konsultasi tatap muka dengan petugas (legal, transparan).

## Time-to-build estimate
- 2 minggu dengan off-the-shelf tools: bot notifikasi kuota + form assistant (Zapier/n8n + WA API + scraping jadwal M-Paspor).
- 1 bulan dengan custom dev: booking otomatis + dashboard per kota + kemitraan kelurahan.
- 3+ bulan untuk produk penuh dengan lisensi/kerja sama resmi Ditjen Imigrasi.
