# BPJS PBI Mendadak Nonaktif, Warga Miskin Kehilangan Jaminan Kesehatan Gratis

**Date observed:** 2026-07-16
**Signal strength:** 5
**Category:** other
**Sources (minimum 3):**
- [164 Ribu Warga Dicoret dari PBI JK, Sekda Sukabumi: Ini soal Nyawa](https://www.detik.com/jabar/berita/d-8444758/164-ribu-warga-dicoret-dari-pbi-jk-sekda-sukabumi-ini-soal-nyawa) — 2026-04-15 — 164 ribu warga Sukabumi dinonaktifkan per Januari 2026
- [Dirut BPJS Buka Suara Usai Ramai Status PBI JK Warga Mendadak Nonaktif](https://news.detik.com/berita/d-8343050/dirut-bpjs-buka-suara-usai-ramai-status-pbi-jk-warga-mendadak-nonaktif) — 2026-02-06 — Dirut BPJS konfirmasi puluhan ribu peserta mendadak dinonaktifkan
- [DPRD Minta Rumah Sakit Tak Tolak Pasien PBI BPJS yang Dinonaktifkan](https://www.detik.com/jatim/berita/d-8356380/dprd-minta-rumah-sakit-tak-tolak-pasien-pbi-bpjs-yang-dinonaktifkan) — 2026-02-14 — 9.920 warga Malang dinonaktifkan, RS diminta jangan tolak
- [164 Ribu Warga Sukabumi Kehilangan PBI BPJS, Bupati Buka Suara](https://www.detik.com/jabar/berita/d-8355087/164-ribu-warga-sukabumi-kehilangan-pbi-bpjs-bupati-buka-suara) — 2026-02-13 — bupati konfirmasi warga kehilangan akses

## The pain (verbatim quotes in Indonesian)
> "Sebanyak 164 ribu warga Kabupaten Sukabumi mendadak dinonaktifkan dari kepesertaan Penerima Bantuan Iuran Jaminan Kesehatan (PBI JK) oleh Kemensos per Januari 2026."
> "Tahukah Anda beberapa orang yang biasa PBI tiba-tiba dinonaktifkan?" (Dirut BPJS Kesehatan, Ali Ghufron Mukti)
> "Sebetulnya BPJS bukan yang mengaktifkan atau nonaktifkan sebagai PBI." (Ali Ghufron Mukti, 6/2/2026)
> "Ribuan Penerima Bantuan Iuran (PBI) BPJS Kesehatan di Kota Malang dinonaktifkan per 1 Februari 2026." (ada 9.920 warga Malang dinonaktifkan)
> "DPRD Kota Malang meminta rumah sakit tak menolak mereka ketika membutuhkan layanan kesehatan." (Proses transisi pemutakhiran data SK Mensos No.3/HUK/2026)

Catatan: penonaktifan massal ini dampak dari pembaruan data nasional (SK Mensos No.3/HUK/2026, berlaku 1 Feb 2026). Warga miskin yang selama ini gratis berobat mendadak harus bayar sendiri atau ditolak RS karena status "nonaktif", padahal mereka tetap miskin. Kepala daerah menyebut ini "soal nyawa".

## Evidence of volume
- 164.000 warga Kabupaten Sukabumi dinonaktifkan per Januari 2026.
- 9.920 warga Kota Malang dinonaktifkan per 1 Februari 2026 (data BPJS Cabang Malang).
- Skala nasional: ramai "PBI JK Mendadak Nonaktif" sampai Komisi IX DPR akan memanggil Menkes dan BPJS.
- Bupati/Walikota di banyak daerah terpaksa siapkan anggaran darurat (Pemkot Malang Rp 170 miliar untuk BPJS 2026) demi reaktivasi warganya.

## Existing solutions (and why they fail)
- Aduan ke Dinsos / lagu groundcheck: lambat, butuh datang fisik, warga sakit tidak sanggup antre.
- Surat keterangan tidak mampu (SKTM): birokrasi panjang, sering ditolak RS saat status PBI belum aktif.
- Pindah ke PBPU (bayar sendiri): mustahil bagi warga miskin yang diblokir akses gratis.
- Hotline BPJS 165: sulit tersambung saat lonjakan keluhan massal.

## Your wedge
Bangun layanan "PBI guard" berbasis WA: warga cek status PBI cukup kirim NIK, bot cek via API Mobile JKN / web resmi, dan jika nonaktif bot pandu langkah reaktivasi (buat SKTM digital, arahkan ke Dinsos terdekat, template pengaduan ke DPRD). Versi B2G: dashboard untuk kelurahan memantau warganya yang PBI nonaktif agar bisa langsung diselamatkan sebelum sakit. Bedanya dari solusi existing: proaktif (notifikasi sebelum warga butuh berobat) dan bahasa lokal sederhana.

## What people would pay
- Gratis untuk warga (disubsidi pemda / CSR), B2G Rp 5-15jt per kelurahan per bulan untuk dashboard monitoring.
- Evidence willingness-to-pay: pemda sudah siapkan ratusan miliar (Malang Rp 170 M) untuk selamatkan PBI, artinya anggaran tersedia untuk alat pencegah murah.
- Comparable: konsultan administrasi bantuan sosial, jasa pengurusan BPJS mandiri (Rp 50-150rb per kasus di marketplace).

## Adjacent opportunities
- Cross-sell ke pain "warga miskin terblokir layanan gratis status desil salah" (sudah ada di vault) jadi satu suite verifikasi status sosial.
- Bundling asuransi mikro murah untuk warga PBI yang ditolak RS saat transisi.
- Edukasi digital "cek BPJS gratis tiap bulan" untuk lansia dan ibu rumah tangga.
- Integrasi dengan posyandu / kader dasawisma untuk deteksi dini.

## Time-to-build estimate
- 2 minggu dengan off-the-shelf tools: bot WA + cek NIK + template aduan (Twilio/WATI + Google Sheets).
- 1 bulan dengan custom dev: integrasi API Mobile JKN + dashboard kelurahan + notifikasi proaktif.
- 3+ bulan untuk produk penuh dengan MoU resmi Kemensos / BPJS Kesehatan.
