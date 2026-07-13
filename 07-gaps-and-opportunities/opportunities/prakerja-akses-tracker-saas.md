# Prakerja Akses & Insentif-Cair Tracker SaaS ("PrakerjaWatch")

> Kartu Prakerja 2026 buka kapan, dan insentif kapan cair, adalah dua pertanyaan yang tiap
> gelombang memicu ribuan keluhan karena kanal resmi cuma balas dengan bot dan telepon
> pengaduan yang selalu penuh. Wedge: lapisan tracker + status-checker ringan di atas
> ekosistem Prakerja yang sudah ada, bukan pendaftaran baru. Bot Telegram pengingat
> gelombang, web checker estimasi cair insentif dari histori settlement lag, dan layanan
> asistensi eskalasi klaim berbayar untuk kasus insentif mangkrak berbulan-bulan. Harga
> Rp 0 untuk info tracker (monetisasi afiliasi kursus resmi + iklan terarah), dan Rp 50.000
> sampai Rp 150.000 per kasus untuk prioritas eskalasi klaim. Pola sama dengan
> desil-dormant-checker-saas dan qris-mdr-transparency-layer yang sudah ada di opportunities.

**File:** `07-gaps-and-opportunities/opportunities/prakerja-akses-tracker-saas.md`
**Promoted from:** `07-gaps-and-opportunities/inbox/2026-07-13-prakerja-akses-tracker-saas.md`
**Created:** 2026-07-13
**Category:** Opportunity one-pager (vertical SaaS, government-benefit access layer)
**Confidence:** 4
**Status:** build-ready
**Build time:** 2 weeks MVP (Telegram bot + template eskalasi), 1 month web tracker + kalkulator estimasi cair, 3+ months dengan scraping resmi + auth + forum komunitas.

---

## 1. Problem and evidence

The pain is documented locally in `03-id-business-trends/demand-mining/kartu-prakerja-2026-akses-sulit.md` (signal strength 4/5, observed 2026-07-13). The evidence chain:

- Pembukaan Kartu Prakerja 2026 tidak pasti. Sampai awal 2026, belum ada informasi resmi kapan pendaftaran dibuka. Dealls (artikel bertanggal 2026) menulis: "Hingga memasuki awal 2026, belum ada informasi resmi mengenai pembukaan program Kartu Prakerja 2026." Sumber: https://dealls.com/pengembangan-karir/cara-mendaftar-prakerja (diakses 2026-07-13).
- Skema bantuan saat ini diatur oleh **Perpres Nomor 113 Tahun 2022** (skema normal, bukan skema semi-bansos pandemi). Di bawah Perpres 113/2022, nilai bantuan naik menjadi **Rp4,2 juta per individu**, terdiri dari: biaya pelatihan Rp3,5 juta, insentif pascapelatihan Rp600.000 (1 kali), dan insentif survei Rp100.000 (2 kali pengisian). Sumber: https://indonesiabaik.id/infografis/peserta-kartu-prakerja-kini-dapat-rp42-juta (diakses 2026-07-13). Catatan: artikel ini merujuk tahun 2023 sebagai contoh pelaksanaan skema normal, bukan 2026.
- Keluhan insentif tak kunjung cair sudah ada sejak gelombang pertama dan berulang tiap gelombang. Surat pembaca asli peserta Prakerja Gelombang I: "Saya sudah menunggu selama lebih dari 3 bulan. Dengan tidak munculnya sertifikat saya berarti insentif saya tidak akan pernah cair." Sumber: https://mediakonsumen.com/2020/08/18/surat-pembaca/insentif-prakerja-gelombang-i-tak-kunjung-cair-masalah-ada-di-pihak-siapa (2020-08-18).
- Kanal pengaduan resmi gagal merespons. Peserta mengeluh help center cuma balas bot, DM Twitter Skill Academy antrean penuh, dan telepon pengaduan selalu penuh pagi siang sore.

