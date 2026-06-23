# Dana QRIS Tertahan Berhari-hari hingga Berminggu-minggu, Modal UMKM Macet Total

**Date observed:** 2026-06-23
**Signal strength:** 5
**Category:** seller

**Sources (minimum 3):**
- [Keluhan Pengusaha UMKM: Dana QRIS Shopee Rp10 Juta Tertahan, Modal Saya Macet Total!](https://mediakonsumen.com/2026/02/01/surat-pembaca/keluhan-pengusaha-umkm-dana-qris-shopee-rp10-juta-tertahan-modal-saya-macet-total) , 2026-02-01 , Seorang pelaku UMKM kuliner di Jakarta Pusat mengadu dana QRIS Shopee Rp10 juta tertahan tanpa kejelasan meski SLA 1 hari kerja
- [Pembayaran Harian QRIS Grab Merchant Tertahan Sebulan Lebih Tanpa Kejelasan](https://mediakonsumen.com/2025/06/03/surat-pembaca/pembayaran-harian-qris-grab-merchant-tertahan-sebulan-lebih-tanpa-kejelasan) , 2025-06-03 , Merchant Grab mengeluhkan dana pembayaran harian QRIS tertahan hampir sebulan, sangat mengganggu kelancaran usaha
- [QRIS UMKM Bermasalah, Menteri Maman Jamin Tak Rugikan Pelaku Usaha?](https://www.liputan6.com/bisnis/read/5773859/qris-umkm-bermasalah-menteri-maman-jamin-tak-rugikan-pelaku-usaha) , 2024-11-07 , Liputan6 melaporkan puluhan ribu pelaku UMKM mengeluhkan layanan InterActive QRIS yang diberhentikan sementara, saldo tertahan lebih 10 hari
- [Dana Penjualan Rp7,6 Juta Tertahan 2 Bulan di GrabMerchant, Komplain 2 Kali Tak Digubris](https://mediakonsumen.com/2025/06/03/surat-pembaca/pembayaran-harian-qris-grab-merchant-tertahan-sebulan-lebih-tanpa-kejelasan) , 2025-06-03 , Merchant lain kehilangan akses dana Rp7,6 juta selama 2 bulan tanpa respons CS yang memadai
- [Melihat Aturan Biaya Admin QRIS](https://www.cnnindonesia.com/ekonomi/20260114131228-85-1187122/melihat-aturan-biaya-admin-qris) , 2026-01-14 , CNN Indonesia mengulas aturan MDR QRIS dan keluhan merchant tentang biaya layanan yang memberatkan

## The pain (verbatim quotes in Indonesian)

> "Saya menulis surat ini dengan perasaan sangat kecewa dan terdesak atas pelayanan Shopee (ShopeePay/Merchant) yang menahan hak saya sebagai penjual. Pada tanggal 28 Januari 2026, saya menerima pesanan besar sebanyak 500 boks makanan dengan total pembayaran Rp10.000.000 (sepuluh juta rupiah) yang dibayarkan pelanggan melalui QRIS Shopee. Berdasarkan aturan yang berlaku, dana tersebut seharusnya masuk ke rekening SeaBank saya dalam waktu satu hari kerja (SLA satu hari). Namun hingga 1 Februari 2026, dana Rp10.000.000 tersebut belum juga dicairkan ke rekening saya." , 2026-02-01 , Yordan, pelaku UMKM kuliner Jakarta Pusat, di Media Konsumen

> "Jika dana ini terus tertahan tanpa alasan yang jelas, usaha saya terancam berhenti beroperasi karena kekurangan modal." , 2026-02-01 , Yordan, pelaku UMKM kuliner Jakarta Pusat, di Media Konsumen

> "Saya sangat kecewa dengan pihak Grab, terkait sistem pembayaran harian QRIS yang tertahan hampir sebulan, sehingga sangat mengganggu kelancaran usaha UMKM saya." , 2025-06-03 , Merchant Grab, di Media Konsumen

> "Mengapa sistem Shopee justru mempersulit kami para pedagang kecil yang sudah jujur berjualan?" , 2026-02-01 , Yordan, pelaku UMKM Jakarta Pusat, di Media Konsumen

> "Biaya layanan shoppe merchant sangat mencekik, pelayanan penarikan juga buruk! lama lama bisa ditinggal merchant kalau berkelanjutan." , 2026-02-01 , Komentar pengguna JfoneStar di Media Konsumen

> "saya pernah mengalami hal yg sama dgn kasus kk, Saya nominal 8jtan. Kl di kasus saya karena memang itu orderan dr pelanggan yah saya buktikan. Dr foto orderan, trus bukti pengiriman dll Itupun dana tertahan ampir 2 mgg lebih🥲" , 2026-02-01 , Komentar pengguna Budi81 di Media Konsumen

## Evidence of volume

- 4+ laporan di Media Konsumen dalam 12 bulan terakhir tentang dana QRIS tertahan di Shopee dan Grab
- Puluhan ribu UMKM terdampak penghentian layanan InterActive QRIS (Liputan6, November 2024)
- Diskusi ramai di r/indotech dan r/indonesia tentang "flaw fatal di sistem QRIS"
- Banyak komentar di artikel Media Konsumen dari merchant yang mengalami kasus serupa
- Pemberitaan di CNN Indonesia, Liputan6, dan Kontan tentang keluhan MDR QRIS dan dana tertahan

## Existing solutions (and why they fail)

- Customer service platform (Shopee, Grab): merespon lambat, tidak memberikan estimasi waktu jelas, sering menutup laporan sepihak tanpa solusi
- Mediasi via Media Konsumen: efektif untuk kasus individual (terbukti Yordan akhirnya dicairkan setelah Media Konsumen membantu hard notice), tapi tidak scalable untuk puluhan ribu merchant
- Regulasi BI tentang QRIS: sudah ada aturan MDR dan SLA settlement, tapi penegakan masih lemah, platform sering abai
- Aduan ke Kementerian UMKM: Menteri Maman sudah turun tangan untuk kasus InterActive QRIS, tapi masalah sistemik masih berulang di platform lain

## Your wedge

Solusi berbasis platform monitoring dan pressure-as-a-service: dashboard yang memonitor settlement QRIS merchant secara real-time, mendeteksi jika dana melebihi SLA, dan secara otomatis mengirimkan pengaduan berjenjang (ke CS platform, ke Media Konsumen, ke Kementerian UMKM, ke OJK). Merchant mikro tidak punya waktu dan pengetahuan untuk mengejar hak mereka sendiri. Dengan sistem yang mengotomatiskan eskalasi dan memberikan transparansi status, merchant bisa mendapatkan dana mereka lebih cepat. Model bisnis bisa freemium untuk merchant individu atau langganan korporat untuk asosiasi UMKM.

Alternatif: payment aggregator untuk UMKM yang memberikan jaminan SLA settlement 1x24 jam dengan dana talangan jika platform telat mencairkan. Ambil fee kecil (0.1%) sebagai asuransi settlement.

## What people would pay

- Saat ini merchant membayar MDR 0.3%-0.7% per transaksi QRIS. Untuk jaminan settlement cepat, merchant mikro bersedia membayar 0.1-0.3% tambahan
- Untuk layanan monitoring dan eskalasi: Rp50.000-100.000/bulan untuk mikro, Rp200.000-500.000/bulan untuk UKM menengah
- Evidence: merchant di Media Konsumen jelas menunjukkan keputusasaan dan willingness to pay untuk mendapatkan dana mereka kembali. Modal Rp10 juta yang tertahan bisa membunuh bisnis mikro
- Perbandingan: jasa penagihan/pengacara untuk sengketa platform digital saat ini Rp500.000-2.000.000 per kasus. Otomatisasi bisa turunkan biaya 90%

## Adjacent opportunities

- Layanan serupa untuk marketplace (Shopee, Tokopedia payout disputes) - masalah payout tertahan juga sering terjadi
- Asurasi settlement untuk agregator pembayaran UMKM lainnya (GoPay, OVO, DANA)
- Platform rating transparansi settlement untuk merchant - "Yelp untuk kecepatan payout platform"
- Konsultasi dan pendampingan hukum untuk merchant yang didenda atau diblokir platform sepihak
- Pelatihan literasi digital merchant tentang cara mengamankan hak mereka di ekosistem pembayaran digital

## Time-to-build estimate

- 2 minggu: Bot monitoring sederhana yang scrape status payout dan kirim notifikasi via WhatsApp. Bisa buat MVP menggunakan no-code (Zapier + Google Sheets + Twilio)
- 1 bulan: Dashboard web dengan integrasi API ke platform pembayaran (Shopee, Gojek, Grab) + sistem eskalasi otomatis
- 3+ bulan: Full platform dengan payment aggregation, dana talangan settlement, asuransi, dan legal support
