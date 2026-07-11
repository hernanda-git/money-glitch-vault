# Bottleneck: Perlindungan Upah Tukang & Escrow Pembayaran Proyek Konstruksi Informal

> Kategori baru: labor-payment protection untuk pekerja fisik konstruksi & gig (tukang, kuli harian, subkontraktor kecil).
> Ditemukan: 2026-07-10. Diperdalam: 2026-07-11.
> Folder: `03-id-business-trends/bottlenecks/`

## Ringkasan Eksekutif (1 paragraf)

Di Indonesia, jutaan tukang bangunan, kuli harian, dan subkontraktor kecil bekerja pada rantai pembayaran yang rapuh. Uang mengalir dari pemilik proyek (pemerintah, developer, yayasan, atau pemilik rumah) melewati kontraktor utama, mandor, lalu baru sampai ke pekerja lapangan. Setiap simpul dalam rantai ini bisa menahan, menunda, atau menggelapkan pembayaran, dan pekerja yang paling ujung (yang paling butuh uang harian) adalah yang paling sering tidak dibayar. Tahun 2026 penuh kasus konkret: proyek Dapur MBG (Makan Bergizi Gratis), proyek Sekolah Rakyat, proyek Koperasi Merah Putih, sampai proyek swasta seperti Mie Gacoan, semuanya memunculkan berita pekerja mogok karena upah tertahan berminggu-minggu hingga berbulan-bulan. Tidak ada infrastruktur escrow atau jaminan pembayaran yang murah dan bisa diakses pekerja informal. Ini adalah bottleneck dengan pain yang sangat tinggi, korban yang jelas, kejadian berulang, dan belum ada pemain fintech yang menyasarnya secara langsung.

## Peta Rantai Pembayaran (di mana uang macet)

```
Pemilik Proyek (Pemda / BGN / Yayasan / Developer / Pemilik Rumah)
        |  (termin / SP2D / pencairan APBN-APBD, sering telat)
        v
Kontraktor Utama (CV/PT, kadang cash-flow tipis, talangi pakai pinjaman)
        |  (retensi 5%, termin 30-60 hari, potongan sepihak)
        v
Subkontraktor / Mandor Borongan
        |  (potong komisi, "uang rokok", talangan pribadi)
        v
Tukang & Kuli Harian  <-- korban paling ujung, tidak punya kontrak tertulis
```

Titik macet paling umum:
- Pencairan APBN/APBD telat, kontraktor sudah kadung mulai kerja pakai talangan.
- Kontraktor tidak dibayar pemberi kerja, otomatis pekerja tidak dibayar (efek domino).
- Mandor menerima uang tapi menahannya (moral hazard, tidak ada transparansi).
- Tidak ada kontrak tertulis untuk pekerja harian, jadi tidak ada bukti hukum.
- Retensi 5% dan termin akhir sering hangus atau ditahan bertahun-tahun.

## Kasus Nyata 2026 (dengan sumber & tanggal)

Setiap kasus di bawah adalah headline riil dari Google News (hl=id) yang dikumpulkan 2026-07-11. URL kanonik berupa link agregator Google News; nama outlet asli dicantumkan agar bisa ditelusuri.

### Proyek Pemerintah / Program Nasional

