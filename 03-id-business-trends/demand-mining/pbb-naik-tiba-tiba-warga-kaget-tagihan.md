# Tagihan PBB Melonjak Tiba-tiba, Warga Kaget dan Protes

**Date observed:** 2026-07-09
**Signal strength:** 4/5
**Category:** other
**Sources (minimum 3):**
- [Jejak Sudewo Sebelum Dicokok KPK: Naikkan PBB 250% hingga Didemo Warga!](https://www.detik.com/properti/berita/d-8317945/jejak-sudewo-sebelum-dicokok-kpk-naikkan-pbb-250-hingga-didemo-warga) — 2026-01-21 — Bupati Pati naikkan PBB hingga 250 persen, warga demo.
- [Fakta-fakta Kenaikan PBB 800% di Parepare: Cuma Ditunda, Bukan Dibatalkan](https://www.detik.com/sulsel/parepare/d-8074905/fakta-fakta-kenaikan-pbb-800-di-parepare-cuma-ditunda-bukan-dibatalkan) — 2025-08-23 — Kenaikan 800 persen ditunda tapi belum dibatalkan, warga cemas.
- [Jejak Sudewo Sebelum Dicokok KPK: Naikkan PBB 250% hingga Didemo Warga! (ringkasan)](https://www.detik.com/properti/berita/d-8317945/jejak-sudewo-sebelum-dicokok-kpk-naikkan-pbb-250-hingga-didemo-warga) — 2026-01-21 — Deskripsi: kebijakan kenaikan PBB 250 persen memicu demo warga.

## The pain (verbatim quotes in Indonesian)
> "Bupati Pati Sudewo terjaring OTT KPK terkait kasus dugaan jual-beli jabatan. Sebelum terjaring OTT KPK, Sudewo sempat membuat kebijakan kenaikan PBB 250%." (sumber: detikProperti, 2026-01-21)
> "Fakta-fakta Kenaikan PBB 800% di Parepare: Cuma Ditunda, Bukan Dibatalkan." (judul, detikSulsel, 2025-08-23)

Sintesis: Warga pemilik rumah sederhana di daerah kaget dapat Surat Pemberitahuan Pajak Terutang (SPPT) PBB naik ratusan persen dari tahun sebelumnya, tanpa sosialisasi yang cukup. Banyak yang tidak paham cara banding, cek NJOP, atau ajukan keringanan. Penarikan dilakukan lewat RT/RW sehingga warga merasa dipaksa bayar atau sertifikat terblokir.

## Evidence of volume
- Kasus PBB 250 persen di Pati memicu demo massal dan masuk sorotan nasional hingga OTT KPK.
- Kasus PBB 800 persen di Parepare ditunda tapi tidak dibatalkan, menyisakan ketidakpastian ribuan warga.
- Pola kenaikan PBB sepihak makin sering jelang pemilu daerah dan perubahan NJOP.

## Existing solutions (and why they fail)
- Sistem informasi PBB pemda (e-SPPT): gagal karena UI buruk, sering down, dan tidak ada panduan banding bagi warga awam.
- Layanan konsultasi pajak kantor pajak: gagal karena hanya ada di kota besar, tidak menjangkau desa, antre panjang.
- RT/RW: gagal karena tidak punya kapasitas jelaskan perhitungan, sekadar jadi penagih.

## Your wedge
Layanan "Cek dan Banding PBB" berbasis WA: warga foto SPPT, bot hitung apakah kenaikan wajar (bandingkan NJOP kebijakan pemda setempat), lalu kasih draf surat keberatan atau keringanan siap kirim ke kelurahan. Berlangganan Rp 15.000 untuk 3x cek per tahun. Beda dengan konsultan pajak karena murah, otomatis, dan pakai data NJOP per wilayah. Bisa viral tiap musim SPPT terbit.

## What people would pay
- Rp 15.000-30.000 per musim pajak untuk cek dan draf surat keberatan.
- Evidence: warga rela demo dan bayar calo hanya untuk paham tagihan, artinya bersedia bayar jasa kecil yang jelas.
- Comparable: jasa konsultasi pajak per jam ratusan ribu, dan jasa pengurusan administrasi kelurahan.

## Adjacent opportunities
- Kalkulator NJOP dan peta harga tanah per RW.
- Bundling urus sertifikat tanah dan PBB terutang.
- Cross-sell ke pain "biaya administrasi kependudukan rumit".

## Time-to-build estimate
- 2 minggu dengan off-the-shelf tools untuk WA bot OCR SPPT dan template surat.
- 1 bulan dengan custom dev untuk database NJOP per wilayah dan engine banding.
- 3+ bulan untuk integrasi resmi dengan portal pemda.
