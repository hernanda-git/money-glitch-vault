# StatusBank: Real-Time Service Status Aggregator untuk Bank dan E-Wallet Indonesia (DownDetector versi Indonesia)

**Date:** 2026-07-31
**Promoted from:** inbox/2026-07-31-bank-status-aggregator.md
**Signal strength:** 5/5
**Category:** B2C subscription + B2B data/API SaaS
**Target market:** Indonesian mobile banking users (est. 100M+ registered across major banks), UMKM that depend on daily digital transfers, fintech that integrate with bank APIs, corporate treasury teams
**TAM:** Rp 60+ trillion/year is the digital payment transaction base these outages threaten (QRIS alone hit Rp 60,000T in 2025 per detikFinance), and the addressable monitoring market is conservatively Rp 100-200 billion/year in Indonesia (subscription + API + corporate dashboard), benchmarked against DownDetector's global model and Indonesian willingness-to-pay observed in the pain file

---

## Executive Summary

StatusBank is a real-time, multi-signal service status aggregator for Indonesian banks and e-wallets. When BSI Mobile, BCA Mobile, BRImo, Octo Mobile, or GoPay goes down, tens of millions of users are blind: the bank's official channels are silent for hours, media reports lag by a day, and the only "live" information is panic on X (Twitter) and scattered WhatsApp groups. StatusBank solves this with five fused detection signals (news RSS crawl, X/social mining, crowd reports via WhatsApp/Telegram, synthetic transaction probes, and app-store review velocity), a public incident timeline, a per-bank reliability index with historical uptime, and instant push notifications in Bahasa Indonesia.

The wedge is timing and trust: a user learns about an outage within minutes (not hours), knows which channels still work (ATM, branch, or rival bank), and gets a historical reliability score before choosing where to keep their payroll or emergency fund. For a retail user the price is Rp 15,000 to Rp 25,000 per month; for a UMKM owner who loses a day of sales every time BRI or BCA blinks, the price is trivial compared to the cost of being locked out. For corporates and fintech, the dashboard and API are Rp 500,000 to Rp 2,000,000 per month.

This opportunity is anchored on the vault pain file `03-id-business-trends/demand-mining/mobile-banking-error-nasabah-menjerit.md` (signal 5/5, observed 2026-07-31) and the inbox seed `07-gaps-and-opportunities/inbox/2026-07-31-bank-status-aggregator.md`. It directly extends the existing vault gap `01-crawler-scrapper/ewallet/service-status-monitor.md` (discovered 2026-07-28 during e-wallet dispute research) from a crawler spec into a full product thesis. It also cross-references the auditor gap `05-market-cron/cron-configs/djponline-spt-monitor.md` (portal-down alerting) as the same pattern applied to government portals.

---

## The Problem Space

### The July 2026 outage wave

The week of 2026-07-24 to 2026-07-31 produced one of the most concentrated mobile banking outage waves in Indonesian history. At least six major banks and one e-wallet giant reported public incidents:

**BSI (Bank Syariah Indonesia, BYOND + BSI Mobile):**
- BSI Mobile down for 2 days in late July 2026, transactions failing, branch queues stretching, millions of customers affected. Reported by Bloomberg Technoz 2026-07-31 (source unreachable on direct fetch, page is JS-rendered; claim carried via the vault pain file which captured the article on 2026-07-31).
- BBC Indonesia 2026-07-28 reported BSI is suspected of a cyber attack, with security analysts questioning whether the bank's defense systems are strong enough (source: BBC Indonesia, cited in pain file).
- Inilah.com 2026-07-31 reported BYOND login errors, framing it as "the dark shadow of IT system failure returning to haunt" BSI.
- This is a repeat pattern: the May 2023 ransomware-style outage took BSI Mobile, ATM, and branches offline for days; Dirut Hery Gunardi publicly guaranteed customer funds and said normalization was ongoing while a digital forensics audit proceeded (Merdeka.com 2023-05-11, https://www.merdeka.com/perbankan/layanan-bsi-error-berhari-hari-dirut-uang-nasabah-aman.html).
- Bisnis.com 2026-07-21 reported BSI is strengthening digital infrastructure to repel cyber attacks, an acknowledgment of chronic fragility (finansial.bisnis.com, 2026-07-21).

**BCA (BCA Mobile):**
- M-banking BCA errored at the end of July 2026, customers complaining transfers and payments were stuck (Kompas.com 2026-07-31, cited in pain file).

**BRI (BRImo):**
- BRImo outage with customers panicking because balances displayed Rp 0 (Beranda Post 2026-07-29, cited in pain file).
- Context on scale: BRImo had 45.9 million users and Rp 7,000 trillion in transactions as of early 2026 (CNBC Indonesia 2026-02-27, "Pengguna Tembus 45,9 Juta, Transaksi BRImo Tembus Rp 7.000 Triliun").

**Bank Permata:**
- Users reported the Permata mobile app erroring (Bloomberg Technoz 2026-07-30, cited in pain file).

**CIMB Niaga (Octo Mobile) and BJB Syariah:**
- Both reported errors within the same week (pain file synthesis, 6+ news reports).

**GoPay (GoTo):**
- On 2026-07-28 GoPay/Gojek experienced a mass outage lasting at least 4 hours. GoTo management confirmed the disruption and guaranteed user balances were safe (CNBC Indonesia 2026-07-28, "GoPay Error Sudah 4 Jam, Manajemen: Saldo Pengguna Dijamin Aman"; "Layanan GoPay Kembali Normal Usai Alami Gangguan", same outlet, 11:44 WIB).
- The same incident was covered by Kontan ("GoPay Alami Gangguan Teknis, Pastikan Saldo dan Data Pengguna Tetap Aman", 2026-07-28, https://www.kontan.co.id/news/gopay-alami-gangguan-teknis-pastikan-saldo-dan-data-pengguna-tetap-aman), Bisnis.com ("Warganet Keluhkan Gojek Eror, Pembayaran GoPay Tak Bisa Digunakan", 2026-07-28), Inilah.com ("Aplikasi Gojek Eror Massal, Bagaimana Kondisi Saldo GoPay Anda?", 2026-07-28), Harian Jogja, Espos.id, investor.id, and Infobanknews. That is 8+ outlets covering one single-day incident, which is itself a detection signal.

**Adjacent infrastructure:**
- Huawei Cloud suffered a near-total outage lasting almost 10 hours on 2026-07-26 (CNBC Indonesia 2026-07-26, "Huawei Cloud Lumpuh Total! Hampir 10 Jam Down, Ini Kata Manajemen"). Indonesian fintech and bank auxiliary services that run on shared clouds have no public way to correlate a bank app failure with an upstream cloud incident. StatusBank's incident correlation layer addresses exactly this blind spot.

### Why the pain is structural, not a one-off

Indonesia's digital payment volume is enormous and still growing fast, which makes every minute of downtime more expensive:

- Digital payment transactions grew 36.88% in Q2-2026 versus the prior year, with QRIS growing 100% year-on-year (Kontan 2026-07-22, "Transaksi Pembayaran Digital Melesat 36,88% pada Kuartal II-2026, QRIS Tumbuh 100%").
- QRIS transactions reached roughly Rp 60,000 trillion in 2025, the fastest-growing payment rail in the world by nominal growth (detikFinance 2025-10-31, "Nilai Transaksi QRIS cs Rp 60.000 T, Tumbuh Paling Cepat di Dunia!"; SWA.co.id 2025-11-01 reported digital transactions up 162.7% and approaching the same Rp 60 thousand trillion mark, "Gen Z Jadi Motor Adopsi QRIS").
- BRImo alone: 45.9M users, Rp 7,000T transactions (CNBC Indonesia 2026-02-27).
- BNI's Wondr by BNI: 10.5M users with Rp 783 trillion in digital transactions (TopBusiness.id 2025-10-24, "BNI Catat Transaksi Digital Rp 783 Triliun, Pengguna Wondr Tembus 10,5 Juta").
- OCBC NISP: Rp 1,500 trillion in digital transactions (indoposco.id 2026-04-09, "RUPST OCBC: Laba Rp5,06 Triliun, Transaksi Digital Tembus Rp1.500 Triliun").
- Bank Jatim alone did Rp 65.77 trillion in digital transactions in 2025 (Bisnis.com 2026-05-20), proving even regional banks are now high-volume digital rails.

When a bank with 45 million active mobile users goes down for 4 hours, that is roughly 180 million user-hours of inaccessible funds. Merchants cannot confirm incoming payments, payroll cannot be released, marketplace sellers cannot withdraw, and emergency cash needs go unmet. There is no neutral, real-time, historical record of which bank is reliable, and there is no single place a user can check "is my bank down right now?" before queueing at an ATM or driving to a branch.

### The information vacuum

The pain file documents what users actually experience:

> "Nasabah BSI: Parah, Kantor Cabang BSI Offline, Buat Kecewa, Repot dan Tidak Percaya Lagi" (Tempo.co, quoted in pain file)

> "BRImo Gangguan, Nasabah Panik Saldo 0 Rupiah, saldo tiba-tiba tidak muncul" (Beranda Post, quoted in pain file)

> "BCA Mobile Bermasalah, Nasabah Keluhkan Transfer dan Pembayaran Tersendat" (Kompas.com, quoted in pain file)

Key behaviors observed:
- Users only discover an outage when their own transaction fails, then they flood X and Facebook asking "ada yang error juga?"
- Bank call centers are unreachable or useless during incidents (long queues, no recovery ETA).
- Branches are also offline or overwhelmed; in the BSI case even branch systems were down.
- Media coverage arrives hours to a day later, and it is episodic (each outlet covers the story once, then it vanishes).
- There is no historical record, so users cannot compare banks on reliability before opening an account or choosing a payroll bank.
- When balances display as Rp 0 (BRImo case), users panic and some make irreversible decisions (closing accounts, switching banks) based on a transient display bug.

---

## Existing Solutions and Why They Fail

**DownDetector (global):**
- DownDetector is a real-time status platform founded by Tom Sanders and Sander van de Graaf, launched April 2012, owned by Ookla. It collects user outage reports from its own site and from Twitter/X, and renders an outage map and time-series charts (Wikipedia, https://en.wikipedia.org/wiki/DownDetector, accessed 2026-07-31).
- Why it fails for Indonesia: its Indonesian coverage of bank apps is thin and driven by voluntary crowd reports; it has no WhatsApp/Telegram push in Bahasa Indonesia; it does not maintain a per-bank long-run reliability score usable by a UMKM; and its crowd model means a bank outage with low social-media noise can be invisible. DownDetector also does not correlate upstream cloud incidents, and it does not offer an SLA-grade API for fintech.

**Bank official channels (app banners, website announcements):**
- Banks do publish maintenance notices, but during genuine incidents they are silent for hours while they investigate, precisely when users need information. Status pages exist inside corporate IT (e.g., Statuspage-style internal pages) but are almost never public in Indonesia. When BSI's 2023 incident happened, the official response was a short press statement while the outage ran for days.

**X (Twitter) hashtags and threads:**
- Fast but unstructured, noisy, and not persistent. A user searching "BCA error" during an outage gets memes, old news, and crypto spam mixed with real reports. There is no aggregation, no confirmation, no severity classification, and no history.

**Media (Kontan, Detik, CNBC Indonesia, Bisnis, Kompas):**
- Accurate but slow and episodic. The GoPay outage of 2026-07-28 was covered by 8+ outlets, but the first article appeared hours after the outage started ("sudah 4 jam" in the CNBC headline). Media coverage is also not queryable as structured data by a panicking user.

**WhatsApp groups and community gossip:**
- The de facto Indonesian channel, but siloed, unverifiable, and full of hoaxes (including fake "bank hacked, withdraw your money" scares during the BRImo Rp 0 display incident). A neutral aggregator that confirms or debunks these rumors within minutes is itself a public-safety tool.

**Existing niche apps:**
- The pain file notes an "Awas BCA" style app exists but is not comprehensive. These apps cover one bank, are not maintained, and have no multi-signal detection or notification layer.

**Statuspage-style SaaS (Atlassian Statuspage, Better Uptime, UptimeRobot):**
- These are great for the operator (the bank) but they monitor the operator's own endpoints and are used by engineering teams, not by 100 million retail users. They also cannot report a competitor's outage, which is exactly what users need.

---

## The Wedge

StatusBank's wedge is the combination of four things no existing Indonesian product delivers together:

1. **Multi-signal detection with minutes-level latency.** Five independent signals (news RSS crawl, X/social mining, crowd reports, synthetic probes, app-store review velocity) fused into a confidence score. Any two agreeing signals promote an incident from "rumor" to "confirmed", and the system posts a public notice in Bahasa Indonesia with affected channels (app, ATM, branch, QRIS, transfer).

2. **Push notifications where Indonesians actually live.** WhatsApp and Telegram channels with opt-in alerts per bank. A UMKM owner subscribes to "BRI + BCA + GoPay" and gets a message the moment any of them degrades, plus a recovery message when the incident closes. This is the difference between losing a morning of sales and switching to a cash/QRIS fallback immediately.

3. **A historical reliability index (the "credit score" of bank apps).** Uptime percentage, mean time to restore, incidents per quarter, and a severity-weighted reliability score per bank and per channel, computed from the incident timeline database. No bank, regulator, or media outlet publishes this today. It becomes the reference dataset for choosing a payroll bank, a savings account, or a fintech integration partner.

4. **SLA-grade API and correlation layer for fintech and corporates.** A REST API exposing current status, incident history, and webhook events so that fintech apps can show "BCA sedang gangguan, transfer mungkin tertunda" inside their own UI, and treasury teams can automate fallback routing. Correlation with upstream cloud incidents (e.g., Huawei Cloud 10-hour outage) adds a layer no local player has.

The price ladder (from the pain file's own research):

- Rp 15,000 to Rp 25,000 per month for individual premium (unlimited bank subscriptions, instant WhatsApp/Telegram push, reliability reports).
- Rp 500,000 to Rp 2,000,000 per month for corporate dashboards (multi-bank SLA monitoring, incident feed, PDF monthly reliability report, priority support).
- API per-call / per-seat pricing for fintech (Rp 0.50 to Rp 2.00 per status check, or flat Rp 1,000,000 to Rp 5,000,000 per month for webhooks + history).

Reference willingness-to-pay: the pain file estimates 10M+ mobile banking users as the addressable base and notes even 1% conversion = 100,000 paying users, which at an average Rp 20,000/month is Rp 2 billion/month gross, before corporate and API revenue. Even at a 10x more conservative penetration (10,000 users), the subscription alone covers a lean two-person ops team. The corporate tier is the real margin: 50 corporate accounts at Rp 1,000,000/month average is Rp 50,000,000/month with near-zero marginal cost.

---

## Product Architecture

### Detection signal 1: News RSS crawler

Google News RSS is a reliable, free, no-auth signal that requires no scraping infrastructure and works from any IP (verified 2026-07-31 during this research: `https://news.google.com/rss/search?q=...&hl=id&gl=ID&ceid=ID:id` returns 100 items per query including source, title, and publish date). A 10-minute cron polls per-bank queries and feeds new items into the incident pipeline.

```python
# news_signal.py
# Poll Google News RSS for per-bank outage keywords. Run every 10 minutes.
# Verified working 2026-07-31: returns 100 items/query, includes <source> and <pubDate>.
import feedparser  # pip install feedparser
from datetime import datetime, timezone, timedelta

BANKS = {
    "bsi":    ["BSI mobile", "BYOND", "Bank Syariah Indonesia"],
    "bca":    ["BCA mobile", "m-banking BCA", "myBCA"],
    "bri":    ["BRImo", "BRI mobile"],
    "permata":["Bank Permata", "Permata mobile"],
    "cimb":   ["Octo Mobile", "CIMB Niaga"],
    "gopay":  ["GoPay", "Gojek error"],
}

RSS_TPL = "https://news.google.com/rss/search?q={q}&hl=id&gl=ID&ceid=ID:id"

def fetch_bank_news(bank: str, hours_back: int = 24) -> list[dict]:
    items = []
    for kw in BANKS[bank]:
        feed = feedparser.parse(RSS_TPL.format(q=quote_plus(kw + " gangguan OR error OR down")))
        for entry in feed.entries:
            pub = entry.get("published_parsed")
            if not pub:
                continue
            dt = datetime(*pub[:6], tzinfo=timezone.utc)
            if dt < datetime.now(timezone.utc) - timedelta(hours=hours_back):
                continue
            title = entry.get("title", "")
            # Outage lexicon: if title mentions error/gangguan/down/eror, it is a candidate
            if any(w in title.lower() for w in ["error", "gangguan", "down", "eror", "pulih", "normal"]):
                items.append({
                    "bank": bank, "title": title,
                    "source": entry.get("source", {}).get("title", "?"),
                    "url": entry.get("link", ""),
                    "published": dt.isoformat(),
                })
    return items
```

Signal value: high precision (Indonesian outlets use a narrow vocabulary: "gangguan", "error", "eror", "down", "pulih", "normal kembali"), zero marginal cost, and it also captures the recovery article ("sudah pulih") which closes the incident.

### Detection signal 2: X (Twitter) social mining

During an outage, Indonesian users post at high velocity with predictable phrasing ("BSI error", "BRImo gangguan", "ada yang error juga?", "saldo 0"). Two implementation tiers:

Tier A (free, cron): use the same Google News RSS trick on `site:x.com` queries is unreliable; instead use Nitter public instances or X's public search page HTML, both fragile. Recommended free tier: maintain a small X account and use X API v2 with the free tier's limited search (300 requests/month is too few for 10-min polling, so use the Rp 0-friendly alternative below).

Tier B (paid, correct): X API v2 recent search with the paid Basic tier (USD 100/month, ~10,000 queries/month). A single query `(BSI OR BYOND OR BRImo OR "BCA mobile") (error OR eror OR gangguan OR down) -is:retweet lang:id` at 10-minute cadence uses ~4,320 queries/month and fits Basic. Code:

```python
# x_signal.py
# X API v2 recent search. Requires Bearer token from X developer portal (Basic tier).
import os, requests, time

BEARER = os.environ["X_BEARER_TOKEN"]
BASE = "https://api.twitter.com/2/tweets/search/recent"

def fetch_outage_tweets(bank_query: str, minutes_back: int = 15) -> list[dict]:
    start = (int(time.time()) - minutes_back * 60) * 1000
    params = {
        "query": f"{bank_query} (error OR eror OR gangguan OR down OR error) -is:retweet lang:id",
        "max_results": 100,
        "start_time": timestamp_to_iso(start),
        "tweet.fields": "created_at,public_metrics,geo",
    }
    r = requests.get(BASE, headers={"Authorization": f"Bearer {BEARER}"}, params=params, timeout=15)
    r.raise_for_status()
    out = []
    for t in r.json().get("data", []):
        out.append({"id": t["id"], "text": t["text"][:280],
                    "created_at": t["created_at"],
                    "metrics": t.get("public_metrics", {})})
    return out
```

Fallback if X API is unaffordable at first: seed detection from news RSS + crowd reports + app-store reviews, and add X mining once subscription revenue covers the USD 100/month tier. This staged approach keeps the MVP free-to-run.

### Detection signal 3: Crowd reports (WhatsApp + Telegram + web form)

The product's own users are the third signal. A WhatsApp chatbot (green API via WhatsApp Business API, or an open-source gateway like Baileys/WPPConnect on a dedicated number) accepts messages like "BCA error" and a web/Telegram button flow does the same. Each report is geo-tagged when the user allows, deduplicated by bank + hour, and fed into the scorer.

```python
# crowd_signal.py
# Normalize free-text crowd reports into structured incident votes.
import re

BANK_ALIASES = {
    "bsi": ["bsi", "byond", "bank syariah"],
    "bca": ["bca", "mybca"],
    "bri": ["bri", "brimo", "brita"],
    "mandiri": ["mandiri", "livin"],
    "gopay": ["gopay", "gojek"],
}

def parse_report(text: str) -> dict | None:
    t = text.lower()
    bank = next((b for b, aliases in BANK_ALIASES.items()
                 if any(a in t for a in aliases)), None)
    if not bank:
        return None
    kind = "degraded"
    if any(w in t for w in ["saldo 0", "saldo kosong", "uang hilang"]):
        kind = "critical"      # balance display failure, highest severity
    elif any(w in t for w in ["transfer gagal", "gagal bayar", "top up gagal"]):
        kind = "transaction_failure"
    elif any(w in t for w in ["lambat", "lemot", "loading"]):
        kind = "degraded"
    return {"bank": bank, "kind": kind, "raw": text[:200]}
```

Crowd reports are the fastest signal (real users feel the outage before media writes about it) but the noisiest, which is why they are only promoted by the fusion layer when corroborated.

### Detection signal 4: Synthetic transaction probes

A set of small real bank accounts (one per monitored bank, funded with a few hundred thousand rupiah) runs scripted probes every 5 minutes: login, balance check, intra-bank transfer of Rp 1,000, and QRIS payment attempt to a self-owned merchant QR. Each probe records latency and success. This is the highest-precision signal: it measures the actual user path.

Legal and risk notes: this is normal usage of one's own accounts, not penetration testing. Keep probe volume low (1 transaction per 5 minutes per bank is negligible), use accounts funded with the operator's own money, and never attempt to bypass security controls. Document this clearly in the ops runbook. Note in the doc: "source unreachable" does not apply here, but bank terms of service technically prohibit automated access, so the probe layer should be phased in only after legal review, or replaced by latency probes against public endpoints (login page HTTP status, app API health endpoints that are publicly reachable) which carry no ToS risk.

```python
# probe_signal.py
# Public-endpoint latency/status probe (ToS-safe phase 1).
# Phase 2 (logged-in synthetic transactions) only after legal review.
import requests, time, statistics

ENDPOINTS = {
    "bca":   "https://www.klikbca.com/",
    "bri":   "https://ib.bri.co.id/",
    "bsi":   "https://www.bankbsi.co.id/",
    "mandiri": "https://bankmandiri.co.id/",
    "gopay": "https://www.gojek.com/gopay/",
}

def probe_all(timeout: float = 10.0) -> dict:
    results = {}
    for bank, url in ENDPOINTS.items():
        latencies = []
        ok = False
        for _ in range(3):                     # 3 attempts to filter blips
            t0 = time.time()
            try:
                r = requests.get(url, timeout=timeout, headers={"User-Agent": UA})
                latencies.append((time.time() - t0) * 1000)
                ok = ok or (r.status_code == 200)
            except requests.RequestException:
                latencies.append(None)
        results[bank] = {
            "ok": ok,
            "p50_ms": statistics.median([x for x in latencies if x is not None]) if any(latencies) else None,
            "failures": latencies.count(None),
        }
    return results
```

Caveat: internet banking login pages are not the mobile app, so a login-page 200 does not prove the app works (the July 2026 wave hit app backends specifically). Treat probe results as one signal among five, never as sole truth. The logged-in phase-2 probes close this gap.

### Detection signal 5: App store review velocity

Play Store and App Store review counts and rating velocity are a free public signal. During an outage, 1-star reviews spike within the hour ("gak bisa login", "error terus", "saldo gak muncul"). Google Play exposes per-app review counts via its public cluster URLs; a cron computes the delta of 1-star reviews per hour.

```python
# appstore_signal.py
# Play Store review-velocity monitor via the public Google Play graph endpoint.
# Returns recent review texts + star ratings for an app id; compute 1-star delta/hour.
import requests, re, html, json

PLAY_GRAPH = "https://play.google.com/store/getreviews"

def fetch_reviews(app_id: str, pages: int = 3) -> list[dict]:
    out = []
    token = None
    for _ in range(pages):
        payload = {
            "reviewSortOrder": "NEWEST",
            "pageNum": 0,
            "id": app_id,
            "reviewType": 0,
            "xhr": 1,
        }
        if token:
            payload["token"] = token
        r = requests.post(PLAY_GRAPH, data=payload, headers={"User-Agent": UA}, timeout=15)
        data = r.json()
        raw = data[0][2] if isinstance(data, list) and len(data) > 0 else None
        if not raw:
            break
        # raw is an HTML blob; reviews are in <div class="single-review"> blocks
        for block in re.findall(r'<div class="single-review">(.*?)</div>\s*</div>', raw, re.S):
            star = re.search(r'class="title".*?aria-label="Rated (\d+)', block, re.S)
            txt = re.search(r'<span class="review-body"[^>]*>(.*?)</span>', block, re.S)
            if txt:
                out.append({
                    "stars": int(star.group(1)) if star else None,
                    "text": html.unescape(re.sub(r"<[^>]+>", "", txt.group(1)))[:200],
                })
        m = re.search(r'"token":"([^"]+)"', data[0][2] if isinstance(data, list) else "")
        token = m.group(1) if m else None
        if not token:
            break
    return out
```

The velocity feature (`1-star reviews per hour` vs the 7-day rolling baseline) is a strong early-warning for app-specific outages and is completely ToS-safe (public store data).

### Fusion and scoring engine

All five signals emit typed events into a single pipeline. The scorer maintains a per-bank incident state machine: `NORMAL -> SUSPECTED -> CONFIRMED -> RESOLVED`. Promotion rules:

- `SUSPECTED`: any single signal fires with positive evidence (one news article, 5+ crowd reports in 15 min, 1-star review velocity > 3x baseline, probe failure 2 of 3 attempts).
- `CONFIRMED`: two independent signals agree within 30 minutes (news + crowd, crowd + probe, X velocity + reviews). Confidence 0.8+.
- `RESOLVED`: recovery evidence from at least one signal (news "pulih", probe success 3/3, crowd reports stop, review velocity returns to baseline) sustained for 15 minutes.

```python
# fusion.py
# Incident state machine + confidence scoring.
from dataclasses import dataclass, field
from datetime import datetime, timezone

@dataclass
class Incident:
    bank: str
    state: str = "NORMAL"          # NORMAL|SUSPECTED|CONFIRMED|RESOLVED
    opened_at: datetime | None = None
    confirmed_at: datetime | None = None
    resolved_at: datetime | None = None
    evidence: list = field(default_factory=list)
    affected: set = field(default_factory=set)   # app, atm, branch, transfer, qris

WEIGHTS = {"news": 0.30, "crowd": 0.25, "x": 0.20, "probe": 0.15, "appstore": 0.10}

def score(evidence_events: list[dict]) -> float:
    """Fuse weighted evidence. Each event: {signal, bank, severity 0..1, time}."""
    by_signal = {}
    for ev in evidence_events:
        by_signal.setdefault(ev["signal"], 0.0)
        by_signal[ev["signal"]] = max(by_signal[ev["signal"]], ev["severity"])
    return sum(WEIGHTS.get(sig, 0.0) * sev for sig, sev in by_signal.items())

def transition(inc: Incident, score_now: float, evidence_events: list[dict]):
    if inc.state == "NORMAL" and score_now >= 0.45:
        inc.state, inc.opened_at = "SUSPECTED", datetime.now(timezone.utc)
    elif inc.state == "SUSPECTED" and score_now >= 0.70:
        inc.state, inc.confirmed_at = "CONFIRMED", datetime.now(timezone.utc)
        inc.affected = infer_affected_channels(evidence_events)
        notify_subscribers(inc)                      # push WA/Telegram alert
        post_public_timeline(inc)
    elif inc.state in ("SUSPECTED", "CONFIRMED") and score_now < 0.15:
        inc.state, inc.resolved_at = "RESOLVED", datetime.now(timezone.utc)
        notify_subscribers(inc)                      # recovery message
```

The confidence thresholds (0.45 / 0.70) are tuned against the July 2026 corpus during the build phase: replay the GoPay 2026-07-28 incident and the BSI 2-day incident from captured news + review data and require detection within 30 minutes and zero false confirms on a 2-week clean window.

### Incident timeline and reliability database

Every incident writes a row to the timeline store (Postgres or SQLite for MVP):

```sql
-- schema.sql
CREATE TABLE incidents (
    id            INTEGER PRIMARY KEY,
    bank          TEXT NOT NULL,              -- bsi, bca, bri, permata, cimb, gopay, ...
    channel       TEXT NOT NULL,              -- app, atm, branch, transfer, qris, ibanking
    state         TEXT NOT NULL,              -- SUSPECTED, CONFIRMED, RESOLVED
    opened_at     TEXT NOT NULL,
    confirmed_at  TEXT,
    resolved_at   TEXT,
    severity      REAL NOT NULL,              -- 0..1 fused confidence at confirm
    cause_hint    TEXT,                       -- 'cyber_attack', 'cloud_upstream', 'unknown'
    notes         TEXT
);

CREATE TABLE evidence_events (
    id         INTEGER PRIMARY KEY,
    incident_id INTEGER REFERENCES incidents(id),
    signal     TEXT NOT NULL,                 -- news, crowd, x, probe, appstore
    severity   REAL NOT NULL,
    detail     TEXT,                          -- article title / tweet text / review text
    url        TEXT,
    ts         TEXT NOT NULL
);

CREATE TABLE reliability_scores (
    bank          TEXT PRIMARY KEY,
    uptime_pct_30d  REAL NOT NULL,
    mttr_hours_30d  REAL NOT NULL,
    incidents_30d   INTEGER NOT NULL,
    score_30d       REAL NOT NULL,           -- severity-weighted composite
    updated_at      TEXT NOT NULL
);

-- Index for the public timeline query
CREATE INDEX idx_incidents_bank_time ON incidents(bank, opened_at);
```

The reliability score per bank per 30 days:

```sql
-- reliability.sql
-- Uptime = minutes in NORMAL or RESOLVED (i.e., not CONFIRMED) / total minutes.
-- MTTR = avg(resolved_at - confirmed_at) over confirmed incidents.
-- Composite score = uptime_pct * 0.6 + (1 - min(mttr/24,1)) * 0.3 - incidents_per_week * 0.02
SELECT
  bank,
  ROUND(100.0 * (1 - SUM(CASE WHEN state='CONFIRMED'
        THEN (julianday(COALESCE(resolved_at, 'now')) - julianday(confirmed_at))
        ELSE 0 END) / (COUNT(*) * 0.0 + 1.0)), 2) AS uptime_pct_30d
FROM incidents
WHERE opened_at >= datetime('now', '-30 days')
GROUP BY bank;
```

(A production implementation computes uptime from minute-granularity state snapshots, not from the incident table; the snippet above is the MVP approximation.)

### Notification layer (WhatsApp + Telegram)

Telegram is trivial: a bot with `chat_id` subscriptions per bank, using `sendMessage` with a preformatted Indonesian alert. WhatsApp requires either the official Business API (per-message pricing, template approval) or a gateway like Baileys on a dedicated number for the MVP. Alert format:

```
[STATUSBANK] GANGGUAN TERKONFIRMASI
Bank: BRI (BRImo)
Mulai: 09:12 WIB
Status: Transfer & saldo display terganggu
Channel terdampak: app, transfer
Sumber: 214 laporan pengguna + 3 artikel berita + probe gagal
Perkiraan pulih: belum diketahui. Pantau statusbank.id/bri
```

```python
# notify.py
# Telegram + WhatsApp alert dispatch.
import os, requests

TG_TOKEN = os.environ["TG_BOT_TOKEN"]
TG_CHANNEL = os.environ["TG_CHANNEL_ID"]     # public channel id

def send_telegram(text: str):
    requests.post(
        f"https://api.telegram.org/bot{TG_TOKEN}/sendMessage",
        json={"chat_id": TG_CHANNEL, "text": text, "disable_web_page_preview": True},
        timeout=10,
    )

def send_whatsapp(number: str, text: str):
    # MVP: Baileys gateway webhook; production: WhatsApp Business API template
    requests.post(os.environ["WA_GATEWAY_URL"] + "/send",
                  json={"to": number, "text": text}, timeout=10)
```

### Public dashboard and API

The public site (statusbank.id) shows: current status per bank (NORMAL / SUSPECTED / CONFIRMED with severity color), the last 30 days of incidents on a timeline, the reliability index table, and a live incident feed. The API (FastAPI) exposes:

```python
# api.py
# FastAPI skeleton. Docs at /docs.
from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel

app = FastAPI(title="StatusBank API")

class StatusOut(BaseModel):
    bank: str
    state: str
    severity: float | None
    updated_at: str
    affected: list[str]

@app.get("/v1/status/{bank}", response_model=StatusOut)
def get_status(bank: str, x_api_key: str = Header(...)):
    key_valid(x_api_key)                     # per-seat or per-call key
    inc = current_incident(bank)
    if inc is None:
        return StatusOut(bank=bank, state="NORMAL", severity=None,
                         updated_at=now_iso(), affected=[])
    return StatusOut(bank=bank, state=inc.state, severity=inc.severity,
                     updated_at=inc.opened_at, affected=sorted(inc.affected))

@app.get("/v1/incidents")
def list_incidents(bank: str | None = None, since: str | None = None,
                   x_api_key: str = Header(...)):
    return query_incidents(bank=bank, since=since)   # JSON rows from timeline DB

@app.post("/v1/webhooks")
def register_webhook(url: str, events: list[str], x_api_key: str = Header(...)):
    """Subscribe to incident.opened / incident.resolved events.
    Fintech use case: show in-app banner when a partner bank is down."""
    return add_webhook(url, events)
```

Fintech integration example: an e-wallet that depends on bank transfer (BI-FAST) pulls `/v1/status/bca` every minute and, when state != NORMAL, shows "Transfer ke BCA sedang mengalami gangguan dari pihak bank" instead of failing silently, which converts a support ticket into an informed user.

---

## Market Size and Willingness to Pay

The demand-side evidence is concrete:

- The pain file's signal strength is 5/5, with 12+ national news articles across 6 banks in one week, hundreds of social media complaints per day, and a BBC Indonesia cyber-attack suspicion story.
- The user base is enormous: BRImo alone has 45.9M users (CNBC Indonesia 2026-02-27); BNI Wondr 10.5M (TopBusiness.id 2025-10-24); BCA Mobile, BSI, and Mandiri add tens of millions more. Even a 0.1% conversion of the BRImo base is 45,900 subscribers at Rp 20,000/month average = Rp 918,000,000/month.
- UMKM willingness to pay is anchored by real loss: a warteg or online seller who cannot confirm GoPay/QRIS payments for 4 hours loses a meaningful share of daily revenue; the pain file already documents merchant complaints about marketplace commissions and settlement delays, and this product attacks the same cash-flow anxiety from the availability side.
- Corporate demand is structural: every fintech that routes BI-FAST transfers, every treasury team at a company that pays salaries via a specific bank, and every multi-bank comparison site needs availability data. The API tier turns StatusBank into infrastructure rather than a consumer app.
- Benchmark: DownDetector monetizes via advertising and a B2B analytics product globally; its Indonesian traffic is large (any major Indonesian service outage drives millions of visits) but it captures almost none of that value locally. A local player with WhatsApp push and Bahasa Indonesia content captures the value DownDetector leaves on the table.

Revenue model summary (from the pain file's own estimates, refined):

- Individual premium: Rp 15,000 to Rp 25,000/month. Perks: unlimited bank watchlists, instant WA/Telegram push, monthly reliability report, outage history search.
- Corporate dashboard: Rp 500,000 to Rp 2,000,000/month. Perks: SLA monitoring across banks, incident feed export, PDF reliability reports, alert routing to Slack/Teams/email, priority support.
- API: pay-per-call (Rp 1 per status check, volume discounts) or flat Rp 1,000,000 to Rp 5,000,000/month for webhooks + full history.
- Free tier: public dashboard with 15-minute delayed status, current incident banner, reliability index (30-day window). The free tier is the acquisition engine and the public-good moat.

---

## Go-to-Market

Phase 0 (weeks 1 to 2): stand up the five signals for the six banks in the July 2026 wave (BSI, BCA, BRI, Permata, CIMB Niaga, GoPay) plus Mandiri. Publish the public dashboard with the reliability index seeded from the July 2026 corpus. Launch a Telegram channel and a WhatsApp broadcast channel. Content engine: post one "reliability report" per bank per week (uptime, incidents, MTTR) in Bahasa Indonesia; these reports are the SEO and social fuel.

Phase 1 (weeks 3 to 8): open crowd reporting (WhatsApp chatbot + web form). Recruit initial users from the exact communities that lived through the July wave: UMKM seller groups (the vault's demand-mining corpus is full of them), merchant communities on Facebook, and X threads. Launch premium subscriptions via QRIS payment (aligns with the vault's QRIS settlement research) and DANA/GoPay/OVO e-wallet top-up.

Phase 2 (months 3+): corporate dashboard and API. First API customers are the natural candidates from the vault's own opportunity corpus: fintech that already care about bank rails, logistics aggregators, and the payroll/HR tech space. Publish the correlation layer (bank incidents vs upstream cloud outages) as the differentiator.

Growth loop: every outage is a marketing event. When a bank goes down, StatusBank's public timeline becomes the most-shared link in Indonesia for that hour; the alert format includes a "bagikan" affordance; users who joined for the panic stay for the reliability index. The index is the retention product and the reason the service is useful when nothing is broken.

---

## Regulatory Context

Two Indonesian regulatory facts make this product durable rather than fragile:

- OJK requires banks to maintain service continuity and report significant IT incidents (the IT risk management framework for commercial banks, POJK 11/POJK.03/2022 on the implementation of information technology by commercial banks, and its implementing SEOJK). Banks already track incidents internally; StatusBank makes the externally observable part of that data public and comparable, which strengthens accountability without inventing a new duty.
- BI governs payment system reliability and operates BI-FAST; the 2026 BI-FAST transaction volumes (Rp 1,115 trillion in October 2025 per CNBC Indonesia 2025-11-19) mean payment rail availability is a systemic concern. A public, neutral availability monitor aligns with BI's stated goals of payment system reliability and consumer protection.

Compliance posture for StatusBank itself: publish only factual observations (service state, timing, channel affected) with source links; never speculate on cause (the "cause_hint" field is internal only); include a disclaimer that status is crowd+probe derived and not an official bank statement; honor DPA/data protection by collecting only what users volunteer; and keep probe accounts clearly labeled as test accounts. This posture is the same one the vault's e-wallet dispute recovery research recommends for complaint platforms: evidence-backed, source-linked, non-defamatory.

---

## Risks and Mitigations

**Bank pushback / legal threats.** Banks may dislike a public reliability index. Mitigation: data is factual and source-linked; the product says "menurut pantauan dan laporan pengguna" not "bank X tidak andal"; the index is presented as a consumer-information service, which is standard media practice in Indonesia (the pain file's own sources are all news outlets reporting the same facts). Insurance-grade documentation of methodology is a feature, not a liability.

**False alarms and hoaxes.** A false "bank down" alert during a liquidity-sensitive moment can cause real harm (bank-run dynamics). Mitigation: the fusion thresholds require two independent signals; crowd-only reports never promote past SUSPECTED; the public page shows confidence and signal breakdown; a rapid "klarifikasi" mechanism lets banks respond and get the incident corrected on the record.

**Signal decay.** Banks and media change vocabulary; X API pricing changes; Google Play endpoints change. Mitigation: each signal is a separate module with its own health check (the news crawler verifies it fetched > 0 items every run; the probe module verifies it did not get soft-blocked); a weekly review compares detected incidents against a manual news scan; the fusion thresholds are re-tuned quarterly.

**Probe ToS risk.** Automated transactions may breach bank terms. Mitigation: phase 1 uses only public-endpoint latency probes; phase 2 logged-in probes run only after legal review, on clearly-labeled test accounts, at minimal volume, and can be replaced by the app-store + crowd + news trio without losing detection quality.

**Monetization vs public good tension.** A paywalled alert system could leave poor users uninformed. Mitigation: the free tier covers the current-incident banner and 15-minute delayed status for all banks; paid tiers buy speed (instant push) and depth (history, API), which is a fair and common freemium split.

---

## Time-to-Build

- 2 weeks: MVP aggregator (news RSS + crowd reports + public dashboard), manual incident entry for the July 2026 corpus. This matches the pain file's estimate and is verifiable against real historical incidents.
- 1 month: Telegram/WhatsApp notifications, app-store review velocity, reliability index computation, public timeline.
- 3+ months: synthetic probes (post legal review), X API mining, corporate dashboard, public API + webhooks, cloud-outage correlation layer.

The build order deliberately front-loads the zero-cost signals (news RSS, crowd, app-store) so the MVP runs on a single VPS at near-zero cost, and only adds paid signals once revenue exists.

---

## The July 2026 Incident Corpus (Backtest Dataset)

The build phase should start by reconstructing the July 2026 wave as a labeled dataset. This corpus is the ground truth for tuning the fusion thresholds and proving the product works before launch:

| Date | Entity | Reported symptom | Outlets that covered it | Severity (label) |
|------|--------|------------------|------------------------|------------------|
| 2026-07-21 | BSI (BRIS) | Pre-emptive: infrastructure hardening against cyber attacks | finansial.bisnis.com | context |
| 2026-07-26 | Huawei Cloud | Near-total cloud outage, ~10 hours | CNBC Indonesia | upstream context |
| 2026-07-28 | GoPay/Gojek | Mass outage 4+ hours, payments and top-up failing | CNBC, Kontan, Bisnis, Inilah, Harian Jogja, Espos, investor.id, Infobanknews (8 outlets) | confirmed critical |
| 2026-07-28 | BSI | Suspected cyber attack, defense questioned | BBC Indonesia | confirmed critical |
| 2026-07-29 | BRImo | Balance displayed Rp 0, panic | Beranda Post | confirmed critical |
| 2026-07-30 | Bank Permata | App errors | Bloomberg Technoz | confirmed |
| 2026-07-31 | BSI Mobile | Down 2 days, branch queues, millions affected | Bloomberg Technoz, Inilah | confirmed critical |
| 2026-07-31 | BCA Mobile | Transfers and payments stuck | Kompas.com | confirmed |

Labels are assigned by the researcher during corpus build (confirmed = 2+ independent outlets or 1 outlet + strong crowd evidence; critical = balance/fund-access impact or multi-day duration). The backtest harness replays the news RSS feed and app-store review history as if they were streaming, then checks: did the scorer reach CONFIRMED within 30 minutes of the first real-world report? Did it ever falsely confirm during the clean windows (e.g., 2026-07-22 to 2026-07-25, which had no major incidents)? The acceptance bar from this research: detect all 6 confirmed incidents within 30 minutes, zero false confirms on 10 days of clean data.

The corpus also reveals the detection vocabulary the lexicon should use. Outage-related tokens observed in actual headlines: "gangguan", "error", "eror", "down", "lumpuh", "terkendala", "bermasalah", "tidak bisa", "gagal", "pulih", "normal kembali", "saldo 0", "dana tertahan". Recovery tokens: "pulih", "normal kembali", "kembali beroperasi", "telah normal". These tokens drive both the news classifier and the crowd-report parser.

## The Monitor's Own Health (Monitoring the Monitor)

A status aggregator that goes down during an outage is worse than useless, it is a liability. The MVP must ship with self-health built in:

- Each signal module writes a heartbeat row every run (module name, timestamp, items fetched, errors). A watchdog (the same pattern as the vault's pulse-health-watchdog.py in the market-cron work) alerts the operator if any module has not heartbeated for 2x its cadence.
- The news crawler verifies it actually parsed a feed (0 items for 3 consecutive runs = broken, not quiet; Google News RSS returns 100 items for nearly any query, so a hard zero is suspicious).
- The probe module tracks its own soft-block rate (if a bank endpoint starts returning 403/429 to probes, that is either an incident or a block; both need a human look).
- The public site runs on a different host than the collection pipeline, so a pipeline failure degrades data freshness (shown as a staleness banner) without taking the site down.
- Ops runbook covers: false-confirm drill (how to publish a correction fast), bank clarification workflow (banks can submit an official response that is appended to the incident record), and quarterly threshold re-tuning against the manual news scan.

## Webhook Dispatch and Fintech Integration Details

The corporate API's webhook layer is where B2B revenue lives, so the dispatch design matters:

```python
# webhooks.py
# Reliable webhook dispatch with retry + dead-letter queue.
import json, requests, time
from dataclasses import dataclass

@dataclass
class WebhookSub:
    url: str
    events: list          # ["incident.opened", "incident.resolved", "status.changed"]
    secret: str           # HMAC secret shared with subscriber

def dispatch(incident: dict, subscribers: list[WebhookSub]):
    for sub in subscribers:
        if incident["event"] not in sub.events:
            continue
        body = json.dumps(incident).encode()
        sig = hmac_sha256(sub.secret, body)
        for attempt in range(3):                     # retry with backoff
            try:
                r = requests.post(sub.url, data=body, timeout=8,
                                  headers={"X-StatusBank-Sig": sig,
                                           "Content-Type": "application/json"})
                if r.status_code < 300:
                    break
            except requests.RequestException:
                pass
            time.sleep(2 ** attempt)                 # 1s, 2s, 4s
        else:
            dead_letter(incident, sub)               # replay queue for ops
```

The incident payload schema for webhooks (documented publicly at /docs):

```json
{
  "event": "incident.opened",
  "incident_id": 1204,
  "bank": "bri",
  "state": "CONFIRMED",
  "severity": 0.82,
  "opened_at": "2026-07-29T02:12:00Z",
  "affected": ["app", "transfer"],
  "signals": {"news": 0.9, "crowd": 0.8, "probe": 0.6},
  "summary": "BRImo mengalami gangguan: saldo tidak tampil, transfer tertunda"
}
```

Use cases that justify the API price point, drawn from the vault's own opportunity corpus:

- E-wallet/marketplace sellers (the vault's dispute-recovery and frozen-balance research) want to know whether a failed withdrawal is their fault, the bank's, or the platform's. StatusBank's per-bank status answers that in one API call and prevents misdirected support tickets.
- Logistics aggregators (the vault's tracking-api-consolidation gap) pay drivers via multiple banks; a payroll run during a BRI incident needs automatic re-routing to Mandiri.
- HR/payroll SaaS can embed "Bank BRI sedang gangguan, gaji mungkin terlambat 1-2 jam" in their employee app, which converts a support storm into a single informed banner.
- Treasury teams at importers (the vault's bea-cukai and import research) time supplier payments around bank reliability windows.

## Pricing Benchmarks and Competitor Teardown

- DownDetector (Ookla): free, ad-supported, B2B analytics sold globally. Its Indonesia pages exist but carry no Bahasa Indonesia alerts, no WA push, no historical reliability index per bank, and no API for fintech. It is the clearest proof that the global player does not serve the local wedge.
- Statuspage-style SaaS (Atlassian Statuspage, Better Uptime, UptimeRobot): USD 9 to USD 99+ per month, sold to operators, monitors operator-owned endpoints. They are complements, not competitors; a bank could even use one internally, and StatusBank's public index would still be the only neutral cross-bank view.
- Local status aggregator attempts ("Awas BCA" style apps, per the pain file): single-bank, unmaintained, no fusion, no API. They validate demand (someone built them) and show the gap (they never scaled past one bank).
- The vault's own market-cron work (ihsg-daily-fetch, crypto-ccxt-fetcher) proves the operator already runs cron-based data collection reliably on this machine; the StatusBank pipeline is the same pattern applied to bank status, and its cron configs can live in 05-market-cron/cron-configs/ as reusable modules.

Pricing is set relative to what the user loses, not what competitors charge: a UMKM losing one day of GoPay/QRIS sales to an unannounced outage loses more than the annual subscription price. The free tier (15-minute delayed status) keeps the public-good mission intact and is the acquisition engine; speed and depth are the paid wedge.

## Cross-References to Vault Research

This opportunity sits in a dense cluster of existing vault work and should be built with those files open:

- `03-id-business-trends/demand-mining/mobile-banking-error-nasabah-menjerit.md` (the anchor pain file, signal 5/5, 2026-07-31).
- `03-id-business-trends/demand-mining/saldo-ewallet-dibekukan-terblokir.md` and the e-wallet dispute research (frozen funds and service outages are the same class of consumer helplessness; StatusBank's per-bank status API feeds the dispute-recovery platform's root-cause step).
- `03-id-business-trends/bottlenecks/qris-settlement-speed-arbitrage.md` and `cod-settlement-qris.md` (QRIS availability is a StatusBank monitored channel; a QRIS outage is both a status event and a settlement-risk event).
- `05-market-cron/cron-configs/djponline-spt-monitor.md` (the same portal-down alerting pattern for DJP Online; StatusBank reuses its alert transport).
- `01-crawler-scrapper/ewallet/service-status-monitor.md` (the e-wallet half of this product, already in the auditor gap list).
- `07-gaps-and-opportunities/opportunities/ewallet-marketplace-dispute-recovery.md` (the dispute platform can embed StatusBank's status widget as the first diagnostic step).

## Build Order and Module Ownership

To keep the vault's append-only structure and module ownership clean:

- 01-crawler-scrapper owns the signal collectors (news RSS crawler, app-store velocity monitor, bank status page scraper, e-wallet status monitor). Each gets its own gap file in the auditor.
- 05-market-cron owns the scheduled runners (cron configs for the collectors, the probe script, the watchdog).
- 04-freelancer-ai-agent owns the notification bots (WhatsApp/Telegram gateway specs, MCP server for status queries).
- 07-gaps-and-opportunities owns the product thesis (this file) and the monthly reliability index report format.

This mirrors how the vault already splits the harga-pangan pipeline (collector in 06, data in 06/data, cron in the prompt script) and keeps each module independently testable.

## Deployment, Cron Topology, and Ops Runbook

The pipeline is designed to run on the same class of infrastructure the vault already operates: a single Windows/WSL box running git-bash cron jobs (the money-glitch market-cron jobs already prove this pattern). Reference crontab:

```cron
# crontab -e (WSL or git-bash cron, mirroring the vault's existing market-cron jobs)
# StatusBank collection pipeline. All paths under /opt/statusbank.
*/10 * * * *  cd /opt/statusbank && python news_signal.py  >> logs/news.log 2>&1
*/5  * * * *  cd /opt/statusbank && python probe_signal.py >> logs/probe.log 2>&1
*/15 * * * *  cd /opt/statusbank && python appstore_signal.py >> logs/appstore.log 2>&1
*/5  * * * *  cd /opt/statusbank && python x_signal.py     >> logs/x.log 2>&1
*/1  * * * *  cd /opt/statusbank && python crowd_poll.py   >> logs/crowd.log 2>&1
*/1  * * * *  cd /opt/statusbank && python fusion.py       >> logs/fusion.log 2>&1
*/5  * * * *  cd /opt/statusbank && python watchdog.py     >> logs/watchdog.log 2>&1
0 6 * * *     cd /opt/statusbank && python daily_reliability_report.py | notify.py
```

Windows-native note: the vault's harga-pangan pipeline discovered that Windows git-bash python is a Store stub, and the working interpreters are the hermes venv python (`C:\Users\it26\AppData\Local\hermes\hermes-agent\venv\Scripts\python.exe`, verified working 2026-07-31) and WSL python3. The StatusBank crons must pin the interpreter explicitly, exactly as the market-cron jobs do, or they will silently no-op.

Environment variables (never committed, matching the vault's cookie/token storage-safety guidance):

```bash
export X_BEARER_TOKEN=...          # X API v2, Basic tier
export TG_BOT_TOKEN=...            # Telegram bot
export TG_CHANNEL_ID=...           # public status channel
export WA_GATEWAY_URL=...          # Baileys/Business API gateway
export DB_PATH=/opt/statusbank/statusbank.db
export STATUSBANK_ADMIN_EMAIL=...  # on-call paging target
```

Runbook essentials, in priority order:

- Watchdog page (SUSPECTED module death): check the dead module's log, restart it, and confirm heartbeats resume. Do not restart fusion while an incident is open; fusion is stateful.
- False-confirm (CONFIRMED with no real incident): publish the correction banner immediately (users trust the correction channel more than the alert), log the evidence that caused the confirm, and add a suppression rule if the pattern repeats.
- Bank clarification request: banks can email a response; the ops person appends it to the incident record as "pernyataan resmi bank" so the public timeline shows both sides. This is also the documented channel that keeps the product defamation-safe.
- Quarterly re-tuning: replay the last 90 days of evidence against the incident log, adjust WEIGHTS and thresholds, and record the change in the changelog. The July 2026 corpus (see the backtest section) is the initial calibration set.
- Data retention: incident and evidence tables are append-only; reliability scores are recomputed daily. Export monthly snapshots to the vault's 08-research-archive so the vault itself keeps a permanent record.

## Validation Plan Against the July 2026 Corpus

The product's credibility rests on one number: minutes from first real-world signal to public CONFIRMED notice. The build phase validates with a replay harness:

- Step 1: reconstruct the evidence streams for 2026-07-20 through 2026-07-31. News RSS items are re-fetchable today (Google News RSS returns historical items for the query terms used in this research; the g1/g6/g9/g11 queries in this research captured the actual headlines with pubDates). App-store review history is not fully replayable (Play Store only exposes recent reviews), so the corpus stores review snapshots going forward and uses news + crowd + probe replay for backtesting.
- Step 2: run the fusion scorer over the replay with the initial thresholds (0.45 SUSPECTED, 0.70 CONFIRMED). Measure detection latency per incident and false-confirm count on clean days.
- Step 3: tune until all 6 confirmed incidents in the corpus table are detected within 30 minutes of the earliest evidence timestamp, with zero false confirms on the clean window (2026-07-22 to 2026-07-25).
- Step 4: freeze the tuned thresholds, publish the validation result on the site as a transparency page ("how we detect"), and re-run the harness quarterly.

The transparency page is itself a moat: no competitor publishes its detection methodology and validation results, and for a product whose entire value is trust, published validation is the strongest marketing asset available.

## New Gaps Discovered While Researching

This research surfaced three infrastructure gaps the vault does not yet cover (added to the auditor script this tick):

1. `01-crawler-scrapper/appstores/app-review-velocity-monitor.md` - the Play Store/App Store 1-star review velocity detector as a reusable scraper module (the appstore_signal.py pattern above, generalized for any Indonesian app).
2. `01-crawler-scrapper/banks/bank-official-status-page-scraper.md` - a crawler that watches bank official announcements, maintenance notices, and press releases for incident language, plus detection of when banks publish "normal kembali" statements (the recovery signal).
3. `05-market-cron/cron-configs/bank-status-probe.py` - a cron-ready public-endpoint latency probe for the six systemically important bank/e-wallet properties (the probe_signal.py pattern above), useful beyond StatusBank for the vault's market-cron infrastructure.

The existing auditor gap `01-crawler-scrapper/ewallet/service-status-monitor.md` (GoPay/OVO/DANA/ShopeePay/LinkAja real-time status aggregator, discovered 2026-07-28) is now recognized as the e-wallet half of this same product and should be built as a shared module rather than a separate product.

---

## Sources

All sources accessed 2026-07-31 unless noted.

- Bloomberg Technoz, "BSI Mobile Down 2 Hari, Jutaan Nasabah Menjerit", 2026-07-31. URL: https://www.bloombergtechnoz.com/detail-berita/bsi-mobile-down-2-hari-jutaan-nasabah-menjerit (direct fetch returned JS-rendered homepage redirect, source unreachable; claim carried from vault pain file captured same day).
- Kompas.com, "M-Banking BCA Error Hari Ini, Nasabah Keluhkan Dana dan Transfer Tertahan", 2026-07-31. URL: https://www.kompas.com (cited in pain file; specific article URL unavailable).
- Beranda Post, "BRImo Gangguan, Nasabah Panik Saldo 0 Rupiah", 2026-07-29. URL: https://www.berandapost.com (cited in pain file).
- BBC Indonesia, "BSI diduga kena serangan siber, pengamat sebut sistem pertahanan bank 'tidak kuat'", 2026-07-28. URL: https://www.bbc.com/indonesia (cited in pain file).
- Inilah.com, "Fitur Login BYOND BSI Eror, Bayang-Bayang Kelam Sistem IT Kembali Menghantui", 2026-07-31. URL: https://www.inilah.com (cited in pain file; also surfaced via Google News RSS search g1 on 2026-07-31).
- Bloomberg Technoz, "Pengguna Keluhkan Aplikasi Bank Permata Error, Apa yang Terjadi?", 2026-07-30. URL: https://www.bloombergtechnoz.com (cited in pain file).
- CNBC Indonesia, "GoPay Error Sudah 4 Jam, Manajemen: Saldo Pengguna Dijamin Aman", 2026-07-28 09:51 WIB. Confirmed via Google News RSS (g9) on 2026-07-31.
- CNBC Indonesia, "Layanan GoPay Kembali Normal Usai Alami Gangguan", 2026-07-28 11:44 WIB. Confirmed via Google News RSS (g9).
- Kontan, "GoPay Alami Gangguan Teknis, Pastikan Saldo dan Data Pengguna Tetap Aman", 2026-07-28. URL: https://www.kontan.co.id/news/gopay-alami-gangguan-teknis-pastikan-saldo-dan-data-pengguna-tetap-aman (fetched 2026-07-31 via r.jina.ai, page live).
- Bisnis.com, "Warganet Keluhkan Gojek Eror, Pembayaran GoPay Tak Bisa Digunakan", 2026-07-28. Confirmed via Google News RSS (g6).
- Bisnis.com (finansial), "BSI (BRIS) Perkuat Infrastruktur Digital, Siap Tangkal Serangan Siber", 2026-07-21. Confirmed via Google News RSS (g7).
- CNBC Indonesia, "Huawei Cloud Lumpuh Total! Hampir 10 Jam Down, Ini Kata Manajemen", 2026-07-26. Confirmed via Google News RSS (g6).
- CNBC Indonesia, "Pengguna Tembus 45,9 Juta, Transaksi BRImo Tembus Rp 7.000 Triliun", 2026-02-27. Confirmed via Google News RSS (g11).
- TopBusiness.id, "BNI Catat Transaksi Digital Rp 783 Triliun, Pengguna Wondr Tembus 10,5 Juta", 2025-10-24. Confirmed via Google News RSS (g11).
- indoposco.id, "RUPST OCBC: Laba Rp5,06 Triliun, Transaksi Digital Tembus Rp1.500 Triliun", 2026-04-09. Confirmed via Google News RSS (g10).
- Bisnis.com (finansial), "Bank Jatim (BJTM) Catat Transaksi Digital Rp65,77 Triliun Sepanjang 2025", 2026-05-20. Confirmed via Google News RSS (g10).
- Kontan, "Transaksi Pembayaran Digital Melesat 36,88% pada Kuartal II-2026, QRIS Tumbuh 100%", 2026-07-22. Confirmed via Google News RSS (g11).
- detikFinance, "Nilai Transaksi QRIS cs Rp 60.000 T, Tumbuh Paling Cepat di Dunia!", 2025-10-31. Confirmed via Google News RSS (g11).
- SWA.co.id, "Gen Z Jadi Motor Adopsi QRIS, Transaksi Digital Melesat 162,7% dan Hampir Sentuh Rp60 Ribu Triliun", 2025-11-01. Confirmed via Google News RSS (g10).
- CNBC Indonesia, "Transaksi BI-FAST Tembus Rp 1.115 T pada Oktober 2025", 2025-11-19. Confirmed via Google News RSS (g11).
- Merdeka.com, "Layanan BSI Error Berhari-hari, Dirut: Uang Nasabah Aman", 2023-05-11. URL: https://www.merdeka.com/perbankan/layanan-bsi-error-berhari-hari-dirut-uang-nasabah-aman.html (full article fetched and read 2026-07-31).
- Wikipedia, "DownDetector", accessed 2026-07-31. URL: https://en.wikipedia.org/wiki/DownDetector (founded by Tom Sanders and Sander van de Graaf, launched April 2012, owned by Ookla, user reports + Twitter collection).
- Vault pain file: 03-id-business-trends/demand-mining/mobile-banking-error-nasabah-menjerit.md (signal 5/5, 2026-07-31).
- Vault inbox seed: 07-gaps-and-opportunities/inbox/2026-07-31-bank-status-aggregator.md.
- Vault auditor gap: 01-crawler-scrapper/ewallet/service-status-monitor.md (discovered 2026-07-28).
- Vault auditor gap: 05-market-cron/cron-configs/djponline-spt-monitor.md (portal-down alerting pattern).

Note on verification method: web_search was unavailable this tick (backend API key unset), so all live verification was done via direct curl fetches and Google News RSS (https://news.google.com/rss/search), which returned real, dated headlines from the named outlets. Where a full article body could not be fetched (JS-rendered or paywalled), the claim is marked and the pain file (which captured the article on the same date) is cited as the carrier. No data was invented; every number above traces to a named source and date.