- **Dapur MBG Krayan, Kalimantan Utara (detikcom, 6 Mar 2026).** "Pekerja Bangunan Dapur MBG di Krayan Belum Dibayar, Kontraktor Pinjam Bank." Kontraktor menalangi upah dengan meminjam ke bank karena pencairan dari pemberi kerja belum turun. Menegaskan pola: kontraktor jadi bank bayangan.
- **Vendor MBG (Kompas.com, 16 Apr 2025).** "Vendor MBG Tak Dibayar, BGN Sudah Transfer ke Yayasan Mitra SPPG Kalibata." BGN mengaku sudah transfer ke yayasan mitra, tetapi vendor di ujung tetap tidak menerima. Ini bukti kebocoran di simpul tengah (yayasan/SPPG), justru argumen kuat untuk escrow berbasis milestone.
- **Dapur MBG Bengkulu (radarseluma.disway.id, 14 Mar 2026).** "Puluhan Dapur MBG di Bengkulu Disegel Pekerja, Tuntut Pembayaran Upah Jelang Lebaran." Penyegelan aset fisik jadi satu-satunya alat tawar pekerja, tanda tidak ada mekanisme klaim formal.
- **Sekolah Rakyat, Banjarbaru (Kompas.com, 23 May 2026; Media Indonesia, 25 May 2026; Radar Banjarmasin, 25 May 2026).** "Pembangunan Sekolah Rakyat di Banjarbaru Terhenti, Pekerja Mogok karena Gaji Belum Dibayar." Setelah mogok dan sorotan media, "Upah Akhirnya Cair, Ratusan Pekerja Proyek Sekolah Rakyat di Banjarbaru Kembali Bekerja." Pola klasik: pembayaran baru cair setelah tekanan publik, bukan karena sistem.
- **Proyek Gedung Koperasi Merah Putih, Lahat (19 Jun 2026).** "Kami Bekerja, Tapi Upah Belum Dibayar: Pekerja Proyek Gedung Koperasi Merah Putih di Lahat Minta Perhatian." Program Koperasi Merah Putih pun tidak imun.
- **Proyek Sanitasi, Banda (ambonkita.com, 21 Apr 2026).** "Upah Pekerja Proyek Sanitasi di Banda Belum Dibayarkan."
- **Kampung Nelayan Merah Putih, Pangandaran (Pikiran Rakyat, 15 Jan 2026).** "Proyek Terlambat, Pekerja Mengeluh Upah Tak Dibayar 2 Minggu."
- **Dana Desa (SAHdaR, 21 Feb 2026).** "Dugaan Korupsi Dana Desa yang Berimbas Upah Tukang (Pekerja Bangunan) Tidak Dibayar." Menghubungkan korupsi hulu dengan gagal-bayar hilir.

### Proyek Swasta

- **Mie Gacoan (Dulohupa.id, 21 Jun 2025).** "Terungkap! Alasan Belum Dibayarkan Upah Pekerja Bangunan Mie Gacoan." Renovasi/pembangunan gerai ritel juga rentan.
- **YVE Habitat (detikcom, 4 Nov 2025).** "Heboh Kabar Tukang YVE Habitat Belum Dibayar, Begini Faktanya!" Developer properti bermasalah dengan tukang.
- **RS Aloe Saboe, Gorontalo (Kompas.com, 23 Feb 2024).** "Upah 2 Bulan Belum Dibayar, Puluhan Pekerja Proyek Bangunan Terlantar." Menahun.
- **SMK Budi Mulia, Kalukku (sulbar.bpk.go.id, 22 Jan 2025).** "Kesal Upah Tak Dibayar Sejak 2 Tahun, Buruh Segel Gedung." Tunggakan dua tahun.

### Kasus Rp 173 Juta (Lamongan)

Kasus pemicu kategori ini (rujukan mining 2026-07-10): tukang bangunan di Lamongan tidak menerima upah dengan total akumulasi ~Rp 173 juta. Nominal ini menunjukkan gagal-bayar bukan "upah satu-dua orang" tetapi akumulasi puluhan pekerja pada satu proyek. Catatan: detail kasus perlu penelusuran ulang; dicatat sebagai anekdot pemicu, bukan angka terverifikasi.

## Skala Pasar (angka)

- **Tenaga kerja konstruksi Indonesia:** sekitar 8-9 juta orang bekerja di sektor konstruksi (BPS, sektor konstruksi menyumbang ~10% PDB). Mayoritas tukang & kuli adalah pekerja harian/borongan tanpa kontrak tertulis.
- **Upah harian tukang 2025 (rujukan 99.co, 25 Mar 2025; Medcom.id, 1 Oct 2025):** kisaran Rp 100.000-Rp 150.000/hari untuk tukang, Rp 90.000-Rp 120.000 untuk kenek/kuli, bervariasi per daerah. Di Kaltara Rp 150.000/hari (KoranKaltara, 9 Oct 2025). Borongan per meter persegi bervariasi Rp 700.000-Rp 1.500.000/m2 tergantung spesifikasi (Kompas.com, 17 Oct 2025).
- **Anomali daya tawar:** "Mengapa Upah Buruh Konstruksi di Bojonegoro Kalah dari Buruh Tani" (SuaraBanyuurip.com, 25 Mar 2026), menandakan upah riil konstruksi tertekan di beberapa daerah.
- **Belanja infrastruktur pemerintah:** APBN infrastruktur biasanya di kisaran Rp 400 triliun-an per tahun; ditambah program baru 2025-2026 (MBG, Sekolah Rakyat, Koperasi Merah Putih, Kampung Nelayan) yang berbasis kontraktor lokal kecil, populasi proyek berisiko gagal-bayar meluas justru karena eksekusi cepat dan pengawasan cash-flow lemah.

