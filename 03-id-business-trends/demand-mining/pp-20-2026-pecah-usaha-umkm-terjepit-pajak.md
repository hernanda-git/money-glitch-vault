# PP 20/2026: UMKM Terjepit, Praktik Pecah Usaha Dibongkar DJP

**Date observed:** 2026-06-29
**Signal strength:** 5/5
**Category:** umkm
**Sources (minimum 3):**
- [DJP Bongkar Modus Pecah Usaha demi Nikmati Pajak UMKM 0,5 Persen](https://money.kompas.com/read/2026/06/25/110203126/djp-bongkar-modus-pecah-usaha-demi-nikmati-pajak-umkm-05-persen) — 2026-06-25 — DJP temukan 14 wajib pajak miliki lebih dari 50 PT/CV untuk hindari pajak
- [DJP Ungkap Modus Pecah Usaha Demi Tarif Pajak UMKM 0,5 Persen](https://m.antaranews.com/amp/berita/5621917/djp-ungkap-modus-pecah-usaha-demi-tarif-pajak-umkm-05-persen) — 2026-06-24 — Antara laporkan temuan DJP soal pemecahan usaha
- [PP 20/2026 Tutup Celah Pecah Usaha untuk Pertahankan Tarif Pajak UMKM](https://ikpi.or.id/en/pp-20-2026-tutup-celah-pecah-usaha-untuk-pertahankan-tarif-pajak-umkm/) — 2026-06-01 — Ikatan Konsultan Pajak Indonesia jelaskan dampak PP baru

## The pain (verbatim quotes in Indonesian)
> "Bayangkan, satu orang pribadi memiliki sampai lebih dari 50 PT atau CV." — Inge Diana Rismawanti, Direktur P2Humas DJP (Kompas, 25 Juni 2026)
> "Begitu PT itu daftar, omzetnya naik. Begitu di tahun ketiga mulai omzetnya turun. Kemudian muncul lagi PT baru. Begitu juga dengan CV." — Inge Diana Rismawanti, DJP (Kompas, 25 Juni 2026)
> "Kenapa mereka tidak bangga naik kelas. Kan harusnya mereka bangga naik kelas. Mungkin nanti bisa naik omzet lebih besar lagi, bukan jadi mikro atau kecil lagi." — Inge Diana Rismawanti, DJP (Kompas, 25 Juni 2026)

## Evidence of volume
- 14 wajib pajak orang pribadi tercatat memiliki lebih dari 50 PT atau CV (data DJP, Juni 2026)
- Sekitar 45 wajib pajak lainnya memiliki antara 26 hingga 50 badan usaha
- Pola omzet turun saat mendekati batas Rp4,8 miliar ditemukan secara konsisten pada ribuan entitas
- PP 20/2026 dikeluarkan sebagai respons langsung terhadap skala praktik ini
- Berita ini menjadi headline di Kompas, Antara, dan berbagai media pajak nasional

## Existing solutions (and why they fail)
- PPh Final 0,5% untuk UMKM: gagal karena UMKM yang sudah besar justru memecah usaha agar tetap di bawah batas Rp4,8 miliar, bukan untuk membantu yang benar-benar kecil
- Coretax DJP: gagal menangkap pola pecah usaha karena sebelumnya hanya melihat per entitas, bukan substansi ekonomi
- Insentif pajak UMKM lainnya: gagal karena tidak ada mekanisme penggabungan omzet antar entitas terkait

## Your wedge
Buat tool otomatis yang bisa mendeteksi pola pecah usaha bagi UMKM dan konsultan pajak. Tool ini bisa: (1) memantau pertumbuhan omzet lintas entitas yang dimiliki satu orang, (2) memberikan peringatan dini saat pola "omzet naik lalu turun, entitas baru muncul" terdeteksi, dan (3) menghitung skor risiko audit untuk setiap portofolio usaha. Konsultan pajak butuh tool ini untuk melindungi klien mereka dari risiko sanksi DJP, sementara UMKM sendiri butuh edukasi agar tidak terjebak praktik yang sekarang bisa kena sanksi berat.

## What people would pay
- Rp200.000-500.000/bulan untuk konsultan pajak yang mengelola puluhan klien UMKM
- Rp50.000-100.000/bulan untuk UMKM individu yang ingin memantau risiko pajak
- Bukti willingnes-to-pay: konsultan pajak sudah bayar Rp500.000-2.000.000/bulan untuk software akuntansi seperti Jurnal atau Accurate, pasti mau bayar tambahan untuk fitur deteksi risiko pajak
- Harga konsultan pajak berkisar Rp1-5 juta per klien per tahun, tool ini bisa jadi value-add yang justifies harga

## Adjacent opportunities
- Dashboard compliance pajak UMKM real-time yang terintegrasi dengan DJP
- Edukasi tentang PP 20/2026 melalui video pendek untuk creator konten pajak
- Bundling dengan layanan pembuatan NIB dan registrasi usaha
- Cross-sell ke asosiasi UMKM dan koperasi yang butuh edukasi regulasi baru

## Time-to-build estimate
- 2 minggu dengan off-the-shelf tools (dashboard sederhana + integrasi API DJP jika tersedia)
- 1 bulan dengan custom dev (deteksi pola + scoring risiko)
- 3+ bulan untuk full product dengan integrasi Coretax dan fitur prediktif
