# Langganan Streaming Mahal, Generasi Muda RI Kepekik Harga Naik Beruntun

**Date observed:** 2026-07-16
**Signal strength:** 4
**Category:** other
**Sources (minimum 3):**
- [Batal Kena PPN 12%, Segini Harga Langganan Netflix hingga Spotify](https://www.detik.com/jatim/bisnis/d-7714354/batal-kena-ppn-12-segini-harga-langganan-netflix-hingga-spotify) — 2025-01-02 — Spotify dan Netflix rekam kenaikan tarif beruntun
- [Netflix Naikkan Harga Langganan di Beberapa Negara, Indonesia Kena?](https://www.detik.com/pop/movie/d-7747768/netflix-naikkan-harga-langganan-di-beberapa-negara-indonesia-kena) — 2025-01-24 — Netflix naikkan harga, Indonesia disorot
- [Duh! Harga Langganan YouTube Premium Naik Lagi](https://inet.detik.com/cyberlife/d-8439891/duh-harga-langganan-youtube-premium-naik-lagi) — 2026-04-13 — YouTube Premium naik ke Rp 273rb/bulan setara USD
- [Netflix Bakal Naikkan Harga Langganan 5 Tahun Berturut-turut](https://inet.detik.com/cyberlife/d-7895600/netflix-bakal-naikkan-harga-langganan-5-tahun-berturut-turut) — 2025-07 — tren kenaikan Netflix global beruntun

## The pain (verbatim quotes in Indonesian)
> "Netflix hingga Spotify yang tadinya diwacanakan kena PPN 12% ternyata batal dikenai PPN." (Detik, Jan 2025)
> "Paket individu YouTube Premium kini dibanderol seharga USD 15,99 atau sekitar Rp 273 ribu per bulan." (Detik, Apr 2026)
> "Kenaikan harga ini berlaku untuk berbagai tipe paket, mulai dari akun individu hingga keluarga." (Detik, Apr 2026 tentang YouTube Premium)
> "Harga Langganan Spotify Naik Lagi di 2026, Warga RI Siap-siap." (judul CNBC Indonesia, Jan 2026)

Catatan: meski wacana PPN 12% untuk Netflix/Spotify batal pada 2025, harga langganan terus naik sendiri setiap tahun. Gen Z dan keluarga dengan beberapa subscription (Netflix, Spotify, YouTube Premium, Disney+, dll) merasa tercekik karena tidak ada cara mudah memantau atau mengoptimalkan pengeluaran langganan.

## Evidence of volume
- Detik (Jan 2025): Netflix dan Spotify masuk daftar layanan yang rekam kenaikan tarif, "batal kena PPN 12%" tapi harga naik sendiri.
- Detik (Jan 2025): Netflix naikkan harga langganan di beberapa negara, Indonesia disorot apakah kena.
- Detik (Apr 2026): YouTube Premium naik ke setara Rp 273rb/bulan, naik USD 2 dari sebelumnya.
- Detik (Jul 2025): Netflix diproyeksikan naikkan harga 5 tahun berturut-turut.
- Detik (Jan 2025): Netflix, Spotify, YouTube Premium semua masuk daftar imbas kenaikan PPN 12% (lalu batal, tapi harga naik sendiri).

## Existing solutions (and why they fail)
- Fitur "Kelola langganan" di masing-masing app: tersebar, tidak ada dashboard gabungan, user lupa mematikan trial.
- Spreadsheet manual: ribet, tidak auto-detect charge dan renewal.
- Password sharing (akun keluarga): makin ditindak tegas oleh Netflix/Spotify, risiko akun dibanned.
- VPN ke negara murah: melanggar ToS, sering keblokir, tidak praktis untuk non-teknis.

## Your wedge
Buat "subscription optimizer" untuk pasar Indonesia: dashboard yang menghubungkan email/PDF tagihan (atau OAuth ke Google Play / App Store) lalu mendeteksi semua langganan aktif, total burn per bulan, tanggal renewal, dan memberi alert "langganan naik harga" plus rekomendasi plan termurah (misal ganti ke plan keluarai vs individu, atau pindah region legal). Versi freemium: gratis untuk 3 langganan, berbayar untuk unlimited + alert harga + fitur "batalkan otomatis sebelum trial habis". Bisa juga agregator promo langganan resmi (bundle Telkomsel/Indihome) supaya user dapat harga lebih murah legally.

## What people would pay
- Rp 15.000 - 30.000 per bulan untuk fitur optimizer + alert (setara harga 1 kopi).
- Evidence willingness-to-pay: artikel CNBC "Warga RI Siap-siap" menunjukkan awarenes tinggi; user sudah merasa "diperes" oleh kenaikan beruntun, siap bayar alat kecil yang menghemat ratusan ribu per bulan.
- Comparable: app budgeting (MoneyLover, Finansialku) berlangganan Rp 20-50rb/bulan; Truebill/Mint di AS punya model serupa.

## Adjacent opportunities
- Cashback / bundling langganan via e-wallet (OVO, DANA, GoPay) cross-sell.
- Edukasi literasi keuangan "subscription fatigue" untuk pelajar/mahasiswa.
- Agregator konten legal murah (mirip JustWatch tapi dengan rekomendasi plan termurah per judul).
- Reminder pembayaran & dispute tagihan langganan salah ke bank.

## Time-to-build estimate
- 2 minggu dengan off-the-shelf tools: Google Sheet + Zapier + Gmail parse + bot WA notifikasi renewal.
- 1 bulan dengan custom dev: koneksi OAuth Play Store/App Store + dashboard + alert harga.
- 3+ bulan untuk produk penuh dengan kemitraan resmi platform streaming / e-wallet.