Kesimpulan skala: bahkan jika hanya 5% dari 8 juta pekerja mengalami penundaan upah per tahun, itu 400.000 kejadian gagal/telat bayar. Dengan upah tertahan rata-rata (asumsi konservatif) Rp 2 juta per orang per kejadian, nilai float yang "hilang sementara" dari kantong pekerja mencapai Rp 800 miliar+ setiap tahun. Ini adalah kolam pain yang bisa dimonetisasi lewat jaminan pembayaran, factoring upah, atau escrow.

## Solusi yang Sudah Ada (dan kenapa gagal menutup gap)

### 1. Jalur hukum & Dinas Ketenagakerjaan
Pekerja bisa mengadu ke Disnaker atau menggugat perdata. Realita: pekerja harian tanpa kontrak tertulis nyaris tidak punya bukti; proses lambat berbulan-bulan; biaya & waktu tidak sepadan dengan upah harian. Praktis tidak dipakai kecuali kasus besar dan kolektif.

### 2. BPJS Ketenagakerjaan (Bukan Penerima Upah / Jasa Konstruksi)
BPJS TK punya program jaminan kecelakaan kerja & kematian untuk pekerja konstruksi (sering diwajibkan di proyek APBN). Tapi BPJS TK TIDAK menjamin pembayaran upah. Ia melindungi risiko kecelakaan, bukan risiko gagal-bayar. Gap tetap terbuka.

### 3. Retensi & termin kontrak (LKPP / Perpres PBJ)
Regulasi pengadaan (Perpres 12/2021 tentang Pengadaan Barang/Jasa) mengatur termin dan retensi 5% untuk kontraktor, tetapi tidak turun sampai perlindungan pekerja individu. Retensi justru sering jadi sumber gagal-bayar hilir.

### 4. SKK & sertifikasi (LPJK / GATENSI / Askonas)
Sertifikasi Kompetensi Kerja (SKK) meningkatkan daya tawar dan formalitas, tetapi tidak menyelesaikan cash-flow. Berita 2026 (Pemkot Tangsel, 12 Feb 2026; GATENSI Baubau, 1 Aug 2025) fokus ke kualitas SDM, bukan jaminan bayar.

### 5. Aplikasi pencari tukang (Kliktukang, Sejasa, Tukang.com, Gravel)
Gravel adalah pemain terdekat: platform yang menghubungkan tukang dengan proyek dan menjanjikan pembayaran tukang lebih pasti (Gravel menahan dana klien lalu membayar tukang). Ini bukti model escrow-untuk-tukang bisa jalan, TETAPI Gravel fokus pada proyek yang mereka orkestrasi sendiri (marketplace tertutup). Gap: mayoritas proyek terjadi DI LUAR platform manapun (proyek pemerintah, mandor tradisional, developer). Tidak ada lapisan escrow/jaminan yang bisa "menempel" pada proyek yang sudah ada tanpa memaksa semua pihak pindah platform.

## The Wedge (di mana celah bisa dibuka)

Gap inti: **tidak ada produk keuangan murah yang menjamin bahwa pekerja lapangan dibayar tepat waktu, terlepas dari kesehatan cash-flow kontraktor di atasnya.** Tiga wedge paling realistis:

### Wedge A: Escrow milestone berbasis WhatsApp untuk proyek kecil/menengah
Pemilik proyek menyetor dana ke rekening escrow (bank/e-wallet berlisensi). Dana dilepas per milestone yang diverifikasi foto geotag + approval mandor. Pekerja terdaftar menerima porsi upahnya langsung ke e-wallet begitu milestone disetujui, memotong risiko mandor menahan. Target awal: renovasi rumah & proyek developer kecil (yang pemiliknya justru mau jaminan pekerjaan selesai). Ini menyelesaikan pain dua sisi: pemilik takut tukang kabur, tukang takut tidak dibayar. Escrow menjembatani kepercayaan.

### Wedge B: Wage advance / factoring upah (talangan berbunga rendah)
Ketika kontraktor terbukti punya kontrak sah tapi pencairan APBN/APBD telat, sebuah lender menalangi upah pekerja lebih dulu (bukan menalangi kontraktor), lalu menagih ke kontraktor/pemberi kerja saat termin cair. Struktur ini mirip invoice financing tapi collateral-nya adalah tagihan upah yang dilindungi undang-undang ketenagakerjaan (upah adalah utang berprioritas). Risiko diturunkan dengan verifikasi kontrak & SP2D.

### Wedge C: Payment-rail + reputasi (data moat)
Setiap kali escrow/talangan dipakai, terbentuk data: kontraktor mana yang telat bayar, proyek mana yang berisiko, mandor mana yang jujur. Skor reputasi pembayaran ini menjadi aset. Pekerja bisa mengecek "apakah kontraktor X track-record-nya bayar?" sebelum ikut proyek, mirip skor kredit tapi untuk perilaku bayar upah. Ini defensible dan makin bernilai seiring volume.

## Berapa yang Mau Dibayar (pricing)

- **Escrow fee (Wedge A):** 1-2,5% dari nilai proyek, dibebankan ke pemilik proyek (mereka yang paling mau bayar untuk kepastian pekerjaan selesai). Pada proyek renovasi Rp 150 juta, fee 2% = Rp 3 juta, wajar dibanding risiko tukang kabur atau sengketa.
- **Wage advance (Wedge B):** biaya 1,5-3% per bulan tenor talangan (setara factoring UMKM), dibebankan ke kontraktor. Untuk upah tertahan Rp 100 juta selama 30 hari, biaya ~Rp 2-3 juta, jauh lebih murah daripada mogok kerja yang menghentikan proyek.
- **Reputasi/SaaS (Wedge C):** langganan bulanan untuk kontraktor/QS yang mau membuktikan track record baik, atau untuk pemilik proyek yang mau due-diligence kontraktor. Rp 99.000-Rp 499.000/bulan.

Yang paling cepat menghasilkan: kombinasi A (fee dari pemilik) + B (spread dari talangan). Pemilik proyek dan kontraktor sama-sama punya kantong dan sama-sama rugi kalau proyek mandek, jadi ada willingness to pay yang jelas di kedua sisi. Pekerja adalah beneficiary, bukan pembayar (justru itu daya tarik distribusi: pekerja akan mengajak proyek lain).

## Arsitektur Teknis (pseudo-code)

Escrow milestone sederhana berbasis state machine, terintegrasi WhatsApp Business API + payment gateway (Midtrans/Xendit) + e-wallet payout (DANA/OVO/GoPay atau bank transfer via disbursement API).

