# QRIS Settlement Speed Arbitrage (the float trap for 32M Indonesian merchants)

> QRIS (Quick Response Code Indonesian Standard) is the official national QR payment standard mandated by Bank Indonesia. By 2024 it had onboarded 32.71 million merchants and processed Rp42 trillion in annual transaction value (Wikipedia, citing BI data). Yet the settlement rail that moves money from a scanned code into a merchant's usable bank balance is still batch, bank-hours, and T+1 by default. That 1 to 3 day float is a structural tax on the working capital of micro merchants who live on daily cashflow. A platform that guarantees same-day (or instant) QRIS settlement for a sub-0.1 percent fee sits on top of an existing, mandated, fast-growing rail and could capture recurring, low-churn revenue. This document breaks down the timing mechanics, the float math, who pays, and where the wedge is.

**File:** `03-id-business-trends/bottlenecks/qris-settlement-speed-arbitrage.md`
**Created:** 2026-07-10
**Category:** Bottleneck analysis
**Priority:** HIGH
**Related files:**
- `03-id-business-trends/bottlenecks/cod-settlement-infrastructure.md`
- `03-id-business-trends/demand-mining/umkm-kredit-bottleneck.md`
- `03-id-business-trends/demand-mining/saldo-penjual-shopee-dibekukan.md`
- `07-gaps-and-opportunities/opportunities/digital-credit-scoring-umkm-qris.md`
- `07-gaps-and-opportunities/inbox/2026-06-30-cross-border-qris-credit-scoring.md`

---

## Table of Contents

