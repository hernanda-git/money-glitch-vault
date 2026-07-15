# Aturan Baru E-Commerce 1 Juli 2026: Seller Kena PPh, Wajib NIB, dan Biaya Harus Transparan

**Date observed:** 2026-07-16
**Signal strength:** 5/5
**Category:** seller
**Sources (minimum 3):**
- [Daftar Aturan Baru yang Berlaku di Shopee, TikTok Shop Cs per 1 Juli 2026](https://teknologi.bisnis.com/read/20260701/84/1984584/daftar-aturan-baru-yang-berlaku-di-shopee-tiktok-shop-cs-per-1-juli-2026) — 2026-07-01 — marketplace, social commerce, dan pedagang digital diikat aturan baru Permendag 19/2026 dan aturan Menkeu.
- [Aturan Baru Ecommerce Berlaku di TikTok-Shopee Mulai 1 Juli](https://www.cnbcindonesia.com/tech/20260703145218-37-747866/aturan-baru-ecommerce-berlaku-di-tiktok-shopee-mulai-1-juli) — 2026-07-03 — seller kena pemungutan PPh, wajib NIB, larangan perang harga, dan kewajiban transparansi biaya komisi/admin.
- [Seller TikTok Shop yang Tidak Adaptasi Bisa Kehilangan Akses Jualan](https://desakarangbendo.id/berita-ekonomi-bisnis/4012282452/tiktok-shop-resmi-ubah-7-aturan-di-2026-seller-yang-tidak-adaptasi-bisa-kehilangan-akses-jualan/) — 2026-07 — 7 aturan TikTok Shop yang kalau tidak dipatuhi seller bisa kehilangan akses.

## The pain (verbatim quotes in Indonesian)
> "Shopee, TikTok Shop, Tokopedia, Lazada, dan Blibli. Kebijakan tersebut langsung dikenakan kepada platform. Diantaranya aturan operasional melalui Permendag No.19." (Bisnis.com, 1 Juli 2026)
> "Marketplace diwajibkan memungut Pajak Penghasilan pedagang dalam negeri yang ada di dalam platform." (CNBC Indonesia, 3 Juli 2026)
> "Aturan baru juga melarang adanya tindakan perang harga dalam aplikasi. Selain itu meminta adanya transparansi biaya yang dipungut kepada pelaku usaha, misalnya besaran biaya admin, pembagian komisi dan potongan pada layanan lain." (CNBC Indonesia, 3 Juli 2026)

Catatan: omzet di bawah Rp500 juta setahun tidak dikenakan PPh final, tapi seller tetap harus punya NIB dan sadar komisi/admin yang sekarang wajib transparan. Quotes di atas kutipan langsung dari berita.

## Evidence of volume
- Aturan berlaku nasional per 1 Juli 2026 ke seluruh platform besar (Shopee, TikTok Shop, Tokopedia, Lazada, Blibli), sehingga menyentuh jutaan seller.
- CNBC mencatat seller diwajibkan punya NIB (Permendag 19/2026) atau platform bisa menolak pendaftaran, kaitan erat dengan file umkm-belum-punya-nib-oss-sulit yang sudah ada.
- TikTok Shop mengubah 7 aturan sekaligus, seller yang tidak adaptasi terancam kehilangan akses jualan.

## Existing solutions (and why they fail)
- Pusat bantuan platform: gagal karena bahasanya legalistik dan tidak translate dampak ke untung-rugi per produk.
- Konsultan perizinan: gagal karena lambat dan mahal untuk seller mikro yang cuma butuh NIB cepat sebelum akun dibekukan.
- Spreadsheet manual: gagal karena seller tidak tahu rumus komisi, admin, PPh, dan potongan lain yang sekarang wajib transparan.

## Your wedge
Buat kalkulator "bersih per produk" khusus seller e-commerce Indonesia: input harga jual, kategori, dan platform, maka keluar rincian komisi, biaya admin, PPh (kalau omzet di atas Rp500 juta), dan margin bersih setelah aturan 1 Juli 2026. Tambah modul pengecekan NIB dan alert kalau akun terancam karena belum NIB. Ini menjawab kebingungan transparansi biaya yang justru kini wajib dari platform tapi seller sendiri tidak punya alat hitungnya. Jalan dengan spreadsheet engine + data komisi per platform, tanpa ML berat.

## What people would pay
- Rp29.000 sampai Rp59.000 per bulan untuk akses kalkulator + cek NIB + alert aturan.
- Bukti willingness to pay: seller marketplace sudah bayar tools seperti Shopee/Seller center tambahan, dan惊 panik kehilangan akses jualan membuat mereka rela bayar sedikit untuk aman.
- Pembanding: jasa pembuatan NIB lewat pihak ketiga rata-rata Rp150.000 sekali buat.

## Adjacent opportunities
- Cross-sell dengan file tiktok-shop-akun-dibekukan-saldo-tertahan dan tiktok-shop-seller-nib-komisi-menjerit yang sudah ada.
- Bundling cek NIB dengan panduan PPh final 0,5% (lihat file pph-final-umkm-terbatas-pt-perorangan).
- Modul peringatan dini aturan platform (TikTok 7 aturan, Shopee policy) agar seller tidak kena suspend.

## Time-to-build estimate
- 2 minggu dengan tools off-the-shelf (kalkulator + crawler perubahan kebijakan platform + form NIB).
- 1 bulan kalau mau integrasi API ke masing-masing seller center.