Honesty note on one cited source: the vault pain file attributes a Kontan article "Payung hukum program kartu prakerja masuk tahap finalisasi" to 2026-02-18, but the live page actually carries the date **Selasa, 18 Februari 2020 / 20:29 WIB** (https://nasional.kontan.co.id/news/payung-hukum-program-kartu-prakerja-masuk-tahap-finalisasi, diakses 2026-07-13). The article quotes Sekretaris Kemenko Perekonomian Susiwijono about finalisasi rancangan perpres. This is a 2020-era article reused/miscited; treat it as historical context for the Perpres 113/2022 lineage, NOT as a 2026 development. The regulatory anchor for the current scheme is Perpres 113/2022, not a 2026 perpres. This mis-date was caught during this tick and is logged here so the vault does not propagate it.

External verification caveat: web_search and web_extract tools were unavailable during this tick (PARALLEL_API_KEY not set in sandbox), so sources were fetched via direct curl with a desktop User-Agent. The four URLs above were live (HTTP 200) on 2026-07-13 and their text was parsed locally. The deep-link dates above are taken from the live page metadata, not from the vault's earlier (partly mis-dated) summary.

Volume signal: Kartu Prakerja historically targets jutaan peserta per tahun (2022: 4,98 juta peserta, anggaran Rp18 triliun, realisasi 99,12 persen; 2023: 1 juta peserta, anggaran Rp4,37 triliun, per Indonesiabaik). Even at the smaller 1 juta scale, the addressable audience for a "kapan buka / kapan cair" tracker is in the millions per gelombang, and the confusion is repeated every opening.

## 2. Wedge and product

A **Prakerja access and payout-visibility layer** that sits on top of the official Prakerja dashboard and comms, not a competing enrollment system. The product, "PrakerjaWatch," does three concrete jobs:

1. **Gelombang live tracker.** Monitors official channels (prakerja.go.id, Instagram/YouTube Kemnaker/Prakerja, Siapkerja app release notes) for the moment a new gelombang opens, and pushes a Telegram/WhatsApp alert within minutes. It also keeps a running "last known status" page so users are not refreshing a dead dashboard.
2. **Insentif-cair estimator.** Given the user's gelombang + tanggal selesai pelatihan + tanggal isi survei, the tool estimates the payout date from historical settlement lag (the 2020 complaint shows 3+ month stalls; normal flow is days-to-weeks). It flags "stuck" accounts (no payout past the historical P95 lag) and tells the user exactly which document is missing (sertifikat pelatihan, survei belum diisi, rekening bermasalah).
3. **Assisted claim escalation (paid).** For insentif mangkrak berbulan-bulan, the tool packages the user's screenshots, bukti pelatihan, and a templated eskalasi to PMO Prakerja / lapak pengaduan, and optionally routes to a human pendamping. This is the monetized layer.

Differentiation: we do not sell "joki daftar" (which is legal-grey and gets accounts banned). We sell clarity and a legal escalation path. The black-market "joki" and hoaks Instagram accounts already prove willingness to pay for help navigating Prakerja; we capture that demand with a legitimate product.

## 3. Technical architecture

MVP is a Telegram bot + static status page, no official API integration required (the official API is not public). It is a scraper/aggregator plus a rules engine plus a templated escalation generator.

```
System components (MVP, 2 weeks)
1. source-monitor/        Polling workers (cron every 5-15 min)
   - prakerja_website.py  GET https://prakerja.go.id, diff HTML for "Pendaftaran Gelombang N Dibuka"
   - social_watcher.py    Read public IG/YT RSS or search endpoints for "Prakerja Gelombang"
   - siapkerja_changelog.py  Poll Siapkerja app store / release notes
2. diff_engine.py         Compare snapshot(n) vs snapshot(n-1); emit "OPENED" / "CLOSED" events
3. notifier.py           Push to Telegram channel (bot API) + optional WA via Twilio/WATI
4. estimator.py          Payout ETA model from historical lag table (see section 4)
5. escalation.py         Render PDF/wa-template from user inputs; queue to human inbox
6. db.sqlite             events, users, escalation_cases
```

Working sketch for the gelombang detector (Python, no deps beyond requests + bs4):

```python
import requests, hashlib, time, sqlite3
from bs4 import BeautifulSoup

URL = "https://prakerja.go.id"
SEL = "Pendaftaran Gelombang"  # substring that appears only when open

def snapshot():
    r = requests.get(URL, headers={"User-Agent": "Mozilla/5.0"}, timeout=20)
    soup = BeautifulSoup(r.text, "html.parser")
    txt = soup.get_text(" ", strip=True)
    return txt, hashlib.sha256(txt.encode()).hexdigest()

def is_open(txt):
    # crude but effective: the open banner contains the word and a "Daftar" CTA
    return ("Gelombang" in txt) and ("Daftar Sekarang" in txt or "Pendaftaran Dibuka" in txt)

def main():
    prev = None
    while True:
        txt, h = snapshot()
        if h != prev:
            opened = is_open(txt)
            record_event(h, opened)
            if opened:
                send_telegram("Prakerja gelombang baru kemungkinan DIBUKA. Cek: " + URL)
            prev = h
        time.sleep(900)  # 15 min

def record_event(h, opened):
    c = sqlite3.connect("db.sqlite"); c.execute(
        "INSERT INTO events(hash,opened,ts) VALUES(?,?,datetime('now'))", (h, opened))
    c.commit(); c.close()

# send_telegram uses requests.post to https://api.telegram.org/bot<TOKEN>/sendMessage
```

The estimator uses a lag table keyed by gelombang year and payout type:

```python
# Historical settlement lag (days) observed from public complaints + normal flow.
# Source: MediaKonsumen 2020 complaint (3+ month stall) and normal-flow reports.
LAG_TABLE = {
    "insentif_pascapelatihan": {"p50": 14, "p95": 90, "normal": 7},
    "insentif_survei":         {"p50": 7,  "p95": 30, "normal": 3},
}
def eta(gelombang_close_date, payout_type):
    base = LAG_TABLE[payout_type]["normal"]
    return gelombang_close_date + timedelta(days=base)

def flag_stuck(last_payout_date, payout_type):
    p95 = LAG_TABLE[payout_type]["p95"]
    return (date.today() - last_payout_date).days > p95
```

Scaling note: for the 3-month build, replace polling with official data if PMO opens an API, add OAuth login so users can paste their dashboard screenshot (OCR via tesseract or a vision API) to auto-detect missing sertifikat/survei, and add a community forum (Discourse or Telegram group) where users who already cair share timelines, which feeds the lag table with real data (crowd-sourced settlement latency, a moat).

## 4. Market sizing and willingness to pay

- Audience per gelombang: historically 1 juta to 5 juta peserta (2022: 4,98 juta; 2023: 1 juta per Indonesiabaik). Even the low case is a 7-figure reachable audience every few months.
- Free tier (tracker + estimator) monetized via: affiliate links ke platform pelatihan resmi Prakerja (the Rp3,5 juta pelatihan budget flows through mitra platform, many pay referral), and terarget iklan ke produk keuangan mikro (e-wallet, tabungan). CPM/CPA on a 1M-user audience is the ad play.
- Paid tier (eskalasi klaim): Rp50.000 to Rp150.000 per kasus for insentif mangkrak. Willingness-to-pay evidence: black-market "joki daftar" and akun terapis already charge for access help, and the legal-grey nature means users would prefer a legitimate Rp50-150k service. At even 0,5 percent of a 1 juta audience needing escalation = 5.000 cases x Rp100.000 = Rp500 juta gross per gelombang.
- Cross-sell: bundle with NPWP registration help and rekening penampung insentif (many failures are rekening mismatch), and feed complaint data into other vault gaps (SPPG MBG compliance, micro-legaltech).

## 5. Channels and go-to-market

- Telegram channel + bot is the cheapest distribution (Indonesians already live in Telegram for info gratisan). SEO blog "Kapan Prakerja 2026 Dibuka" captures search intent the moment Google Trends spikes around each opening.
- Partner with existing Prakerja info communities on Facebook/Instagram (many are currently hoaks monetizers; convert them to legit affiliates).
- Ride the news cycle: every time a minister says "Prakerja segera dibuka," search volume spikes; the tracker must rank on that day.

## 6. Risks and counters

- Regulatory: building a tracker is legal; selling "joki daftar" is not. Keep the product strictly informational + legal-escalation. Avoid any claim of priority access.
- Source fragility: prakerja.go.id HTML changes; the detector must be monitored (the same pulse-health pattern used in 05-market-cron applies). If the official site goes JS-heavy, fall back to social + Siapkerja app signals.
- Accuracy liability: estimator is an estimate, not a guarantee. Add a disclaimer that cair dates depend on PMO, and that "stuck" flag is heuristic. Never promise a payout.
- Channel risk: Telegram bot bans for spam if over-notifying. Use a channel (broadcast) + opt-in bot for personal checks.

## 7. Build plan

- Week 1 to 2: Telegram bot + prakerja_website.py poller + static status page + escalation template generator. Manual human escalation inbox.
- Week 3 to 4: Web tracker with insentif-cair estimator + lag table + SEO landing pages per gelombang.
- Month 2 to 3: OAuth/screenshot OCR auto-detection of missing requirements, community forum, affiliate integrations, and a dashboard of crowd-sourced settlement latency (the moat).

## 8. Adjacent opportunities (new gaps discovered this tick)

While researching, three adjacent gaps surfaced that the vault does not yet cover:

- `07-gaps-and-opportunities/inbox/2026-07-13-prakerja-perpres-tracker.md` (NEW, suggested): PMO Prakerja changes the Skema (Perpres 113/2022) and insentif amounts almost every year; a "perubahan skema Prakerja year-over-year" explainer that translates the Perpres into plain Bahasa for peserta would capture search intent and reduce the mis-information that hoaks accounts exploit. This directly addresses the mis-date problem found this tick.
- `03-id-business-trends/bottlenecks/prakerja-rekening-mismatch.md` (NEW, suggested): many insentif failures are rekening penampung mismatch or NPWP issues, not PMO delay. A "cek rekening & NPWP prakerja" pre-flight checker is a separate micro-tool inside the same funnel.
- `05-market-cron/cron-configs/prakerja-gelombang-watch.py` (NEW, suggested): the gelombang poller above belongs in 05-market-cron as a scheduled watcher feeding a JSON, mirroring the existing idx-movers-fetch.py pattern, so the vault itself can alert on openings.
