# Investor Kena Tipu Startup "Unicorn", Laporan Keuangan Dimanipulasi

**Date observed:** 2026-07-20
**Signal strength:** 5
**Category:** investor
**Sources (minimum 3):**
- [Dana Pensiun PNS Malaysia Jadi Korban Startup RI (eFishery)](https://finance.detik.com/berita-ekonomi-bisnis/d-8581116/dana-pensiun-pns-malaysia-jadi-korban-startup-ri) — 2026-07-19 — KWAP rugi hampir RM200 juta (Rp860 miliar) karena manipulasi laporan keuangan
- [951 Entitas Pinjol & Investasi Bodong Disetop, Ini 5 Modusnya](https://finance.detik.com/berita-ekonomi-bisnis/d-8505968/951-entitas-pinjol-investasi-bodong-disetop-ini-5-modusnya) — 2026-07 — OJK setop ratusan entitas investasi bodong
- [OJK Jateng: Korban Penipuan Keuangan Tak Perlu Lapor Polisi](https://finance.detik.com/berita-ekonomi-bisnis/d-8475116/ojk-jateng-sebut-korban-penipuan-keuangan-tak-perlu-lapor-polisi-ini-alasannya) — 2026-07 — OJK akui tingginya kasus penipuan keuangan
- [Waspada Pinjol Ilegal, Ini Ciri dan Cara Menghindarinya](https://finance.detik.com/berita-ekonomi-bisnis/d-8470154/waspada-pinjol-ilegal-ini-ciri-dan-cara-menghindarinya) — 2026-07 — edukasi publik soal modus investasi palsu

## The pain (verbatim quotes in Indonesian)
> "Meskipun demikian, investasi eFishery merupakan penipuan yang direncanakan, dan terdapat manipulasi laporan keuangan oleh manajemen eFishery." — Perdana Menteri Malaysia Anwar Ibrahim dalam laporan tertulis ke parlemen, 15 Juli 2026

> "Keputusan tersebut telah melalui proses evaluasi dan tata kelola, berdasarkan informasi yang tersedia pada saat itu, yang mencakup verifikasi laporan keuangan oleh auditor bersertifikat yang diakui secara internasional." — Anwar Ibrahim, menunjukkan bahwa auditor internasional pun tertipu

> "Konsorsium investor, termasuk KWAP, juga melakukan uji tuntas independen untuk memastikan bahwa semua informasi lengkap dan valid untuk pertimbangan investasi." — Anwar Ibrahim, membuktikan due diligence independen tetap gagal mendeteksi fraud

## Evidence of volume
- eFishery (mantan decacorn akuakultur) didanai US$200 juta Seri D (2023), US$47,7 juta di antaranya dari KWAP. Korban lain: Temasek, SoftBank, 42XFund, Northstar.
- OJK sudah setop 951 entitas pinjol dan investasi bodong per Juli 2026, mengindikasikan volume penipuan investasi yang masif.
- Kasus serupa (Wili, Putra Siregar, dll) terus muncul. Investor ritel dan institusi sama-sama kehilangan uang karena tidak ada verifikasi independen yang andal.
- 1 diskusi viral di X/WhatsApp group investor tentang "gimana ngecek startup beneran atau bohong" setiap kali kasus eFishery menyebar.

## Existing solutions (and why they fail)
- Auditor eksternal (Big Four): gagal di eFishery padahal laporan "diverifikasi auditor bersertifikat internasional". Mahal (ratusan juta) dan masih bisa tertipu.
- Uji tuntas (due diligence) konsultan M&A: hanya terjangkau investor institusi, butuh bulan, dan tetap kecolongan di eFishery.
- OJK registry / CEKREKENING: hanya cover rekening bank dan entitas berizin, tidak cover startup privat pra-IPO yang pakai PT tertutup.
- Media investigasi: muncul terlambat, setelah uang hilang.

## Your wedge
Bangun layanan "startup truth-score" untuk investor ritel dan institusi kecil: agregasi data ops (izin, NPWP, direksi, riwayat litigasi di SIPP), cross-check klaim revenue vs struk pajak (Coretax/DJP), pengecekan konsistensi laporan keuangan vs pembayaran pajak, dan alert jika ada "growth too good to be true". Produk berbentuk SaaS berlangganan + laporan DD instan per target startup. Wedge: otomatisasi cross-check pajak vs klaim yang selama ini manual dan mahal, jadi terjangkau (mulai Rp50.000/cek). Bisa juga jadi API yang dipakai platform equity crowdfunding lokal (Sanders, Biznet, dll) untuk verifikasi emiten.

## What people would pay
- Price point: Rp50.000 - Rp150.000 per laporan DD instan untuk investor ritel. Rp1-5 juta/bulan untuk langganan institusi kecil (family office, koperasi).
- Evidence willingness-to-pay: investor institusi (KWAP) menghabiskan jutaan untuk DD dan tetap rugi Rp860M. Investor ritel di grup WA siap bayar murah asal ada "tombol cek".
- Comparable: layanan KYC/background check fintech lokal (eg. langsia, pequ, advokat litigasi) mematok Rp50-300 ribu per cek.

## Adjacent opportunities
- API verifikasi entitas untuk platform equity crowdfunding dan P2P lending lokal.
- Bundling dengan loker-scam-verifier (sudah ada di gaps inbox) dan umrah-travel-verifier.
- Whistleblower marketplace khusus karyawan startup yang mau laporkan manipulasi.

## Time-to-build estimate
- 2 minggu dengan off-the-shelf tools: scraper OSS/DJP/cekrezeki + template laporan + bot Telegram.
- 1 bulan dengan custom dev: scoring engine dan dashboard historis.
- 3+ bulan untuk produk penuh dengan API komersial.