```python
# escrow_project.py -- state machine untuk escrow proyek konstruksi
from enum import Enum
from dataclasses import dataclass, field
from datetime import datetime

class ProjectState(str, Enum):
    DRAFT = "draft"                 # kontrak dibuat, belum ada dana
    FUNDED = "funded"               # pemilik sudah setor ke escrow
    IN_PROGRESS = "in_progress"     # ada minimal 1 milestone jalan
    MILESTONE_REVIEW = "review"     # bukti diajukan, menunggu approval
    DISPUTED = "disputed"           # sengketa, dana ditahan
    COMPLETED = "completed"         # semua milestone lunas
    REFUNDED = "refunded"           # dana dikembalikan ke pemilik

@dataclass
class Milestone:
    id: str
    label: str                     # "Pondasi selesai", "Atap terpasang"
    amount_idr: int                # porsi dana untuk milestone ini
    worker_split: dict             # {worker_id: idr} pembagian ke pekerja
    proof_urls: list = field(default_factory=list)  # foto geotag
    approved_by: str = None        # id pemilik/QS yang approve
    released_at: datetime = None

@dataclass
class EscrowProject:
    id: str
    owner_id: str                  # pemilik proyek (pembayar fee)
    contractor_id: str
    total_idr: int
    fee_bps: int = 200             # 2.0% fee ke platform
    state: ProjectState = ProjectState.DRAFT
    milestones: list = field(default_factory=list)
    balance_idr: int = 0           # dana tersimpan di escrow

    def fund(self, amount_idr: int):
        assert self.state in (ProjectState.DRAFT, ProjectState.FUNDED)
        self.balance_idr += amount_idr
        self.state = ProjectState.FUNDED

    def submit_proof(self, ms_id: str, urls: list):
        ms = self._get(ms_id)
        ms.proof_urls.extend(urls)
        self.state = ProjectState.MILESTONE_REVIEW

    def approve_and_release(self, ms_id: str, approver_id: str):
        assert approver_id == self.owner_id, "hanya pemilik yang approve"
        ms = self._get(ms_id)
        assert ms.proof_urls, "tidak ada bukti pekerjaan"
        assert self.balance_idr >= ms.amount_idr, "saldo escrow kurang"
        fee = ms.amount_idr * self.fee_bps // 10000
        net = ms.amount_idr - fee
        # payout langsung ke tiap pekerja, potong risiko mandor menahan
        for worker_id, idr in ms.worker_split.items():
            disburse(worker_id, idr)      # panggil API disbursement
        self.balance_idr -= ms.amount_idr
        ms.approved_by = approver_id
        ms.released_at = datetime.utcnow()
        collect_fee(fee)
        if all(m.released_at for m in self.milestones):
            self.state = ProjectState.COMPLETED
        else:
            self.state = ProjectState.IN_PROGRESS

    def _get(self, ms_id):
        return next(m for m in self.milestones if m.id == ms_id)


def disburse(worker_id: str, idr: int):
    """Xendit/Midtrans disbursement ke e-wallet atau rekening bank pekerja."""
    # POST https://api.xendit.co/disbursements
    # body: {external_id, bank_code, account_number, amount}
    pass

def collect_fee(idr: int):
    pass
```

Alur WhatsApp (tanpa perlu app, karena tukang & mandor sudah pakai WA):
- Pemilik kirim "MULAI PROYEK" -> bot buat link setoran escrow (Xendit invoice).
- Setelah dana masuk, bot kirim kode proyek ke mandor & pekerja terdaftar.
- Mandor kirim foto milestone lewat WA -> disimpan sebagai proof (geotag dari metadata/lokasi WA).
- Pemilik balas "SETUJU <kode>" -> payout otomatis ke tiap pekerja, notifikasi ke semua pihak.
- Jika ada sengketa, "SENGKETA <kode>" -> state DISPUTED, dana beku, tim mediasi masuk.

Kunci: pekerja menerima uang LANGSUNG dari escrow, bukan lewat tangan mandor. Ini yang memutus moral hazard.

## Aspek Regulasi & Kepatuhan

- **Escrow butuh partner berlisensi.** Menahan dana pihak ketiga = kegiatan yang diawasi OJK/BI. Solusi cepat: gunakan escrow bank (BCA/Mandiri punya layanan rekening penampungan) atau payment gateway berizin (Xendit, Midtrans/GoTo Financial, Doku) yang sudah punya lisensi disbursement & e-money. Jangan menahan dana di rekening pribadi/PT sendiri tanpa izin.
- **Upah sebagai utang prioritas.** UU Ketenagakerjaan & UU Kepailitan menempatkan upah pekerja sebagai kreditur preferen. Ini menurunkan risiko wage-advance (Wedge B) karena tagihan upah punya prioritas hukum saat kontraktor pailit.
- **PMK 168/2023 (PPh 21 tenaga kerja lepas).** Talangan/pembayaran upah harian memicu kewajiban potong PPh 21 untuk pegawai tidak tetap (rujukan Ortax, 10 Jan 2024). Platform escrow bisa jadi nilai tambah dengan mengotomasi bukti potong, membantu formalisasi.
- **Perlindungan data.** Nomor rekening/e-wallet & KTP pekerja adalah data pribadi (UU PDP 27/2022). Perlu consent & enkripsi.

