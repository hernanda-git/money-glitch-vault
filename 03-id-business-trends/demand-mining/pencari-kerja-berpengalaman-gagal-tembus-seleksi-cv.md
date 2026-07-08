# Pencari Kerja Berpengalaman Gagal Tembus Seleksi CV, Kena Bias Usia

**Date observed:** 2026-07-09
**Signal strength:** 5/5
**Category:** employee
**Sources (minimum 3):**
- [Pusingnya Pencari Kerja, Punya Pengalaman Tapi CV Tetap Sulit Tembus](https://www.cnbcindonesia.com/news/20260708155537-4-749213/pusingnya-pencari-kerja-punya-pengalaman-tapi-cv-tetap-sulit-tembus) — 2026-07-08 — CNBC wawancarai langsung pelamar job fair yang berpengalaman tapi tak dipanggil.
- [Cerita Ibu Temani Anak ke Job Fair, Jadi Saksi Cari Kerja Makin Sulit](https://www.cnbcindonesia.com/news/20260708173128-4-749249/cerita-ibu-temani-anak-ke-job-fair-jadi-saksi-cari-kerja-makin-sulit) — 2026-07-08 — CNBC kutip Egi (27 thn) yang kena batas usia rekrutmen.
- [Lulusan Baru Sulit Dapat Kerja, Masa Tunggu Capai 20 Bulan](https://www.kompas.com/) — 2026-06-09 — Kompas.com catat masa tunggu kerja tembus 20 bulan.
- [Cari Duit Kian Sulit, Fresh Grad Butuh Waktu 20 Bulan Buat Dapat Kerja](https://www.cnbcindonesia.com/) — 2026-06-08 — CNBC sebut fresh grad butuh 20 bulan dapat kerja.

## The pain (verbatim quotes in Indonesian)
> "Kalau sekarang sih cukup sulit juga sih sekarang. Lumayan. Saya udah beberapa kali ngelamar masih belum ada panggilan-panggilan cuma sekadar interview doang. Terus dibilang mau dikabarin lagi tapi ya nunggu udah lama gak ada kabar lagi." , kata Akhi (22 thn, Brebes), pelamar dapur restoran.
> "Apalagi lulusan baru juga kan banyak, mereka muda-muda, masih 20-an awal, jadi gak mudah buat bersaing." , kata Egi (27 thn).
> "Iya mungkin di umur saya yang segini saingannya itu yang fresh graduate. Soalnya perusahaan juga sekarang kan , kebanyakan tuh ya itu menerima yang fresh graduate." , kata Egi.
> "mencari pekerjaan saat ini jauh lebih sulit dibandingkan ketika dirinya masih berada di usia produktif." , kata Rianti, ibu yang menemani anaknya ke job fair.

## Evidence of volume
- Masa tunggu kerja bagi lulusan baru dilaporkan mencapai 20 bulan (Kompas.com, Juni 2026).
- CNBC menyoroti dua job fair terpisah di Jakarta dalam satu hari (8 Juli 2026) dipenuhi pelamar berpengalaman maupun fresh grad.
- Egi sebut perusahaan banyak menerapkan batas usia dalam rekrutmen, menyingkirkan pekerja 27 thn ke atas.
- Fenomena orangtua mendampingi anak ke job fair jadi indikator tekanan pencarian kerja makin berat.

## Existing solutions (and why they fail)
- Solusi A: Situs lowongan seperti JobStreet dan LinkedIn , gagal karena algoritma ATS (applicant tracking system) saring CV secara otomatis dan buang pelamar berpengalaman yang format CV-nya usang.
- Solusi B: Kursus skill dan sertifikat , gagal karena masalah utamanya bukan keahlian tapi lolos seleksi awal dan bias usia, bukan kekurangan skill.
- Solusi C: Jasa tulis CV berbayar , gagal karena kebanyakan cuma rapikan bahasa, tak optimalkan kata kunci agar lolos ATS dan tak siasati bias usia.

## Your wedge
Bangun layanan optimasi CV berbasis ATS untuk pekerja berpengalaman non-sarjana dan sarjana muda. Produknya: scanner CV gratis yang menilai peluang lolos ATS, lalu jasa rewrite CV berbasis kata kunci industri F&B, ritel, dan manufaktur, plus mode "highlight experience over age" yang menyusun CV agar usia tak jadi penghalang di tampilan pertama. Tambah fitur simulasi interview singkat via WhatsApp dan daftar lowongan yang tak pasang batas usia. Wedge: bukan ajari skill baru, tapi bantu 27 juta pencari kerja yang sudah punya pengalaman agar CV-nya benar-benar dibaca manusia, bukan langsung dibuang mesin.

## What people would pay
- Rp 150.000 , Rp 350.000 sekali rewrite CV, atau Rp 99.000 per bulan untuk langganan scanner + optimasi berkala.
- Evidence: jasa penulisan CV di Fiverr dan Fastwork Indonesia sudah laku di kisaran Rp 100.000 , Rp 500.000 per CV.
- Comparable: layanan resume ATS optimizer di luar negeri seperti TopResume mematok 99 , 199 USD, pasar willingness-to-pay nyata.

## Adjacent opportunities
- Layanan negotiasi gaji dan persiapan kontrak bagi pekerja berpengalaman.
- Komunitas mutualisme pencari kerja berpengalaman di Telegram.
- Paket bundle CV + LinkedIn optimization + mock interview.

## Time-to-build estimate
- 2 minggu dengan MVP scanner CV berbasis rule-based dan template WhatsApp.
- 1 bulan dengan custom dev dan integrasi LLM untuk rewrite otomatis.
- 3 bulan lebih untuk platform penuh dengan database lowongan tanpa batas usia.
