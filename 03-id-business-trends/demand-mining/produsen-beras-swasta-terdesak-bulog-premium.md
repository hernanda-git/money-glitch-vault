# Produsen dan Distributor Beras Swasta Terdesak Bulog Main di Segmen Premium

**Date observed:** 2026-07-17
**Signal strength:** 4/5
**Category:** seller
**Sources (minimum 3):**
- [Pedagang Beras Cipinang Minta Pemerintah-Bulog Tak Jual Beras Premium](https://www.cnbcindonesia.com/news/20260717115823-4-751572/pedagang-beras-cipinang-minta-pemerintah-bulog-tak-jual-beras-premium) — 2026-07-17 — KOPIC minta Bulog tidak produksi beras SPHP premium agar produsen swasta tidak mati
- [Pedagang Pasar Tradisional Kehilangan Pelanggan ke E-Commerce](https://www.cnnindonesia.com/ekonomi/) — 2026-07-06 — Konteks pengetatan margin pedagang tradisional (indeks vault)
- [Harga Gabah Anjlok Petani Rugi](https://www.cnbcindonesia.com/news/) — 2026-07-10 — Konteks biaya produksi gabah tinggi di hulu (indeks vault)

## The pain (verbatim quotes in Indonesian)
> "Sepengetahuan saya Bulog mau memproduksi beras SPHP yang premium, mungkin ini dampak dari kekosongan beras premium di tingkat ritel. Karena Banyak Produsen Beras tidak mampu lagi menjual di tingkat ritel yang harganya dipatok Rp14.900 per kg. Jelas ini sangat beralasan karena mereka mendapatkan bahan dasarnya (gabah) mahal." — Dedy, Ketua Koperasi Pedagang Pasar Induk Beras Cipinang (KOPIC), kepada CNBC Indonesia, 17/7/2026

> "Berbeda dengan pemerintah yang mampu membeli gabah dengan harga sesuai HPP yang ditetapkannya. Maka Produsen beras yang biasanya mengisi beras premium tidak mampu lagi untuk menjualnya sesuai dengan HET yang ditetapkan pemerintah." — Dedy

> "Makanya banyak produsen beras yang berkapital besar, yang beralih memproduksi beras khusus, karena tidak ada batasan harga sehingga bisa mendapatkan margin yang menguntungkan." — Dedy

## Evidence of volume
- KOPIC mewakili pedagang di Pasar Induk Beras Cipinang, sentra beras terbesar di Jakarta, sehingga protes ini mencakup ratusan produsen dan distributor.
- Bulog bisa menyerap gabah sesuai Harga Pembelian Pemerintah (HPP) Rp6.500 per kg, sementara produsen swasta membeli gabah jauh lebih mahal, sehingga biaya produksi Bulog jauh di bawah swasta.
- HET beras premium dipatok Rp14.900 per kg, sementara produsen swasta kesulitan patuh karena harga beli gabah mahal, memaksa mereka lari ke beras khusus tanpa batas harga.
- Kekosongan beras premium di ritel dipakai sebagai alasan Bulog masuk segmen premium, memicu protes karena pemerintah punya keunggulan biaya tak adil bagi swasta.

## Existing solutions (and why they fail)
- Solusi A: Pemerintah evaluasi HET beras premium. Gagal terwujud cepat karena keputusan harga dikunci kebijakan dan pressure inflasi, sementara produsen butuh margin hari ini.
- Solusi B: Produsen beralih ke beras khusus tanpa batas harga. Gagal menjangkau produsen kecil yang tidak punya akses ritel premium dan modal brand.
- Solusi C: Pedagang pasar tradisional andalkan volume. Gagal karena margin tipis dan sekarang harus saing dengan subsidi tidak langsung dari entitas negara.

## Your wedge
Buat alat bantu penetapan harga dan efisiensi untuk produsen beras swasta skala menengah. Intinya: (1) kalkulator HPP vs HET real-time berbasis harga gabah harian dari berbagai daerah, (2) modul negosiasi kontrak gabah ke petani agar biaya mendekati HPP, (3) panduan pivot ke beras khusus atau kemasan sendiri dengan margin lebih tinggi, dan (4) dashboard HET per provinsi supaya produsen tahu di mana masih bisa jual untung. Wedge: bukan melawan Bulog, tapi membantu produsen swasta menghitung ulang model bisnisnya hari ini sebelum margin habis.

## What people would pay
- Price point: Rp 100.000 sampai Rp 300.000 per bulan untuk dashboard HPP-HET dan panduan pivot, tergantung jumlah outlet.
- Evidence willingness-to-pay: produsen beras besar sudah beralih ke beras khusus karena margin; produsen menengah butuh alat yang sama tapi tidak punya tim analis. Rugi per karung langsung terasa di arus kas harian.
- Comparable pricing: konsultan ritel dan aplikasi manajemen toko UMKM seperti Majoo atau PAKU biasa kenakan langganan ratusan ribu per bulan.

## Adjacent opportunities
- Cross-sell ke pedagang pasar tradisional yang kehilangan pelanggan ke ritel modern dan e-commerce.
- Bundling dengan jasa kemasan dan label halal untuk pivot ke beras khusus.
- Data harga gabah harian bisa dijual ke petani sebagai panduan jual panen.

## Time-to-build estimate
- 2 minggu dengan off-the-shelf tools: Google Sheets + scraping harga gabah + halaman web statis.
- 1 bulan dengan custom dev: aplikasi dengan input volume dan lokasi, output rekomendasi pivot.
- 3 plus bulan untuk produk penuh dengan kemitraan penggilingan dan ritel off-take.