## Sinyal Validasi (kenapa sekarang waktunya)

- Frekuensi berita gagal-bayar meningkat 2026 seiring program padat karya baru (MBG, Sekolah Rakyat, Koperasi Merah Putih) yang menyebar ke kontraktor kecil dengan cash-flow tipis dan pengawasan lemah. Setiap program = pipeline proyek baru = pipeline risiko baru.
- Pola berulang "cair setelah viral/mogok" membuktikan tidak ada mekanisme preventif. Pasar menunggu solusi sistemik.
- Infrastruktur pembayaran (QRIS, e-wallet, disbursement API) sudah matang dan murah, membuat payout mikro ke ribuan pekerja layak secara teknis dan biaya, hal yang 5 tahun lalu mustахil.
- Gravel membuktikan model escrow-tukang investable (sudah raih pendanaan ventura), tapi menyisakan seluruh pasar off-platform.

## Risiko & Mitigasi

- **Adopsi mandor rendah** (mandor kehilangan kontrol dana). Mitigasi: beri mandor fee transparan & dashboard, posisikan sebagai alat yang membuat mandor terlihat kredibel, bukan menggantikannya.
- **Sengketa kualitas pekerjaan.** Mitigasi: milestone kecil, foto geotag, opsi mediasi pihak ketiga (QS/arsitek freelance).
- **Fraud kolusi** (mandor + pemilik palsu). Mitigasi: verifikasi kontrak & identitas, batasi limit awal, skor reputasi.
- **Ketergantungan program pemerintah** yang bisa berubah kebijakan. Mitigasi: mulai dari proyek swasta/renovasi yang tidak bergantung siklus APBN.

## Sumber (dikumpulkan 2026-07-11 via Google News RSS, hl=id)

- detikcom, "Pekerja Bangunan Dapur MBG di Krayan Belum Dibayar, Kontraktor Pinjam Bank", 6 Mar 2026.
- Kompas.com, "Vendor MBG Tak Dibayar, BGN Sudah Transfer ke Yayasan Mitra SPPG Kalibata", 16 Apr 2025.
- radarseluma.disway.id, "Puluhan Dapur MBG di Bengkulu Disegel Pekerja", 14 Mar 2026.
- Kompas.com / Media Indonesia / Radar Banjarmasin, "Sekolah Rakyat Banjarbaru mogok & cair", 23-25 May 2026.
- Lahat, "Pekerja Proyek Gedung Koperasi Merah Putih Minta Perhatian", 19 Jun 2026.
- ambonkita.com, "Upah Pekerja Proyek Sanitasi di Banda Belum Dibayarkan", 21 Apr 2026.
- Pikiran Rakyat, "Kampung Nelayan Merah Putih Pangandaran, Upah Tak Dibayar 2 Minggu", 15 Jan 2026.
- SAHdaR, "Dugaan Korupsi Dana Desa Berimbas Upah Tukang Tidak Dibayar", 21 Feb 2026.
- Dulohupa.id, "Alasan Belum Dibayarkan Upah Pekerja Bangunan Mie Gacoan", 21 Jun 2025.
- detikcom, "Heboh Kabar Tukang YVE Habitat Belum Dibayar", 4 Nov 2025.
- Kompas.com, "Upah 2 Bulan Belum Dibayar, Pekerja RS Aloe Saboe Gorontalo Terlantar", 23 Feb 2024.
- sulbar.bpk.go.id, "Buruh Segel Gedung SMK Budi Mulia Kalukku, Upah Tak Dibayar 2 Tahun", 22 Jan 2025.
- 99.co, "Upah Tukang Bangunan Harian dan Borongan Tahun 2025", 25 Mar 2025.
- Medcom.id, "Tarif Tukang Bangunan Harian dan Borongan 2025", 1 Oct 2025.
- Kompas.com, "Kisaran Upah Tukang Bangunan Borongan Per Meter Persegi", 17 Oct 2025.
- KoranKaltara.com, "Upah Harian Tukang Bangunan di Kaltara Rp150 Ribu", 9 Oct 2025.
- SuaraBanyuurip.com, "Mengapa Upah Buruh Konstruksi di Bojonegoro Kalah dari Buruh Tani", 25 Mar 2026.
- Ortax, "Cara Hitung PPh 21 Pegawai Tidak Tetap Sesuai PMK 168/2023", 10 Jan 2024.
- LKPP / Perpres 12/2021 tentang Pengadaan Barang/Jasa Pemerintah (termin & retensi).
- Gravel (gravel.id) sebagai pembanding model escrow-tukang.

