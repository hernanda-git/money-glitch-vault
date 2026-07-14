# Seller Marketplace Rugi Akibat Retur Fiktif dan Beban Biaya Retur COD

**Date observed:** 2026-07-14
**Signal strength:** 5
**Category:** seller
**Sources (minimum 3):**
- [Rugi Besar di Balik COD: Fakta Mengejutkan Retur Barang di E-Commerce Indonesia](https://jambisun.id/skandal-cod-ecommerce-2026-seller-rugi-retur-tiktok-shopee/) — 2026 — Seller rugi puluhan hingga ratusan juta akibat retur COD tidak transparan
- [Beda Kebijakan Shopee dan TikTok Shop soal Biaya Retur Seller](https://teknologi.bisnis.com/read/20260414/84/1966421/beda-kebijakan-shopee-dan-tiktok-shop-soal-biaya-retur-seller) — 2026-04-14 — TikTok Shop mulai 1 Juni 2026 bebankan biaya retur ke seller maksimal Rp10.000 per transaksi
- [TikTok Shop bebankan biaya pengiriman gagal dan retur ke seller per 1 Juni 2026](https://www.msn.com/id-id/ekonomi/umum/tiktok-shop-bebankan-biaya-pengiriman-gagal-dan-retur-ke-seller-per-1-juni-2026/ar-AA24ryJw) — 2026-06-01 — Aturan baru bebankan ongkir gagal dan retur ke penjual
- [Qoo10: COD e-commerce kacau, seller Shopee dan TikTok Shop menanggung rugi tiap retur](https://www.qoo10.co.id/sains/337454/cod-e-commerce-kacau-seller-shopee-dan-tiktok-shop-menanggung-rugi-setiap-retur/) — 2026 — Analisis beban rugi seller per retur

## The pain (verbatim quotes in Indonesian)
> "Sistem COD e-commerce Indonesia kembali menuai sorotan. Para seller dari berbagai platform seperti TikTok Shop, Shopee, dan Lazada mengaku mengalami kerugian besar akibat mekanisme retur barang yang dinilai tidak transparan." — jambisun.id, 2026

> "Ega, seorang seller aksesoris, mengungkapkan bahwa sistem sering mencatat alasan retur seperti 'pembeli menolak paket' atau 'alamat tidak jelas'. Namun kenyataannya, informasi tersebut kerap berbeda dengan pengakuan pembeli." — jambisun.id, 2026

> "Sejumlah pelaku usaha mengaku kerugian akibat retur COD mencapai puluhan hingga ratusan juta rupiah." — jambisun.id, 2026

> "Lemahnya sistem verifikasi membuat pembeli bisa dengan mudah membatalkan pesanan tanpa konsekuensi. Hal ini memperparah kerugian karena seller sudah mengeluarkan biaya operasional sejak awal." — jambisun.id, 2026

## Evidence of volume
- TikTok Shop resmi membebankan biaya retur ke seller per 1 Juni 2026 (maksimal Rp10.000 per transaksi), sinyal perubahan kebijakan yang memberatkan penjual
- Seller aksesoris tunggal (Ega) melaporkan ketidakcocokan data antara laporan pembeli dan ekspedisi, kerugian puluhan hingga ratusan juta
- Banyak artikel 2026 membahas "COD kacau" dan "retur fiktif", menunjukkan topik sedang naik daun di kalangan seller
- Komplain seller di forum Shopee University dan TikTok Seller Center tentang retur barang cacat/salah yang sebenarnya bukan salah seller

## Existing solutions (and why they fail)
- Seller Center / Pusat Edukasi platform (Shopee, TikTok): hanya berisi SOP, tidak membantu memverifikasi keabsahan retur secara independen
- Asuransi kiriman ekspedisi: mahal dan tidak mencakup retur COD yang diklaim "pembeli menolak"
- Komunitas seller di media sosial: berbagi tips tapi tidak ada alat otomatis untuk bukti dan dispute

## Your wedge
Buat alat "ReturGuard" untuk seller: ekstrak data pesanan, cocokkan alasan retur dari platform dengan bukti foto/video pengiriman dan chat pembeli, lalu hasilkan draf banding (appeal) otomatis ke tim dispute platform. Fitur deteksi pola: flag pembeli yang sering retur fiktif. Ini mengubah proses banding manual yang lama jadi satu klik. Untuk COD, tambah modul pelacakan status paket via API ekspedisi agar seller punya bukti objektif saat paket "ditolak".

## What people would pay
- Langganan SaaS per toko: Rp50.000 sampai Rp150.000 per bulan tergantung volume order
- Jasa banding per kasus untuk seller yang malas pakai tools: Rp15.000 sampai Rp30.000 per dispute
- Bukti willingness-to-pay: seller sudah bayar agensi ads dan tools analitik; kerugian retur langsung potong laba sehingga mereka rela bayar untuk selamatkan margin
- Pembanding: tools analitik marketplace (LikeData, Sangfor) berlangganan ratusan ribu per bulan

## Adjacent opportunities
- Modul verifikasi foto otomatis untuk bukti kondisi barang saat dikirim
- Cross-sell dengan layanan "Cek Saldo Hilang" e-wallet untuk seller yang dananya stuck
- Dashboard net margin riil setelah potong komisi, ongkir, dan retur (sudah ada draft di inbox)

## Time-to-build estimate
- 2 minggu dengan off-the-shelf tools: Google Sheets + Apps Script + notifikasi WA untuk draf banding
- 1 bulan dengan custom dev: scraping order + OCR bukti foto + pelacakan API ekspedisi
- 3+ bulan untuk produk penuh dengan ML deteksi pola pembeli nakal lintas platform