1. [What QRIS Actually Is](#1-what-qris-actually-is)
2. [The Settlement Rail: How Money Moves From Scan To Balance](#2-the-settlement-rail-how-money-moves-from-scan-to-balance)
3. [The T+1 Float Problem, Quantified](#3-the-t1-float-problem-quantified)
4. [Why It Matters More For Micro Merchants Than Aggregators](#4-why-it-matters-more-for-micro-merchants-than-aggregators)
5. [The Unit Economics of Float](#5-the-unit-economics-of-float)
6. [Worked Example: A Warung Owner In Cirebon](#6-worked-example-a-warung-owner-in-cirebon)
7. [BI-FAST Exists But Is Not The Default For QRIS Merchant Payout](#7-bi-fast-exists-but-is-not-the-default-for-qris-merchant-payout)
8. [MDR, Acquirer Credits, and Who Already Earns On The Rail](#8-mdr-acquirer-credits-and-who-already-earns-on-the-rail)
9. [Cross-Border QRIS Settlement: A Separate And Larger Float Problem](#9-cross-border-qris-settlement-a-separate-and-larger-float-problem)
10. [The Regulatory Frame: BI PADG 21/18 and MDR Caps](#10-the-regulatory-frame-bi-padg-2118-and-mdr-caps)
11. [Why Banks Do Not Offer Same-Day QRIS Settlement Voluntarily](#11-why-banks-do-not-offer-same-day-qris-settlement-voluntarily)
12. [Existing Solutions And Why They Fall Short](#12-existing-solutions-and-why-they-fall-short)
13. [The Wedge: A Same-Day Settlement Layer](#13-the-wedge-a-same-day-settlement-layer)
14. [Proposed Technical Architecture](#14-proposed-technical-architecture)
15. [QRIS Open API As The Integration Surface](#15-qris-open-api-as-the-integration-surface)
16. [Pricing Model And What People Would Pay](#16-pricing-model-and-what-people-would-pay)
17. [Cross-Border Micro-Merchant Credit Scoring Extension](#17-cross-border-micro-merchant-credit-scoring-extension)
18. [Risks, Constraints, And Regulatory Landmines](#18-risks-constraints-and-regulatory-landmines)
19. [New Gaps Discovered](#19-new-gaps-discovered)
20. [References And Source Notes](#20-references-and-source-notes)

---

## 1. What QRIS Actually Is

QRIS is the Quick Response Code Indonesian Standard, a national QR payment standard developed by Bank Indonesia (BI) together with the Indonesian Payment System Association (ASPI). The name is a wordplay on "keris," the traditional dagger, and stands for "Kode QR Standar Indonesia." It was launched on 17 August 2019 (Indonesia's 74th independence day) following BI Board of Governor Decree No. 21/18/PADG/2019 on the implementation of the QR national standard for payment purposes (Wikipedia, "QRIS").

Before QRIS, every payment app issued its own proprietary QR. A GoPay QR could not be read by OVO, a DANA QR could not be read by ShopeePay. Merchants had to plaster four or five different stickers on the cashier. QRIS unified them into a single, EMVCo-compatible code that any participating app can scan. Per Bank Indonesia's own description, QRIS "menyatukan" (unifies) the various QR codes issued by Penyelenggara Jasa Sistem Pembayaran (PJSP, Payment Service Providers) so one code works across all of them (Kompas, "Apa Itu QRIS," 6 August 2024).

Key structural facts:

- QRIS is mandatory. All PJSPs that offer QR payments must implement it. There is no opt-out for licensed payment players.
- It supports both person-to-merchant (P2M) and person-to-person (P2P) flows.
- A dynamic QR (nominal embedded) and a static QR (fixed merchant ID) both exist. Dynamic QR is used at POS and online checkout; static QR is the printed sticker on the warung wall.
- QRIS Tap, an NFC variant, was added later and is live as of the QRIS-TAP page on the BI site.
- Transaction growth has been explosive. Wikipedia, citing BI, reports QRIS transaction volume surged 226.54 percent year on year, reaching 50.50 million users and 32.71 million merchants onboarded by 2024, with total annual transaction value of Rp42 trillion (about USD 2.57 billion). Those are 2024 figures; the rail has only grown since.

The point for this document: 32.71 million merchants is a massive, captive, fast-growing surface. Almost none of them have a settlement product tuned to their cashflow. They accept QRIS because they must, but the money arrives on bank terms, not merchant terms.

## 2. The Settlement Rail: How Money Moves From Scan To Balance

The scan is instant. The settlement is not. Understanding the gap requires tracing the path a single rupiah takes after a customer scans a warung's QRIS code.

Step by step for a P2M QRIS transaction in Indonesia:

1. Customer opens a QRIS-enabled app (GoPay, OVO, DANA, ShopeePay, or a mobile banking app from BCA, BRI, BNI, Mandiri, etc.) and scans the merchant QR.
2. The app sends an authorization request to the customer's PJSP (the issuer/acquirer on the customer side).
3. The PJSP routes the transaction through the national QR switch operated under BI/ASPI rules. The switch identifies the merchant's acquiring PJSP via the NMID (National Merchant ID) encoded in the QR.
4. The customer's funds are debited in near real time and held in the switching/settlement layer.
5. The merchant's acquiring bank or e-wallet receives a credit entry. This is where the lag begins.
6. The acquiring PJSP batches merchant credits and moves them to the merchant's settlement account, typically on a T+1 basis aligned with bank clearing windows.
7. The merchant sees the balance as "settled" and can withdraw or use it. If the merchant's settlement account is at a different bank than the acquirer, an interbank transfer adds another hop.

The critical observation: steps 1 through 4 happen in seconds. Steps 5 through 7 happen on a schedule. The scheduled batch, combined with bank cut-off times (usually around 16:00 to 17:00 WIB for same-day interbank rails), means a transaction at 18:00 on Friday settles on Monday. That is a three-day float for a weekend sale.

This is not a bug specific to QRIS. It is the legacy of Indonesia's batched national clearing system (SKNBI). But QRIS sits on top of that legacy clearing for the merchant payout leg, so merchants inherit the slowness even though the scan was instant.

Note on source transparency: Bank Indonesia's QRIS pages (bi.go.id/fungsi-utama/.../qris) were intermittently unreachable on the connection used for this research (TLS handshake failures), so the precise BI-published settlement SLA for the merchant payout leg could not be quoted verbatim. The T+1 default is documented behaviorally across merchant onboarding materials (Bittime notes "proses aktivasi 1-7 hari kerja" for onboarding, not settlement, but merchant forums and aggregator docs consistently describe next-day payout as the norm) and is consistent with Indonesia's batched clearing architecture. Any platform builder must confirm the exact SLA with their acquiring PJSP before making product promises.

## 3. The T+1 Float Problem, Quantified

"Float" is the money that has been collected from customers but not yet made available to the merchant. It is interest-free working capital that sits in the settlement layer.

Assume a micro merchant does Rp 1,000,000 of QRIS sales per day (about USD 62, a realistic warung or online seller number). At T+1 settlement with a daily batch after the cut-off, the merchant always has roughly one day of sales in flight, plus weekend amplification.

Conservative float model:

- Average in-flight balance: 1.0 to 1.5 days of sales on weekdays = Rp 1,000,000 to Rp 1,500,000.
- Weekend effect: Friday evening through Sunday sales settle Monday, so Friday+Saturday+Sunday = ~3 days of sales in flight over the weekend = Rp 3,000,000.
- Average annual in-flight float for this single merchant: roughly Rp 1,300,000, continuously.

Now scale. If 32.71 million merchants each hold even Rp 500,000 of in-flight float on average (a deliberately low number, many hold far more), total systemic float is about Rp 16.3 trillion sitting unproductively in settlement accounts at any given moment. That is the size of the pool a same-day settlement product competes to unlock.

The merchant does not "lose" this money; they lose the use of it. For a business running on 5 to 10 percent weekly margins, a one-day delay on receivables is the difference between being able to restock tonight or missing tomorrow's sales.

## 4. Why It Matters More For Micro Merchants Than Aggregators

Large merchants and aggregators have treasury teams, credit lines, and the bargaining power to negotiate faster payouts or to simply absorb the float. A national retailer with Rp 10 billion in monthly QRIS volume can fund its inventory from a bank line and treat the T+1 as irrelevant.

Micro merchants cannot.

The asymmetry:

- A warung owner in Cirebon buying vegetables at 05:00 needs yesterday's QRIS money in her account before the wholesaler market closes at 09:00. T+1 means Friday's sales are not usable until Monday. She either borrows from the arisan, runs a tab with the supplier, or misses the early-morning price.
- An online seller on TikTok Shop or Shopee who prints QRIS for repeat buyers needs the cash to buy raw materials for the next batch. The gap forces her into the informal credit market at 5 to 10 percent per week (see `umkm-kredit-bottleneck.md`).
- A food cart near a campus settles at night; the cart owner buys ingredients each morning. The float directly suppresses how much he can cook and sell.

This is why settlement speed is not a "nice to have" for the 32.71 million, it is a working-capital product. The wedge is not "faster payments" as a feature, it is "working capital as a service" layered on a rail they already use.

## 5. The Unit Economics of Float

To size the opportunity, treat settlement speed as a fee-for-speed product. The merchant is effectively renting their own float back, one day earlier, for a fee.

Reference rates as of research (Indonesia, mid-2026 context):

- BI 7-Day Reverse Repo Rate has hovered around 5.5 to 6.0 percent through 2024 to 2025 (source: BI rate page, bi.go.id/id/statistik/indikator/bi-rate.aspx, reachable). That is the risk-free opportunity cost of one day of float: roughly 0.015 to 0.016 percent per day.
- Informal merchant loan rates run 5 to 15 percent per week (260 to 780 percent annualized) for unbanked micro merchants. This is the rate the float would otherwise be borrowed at.
- QRIS MDR for UMKM is around 0.3 percent per transaction (Bittime, "Cara Buat QRIS All Payment 2026"). That is the established willingness-to-pay benchmark for a payments tax.

A same-day settlement product priced at 0.1 percent of settled volume is:

- One third of the MDR the merchant already pays, so psychologically cheap.
- About 6 to 7 times the risk-free daily float cost, so the provider is compensated for advancing the money.
- A tiny fraction (roughly 1 to 2 percent) of the informal loan rate, so the merchant is unambiguously better off using it instead of borrowing.

At 0.1 percent on Rp 1,000,000 daily volume, the merchant pays Rp 1,000 per day, or Rp 30,000 per month, to get their money same-day. In return they avoid a Rp 50,000 to Rp 150,000 informal loan or a lost restock. The value exchange is lopsided in the merchant's favor, which is exactly what you want for adoption.

Provider side: advancing Rp 1,000,000 for one day at 0.1 percent yields Rp 1,000 gross. To make this work the provider needs either (a) a warehouse line of credit at sub-0.05 percent per day, or (b) to net across millions of merchants so the float advanced to merchant A is covered by float collected from merchant B that same day (the marketplace-balance model). Model (b) is the real wedge: a settlement aggregator does not need much capital if its inflows and outflows are large and offsetting.

## 6. Worked Example: A Warung Owner In Cirebon

Ibu Siti runs a warung in Cirebon with Rp 1,200,000 average daily QRIS sales (customers scanning her static QR for groceries and cooked food). Her acquiring bank pays out next business day.

Current state, a normal week:

- Monday sales (Rp 1.2M) land Tuesday.
- Friday evening sales (Rp 0.8M, after 17:00 cut-off) plus Saturday (Rp 1.2M) and Sunday (Rp 1.0M) all land Monday = Rp 3.0M in flight over the weekend.
- Her average usable balance lags her real sales by 1.3 days.

The pain point: Sunday night she realizes she is short Rp 700,000 to buy vegetables Monday at 05:00 wholesale prices. The QRIS money from the weekend is stuck until Monday afternoon. She borrows Rp 700,000 from the supplier at 10 percent per week = Rp 70,000 interest, or skips the early buy and pays 15 percent more at the retail market.

With same-day settlement at 0.1 percent:

- Every day's QRIS money is in her account by 20:00 the same day (or instantly for dynamic QR checkout).
- Sunday's Rp 1.0M is available Sunday night. She buys vegetables Monday at wholesale. She pays the settlement product Rp 1,200 per day = Rp 36,000/month.
- She eliminates the Rp 70,000 weekly informal loan = Rp 280,000/month saved, net positive by Rp 244,000/month, about 20 percent of her food cost swing.

For 32.71 million merchants, even if only 5 percent (1.6M) adopt at Rp 1,000/day average fee on Rp 1M daily volume, that is Rp 1.6 billion per day in fees, or roughly Rp 48 billion per month, recurring. This is a payments-adjacent annuity, not a one-time sale.

## 7. BI-FAST Exists But Is Not The Default For QRIS Merchant Payout

Bank Indonesia operates BI-FAST, an interbank credit transfer service that processes transactions in real time, 24/7, with a per-transaction fee capped at Rp 2,500 (source: BI, bi-fast documentation; BI-FAST was launched in 2021 and the fee was later reduced to Rp 2,500). So the raw capability for instant settlement already exists in the national plumbing.

The catch: BI-FAST is a consumer/corporate transfer rail, not the default merchant payout mechanism for QRIS. QRIS merchant payouts are handled by the acquiring PJSP's internal batching and then an interbank transfer if the merchant banks elsewhere. Most merchants experience T+1 because their acquirer batches rather than because the national rail cannot move faster.

This is the central insight of the arbitrage: the speed is available, the orchestration is missing. A settlement layer that, on behalf of the merchant, pulls the BI-FAST rail (or the acquirer's real-time API where available) to push merchant funds the same day is technically feasible today. The blocker is commercial, not technical: acquirers have no incentive to accelerate payout because the float earns them spread, and merchants lack the integration muscle to demand it.

## 8. MDR, Acquirer Credits, and Who Already Earns On The Rail

QRIS is not free to operate. The Merchant Discount Rate (MDR) is the fee split among the parties. For UMKM the MDR is capped around 0.3 percent (Bittime, 2026). That 0.3 percent is split between the issuer, the acquirer, the switch, and ASPI/BI scheme fees.

Where the float value goes today:

- The acquirer holds merchant funds from scan to payout. During that hold the acquirer can invest the float or use it for its own liquidity. The acquirer therefore has a mild disincentive to accelerate payout.
- The issuer (customer's app) debits instantly and has no float problem on its side.
- The merchant is the only party starved of liquidity, and the only party with no seat at the table to negotiate speed.

A same-day settlement product inserts a new actor, the settlement orchestrator, who pays the merchant early and is reimbursed by the acquirer's batch later, charging the merchant a transparent 0.1 percent for the service. This is structurally similar to invoice factoring, but for QR receivables and at a fraction of factoring rates.

## 9. Cross-Border QRIS Settlement: A Separate And Larger Float Problem

QRIS Antarnegara (cross-border QRIS) has expanded fast and creates a settlement problem an order of magnitude worse than domestic.

Per the Indonesian Wikipedia "QRIS" article, the cross-border rollout timeline is:

- Thailand (Thai QR Payment / PromptPay): 29 August 2022
- Malaysia (DuitNow): 8 May 2023
- Singapore (SGQR+ / NETS QR): 17 November 2023
- Japan (JPQR Global): 17 August 2025 (first non-ASEAN country, launched on Indonesia's 80th independence day)
- South Korea (Seoul Pay, Jeju Pay / Tamna Jeon): 1 April 2026
- Planned future links: India, China, and Saudi Arabia.

So as of mid-2026, an Indonesian merchant can be paid by a tourist from at least five countries via QRIS Antarnegara. The settlement involves two central banks, two currencies, and FX conversion. The payout to the Indonesian merchant is slower and the float larger because of the cross-currency leg. A merchant in Bali accepting SGQR+ payment from a Singaporean tourist may wait several business days for the rupiah to land, and bears FX timing risk on top.

This is the exact gap logged in `07-gaps-and-opportunities/inbox/2026-06-30-cross-border-qris-credit-scoring.md`: cross-border QRIS micro-merchants have a unique credit profile and no one builds scoring or faster settlement for them. The settlement-speed product and the credit-scoring product are two faces of the same cross-border float problem.

## 10. The Regulatory Frame: BI PADG 21/18 and MDR Caps

The QRIS standard is governed by BI Board of Governor Decree No. 21/18/PADG/2019 (ratified 16 August 2019). Any settlement-layer product must operate as a registered PJSP or partner with one, because holding or moving customer funds requires a license (or a partnership with a licensed bank/acquirer). The payment aggregator cannot simply take merchant money into its own account; that would be unlicensed fund holding.

Practical structures:

- License-light: partner with an acquiring bank or e-money PJP that already holds the license, and provide the orchestration/UX layer on top. The bank remains the fund holder; the product improves the payout speed via BI-FAST or the bank's real-time API.
- Full license: obtain e-money or payment gateway registration from BI. Higher capex, full control.
- Model (a) is the realistic entry wedge for a startup. Model (b) is the eventual moat.

The MDR cap (around 0.3 percent for UMKM) also caps how much can be stacked on top. A 0.1 percent settlement fee sits within headroom but a same-day product must be careful not to push total cost above merchant tolerance. The 0.1 percent figure is a design choice, not a regulatory limit; BI could in principle object to "double charging," so the fee must be positioned as a voluntary acceleration service the merchant opts into, not a mandatory tax.

## 11. Why Banks Do Not Offer Same-Day QRIS Settlement Voluntarily

If BI-FAST can move money instantly, why does no bank market "same-day QRIS payout" to warungs? Four reasons:

1. Float income. The batched hold earns the acquirer spread. Accelerating payout removes that.
2. Batch operational simplicity. Banks built their settlement on SKNBI batch windows. Re-architecting to real-time per-merchant payout is engineering work with no obvious revenue upside for them.
3. No merchant demand signal. Micro merchants do not file tickets asking for faster settlement; they just borrow informally. The pain is invisible to the bank.
4. Risk. Advancing funds before the acquirer batch reconciles introduces counterparty and fraud exposure the bank's risk team dislikes.

All four are exactly the conditions a focused fintech can exploit: the bank will not build it, the merchant needs it, and the technical rails (BI-FAST, acquirer APIs, QRIS Open API) already exist.

## 12. Existing Solutions And Why They Fall Short

What exists today that touches this problem:

- Bank merchant dashboards (BCA livin' Merchant, Mandiri, BRI, BNI merchant portals). They show QRIS transactions but pay out on the bank's default schedule. No acceleration product.
- E-wallet merchant accounts (GoPay for Business, OVO, DANA, ShopeePay). Payout to linked bank is T+1 to T+2. Some offer "instant withdrawal" to the e-wallet balance but not to the merchant's bank, and the e-wallet balance itself is then stuck behind another withdrawal limit.
- QRIS Open API aggregators (qris.id, interactive.co.id). These let software generate dynamic QRIS and receive notifications, but their value prop is integration and "pencairan dana di semua bank" (payout to all banks), not speed. They still ride the acquirer's batch.
- Invoice factoring and supply-chain finance players. Serve larger businesses, not Rp 1M/day warungs, and price at factoring rates (several percent), not 0.1 percent.
- BI-FAST for the consumer. Available to individuals sending money, but not packaged as a merchant receivables accelerator.

None of these is positioned as "your QRIS money, in your bank account tonight, for 0.1 percent." That positioning is open.

## 13. The Wedge: A Same-Day Settlement Layer

The wedge is a thin orchestration layer, not a new rail. It does three things:

1. Sits between the merchant's QRIS acquirer and the merchant's bank account.
2. On each settled QRIS transaction, advances the merchant the equivalent amount the same day (via BI-FAST or the acquirer's real-time payout API where available), then is reimbursed when the acquirer's batch lands.
3. Charges a flat, transparent 0.1 percent (or a per-transaction floor like Rp 250) for the acceleration, billed only when the merchant opts in per transaction or per day.

Why this is defensible:

- It is license-light if built on a partner bank.
- It needs little net capital if it nets across a large merchant base (inflows from batch reimbursement offset outflows to merchants).
- It is sticky: once a warung's daily restock depends on tonight's payout, churn is near zero.
- It is regulator-friendly: it makes QRIS more useful, which aligns with BI's financial-inclusion mandate.

## 14. Proposed Technical Architecture

The system is an event-driven settlement orchestrator. Below is a concrete skeleton in Python (pseudo-production, comments explain each step). This is the same architectural family as the canonical bot skeleton in `02-trading-bot/architectures/event-driven-baseline.md`: a queue, a state machine, idempotent handlers.

```python
# qris_instant_settle/settlement_orchestrator.py
# Thin layer that advances QRIS merchant payouts the same day.
# Assumes a partner acquiring bank exposes:
#   - webhook: transaction.settled (merchant gets credited in batch T+1)
#   - API:     POST /v1/payout/instant  (pushes to merchant bank via BI-FAST)
# The orchestrator nets across merchants so capital need is small.

import os, time, json, hmac, hashlib, asyncio
from dataclasses import dataclass, field
from enum import Enum

class SettlementState(str, Enum):
    SCANNED = "scanned"            # customer paid, in switch
    BATCH_QUEUED = "batch_queued"  # acquirer will pay T+1
    ADVANCED = "advanced"          # we paid merchant early
    REIMBURSED = "reimbursed"      # acquirer batch repaid us
    FAILED = "failed"

@dataclass
class QRISReceivable:
    txn_id: str
    merchant_id: str
    amount_idr: int
    fee_bps: int = 10              # 0.1% acceleration fee (10 bps)
    state: SettlementState = SettlementState.BATCH_QUEUED
    advanced_at: float = 0.0
    reimbursed_at: float = 0.0

# In-memory store; in prod use Postgres + a ledger. Shown for clarity.
LEDGER: dict[str, QRISReceivable] = {}

PARTNER_BANK_KEY = os.environ["PARTNER_BANK_WEBHOOK_SECRET"]

def verify_webhook(body: bytes, signature: str) -> bool:
    # Acquirer signs payload with HMAC-SHA256. Always verify before trusting.
    expected = hmac.new(PARTNER_BANK_KEY.encode(), body, hashlib.sha256).hexdigest()
    return hmac.compare_digest(expected, signature)

async def on_acquirer_batch_event(r: QRISReceivable):
    """Called when the acquirer's T+1 batch finally credits us back."""
    r.state = SettlementState.REIMBURSED
    r.reimbursed_at = time.time()
    # Capital freed; available to advance another merchant. Netting works here.

async def advance_to_merchant(r: QRISReceivable):
    """Push funds to merchant bank same-day via BI-FAST through partner bank."""
    fee = int(r.amount_idr * r.fee_bps / 10_000)   # 0.1% of amount
    net = r.amount_idr - fee
    payload = {
        "merchant_id": r.merchant_id,
        "amount_idr": net,
        "ref": r.txn_id,
        "rail": "BI_FAST",          # real-time 24/7 interbank rail
    }
    # POST to partner bank payout API (omitted: auth, retries, idempotency key)
    r.state = SettlementState.ADVANCED
    r.advanced_at = time.time()
    LEDGER[r.txn_id] = r
    # Schedule reconciliation against the T+1 batch reimbursement.
    asyncio.create_task(wait_for_reimbursement(r))

async def wait_for_reimbursement(r: QRISReceivable):
    # In prod this is driven by the acquirer batch webhook, not a sleep.
    # Shown to illustrate the netting cycle.
    await asyncio.sleep(0)  # placeholder for webhook-driven reimbursement
```

The idempotency and reconciliation logic is the hard part. Because payouts and reimbursements arrive on different schedules, every transaction needs a stable `txn_id` and a state machine that tolerates duplicate webhooks (the carrier/webhook reliability problem documented in `03-id-business-trends/bottlenecks/carrier-webhook-reliability.md` applies here too: QRIS acquirer webhooks are also best-effort and non-idempotent).

## 15. QRIS Open API As The Integration Surface

The QRIS Open API Platform (qris.id/homepage/open-api) lets a software vendor generate dynamic QRIS codes and receive transaction notifications, "support semua pembayaran dompet digital" (all e-wallet payments) through one integration. This is the natural integration surface for the settlement layer:

- Generate a dynamic QR per checkout with the exact nominal.
- Receive the "transaksi masuk" (transaction received) notification via the app or webhook.
- Trigger the same-day advance immediately on notification, rather than waiting for the acquirer batch.

The Open API removes the need to integrate per e-wallet. One QRIS integration covers GoPay, OVO, DANA, ShopeePay, LinkAja, and mobile banking. That is the same "universal integration tax" thesis behind `04-freelancer-ai-agent/mcp-servers/logistics-orchestrator-mcp.md`, applied to payments instead of logistics.

## 16. Pricing Model And What People Would Pay

Pricing tiers that map to merchant behavior:

- Per-transaction opt-in: 0.1 percent of the advanced amount, with a floor of Rp 250 per advance. Merchant pays only when they choose speed. Best for occasional need (weekend restock).
- Daily auto-advance subscription: Rp 15,000 to Rp 30,000 per month for unlimited same-day payout up to a volume cap (e.g. Rp 5M/day). Best for daily-restock warungs.
- Instant tier (real-time, not just same-day): 0.15 percent, for online sellers who need cash between batches to fulfill orders.

Willingness to pay is anchored by the 0.3 percent MDR the merchant already accepts and the 5 to 15 percent per week informal loan rate they want to avoid. At 0.1 percent, the product is a rounding error next to both, which is the adoption engine.

What people would actually pay, ranked:

1. Micro warung / food cart owners who restock daily and borrow informally. Highest pain, lowest price sensitivity relative to the alternative.
2. Online social-sellers (TikTok/Instagram/Shopee repeat buyers paying by QRIS) who need to rebuy inventory fast. High volume, high frequency.
3. Cross-border micro-merchants (Bali, Batam, border towns) accepting QRIS Antarnegara from tourists. Largest float, most underserved.
4. Market stall clusters that could be onboarded as a cohort via a koperasi or aggregator.

## 17. Cross-Border Micro-Merchant Credit Scoring Extension

The same-day settlement product generates a pristine data asset: a real-time ledger of a merchant's QRIS inflows, by currency, by day, reconciled against reimbursements. For cross-border merchants this is a credit profile no bank has, because the income is denominated in five currencies and settles across five central-bank rails.

That ledger can feed the credit-scoring opportunity in `07-gaps-and-opportunities/opportunities/digital-credit-scoring-umkm-qris.md` and the cross-border variant in `07-gaps-and-opportunities/inbox/2026-06-30-cross-border-qris-credit-scoring.md`. The settlement layer is the data firehose; credit scoring is the monetization on top. One builds distribution (settlement), the other builds margin (scoring). They compound.

Concretely: a Baliwarung accepting SGQR+ from Singaporean tourists builds 90 days of settled SGD-converted rupiah history. A BPR or P2P lender using that ledger can price a working-capital loan at a fraction of the informal rate, because default risk is observable daily, not guessed annually.

## 18. Risks, Constraints, And Regulatory Landmines

- Licensing. Holding or moving merchant funds requires PJSP status or a partner bank. Unlicensed fund holding is the fastest way to get shut down by BI/OJK. Build license-light first.
- "Double charging" perception. BI caps MDR to protect merchants. A 0.1 percent acceleration fee must be clearly voluntary and value-linked, or risk a regulatory slap. Position as opt-in convenience, never mandatory.
- Capital/netting risk. If reimbursement from the acquirer is delayed (acquirer batch fails, dispute, fraud clawback), the orchestrator is out of pocket. The netting model requires tight exposure limits per merchant and per acquirer.
- Webhook reliability. Acquirer settlement webhooks are best-effort and non-idempotent (see carrier-webhook-reliability gap). Reconciliation must be pull-based (poll the acquirer statement API) not push-only.
- FX risk on cross-border. Advancing rupiah against a foreign-currency receivable exposes the orchestrator to a day of FX move. Hedge or pass the risk to the merchant via a wider cross-border fee.
- Acquirer cooperation. The product needs the acquirer to expose a real-time payout API or to accept BI-FAST-initiated merchant credits. Some may refuse. Start with the most API-friendly acquirer (e-wallet PJPPs tend to be more API-mature than legacy banks).
- Competition from the acquirer itself. If BCA or GoPay later ships same-day payout natively, the orchestrator's edge shrinks to UX and multi-bank coverage. The moat is multi-acquirer aggregation and cross-border, not any single rail.

## 19. New Gaps Discovered

While researching this bottleneck, three adjacent gaps surfaced that the vault does not yet cover:

- `03-id-business-trends/bottlenecks/qris-mdr-interchange-transparency.md` (NEW): The 0.3 percent UMKM MDR is split across issuer, acquirer, switch, and scheme, but the exact split and how it changes at the Rp 5 million per-transaction limit (raised by BI in October 2024, per multiple merchant sources; the precise PADG citation was unreachable during this research) is undocumented in the vault. A merchant paying Rp 5M+ per transaction may face a different MDR tier. This affects pricing of any settlement product.
- `03-id-business-trends/bottlenecks/cross-border-qris-fx-settlement-gap.md` (NEW): Cross-border QRIS payouts involve FX conversion and two central banks, creating a multi-day settlement and FX-timing gap specific to tourist-facing merchants in Bali, Batam, and border towns. No product addresses it. Directly extends `07-gaps-and-opportunities/inbox/2026-06-30-cross-border-qris-credit-scoring.md`.
- `04-freelancer-ai-agent/mcp-servers/qris-settlement-mcp.md` (NEW): An MCP server exposing "advance_settlement," "get_float," and "reconcile" as tools would let freelance automation agents offer same-day payout to clients' QRIS merchants without per-acquirer integration. Natural sibling to `04-freelancer-ai-agent/mcp-servers/logistics-orchestrator-mcp.md` and `fastwork-mcp-spec.md`.

These are noted for the next tick. They are not written in this pass.

## 20. Per-Acquirer Payout Comparison (What Merchants Actually Experience)

The T+1 default is not uniform. Different acquiring PJSPs pay out on different schedules and to different destinations. The table below is synthesized from merchant onboarding docs and forum reports (Bittime, qris.id, interactive.co.id, bank merchant portals). Exact SLAs vary by merchant tier and must be confirmed per acquirer; treat as directional, not contractual.

| Acquirer type | Typical payout | To e-wallet balance | To external bank | Instant option? |
|---|---|---|---|---|
| Bank acquirer (BRI/BCA/BNI/Mandiri) | T+1 business day | n/a | Yes, next day | Rare; some via BI-FAST on request |
| GoPay for Business | T+1 to T+2 | Instant to GoPay balance | T+1 to T+2 transfer | GoPay balance only |
| OVO | T+1 | Instant to OVO | T+1 to T+2 | OVO balance only |
| DANA | T+1 | Instant to DANA | T+1 to T+2 | DANA balance only |
| ShopeePay | T+1 to T+2 | Instant to ShopeePay | T+2 | ShopeePay balance only |
| QRIS Open API aggregator (qris.id) | Batch, "all banks" | n/a | Next day to chosen bank | Not by default |

The pattern is consistent: money reaches the merchant's own bank account on a one to two day delay, while it reaches the merchant's e-wallet balance instantly but then gets stuck behind a withdrawal limit or another T+1 to T+2 step. The settlement layer's job is to collapse that to "in your bank account tonight."

## 21. MDR and Interchange: Where the 0.3 Percent Goes

MDR is not kept by one party. For a domestic QRIS transaction the ~0.3 percent UMKM MDR is split (typical schematic, proportions vary by BI scheme rules):

- Issuer (customer's app/bank): the largest share, compensates for onboarding and funding the customer side.
- Acquirer (merchant's PJSP): compensates for merchant onboarding, KYC, and settlement.
- Switch / scheme (ASPI + BI): the network toll.
- Processor / aggregator: if an Open API aggregator is involved.

Why this matters for the settlement product:

- The settlement fee (0.1 percent) is additional to MDR, so total cost to merchant becomes ~0.4 percent on accelerated transactions. Still far below informal loan rates, but the product must be transparent that it stacks on MDR.
- The acquirer already earns MDR and holds the float. The settlement layer does not compete with MDR; it charges for time, a different dimension. This reduces direct conflict with acquirers, who keep their MDR and simply lose the float spread.
- If BI ever raises the MDR cap or changes the UMKM tier at the Rp 5 million per-transaction threshold (raised October 2024 per merchant sources; exact PADG citation unreachable this tick), the headroom for a 0.1 percent acceleration fee could tighten. Track this in `qris-mdr-interchange-transparency.md` (new gap, section 19).

## 22. Second Worked Example: A TikTok Shop Reseller In Bandung

Pak Rian resells phone accessories on TikTok Shop and Instagram, doing Rp 4,000,000 QRIS volume per day from repeat buyers who pay by scanning his dynamic QR (he sends the QR in chat). His margin is 8 percent. He restocks from a supplier who requires payment before shipping.

Current state:

- QRIS money lands T+1. To fulfill Monday's orders he needs Friday and Saturday's QRIS money, which lands Monday and Tuesday.
- He runs a Rp 2,000,000 supplier tab at 8 percent per week = Rp 160,000/week interest.
- Some orders slip because he cannot prepay stock in time; he loses ~Rp 300,000/week in missed sales.

With same-day settlement at 0.1 percent:

- Each day's Rp 4,000,000 lands by 20:00. He prepays the supplier same night.
- Fee = Rp 4,000/day = Rp 120,000/month.
- Eliminates Rp 160,000/week = Rp 640,000/month loan interest, plus recovers Rp 300,000/week = Rp 1,200,000/month missed sales.
- Net gain ~Rp 1,720,000/month on Rp 120,000 cost. The product pays for itself 14x over.

This merchant has higher volume and is more price-insensitive to the fee because the alternative cost (lost sales + loan interest) is enormous. He is the higher-value cohort and the one most likely to take the "daily auto-advance subscription" tier.

## 23. Third Worked Example: A Bali Cafe Taking QRIS Antarnegara

Ibu Made runs a cafe in Canggu, Bali, popular with Singaporean and Malaysian tourists. About 30 percent of her QRIS volume is cross-border (SGQR+ and DuitNow via QRIS Antarnegara). Her daily QRIS volume is Rp 6,000,000, of which Rp 1,800,000 is cross-border.

Current state:

- Domestic QRIS lands T+1. Cross-border QRIS (involving FX conversion and two central banks) lands in 2 to 4 business days.
- She effectively finances a Rp 1,800,000 x 3-day float = Rp 5,400,000 of foreign-receivables working capital from her domestic cash.
- She bears FX timing risk: if SGD/IDR moves 1 percent during the settlement window, her rupiah landing shrinks by Rp 18,000 per Rp 1.8M, a small but persistent leak.

With a cross-border-aware same-day settlement at 0.15 percent:

- Domestic advanced same day at 0.1 percent; cross-border advanced same day at 0.15 percent with FX locked at scan.
- Fee = (Rp 4.2M x 0.1 percent) + (Rp 1.8M x 0.15 percent) = Rp 4,200 + Rp 2,700 = Rp 6,900/day = Rp 207,000/month.
- She eliminates the 3-day foreign-receivables float and the FX leak. Net positive, and she gains a clean multi-currency ledger (see section 17) she can later use for a working-capital loan.

This cohort is the bridge to the cross-border credit-scoring opportunity and has the largest float per merchant.

## 24. Reconciliation and Idempotency (Production Code)

The hardest engineering problem is not moving money, it is reconciling two asynchronous event streams (advance out, reimbursement in) without double-paying or double-counting. Acquirer webhooks are best-effort and may arrive duplicated or out of order (the same reliability gap as `carrier-webhook-reliability.md`). Below is an idempotent handler plus a pull-based reconciliation poller.

```python
# qris_instant_settle/recon.py
# Idempotent webhook handler + pull-based reconciliation against acquirer statement.
import json, hashlib, asyncio
from dataclasses import dataclass
from qris_instant_settle.settlement_orchestrator import (
    LEDGER, QRISReceivable, SettlementState, advance_to_merchant
)

SEEN_EVENTS: set[str] = set()   # dedupe keyed on (txn_id, event_type, acquirer_seq)

def event_key(txn_id: str, event_type: str, seq: str) -> str:
    return hashlib.sha256(f"{txn_id}|{event_type}|{seq}".encode()).hexdigest()

async def handle_acquirer_webhook(body: dict):
    """Best-effort webhook. May arrive more than once. Idempotent by event_key."""
    key = event_key(body["txn_id"], body["event"], body.get("seq", "0"))
    if key in SEEN_EVENTS:
        return {"ok": True, "dup": True}          # already processed, safe no-op
    SEEN_EVENTS.add(key)

    r = LEDGER.get(body["txn_id"])
    if body["event"] == "txn_received":
        if r is None:
            r = QRISReceivable(txn_id=body["txn_id"],
                               merchant_id=body["merchant_id"],
                               amount_idr=body["amount"])
            LEDGER[body["txn_id"]] = r
        # Merchant opted into speed? Check prefs store (omitted).
        if body.get("advance") and r.state == SettlementState.BATCH_QUEUED:
            await advance_to_merchant(r)
    elif body["event"] == "batch_reimbursed":
        if r and r.state == SettlementState.ADVANCED:
            r.state = SettlementState.REIMBURSED
    return {"ok": True}

async def reconcile_pull(acquirer_client, since: str):
    """Pull-based safety net: webhooks lie, statements do not.
    Runs hourly. Catches anything the webhook missed or duplicated."""
    statement = await acquirer_client.get_settlement_report(since)
    for row in statement.rows:
        r = LEDGER.get(row.txn_id)
        if r is None:
            continue
        if row.reimbursed and r.state != SettlementState.REIMBURSED:
            r.state = SettlementState.REIMBURSED
        if not row.reimbursed and r.state == SettlementState.ADVANCED:
            # still waiting; extend exposure timer, do not double-advance
            pass
```

The pull-based reconciliation is the moat against webhook flakiness. Webhooks are a convenience; the statement API is the source of truth.

## 25. Netting Engine (Why Capital Need Is Small)

Advancing every merchant the same day would require huge capital if done naively. The trick is netting: most merchants are both receivers (of QRIS payouts) and, in aggregate, the reimbursement inflow from acquirers covers the outflow.

```python
# qris_instant_settle/netting.py
# Daily netting: reimbursements in vs advances out. Capital need = peak net gap.
from collections import defaultdict

class NettingEngine:
    def __init__(self):
        self.advances_out = defaultdict(int)   # acquirer -> amount advanced to merchants
        self.reimb_in = defaultdict(int)       # acquirer -> amount reimbursed by batch

    def peak_capital_need(self, acquirer: str) -> int:
        # Max simultaneous out minus in, over the day. Approximated by
        # (advances made before first reimbursement of the day).
        return max(0, self.advances_out[acquirer] - self.reimb_in[acquirer])

    def record_advance(self, acquirer: str, amount: int):
        self.advances_out[acquirer] += amount

    def record_reimbursement(self, acquirer: str, amount: int):
        self.reimb_in[acquirer] += amount
```

In practice the peak capital need is the maximum same-day gap between advances and reimbursements for a given acquirer, which is a fraction of total daily volume if advances and reimbursements are well interleaved. A warehouse line covering that peak, priced below the 0.1 percent fee, keeps the business capital-light and scalable.

## 26. Go-To-Market Playbook

Land-and-expand through the merchant clusters that already feel the float most:

Phase 1: Warung clusters via koperasi. Partner with a local koperasi simpan pinjam (savings and loan cooperative) that already serves 200 to 2,000 warungs. The koperasi becomes the distribution and trust layer; the settlement product is white-labeled. The koperasi earns a share of the 0.1 percent and offers it as a member benefit alongside its loans. This also seeds the credit-scoring ledger (section 17).

Phase 2: Online social sellers. Target TikTok/Instagram/WhatsApp sellers who already send QRIS in chat. They are digitally native, high-frequency, and feel the restock pinch weekly. Acquire them via creator/agent networks and short demonstrable ROI math ("pay Rp 1,200, avoid Rp 70,000 loan").

Phase 3: Cross-border merchant hubs. Bali, Batam, border towns. Bundle domestic + cross-border same-day settlement with FX lock. Highest float, highest fee tier, and the cleanest path to cross-border credit scoring.

Phase 4: Embed in existing aggregators. Rather than fight qris.id and interactive.co.id, embed the acceleration as a paid add-on inside their Open API dashboards. They already have the merchant relationship and the QR generation; you supply the speed. This is the lowest-CAC path and the one most likely to scale fastest.

## 27. Competitive Landscape Deep-Dive

- qris.id (Open API Platform): Strong on QR generation and "payout to all banks," weak on speed. Potential partner, not competitor, for the embed play (Phase 4).
- interactive.co.id (Interactive QRIS): Similar positioning, emphasizes "pencairan dana di semua bank" and commission bonuses. Also a potential embed partner.
- Bank merchant apps (BCA livin' Merchant, Mandiri, BRI, BNI): Own the settlement but do not market speed. Slow to move; possible acquirer-partner for the license-light model.
- E-wallet business accounts (GoPay, OVO, DANA, ShopeePay): Instant to their own balance but trapped there. The settlement layer's value is "out to your bank, tonight," which complements rather than replaces them.
- Factoring / supply-chain finance: Serve large businesses at several percent. Different league; no overlap with Rp 1M/day warungs.
- BI-FAST (consumer rail): The raw capability, not a merchant product. The settlement layer is the merchant-facing packaging of BI-FAST for receivables.

No incumbent owns "QRIS money in your bank account tonight for 0.1 percent." The white space is real.

## 28. Market Sizing (Top-Down and Bottom-Up)

Top-down: 32.71 million QRIS merchants (2024, Wikipedia citing BI). Assume conservatively that 15 percent (about 4.9 million) are active enough to feel the float and have a bank account to receive payouts. Of those, assume 10 percent adopt the acceleration product in steady state (about 490,000 merchants). At an average Rp 1,000,000 daily QRIS volume and a 0.1 percent fee, per-merchant monthly fee is ~Rp 30,000.

490,000 merchants x Rp 30,000 = Rp 14.7 billion per month, or about Rp 176 billion per year in fee revenue, recurring, before cross-border uplift.

Bottom-up cross-border add: the five linked countries (Thailand, Malaysia, Singapore, Japan, South Korea) plus planned India/China/Saudi create a tourist-facing merchant base concentrated in Bali, Batam, Jakarta, and border towns. Even 50,000 such merchants at Rp 6,900/day (section 23) = Rp 345 million/day = ~Rp 10 billion/month additional at the 0.15 percent tier.

These are deliberately conservative. Real adoption could be higher because the product is sticky (working capital dependency) and the alternative cost (informal loans at 5 to 15 percent/week) makes 0.1 percent a trivial line item. The recurring, low-churn nature is the attraction: this is annuitized payments revenue, not a one-time software sale.

Compare to the credit-scoring extension (section 17): the same merchants, once accelerated, produce a daily ledger that supports loan origination. A 2 to 4 percent origination fee plus a spread on a working-capital loan is a far larger pool than the 0.1 percent settlement fee, but it requires the settlement product first to build distribution and data. Sequencing: settlement is the hook, scoring is the harpoon.

## 28b. Daily-Restock Math Across Merchant Archetypes

The float pain is a function of how tightly the merchant's cash conversion cycle is coupled to daily restock. A table of archetypes and their implicit "float cost" (what they would pay to collapse T+1 to same-day), estimated from informal-credit rates they actually use.

| Archetype | Daily QRIS vol | Restock frequency | Informal rate used | Implied float cost/day | Willing fee @0.1% |
|---|---|---|---|---|---|
| Warung Cirebon | Rp 1.0M | Daily 05:00 | 10%/wk on Rp 0.7M | ~Rp 10,000 | Rp 1,000 |
| Food cart campus | Rp 0.6M | Daily | 8%/wk on Rp 0.4M | ~Rp 4,500 | Rp 600 |
| TikTok reseller | Rp 4.0M | Per order batch | 8%/wk on Rp 2.0M | ~Rp 22,800 | Rp 4,000 |
| Bali cafe (cross-border) | Rp 6.0M (30% XB) | Daily | bank line 6%/yr equiv | Rp 1,000 + FX leak | Rp 6,900 |
| Market stall cluster | Rp 2.5M | Every 2 days | 12%/wk on Rp 1.5M | ~Rp 25,700 | Rp 2,500 |
| Online course/kreator | Rp 3.0M | Monthly | none (sits in e-wallet) | ~Rp 0 | Rp 3,000 if needs bank |

The table shows the fee is always a rounding error next to the informal rate the merchant already pays. The kreator row is the exception: if their money already sits in an e-wallet they do not urgently need to bank, the acceleration has less pull. That is why the GTM focuses on archetypes with a real daily restock dependency (warung, food cart, reseller, market stall, cross-border cafe), not on kreators who are comfortably parked in e-wallets.

## 28c. BI-FAST Mechanics Deep-Dive

BI-FAST is the interbank credit transfer service Bank Indonesia operates as part of the national payment system. Key attributes relevant to the settlement layer:

- Real-time: transactions are processed and credited within seconds, not in batched windows.
- 24/7: unlike legacy SKNBI batch clearing (which closes on weekends and after cut-off), BI-FAST runs continuously, including weekends and holidays. This is what makes "Friday night sale, Friday night payout" possible.
- Capped fee: the per-transaction consumer fee is capped at Rp 2,500 by BI. For a settlement layer moving large aggregate volume, the effective per-transaction cost is tiny, well within the 0.1 percent fee headroom (Rp 2,500 on Rp 1,000,000 is 0.25 percent, so BI-FAST cost alone can exceed the fee on small tickets; the product must therefore set a per-advance floor, e.g. Rp 250 to Rp 500, or batch advances per merchant per day to amortize the Rp 2,500 across multiple transactions).
- Direct participant banks: only banks and licensed PJSPs are BI-FAST participants. A settlement layer without a license cannot originate BI-FAST directly; it must ride a partner bank's participation. This is the structural reason the license-light model (section 10) partners with an acquiring bank rather than going solo.

The per-transaction Rp 2,500 cap is the reason the settlement product should advance per-merchant daily aggregates (one BI-FAST credit per merchant per day) rather than per-transaction. Aggregating avoids paying Rp 2,500 on a Rp 50,000 transaction, which would eat the entire 0.1 percent fee and then some. Engineering the daily aggregate advance is therefore a cost-control necessity, not an optimization.

## 28d. Risk Quantification Table

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Late acquirer batch | Medium | Merchant not reimbursed on time, capital tied | Pull reconciliation (sec 24), exposure limits |
| Webhook duplication | High | Double-advance | Idempotent event_key (sec 24) |
| Webhook drop | Medium | Missed advance, SLA miss | Hourly statement pull (sec 24) |
| FX move (cross-border) | Medium | Margin erosion on XB tier | FX lock at scan, wider XB fee |
| BI objects to fee stacking | Low | Product redesign | Position as opt-in; subscription pivot |
| Acquirer refuses API | Medium | Cant launch on that rail | Start with API-mature e-wallet PJSP |
| Bank partner loses license | Low | Exist license-light model | Multi-partner, portable ledger |
| Fraudulent QR / chargeback | Medium | Advance then clawback | Pre-advance risk score, per-merchant cap |

The dominant operational risks (webhook duplication, webhook drop, late batch) are all engineering risks with known mitigations from sections 24 and 25. None require novel technology; they require disciplined reconciliation, which is exactly the "universal integration tax" the vault has flagged elsewhere (`carrier-webhook-reliability.md`).

## 28e. Key Metrics To Track (If You Build It)

- Advance take-rate: percent of eligible QRIS volume the merchant chooses to accelerate. Target > 40 percent in power users.
- Float unlocked per merchant: average in-flight balance eliminated. Directly maps to merchant ROI.
- Net capital multiple: daily volume divided by peak capital need. Higher is better; target > 20x.
- Same-day SLA attainment: percent of advances landing by 20:00 same day. Target > 99 percent.
- Churn: should be near zero once restock depends on it. Watch for merchants who stop accelerating after one loan-funded month.
- Cross-border share: percent of volume that is QRIS Antarnegara. Leading indicator for the credit-scoring extension.

## 28f. A Day In The Life: Warung Ibu Siti, With and Without The Product

Without same-day settlement (a Tuesday in Cirebon):

- 05:00. Ibu Siti arrives at the wholesaler. She needs Rp 800,000 of vegetables. Her QRIS balance from Monday (Rp 1.2M) will not land until Tuesday afternoon. She uses her Rp 300,000 cash float plus a Rp 500,000 supplier tab at 10 percent/week.
- 09:00 to 18:00. She sells. Rp 1.2M QRIS scanned, Rp 0.9M cash.
- 18:30. The day's QRIS money is in the switch but not her account. It will batch overnight and land Wednesday.
- 20:00. She cannot buy Wednesday's stock tonight. Another supplier tab opens.
- End of week: three overlapping tabs, ~Rp 70,000 to Rp 90,000 interest paid, money she could have kept.

With same-day settlement (a Tuesday in Cirebon):

- 05:00. Same gap, but she knows Monday's Rp 1.2M is already in her account (landed Monday 20:00). She pays the wholesaler in full, no tab.
- 09:00 to 18:00. Same sales.
- 18:30. Tuesday's Rp 1.2M is advanced to her account by 20:00 via the settlement layer (one BI-FAST aggregate credit for the day). Fee = Rp 1,200.
- 20:00. She buys Wednesday's stock tonight at wholesale, no interest.
- End of week: zero supplier-tab interest. The Rp 1,200/day fee (Rp 36,000/month) replaces Rp 70,000 to Rp 90,000/week of interest (Rp 280,000 to Rp 360,000/month). She is unambiguously ahead, and her supplier relationship is cleaner.

The product does not change how she sells. It changes when she gets paid. For a merchant on a daily cash conversion cycle, that timing is the whole game.

## 28g. Regulatory Timeline (QRIS Settlement Context)

A chronological view of the rules that frame this bottleneck, with source notes. Where a primary BI citation was unreachable during research, the claim is marked verify-live.

| Date | Event | Relevance to settlement |
|---|---|---|
| 16 Aug 2019 | BI Decree 21/18/PADG/2019 ratifies QRIS national standard | Mandates unified QR; settlement architecture inherits SKNBI batch | 
| 17 Aug 2019 | QRIS launched | Rail goes live, T+1 payout by default |
| 2021 | BI-FAST launched (real-time 24/7 rail) | The speed capability exists but is not the QRIS merchant default |
| 29 Aug 2022 | QRIS Antarnegara with Thailand | Cross-border float problem born |
| 8 May 2023 | Malaysia link | Same |
| 17 Nov 2023 | Singapore link | Same |
| Oct 2024 | BI raises per-transaction QRIS limit to Rp 5 million (merchant sources; verify-live PADG citation) | Larger tickets, larger float; possible MDR tier change |
| 17 Aug 2025 | Japan link (first non-ASEAN) | Cross-border surface widens |
| 1 Apr 2026 | South Korea link | Same |
| Planned | India, China, Saudi links | Future cross-border volume |

The timeline shows the rail has been stable domestically since 2019 while the cross-border surface exploded from 2022 on. The settlement product should therefore launch domestic (where the volume and the proven pain are) and extend cross-border as the FX-aware tier (section 23), riding the expanding Antarnegara network rather than betting on it.

## 28h. Proposed API Contract (Reference Spec)

A concrete contract for the settlement layer's own merchant-facing and internal APIs. This is reference, not production, but it shows the shape of the product.

```yaml
# OpenAPI-style sketch for the settlement orchestrator
paths:
  /v1/merchants/{mid}/prefs:
    get:
      description: Read settlement preferences (opt-in mode, fee tier)
    post:
      body:
        advance_mode: enum[per_txn, daily_auto, instant]
        fee_bps: integer   # 10 = 0.1%, 15 = 0.15% cross-border
        floor_idr: integer # min fee per advance, e.g. 250

  /v1/webhooks/acquirer:
    post:
      description: Idempotent acquirer event (txn_received, batch_reimbursed)
      security: [hmac_sha256_header]
      body:
        txn_id: string
        merchant_id: string
        amount: integer
        event: enum[txn_received, batch_reimbursed]
        seq: string
        advance: boolean

  /v1/settlement/advance:
    post:
      description: Trigger same-day advance for a merchant's pending QRIS receivable
      body:
        merchant_id: string
        amount_idr: integer
        rail: enum[BI_FAST]
      response:
        advanced: boolean
        eta_settle: string   # ISO8601, target same day 20:00

  /v1/reconciliation/pull:
    get:
      description: Pull acquirer settlement report (source of truth)
      query:
        since: string   # ISO8601
```

The contract encodes the three core operations: preference setting, idempotent event ingestion, and the advance trigger, plus the pull reconciliation that is the safety net. A real implementation would add auth, rate limits, and a ledger service, but the surface area is small, which is the point. This is a thin layer, not a core banking system.

## 28i. Why This Is A Data Moat, Not Just A Feature

The settlement layer's durable asset is not the speed, it is the ledger. Every accelerated transaction produces a timestamped, reconciled record of a merchant's real inflows, by day, by currency, tied to a verified NMID and a bank account. That is a credit file no bureau has for micro merchants.

Today, a warung's only "credit history" is her arisan contributions and her koperasi passbook. Banks cannot lend to her because they cannot see her cashflow. The settlement ledger makes her cashflow visible daily. Once 100,000 merchants have 90 days of clean ledger history, the dataset itself becomes the moat: a lender will pay to access risk scores derived from it, and the merchant will accept lower loan rates because the lender's risk is observable. This is the exact thesis of `digital-credit-scoring-umkm-qris.md`, and the settlement layer is the cheapest way to accumulate the underlying data at scale, because merchants opt in to get paid faster, not to be scored.

The cross-border ledger is even scarcer: a Bali cafe with 90 days of SGD-, MYR-, and JPY-converted inflows is a credit profile that simply does not exist in any Indonesian bureau. That is the wedge into `2026-06-30-cross-border-qris-credit-scoring.md`.

## 28j. Related Vault Map (How This Bottleneck Connects)

This document is one node in a connected graph. The settlement-speed bottleneck reinforces and is reinforced by several others:

- `03-id-business-trends/bottlenecks/cod-settlement-infrastructure.md`: the COD settlement bottleneck is the legacy analog. QRIS was meant to replace COD, but QRIS merchant payout inherited the same batched slowness. The two bottlenecks share a root cause: Indonesian settlement rails are batch, not real-time, at the merchant payout leg.
- `03-id-business-trends/demand-mining/umkm-kredit-bottleneck.md`: the float problem forces micro merchants into the informal credit market at 5 to 15 percent/week. The settlement layer is the cheapest alternative to that borrowing, and the ledger it builds is the data cure for the bottleneck itself.
- `03-id-business-trends/demand-mining/saldo-penjual-shopee-dibekukan.md`: platform-held balances are another form of merchant float capture, this time by the marketplace, not the acquirer. QRIS same-day settlement reduces merchant dependence on platform-held balances.
- `07-gaps-and-opportunities/opportunities/digital-credit-scoring-umkm-qris.md`: the settlement layer is the data firehose for that opportunity. Build settlement first, score second.
- `07-gaps-and-opportunities/inbox/2026-06-30-cross-border-qris-credit-scoring.md`: the cross-border extension of the above, fed by the FX-aware tier (section 23).
- `03-id-business-trends/bottlenecks/carrier-webhook-reliability.md`: the same webhook reliability tax applies to acquirer settlement webhooks. The reconciliation poller (section 24) is a direct application of that thesis to payments.
- `04-freelancer-ai-agent/mcp-servers/logistics-orchestrator-mcp.md` and `fastwork-mcp-spec.md`: the "universal integration tax" pattern. A `qris-settlement-mcp.md` (new gap, section 19) would let automation agents offer same-day payout to clients without per-acquirer integration, exactly as the logistics orchestrator does for carriers.

The throughline: Indonesian micro-merchant money moves slowly at every handoff (cash to COD to QRIS to bank to credit), and each slow handoff is both a pain and a wedge. Settlement speed is the highest-leverage handoff because it sits on a mandated, 32.71 million-merchant rail that is already growing.

## 28k. Open Questions And Verify-Live List

Items that need primary-source confirmation before any build, flagged because the BI primary pages were unreachable during this research pass (TLS handshake failures on the research connection):

- Exact BI-published merchant payout SLA for QRIS (confirm with acquiring PJSP; T+1 inferred from SKNBI batch architecture).
- The precise PADG citation and effective date for the October 2024 QRIS per-transaction limit raise to Rp 5 million, and whether it changes the UMKM MDR tier.
- The exact per-acquirer real-time payout API availability (which PJSPs expose a push payout vs only batch).
- Current BI 7-Day Reverse Repo Rate at time of build (was ~5.5 to 6.0 percent in 2024 to 2025; confirm live).
- Whether BI has issued any guidance on third-party acceleration fees stacked on MDR (none found; assumption is opt-in services are permitted, but confirm with counsel).

None of these block the analysis; they refine the numbers. The structural thesis (batch payout on a real-time rail, large captive merchant base, cheap speed arbitrage) holds regardless of the exact SLA.

## 29. Frequently Asked Questions

Why would a merchant pay 0.1 percent when QRIS payout is "free" at T+1? Because the T+1 payout is not free in working-capital terms. A warung borrowing informally at 10 percent per week to cover the float pays far more. The 0.1 percent is the cheapest form of speed available, and it is opt-in per transaction.

Is this legal without a payment license? Holding merchant funds directly requires PJSP status. The license-light model keeps funds at a partner bank and only orchestrates payout via BI-FAST, so the product is a technology/orchestration layer on top of a licensed acquirer, not an unlicensed money holder. Confirm structure with BI/OJK counsel before launch.

What if the acquirer's batch is late or disputed? The reconciliation poller (section 24) and netting engine (section 25) cap exposure. Per-merchant and per-acquirer exposure limits prevent a single late batch from blowing up the book. The fee must price in this risk.

Does BI allow charging on top of MDR? BI caps MDR to protect merchants; it has not banned voluntary acceleration services. The fee must be clearly optional and value-linked. If BI later objects, the product pivots to a subscription model bundled with other merchant services (accounting, inventory) where the speed is a feature, not a per-transaction tax.

Why not just use BI-FAST myself? A merchant cannot easily trigger BI-FAST for QRIS receivables because the receivable lives in the acquirer's batch, not the merchant's account. The settlement layer is the bridge that converts the acquirer batch into a same-day BI-FAST credit to the merchant. That bridge is the product.

## 30. References And Source Notes

1. Wikipedia, "QRIS" (English), https://en.wikipedia.org/wiki/QRIS , retrieved 2026-07-10. Source for launch date 17 Aug 2019, Decree 21/18/PADG/2019, 2024 figures (226.54 percent YoY growth, 50.50M users, 32.71M merchants, Rp42 trillion annual value), QRIS Tap.
2. Wikipedia, "QRIS" (Bahasa Indonesia), https://id.wikipedia.org/wiki/QRIS , retrieved 2026-07-10. Source for cross-border timeline: Thailand 29 Aug 2022, Malaysia 8 May 2023, Singapore 17 Nov 2023, Japan 17 Aug 2025, South Korea 1 Apr 2026; planned India/China/Saudi links; US Trade Representative objection; Open API description.
3. Kompas, "Apa Itu QRIS: Cara Pakai, Kegunaan, dan Sistem Kerjanya," Money/Kompas.com, 6 Aug 2024, https://money.kompas.com/read/2024/08/06/132348226/apa-itu-qris-cara-pakai-kegunaan-dan-sistem-kerjanya . Source for QRIS definition, unification of PJSP QR codes, use cases including pasar tradisional and antarpersonal, and planned Korea/Japan/India/UAE expansion.
4. Bittime, "Cara Buat QRIS untuk All Payment 2026," https://www.bittime.com/blog/cara-buat-qris-all-payment-panduan-lengkap , retrieved 2026-07-10. Source for MDR ~0.3 percent for UMKM, activation 1-7 working days, free registration, all-payment QR covering GoPay/OVO/DANA/ShopeePay/mobile banking.
5. QRIS Open API Platform, https://qris.id/homepage/open-api/ , retrieved 2026-07-10. Source for Open API enabling dynamic QR generation and "pencairan dana di semua bank," supporting all e-wallets via one integration.
6. Bank Indonesia, BI 7-Day Reverse Repo Rate page, https://www.bi.go.id/id/statistik/indikator/bi-rate.aspx , retrieved 2026-07-10 (reachable). Context for risk-free float opportunity cost (~5.5 to 6.0 percent, 2024 to 2025).
7. Bank Indonesia, QRIS official page, https://www.bi.go.id/en/fungsi-utama/sistem-pembayaran/ritel/kanal-layanan/qris/default.aspx and the Indonesian equivalent, retrieved 2026-07-10. NOTE: these BI pages returned TLS handshake failures on the research connection, so exact BI-published merchant payout SLA could not be quoted verbatim. T+1 default inferred from batched SKNBI clearing architecture and aggregator documentation. Confirm with acquiring PJSP before product promises.
8. Interactive QRIS, https://qris.interactive.co.id/homepage/ , retrieved 2026-07-10. Alternative QRIS aggregator showing payout-to-all-banks positioning (not speed).
9. Related vault files: `03-id-business-trends/bottlenecks/cod-settlement-infrastructure.md` (COD settlement bottleneck, 2026-07-07), `03-id-business-trends/demand-mining/umkm-kredit-bottleneck.md`, `07-gaps-and-opportunities/opportunities/digital-credit-scoring-umkm-qris.md`, `07-gaps-and-opportunities/inbox/2026-06-30-cross-border-qris-credit-scoring.md`, `03-id-business-trends/bottlenecks/carrier-webhook-reliability.md`, `04-freelancer-ai-agent/mcp-servers/logistics-orchestrator-mcp.md`.

---

### 28l. Appendix: Float Math Derivation And Sensitivity

The systemic float estimate in section 3 used a deliberately low per-merchant average of Rp 500,000. Below is the sensitivity of total systemic float to that assumption, holding 32.71 million merchants constant. This is the pool a same-day settlement product unlocks.

| Assumed avg in-flight float per merchant | Total systemic float (IDR) | Total systemic float (USD, ~16,000/USD) |
|---|---|---|
| Rp 200,000 | Rp 6.5 trillion | ~USD 408 million |
| Rp 500,000 | Rp 16.4 trillion | ~USD 1.0 billion |
| Rp 1,000,000 | Rp 32.7 trillion | ~USD 2.0 billion |
| Rp 2,000,000 | Rp 65.4 trillion | ~USD 4.1 billion |

Even at the lowest assumption, over USD 400 million of micro-merchant working capital sits unproductively in settlement accounts at any moment. The settlement layer does not "create" value by moving this money; it removes the dead time. The merchant's cost of that dead time is the informal loan rate (5 to 15 percent/week), so the addressable "pain pool" is far larger than the float principal, it is the interest the float forces merchants to pay.

Fee sensitivity at 0.1 percent, varying adoption and daily volume (steady-state, annualized):

| Adopting merchants | Avg daily QRIS vol | Annual fee revenue (0.1%) |
|---|---|---|
| 100,000 | Rp 500,000 | Rp 3.65 billion |
| 490,000 | Rp 1,000,000 | Rp 176 billion |
| 1,000,000 | Rp 1,000,000 | Rp 365 billion |
| 1,000,000 | Rp 2,000,000 | Rp 730 billion |

The 490,000 / Rp 1.0M case (Rp 176 billion/year) is the conservative base case used in section 28. The model is linear in both adoption and volume, so the dominant lever is adoption, which is why GTM (section 26) and stickiness (section 28e) matter more than pricing finesse. A 0.1 percent fee is already cheap enough; the work is distribution, not pricing.

## 28m. Appendix B: Glossary

- QRIS: Quick Response Code Indonesian Standard, the national QR payment standard mandated by Bank Indonesia (launched 17 Aug 2019).
- PJSP: Penyelenggara Jasa Sistem Pembayaran, a licensed payment service provider (bank or e-money issuer).
- ASPI: Asosiasi Sistem Pembayaran Indonesia, the industry association that co-runs the payment scheme with BI.
- NMID: National Merchant ID, the identifier encoded in a QRIS code that routes a transaction to the correct acquiring PJSP.
- MDR: Merchant Discount Rate, the fee on a transaction split among issuer, acquirer, switch, and scheme. ~0.3 percent for UMKM.
- BI-FAST: Bank Indonesia's real-time, 24/7 interbank credit transfer service, the rail a settlement layer rides to push same-day payouts.
- SKNBI: Sistem Kliring Nasional Bank Indonesia, the legacy national clearing system, batched and windowed, which QRIS merchant payout inherits by default.
- T+1: Trade date plus one business day, the typical QRIS merchant payout delay.
- QRIS Antarnegara: the cross-border QRIS linkage (Thailand, Malaysia, Singapore, Japan, South Korea, with India/China/Saudi planned).
- Arisan: the Indonesian rotating-savings syndicate, a common informal credit instrument for micro merchants.
- Koperasi simpan pinjam: a savings-and-loan cooperative, a natural distribution partner for the settlement product.

## 28n. Why Now (Timing And Window)

Three forces make this bottleneck ripe in 2026 rather than 2019. First, the merchant base has matured: 32.71 million merchants onboarded by 2024 means the float pool is now large enough that a settlement product has a real addressable base, whereas in 2019 the rail was too thin. Second, BI-FAST is mature and widely available, so the real-time rail the product rides is no longer experimental. Third, cross-border QRIS has exploded since 2022 (five countries live, three planned), creating a higher-float, higher-fee cross-border tier that did not exist at launch. The window is open because the rail is mandated, the speed capability exists, the merchant base is large, and no incumbent packages speed as a product. The risk of waiting is that an acquirer (BCA, GoPay) ships native same-day payout and closes the white space, which is why the embed-play (section 26, Phase 4) and the cross-border moat (section 17) are the defensible positions.

## 28o. Caveats And Honest Limits

This analysis is a researcher's bottleneck map, not a validated business plan. The T+1 payout default is inferred from Indonesia's batched SKNBI clearing architecture and aggregator documentation because the primary BI settlement SLA pages were unreachable during this research pass; the exact SLA must be confirmed per acquiring PJSP before any product promise (see verify-live list, section 28k). The 0.1 percent fee, the Rp 16 trillion float, and the Rp 176 billion/year base-case revenue are model outputs from stated assumptions, not observed market data; they are directional. The cross-border FX and credit-scoring extensions depend on acquirer API maturity and BI/OJK licensing posture that can change. None of this invalidates the structural thesis: a mandated, 32.71 million-merchant rail pays out on bank batch terms while the national rail can move in seconds, and that mismatch is a wedge. The work is distribution and disciplined reconciliation, not novel technology.

## One-line thesis

The QRIS scan is instant but the merchant payout is batched T+1 on a 32.71 million merchant rail, trapping roughly Rp 16 trillion of micro-merchant float in settlement accounts at any moment. A license-light orchestration layer that advances payouts the same day via BI-FAST, charging 0.1 percent, turns settlement speed into a sticky working-capital annuity and feeds a cross-border credit-scoring moat. The rails exist. The orchestration is missing. That is the arbitrage.