## Catatan Cross-cutting (gap baru yang ditemukan)

Lihat penambahan pada auditor: (1) skor reputasi pembayaran kontraktor sebagai data moat, (2) integrasi bukti potong PPh 21 pekerja lepas untuk formalisasi, (3) API verifikasi SP2D/kontrak untuk underwriting wage-advance.

## Unit Economics (skenario konservatif)

Asumsi model gabungan escrow (Wedge A) + wage-advance (Wedge B), tahun operasi ke-2.

```
Escrow (Wedge A)
  Proyek diproses/bulan          : 200 proyek
  Nilai rata-rata proyek         : Rp 120.000.000
  Fee escrow                     : 2.0%
  GMV/bulan                      : Rp 24.000.000.000
  Revenue escrow/bulan           : Rp 480.000.000

Wage-advance (Wedge B)
  Volume talangan/bulan          : Rp 5.000.000.000
  Biaya rata-rata (tenor 30 hari): 2.2%
  Revenue talangan/bulan         : Rp 110.000.000
  Cost of funds (asumsi 1.0%/bln): Rp 50.000.000
  Gross spread/bulan             : Rp 60.000.000

Total gross revenue/bulan        : ~Rp 540.000.000
Biaya payment gateway (~0.7% GMV): ~Rp 168.000.000
Gross margin kotor               : ~Rp 372.000.000/bulan
```

Biaya akuisisi ditekan karena distribusi viral: setiap pekerja yang dibayar tepat waktu adalah kanal referral ke proyek berikutnya. CAC utama adalah edukasi pemilik proyek & mandor, bukan iklan berbayar.

## Go-To-Market (urutan yang realistis)

Mulai dari satu kota tier-2 dengan banyak proyek renovasi/developer kecil (mis. Malang, Solo, atau Sidoarjo) alih-alih Jakarta yang ramai pemain. Rekrut 20-30 mandor "champion" yang sudah punya reputasi baik dan jadikan mereka simpul pertama; mereka membawa pekerja tetap dan proyek berulang. Pemilik proyek renovasi rumah adalah pembeli awal terbaik karena mereka takut tukang kabur di tengah jalan dan mau membayar untuk kepastian. Setelah alur escrow renovasi terbukti, baru ekspansi ke developer kecil, lalu ke proyek pemerintah lewat kemitraan dengan kontraktor yang butuh talangan saat pencairan APBD telat. Program pemerintah (MBG, Sekolah Rakyat) dijadikan channel wage-advance, bukan channel awal, karena siklus birokrasinya lambat dan berisiko regulasi.

Metrik utara: persentase proyek yang selesai tanpa satu pun keluhan gagal-bayar pekerja. Ini adalah bukti sosial paling kuat dan bahan pemasaran organik yang tidak bisa ditiru pesaing off-platform.

## Kesimpulan

Gagal-bayar upah tukang bukan anomali, melainkan fitur struktural dari rantai pembayaran konstruksi Indonesia yang panjang, informal, dan tanpa jaminan. Sinyal 2026 (MBG, Sekolah Rakyat, Koperasi Merah Putih, plus kasus swasta) menunjukkan frekuensi dan skala yang cukup untuk membangun bisnis. Wedge paling cepat adalah escrow milestone berbasis WhatsApp untuk proyek renovasi/developer kecil (fee dari pemilik) dikombinasikan dengan wage-advance saat pencairan pemerintah telat (spread dari kontraktor). Pekerja adalah beneficiary dan mesin distribusi, bukan pembayar. Data reputasi pembayaran yang terakumulasi menjadi moat jangka panjang.
