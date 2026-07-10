# Warung Kelontong Collective-Buying + Loyalty Toolkit (WA-first)

**Date:** 2026-07-10
**Source:** money-glitch-vault-enricher (autonomous cron tick)
**Promoted from:** 07-gaps-and-opportunities/inbox/2026-07-10-warung-collective-buying.md
**Category:** Opportunity one-pager (research, not a pitch)
**Related pain:** 03-id-business-trends/demand-mining/warung-kelontong-kalah-minimarket.md (signal strength 5)
**Related bottlenecks:** 03-id-business-trends/bottlenecks/cod-settlement-infrastructure.md, 03-id-business-trends/bottlenecks/warung-micro-fulfillment.md
**Related inbox:** 07-gaps-and-opportunities/inbox/2026-07-06-umkm-halal-cert-automation.md (adjacent SME tooling demand)
**Data-verification note:** Live web verification (search + extract) was unavailable during this tick because the cron environment has no PARALLEL_API_KEY configured. All quantitative claims below are drawn from established public knowledge of Indonesia's retail, payments, and SME landscape, and are annotated with their canonical source URL. Figures that require live re-confirmation are flagged "(verify live)". No live numbers were invented. Where a specific live check was attempted and blocked, the phrase "source unreachable (live check blocked this tick)" is noted. Cite before acting on any number.

---

## Executive Summary

Indonesia's traditional retail layer is made of millions of warung kelontong, the family-run kiosks that sit on nearly every neighborhood corner and village lane. They are being structurally squeezed by the modern minimarket chains, Alfamart and Indomaret, whose combined outlet count now spans tens of thousands of stores nationwide. The chains win on three things a single warung cannot match on its own: bulk procurement pricing, cashless acceptance (QRIS), and customer loyalty programs. A warung owner does not lose because they are lazy. They lose because they lack economies of scale that the franchise model hands to the chain for free.

The wedge is to give warungs that scale without a franchise. A WhatsApp first toolkit lets groups of warungs in one RW or desa aggregate their weekly purchasing into a single bulk order, capture a QRIS accept code with zero monthly fee (Bank Indonesia has waived merchant discount for micro merchants), and run a simple points based loyalty loop for their regular customers. None of this requires the warung owner to install a new app. It runs inside the phone they already hold. The buyer is literate in WhatsApp, not in ERP.

This one-pager is deliberately a research document, not a pitch deck. It maps the market, the pain, the existing failed solutions, the technical architecture, working pseudo code for the core engines, unit economics, regulatory surface, and the metrics that would prove or kill the idea. The intent is to give a builder enough grounded detail to ship a two week minimum viable version and a three month real product.

---

## The Market Context

### How many warungs there are

The warung kelontong is the unit cell of Indonesian informal retail. Public estimates put the count in the low millions. Bank Indonesia and various retail studies have historically cited on the order of 3 to 4 million traditional kiosks and small grocery outlets across the archipelago, a figure repeated in trade press and academic work on Indonesian distribution (verify live: see BPS retail census and Bank Indonesia payments reports at https://www.bps.go.id and https://www.bi.go.id). Even taking a conservative floor, this is the largest single class of retail outlet in the country and the dominant point of sale for fast moving consumer goods in tier 2, tier 3, and rural Indonesia.

The modern minimarket counterweight is concentrated. Alfamart, operated by PT Sumber Alfaria Trijaya Tbk, runs an outlet network that public annual reports place in the high tens of thousands (verify live: Alfamart annual report at https://www.alfamartkorpri.com and https://www.indomaret.co.id). Indomaret, operated by PT Indomarco Prismatama, runs a comparable or larger network. The two chains together account for the overwhelming majority of modern minimarket outlets nationally. The asymmetry is the whole story: a few dozen thousand chain stores are out competing a few million family kiosks because the chains buy at pallet scale and the kiosks buy at carton scale.

Source: Alfamart investor relations and Indomaret corporate pages, annual reports (verify live). Source: Katadata retail coverage at https://katadata.co.id for outlet-count tracking.

### The moratorium signal

Since February 2026 the idea of a moratorium on new minimarket permits has become a national policy conversation. Reporting in Tirto and Bisnis.com documented the Menteri Desa requesting a stop to new Alfamart and Indomaret permits in villages, framed as protecting community enterprises (sources: Tirto at https://tirto.id, Bisnis.com at https://bisnis.com, both reporting 2026-02-26). The Menteri Koperasi dan UKM has similarly signaled concern about the survival of warung tradisional. Regional moratoriums are not new: Denpasar, Padang, and several other city governments have previously restricted new minimarket permits.

The key research insight is that a moratorium is a political band aid. It does nothing for the warung that has already lost half its foot traffic to a store 50 meters away. It also does nothing to fix the warung's structural cost disadvantage. A moratorium freezes the competitive frontier but does not move the warung forward. That gap between "protected but still uncompetitive" is precisely where a tooling product lives. The policy tailwind (government openly worried about warung survival) also lowers regulatory and narrative risk for a warung empowerment product and may open Dinas Koperasi and koperasi partnerships that would be harder without the political cover.

Source: CNN Indonesia warung coverage at https://www.cnnindonesia.com (2026-02-26). Source: Media Indonesia Mendes statement (2026-02-26, link unreachable this tick, verify live).

---

## The Pain, Quantified Where Possible

The pain file (03-id-business-trends/demand-mining/warung-kelontong-kalah-minimarket.md) synthesized four national news items in a twelve month window, a strong signal of durable public attention. The mechanism of loss is concrete:

- Foot traffic migration. When a minimarket opens within walking distance, the warung loses the convenience shopper who used to buy one or two items. The chain offers air conditioning, clean aisles, QRIS, and discounts the warung cannot match.
- Price disadvantage. The warung buys from a local distributor at carton scale, sometimes with credit terms that carry implicit cost. The chain buys direct from principal at pallet and container scale, negotiates slotting and rebates, and passes part of that to shelf price.
- Cashless gap. Younger and middle class shoppers increasingly expect QRIS. A warung without a reliable QRIS accept code literally cannot take the sale from a customer who has no cash. Many warung owners do use personal e-wallet QR, but that mixes personal and business cash and gives no data.
- No loyalty hook. The chain's member card and app push discounts and recall. The warung has no mechanism to reward the regular or to know what the regular actually buys.

A representative synthesized quote from the pain file, drawn from CNN Indonesia and Bisnis.com reporting: "Warung kelontong saya sepi, pembeli lebih milih Alfamart karena ada AC, bisa bayar QRIS, dan diskon." Another from the Madura warung report: "Dulu dalam sebulan bisa putar uang lima juta, sekarang nyaris nol karena minimarket buka 50 meter dari rumah." These are syntheses of published reporting, not direct verbatim quotes, because the underlying article bodies were blocked this tick (source unreachable for full text, headline and date confirmed).

The structural loss is a cash flow problem before it is a margin problem. The warung turns over small absolute amounts. A 30 to 50 percent drop in daily transaction count can erase profit entirely because fixed costs (rent, electricity, the owner's own labor) do not shrink. That is why a 2 week tool that recovers even 15 percent of lost basket is economically meaningful to the owner even at tiny absolute rupiah values.

---

## Existing Solutions and Why They Fail

### Digital cashier apps

Moka (https://moka.pos) and Pawoon (https://pawoon.com) and Kasir Pintar are the visible incumbents in the warung digital cashier space. They solve record keeping: sales log, inventory count, simple reports. They fail the warung empowerment test on three axes:

- Pricing floor. Moka starts around Rp 199.000 per month, Pawoon around Rp 99.000 per month (verify live for current tiers). For a warung doing a few million rupiah in monthly turnover, a six figure monthly SaaS fee is a large share of profit. Many warung owners subscribe, see the report they do not act on, and churn.
- Wrong job. The cashier app optimizes the owner's internal bookkeeping. It does nothing to pull customers back from the minimarket or to lower the cost of goods. It is a ledger, not a weapon.
- App fatigue. Asking a warung owner to learn a new dashboard is a heavy ask. The phone already has WhatsApp open all day. A new app is a second surface that gets ignored.

### Koperasi and PKK style programs

Government backed cooperative and community programs exist to aggregate warung purchasing, but they are slowed by bureaucracy. The warung mikro finds joining cumbersome, the aggregation is often manual and slow, and the benefit arrives late. The pain file notes that warung mikro struggle to join these programs. The opportunity is not to replace koperasi but to give them a lightweight digital coordination layer they currently lack.

### The moratorium itself

As discussed, the permit moratorium protects the frontier but does not upgrade the incumbent warung. It is necessary political cover but insufficient economically.

### What is missing

Nothing in the market gives a warung three things at once, for free or near free, inside WhatsApp: (1) pooled buying power to approach distributor or principal pricing, (2) a clean QRIS accept with separated business settlement and zero monthly fee, (3) a loyalty loop that makes the regular come back. That combination, delivered where the owner already lives, is the wedge.

---

## The Wedge: WA-first Collective Buying Plus QRIS Plus Loyalty

The product is a toolkit, not a platform that demands the warung change behavior. It has four modules, each shippable independently so the minimum viable version can launch in two weeks:

### Module 1, group buying aggregator

Warungs in one RW or desa join a WhatsApp group managed by the bot. Each week the bot posts an open order for a basket of fast moving staples: beras, gula, minyak goreng, telur, mie instan, sabun, rokok (where compliant), and so on. Each warung taps to add its quantity. The bot sums the RW total. When the pooled volume crosses a distributor or principal threshold (for example one pallet of beras), the bot locks the group order and sends it to a pre negotiated supplier who delivers to a single drop point. Each warung pays its share via QRIS. The warung gets pallet scale price on a carton scale order.

The mechanism is identical to what a koperasi is supposed to do, but the coordination cost drops from meetings and ledgers to a WhatsApp thread and a background worker.

### Module 2, QRIS accept with clean settlement

Bank Indonesia's QRIS standard lets any merchant accept any QRIS wallet or bank app through one code. Critically for micro merchants, BI has waived the merchant discount rate for merchants below a transaction volume threshold, meaning a qualifying micro warung can accept QRIS at effectively zero percentage cost rather than the standard rate charged to larger merchants (verify live: BI QRIS page at https://www.bi.go.id/id/sistem-pembayaran/inisiatif-bank-indonesia/qris/ and the relevant PBI on QRIS MDR). This removes the single biggest objection to cashless adoption: the fee.

The toolkit does not build its own payment rail. It integrates a licensed QRIS aggregator (a registered payment gateway or a BPR/Bank Umum sponsored acquiring arrangement) that mints a static or dynamic QR per warung and settles to the warung's own account. The bot simply shows the QR when a customer wants to pay and confirms settlement via the aggregator callback. No monthly fee, no new app, just a QR image in WhatsApp.

### Module 3, loyalty ledger

The bot keeps a per customer points balance keyed to the customer's WhatsApp number or a simple member code. Each purchase accrues points. The warung owner can configure a simple rule, for example 1 point per Rp 10.000, redeemable at a threshold. The bot reminds the regular when points are close to a reward. This is the minimarket member card, rebuilt as a WhatsApp thread. It costs the warung nothing to run because the ledger is just rows in a database behind the bot.

### Module 4, smart stock signal (later phase)

Once enough pooled order and sales data accumulates, the bot can suggest what a given warung should stock next week based on aggregate RW demand and seasonality. This is the "stok pintar" promise from the pain file, but it is a phase two feature, not required for launch. It depends on data the earlier modules collect as a side effect.

---

## Technical Architecture

The system is a backend service plus a WhatsApp interface. It does not need a native mobile app. The reference stack is Python FastAPI (or Flask) for the bot backend, a PostgreSQL database, a WhatsApp Business API connection (either Meta's cloud API or an official BSP such as 360Dialog or Twilio), and a QRIS aggregator SDK. A cron worker runs the weekly group buy lifecycle.

### Component map

The WhatsApp Business Platform webhook receives inbound messages and delivers outbound templates and session replies. The bot orchestrator parses intent (join group, add item, check QR, redeem points, ask stock). The group buy engine manages the weekly order lifecycle per RW. The supplier connector posts locked orders to the distributor and ingests delivery confirmation. The payments connector mints QRIS codes and listens for settlement callbacks. The loyalty ledger accrues and redeems points. An admin dashboard (optional, for the operator not the warung) shows RW aggregation, margins, and churn.

### WhatsApp delivery constraints

The WhatsApp Business Platform distinguishes session messages (replied within 24 hours of a user message, free) from template messages (proactive, pre approved, billed). The group buy open announcement and the loyalty reminder are proactive, so they must use approved templates or ride within an open session. The bot must be designed so that most interaction happens inside the 24 hour window after the warung owner messages, and template messages are reserved for the weekly order open and critical reminders. This is a real cost and compliance surface, not a detail. Pricing and template policy are at https://developers.facebook.com/docs/whatsapp (verify live for current rates).

---

## Working Pseudo Code

The following snippets are illustrative reference implementations in Python. They are pseudo code with comments, not a complete production system. They show the shape of the core logic so a builder can start.

### Inbound webhook handler

```
# FastAPI webhook for WhatsApp Business Cloud API
# Meta sends POST /webhook with a signed payload; verify the X-Hub-Signature-256 header.
from fastapi import FastAPI, Request
import hmac, hashlib, os

app = FastAPI()
APP_SECRET = os.environ["WA_APP_SECRET"]

def verify_signature(raw_body: bytes, sig: str) -> bool:
    expected = hmac.new(APP_SECRET.encode(), raw_body, hashlib.sha256).hexdigest()
    return hmac.compare_digest(expected, sig)

@app.post("/webhook")
async def webhook(request: Request):
    raw = await request.body()
    sig = request.headers.get("X-Hub-Signature-256", "")
    if not verify_signature(raw, sig):
        return {"status": "forbidden"}
    payload = await request.json()
    # Meta wraps messages under entry[0].changes[0].value.messages[0]
    for change in payload["entry"][0]["changes"]:
        val = change["value"]
        if "messages" not in val:
            continue
        for msg in val["messages"]:
            wa_id = msg["from"]            # customer WhatsApp number, E.164
            text = msg.get("text", {}).get("body", "").strip().lower()
            handle_message(wa_id, text)
    return {"status": "ok"}

def handle_message(wa_id: str, text: str):
    # Route intent. This is the orchestrator stub.
    if text.startswith("join"):
        join_group(wa_id, text)
    elif text.startswith("beli") or text.startswith("order"):
        add_to_order(wa_id, text)
    elif text in ("qr", "bayar"):
        send_qris(wa_id)
    elif text in ("poin", "saldo"):
        send_loyalty_balance(wa_id)
    else:
        send_help(wa_id)
```

### Group buy lifecycle engine

```
# Weekly group-buy state machine per RW group.
# States: IDLE -> OPEN -> LOCKED -> DELIVERED -> SETTLED
import datetime

GROUP_BUY_THRESHOLDS = {
    "beras_5kg": 20,    # pallet-ish volume that unlocks distributor price
    "minyak_2l": 30,
    "gula_1kg": 25,
    "telur_satuan": 100,
    "mie_dus": 15,
}

def open_order(rw_id: str):
    # Called by cron every Monday 08:00 WIB. Sends template to group.
    create_order(rw_id, status="OPEN", opened_at=datetime.datetime.now())
    send_template(rw_id, "group_buy_open", {"week": iso_week()})

def add_to_order(wa_id: str, text: str):
    # Parse "beli beras_5kg 3" -> item + qty
    _, item, qty = text.split()
    qty = int(qty)
    order = get_open_order_for_warung(wa_id)
    if not order:
        return send_help(wa_id)
    upsert_line(order.id, wa_id, item, qty)
    # Check if crossing threshold triggers a better price tier
    total = sum_lines(order.id, item)
    if total >= GROUP_BUY_THRESHOLDS.get(item, 1e9):
        notify_price_unlock(order.id, item, tier="distributor")
    send_confirmation(wa_id, item, qty, running_total=total)

def lock_order(rw_id: str):
    # Called by cron Friday 18:00 WIB or when all thresholds met.
    order = get_open_order(rw_id)
    if order.status != "OPEN":
        return
    lines = aggregate_lines(order.id)   # item -> total qty across RW
    supplier = pick_supplier(lines)      # cheapest quote meeting MOQ
    po = create_po(supplier, lines, drop_point=rw_id)
    send_po_to_supplier(po)
    order.status = "LOCKED"
    notify_warungs(order.id, "Pesanan RW terkunci, total %s, estimasi harga lebih murah" % po.savings_pct)

def confirm_delivery(rw_id: str):
    # Supplier or operator marks delivered; unlock per-warung QRIS split payments.
    order = get_open_order(rw_id)
    order.status = "DELIVERED"
    for wa_id, owe in compute_per_warung_owe(order.id).items():
        send_qris(wa_id, amount=owe, memo="Warung buy %s" % rw_id)
```

### QRIS code minting and settlement

```
# QRIS dynamic code via a licensed aggregator SDK (pseudo).
# A real integrator uses a PJP or bank-sponsored acquirer, never builds the rail.
import os, requests, uuid

AGG_BASE = os.environ["QRIS_AGG_BASE"]
AGG_TOKEN = os.environ["QRIS_AGG_TOKEN"]

def mint_dynamic_qris(warung_wa_id: str, amount: int, memo: str) -> str:
    # Dynamic QR carries exact amount; static QR is amountless for over-the-counter.
    resp = requests.post(f"{AGG_BASE}/v1/qris/dynamic",
        headers={"Authorization": f"Bearer {AGG_TOKEN}"},
        json={
            "merchant_id": get_merchant_id(warung_wa_id),  # mapped per warung
            "amount": amount,
            "reference_id": uuid.uuid4().hex,
            "memo": memo,
            "expiry_seconds": 900,
        }, timeout=10)
    resp.raise_for_status()
    return resp.json()["qr_string"]   # EMV QR string to render as image

def qris_callback(request: Request):
    # Aggregator calls this on settlement. Verify signature, credit ledger.
    body = await request.json()
    if not verify_agg_sig(body):
        return {"status": "forbidden"}
    warung = resolve_merchant(body["merchant_id"])
    credit_business_ledger(warung, body["amount"], body["reference_id"])
    notify_warung_paid(warung, body["amount"])
    return {"status": "ok"}
```

### Loyalty accrual

```
# Points ledger keyed by customer WhatsApp number.
def accrue_points(customer_wa_id: str, warung_wa_id: str, amount_idr: int):
    # Rule: 1 point per Rp 10.000 spent, configurable per warung.
    rule = get_loyalty_rule(warung_wa_id)
    points = amount_idr // rule["idr_per_point"]
    upsert_customer_points(customer_wa_id, warung_wa_id, delta=points)
    maybe_nudge_redeem(customer_wa_id, warung_wa_id)

def redeem_points(customer_wa_id: str, warung_wa_id: str, points: int):
    bal = get_customer_points(customer_wa_id, warung_wa_id)
    if points > bal:
        send_reply(warung_wa_id, "Poin tidak cukup")
        return
    discount = points * get_redeem_rate(warung_wa_id)  # e.g. 1 point = Rp 10
    apply_discount_to_current_sale(warung_wa_id, discount)
    deduct_customer_points(customer_wa_id, warung_wa_id, points)
```

### Data model sketch

```
warung(id, wa_id unique, rw_id, merchant_id, joined_at)
rw_group(id, name, drop_point, supplier_id)
customer(id, wa_id unique)
group_order(id, rw_id, status, opened_at, locked_at)
order_line(id, order_id, warung_id, item, qty)
supplier(id, name, moq_json, price_json)
po(id, supplier_id, order_id, total_qty_json, savings_pct)
ledger_entry(id, warung_id, type[credit/debit], amount, ref, at)
points_balance(id, customer_wa_id, warung_wa_id, points)
```

This schema is intentionally flat. The phase two smart stock module adds a `sales_event` table fed by the loyalty and QRIS flows, which then powers demand forecasting per RW.

---

## Unit Economics and Willingness to Pay

The pain file estimated willingness to pay in the range of Rp 0 to Rp 50.000 per month, or a 1 percent take rate on the pooled buy. This is the right anchor. A warung that already churned from Moka at Rp 199.000 per month will not pay a six figure SaaS fee. The model that fits is free base plus a small cut of the value created:

- Group buy take rate. Charge the supplier or take a 1 to 2 percent spread on the aggregated order. The warung pays the same or less than its old distributor price, the supplier gets a guaranteed bulk order with lower go to market cost, and the toolkit earns the spread. This aligns incentives: the toolkit only makes money when the warung saves money.
- QRIS. If the aggregator pays a share of MDR or the toolkit negotiates a micro merchant rate, there may be a small per transaction rebate. With BI's MDR waiver for micro merchants, the warung pays nothing, which is the selling point.
- Loyalty. Free, because it increases order frequency and therefore the group buy volume that the toolkit monetizes.

A simple model: a RW of 30 warungs each buying Rp 1.500.000 of staples per week pools Rp 45.000.000 weekly. A 1.5 percent spread is Rp 675.000 per week per RW, about Rp 2.7 million per month, before payment rebates. At a few hundred RWs that is a real business. The cost side is the WhatsApp API messages (templates billed per 24 block, see Meta pricing), the aggregator integration, and light operator time. The marginal cost per RW is low once the engine runs, which is why the model scales with coordination, not headcount.

Note these are illustrative arithmetic from stated assumptions, not observed financials (verify live: build a real cohort before committing capital).

---

## Go To Market in the Indonesian Context

### Start with the RW, not the nation

The unit of adoption is the RW (rukun tetangga), the smallest neighborhood administrative unit. A single motivated warung owner or a kader PKK can be the champion who brings the other 10 to 40 warungs in the RW into the WhatsApp group. The toolkit should ship with a "buka grup RW" flow that a champion runs.

### Partner the koperasi, do not fight it

Dinas Koperasi and existing koperasi already have the relationships and sometimes the supplier contacts. The toolkit is the digital layer they lack. A pilot can be brokered through a local koperasi that agrees to be the legal drop point and trust anchor. This also softens the regulatory story.

### Use the moratorium tailwind

With government openly worried about warung survival in 2026, a warung empowerment toolkit has narrative alignment with policy. That does not mean government funding (which is slow), but it means low political risk and possible local government amplification (kelurahan bulletin, posyandu cross post, etc.).

### Warung as community hub

The pain file notes adjacent plays: PPOB (titip bayar listrik, pulsa, BPJS), isi ulang, and cross sell to traditional market traders. The QRIS accept and the WhatsApp thread are the foundation for all of these. A warung that becomes the cashless and PPOB node of its RW increases foot traffic, which is the entire game.

---

## Regulatory Surface

### Payments

QRIS acceptance must go through a licensed acquiring path. Building a payment rail directly is not permitted for a non licensed entity. The toolkit integrates a registered PJP (Penyelenggara Jasa Pembayaran) or a bank sponsored arrangement. Bank Indonesia's QRIS rulebook and PJP licensing regime are at https://www.bi.go.id (verify live for the exact POJK/PBI numbers). The MDR waiver for micro merchants is the key economic fact and must be confirmed live before pricing.

### Data protection

The toolkit stores customer WhatsApp numbers and purchase behavior. Indonesia's Personal Data Protection Law, Undang Undang No. 27 Tahun 2022, applies. The system must have a privacy notice, a lawful basis for processing (consent for loyalty), data retention limits, and a deletion path. The Komdigi (Kementerian Komunikasi dan Digital) oversees aspects of this; see https://www.komdigi.go.id (verify live). For a two week MVP, at minimum a plaintext consent message and a delete command are required before any customer number is stored.

### Cooperative and trade law

If the toolkit formally organizes buying through a koperasi, the cooperative legal form (UU No. 25 Tahun 1992 about cooperatives) and its reporting apply to the cooperative, not necessarily to the software vendor. Keep the vendor role as a technology provider, not as the buyer, to avoid becoming a trading entity with its own licensing obligations.

### Competition

Aggregating warung demand and negotiating supplier price is normal commerce. The risk is if the toolkit were to abuse a dominant position or lock suppliers exclusively in an anti competitive way. At the scale described this is not a near term concern, but the design should avoid exclusivity clauses that could later draw KPPU attention (https://www.kppu.go.id, verify live).

---

## Metrics That Prove or Kill the Idea

The idea lives or dies on three numbers, not on signups:

- Pooled savings realization. Does the RW actually buy at a lower unit price after aggregation than before? Measure average unit cost per item pre and post adoption. If the spread does not materialize, the core promise fails.
- Repeat order rate. Do warungs reorder through the group buy week after week? A one time bulk buy that does not repeat means the coordination cost exceeded the benefit.
- QRIS adoption and loyalty frequency. Does accepting QRIS and running points increase transaction count at the warung? The whole point is to win back the cashless convenience shopper. If QRIS volume rises but total basket does not, the warung is just converting cash sales to QRIS sales with no net gain.

A healthy pilot shows double digit percentage reduction in unit cost on at least three staples, a repeat order rate above 60 percent across the RW within a month, and a measurable lift in weekly transaction count at participating warungs. Anything weaker than that is a research result, not a product.

---

## Build Plan

### Two week MVP

- WhatsApp bot with join, beli, qr, poin commands.
- One RW, one supplier, manual PO by operator.
- Static QRIS per warung via one aggregator.
- Flat loyalty rule, 1 point per Rp 10.000.
- Google Sheet or SQLite backend, no dashboard.

### One month version

- Automated weekly lifecycle cron.
- Multiple suppliers with simple price comparison.
- Dynamic QRIS with settlement callback.
- Basic admin view of RW aggregation.

### Three month product

- Smart stock suggestions from accumulated data.
- Koperasi white label mode.
- PPOB and isi ulang add ons.
- Churn and savings dashboards.
- Privacy controls per UU PDP.

This plan matches the pain file's own time to build estimate and extends it with the data driven phase two.

---

## Risks and Honest Caveats

- Supplier reliability. A warung that gets a late or short delivery loses trust faster than it was won. The drop point and supplier SLA are the operational risk, not the software.
- WhatsApp cost creep. Template message billing can erode margin if the bot is chatty. Design for sparse, high value templates.
- Champion dependency. Adoption hinges on one motivated person per RW. Losing the champion can collapse the group. The toolkit should make the champion role easy to hand off.
- Cash mindset. Some warung owners and customers still prefer cash. QRIS is an add, not a replacement, in early phases.
- Data quality. Phase two forecasting is only as good as the phase one data. If warungs under report or skip the bot, the smart stock signal is noise.

---

## Cross Links Inside the Vault

This opportunity reinforces and is reinforced by sibling files:

- 03-id-business-trends/demand-mining/warung-kelontong-kalah-minimarket.md is the originating pain signal.
- 03-id-business-trends/bottlenecks/warung-micro-fulfillment.md frames the warung as a last mile node, which this toolkit digitizes.
- 03-id-business-trends/bottlenecks/cod-settlement-infrastructure.md covers the settlement layer this toolkit depends on for QRIS.
- 03-id-business-trends/bottlenecks/umkm-npwp-registration-gap.md is adjacent: formalization helps warungs access the supplier credit this toolkit surfaces.
- 07-gaps-and-opportunities/inbox/2026-07-06-umkm-halal-cert-automation.md shows parallel demand for lightweight SME tooling delivered simply.
- 07-gaps-and-opportunities/opportunities/halalready-certification-platform.md and bpr-digital-transformation-saas.md are sibling plays in the SME empowerment thesis.

---

## Source List and Verification Status

Canonical URLs cited (all require live re-confirmation of current figures this tick could not perform):

- Bank Indonesia QRIS: https://www.bi.go.id/id/sistem-pembayaran/inisiatif-bank-indonesia/qris/ (verify live: MDR waiver threshold and current rate)
- Bank Indonesia payments statistics: https://www.bi.go.id (verify live: warung and QRIS merchant counts)
- BPS retail census: https://www.bps.go.id (verify live: traditional kiosk count)
- Kementerian Koperasi dan UKM: https://www.kemenkopukm.go.id (verify live: warung policy and moratorium stance)
- Kementerian Perdagangan: https://www.kemendag.go.id (verify live: minimarket permit policy)
- Alfamart investor relations: https://www.alfamartkorpri.com (verify live: outlet count)
- Indomaret corporate: https://www.indomaret.co.id (verify live: outlet count)
- Tirto moratorium coverage: https://tirto.id (2026-02-26, link unreachable full text this tick)
- Bisnis.com warung Madura coverage: https://bisnis.com (2025-10-30, headline confirmed)
- CNN Indonesia warung coverage: https://www.cnnindonesia.com (2026-02-26, headline confirmed)
- Katadata retail: https://katadata.co.id (verify live: chain outlet tracking)
- WhatsApp Business Platform docs: https://developers.facebook.com/docs/whatsapp (verify live: template pricing)
- OJK for any BPR sponsored acquiring path: https://www.ojk.go.id (verify live)
- Komdigi PDP: https://www.komdigi.go.id (verify live: UU PDP implementation guidance)
- KPPU competition: https://www.kppu.go.id (verify live)

Verification status: live web search and extract were blocked this tick due to missing PARALLEL_API_KEY in the cron environment (same condition as the BPR SaaS one-pager dated 2026-07-09). No live quantitative figure was invented. Every numeric claim above is either an established public knowledge estimate flagged "(verify live)" or explicit illustrative arithmetic from stated assumptions. Headlines and dates that were confirmed through the prior pain file are noted as confirmed; full article bodies marked "source unreachable this tick" where blocked. A builder must re verify all figures against the live URLs above before committing resources.

---

## Supplier and Distributor Economics, Worked

To judge whether the pooled buy actually delivers savings, the toolkit must understand the distribution ladder it is inserting into. Indonesian FMCG distribution typically runs principal (pabrik) to distributor (PT authorized) to sub distributor or agen to warung. Each step adds margin and the warung sits at the bottom paying the most per unit.

A worked example for beras medium 5 kg, using illustrative price ladder assumptions (verify live with a real distributor quote):

- Principal ex mill price: Rp 58.000 per 5 kg.
- Distributor sells to agen at Rp 60.500 (margin Rp 2.500).
- Agen sells to warung at Rp 63.000 (margin Rp 2.500), often with 1/30 or 2/60 credit terms that carry implicit cost if the warung cannot pay fast.
- Warung sells to consumer at Rp 68.000, gross margin Rp 5.000 before spoilage and labor.

When the RW pools 30 warungs at, say, 10 bags each, that is 300 bags, roughly half a pallet. At that volume the toolkit can approach the distributor directly and skip the agen margin, or approach the principal's program for modern warung aggregation. Even capturing Rp 1.500 of the agen margin per bag yields Rp 450.000 saved across the RW, about Rp 15.000 per warung per week. For a warung turning over a few million rupiah monthly, Rp 15.000 weekly on one staple is meaningful, and the same logic compounds across the basket.

The toolkit's job is to make that half pallet threshold reachable for warungs that individually buy one or two bags. The group buy engine is literally a volume consolidator. The savings are real whenever the per unit price curve is decreasing in order size, which it is throughout FMCG because fixed logistics and margin steps are amortized over more units.

The 1.5 percent spread model from the unit economics section can be read two ways. Either the toolkit negotiates the lower price and keeps a sliver (supplier funded, because the supplier gets a guaranteed bulk order with lower sales cost), or the toolkit passes the full saving to the warung and charges the supplier a small finder fee. The cleaner story for adoption is to pass most of the saving to the warung and monetize from the supplier side, because warung trust is the scarce asset and the toolkit should spend it on the warung's benefit, not its own margin.

---

## Competitive Teardown: Who Else Touches This

### Warung Pintar (parent: Astra / Grab era experiments)

Warung Pintar was a funded experiment that put a tech enabled kiosk with a digital vending facade and a back office system into neighborhoods, often run by an operator rather than a traditional warung owner. It raised significant capital then retrenched. Its lesson for this toolkit: a heavy physical kiosk build is expensive and slow. The WA first approach deliberately avoids hardware. The risk it teaches is that fancy kiosks do not beat a warung owner's local relationships; the toolkit should empower the existing owner, not replace them with a machine.

Source: Tech in Asia and KrASIA coverage of Warung Pintar (verify live at https://www.techinasia.com and https://kr-asia.com).

### Mbiz and Ralali (B2B procurement marketplaces)

Mbiz (https://mbiz.co.id) and Ralali (https://ralali.com) are B2B e procurement platforms that let businesses buy supplies online, sometimes with aggregated catalogs. They target larger warung, kantin, and SME buyers with a web or app interface and credit lines. They fail the micro warung on the same axes as the cashier apps: app fatigue, minimum order friction, and no local community coordination. They are the supplier side opportunity, not the competitor, for this toolkit. The toolkit can be the lightweight front end that feeds aggregated RW orders into a Mbiz or Ralali bulk quote.

### Kudi and similar agent banking

Kudi (acquired) and similar agent banking plays turned warungs into cash in/cash out points. They proved warungs will act as financial nodes if the tool is simple and the warung earns a fee. That validates the QRIS and PPOB module here. The difference is this toolkit adds procurement leverage, not just cash services.

### Modern chain private label

Alfamart and Indomaret private label products are themselves a low price weapon. The warung cannot beat private label on branded margin, but it can beat it on fresh, on credit relationships, and on the neighbor feel. The toolkit should steer pooled buys toward items where the warung's local edge holds, not pick a losing fight on branded soda.

---

## Regional Variation: Java Versus Luar Jawa

The toolkit's economics differ sharply by geography, and the build should account for it from day one.

- Java tier 1 and 2. Dense RW, short distances, many warungs per RW, mature distributor coverage. High competition from chains means high pain and high willingness to try. The drop point logistics are easy. This is the best pilot zone.
- Java tier 3 and rural. Fewer warungs per RW, longer supplier distance, weaker chain presence but also weaker distributor service. The pooled buy matters more because the warung is even more isolated, but the drop point and last mile within the RW need a trusted aggregator (often the koperasi or a single larger warung).
- Luar Jawa, Sulawesi, Sumatera, Papua. Fragmented supply, higher transport cost, sometimes only one distributor covering a wide area. The pooled buy can unlock price the warung has never seen, but supplier reliability and delivery SLA are the dominant risk. Pilot here only after the Java engine is proven, or run a deliberately small single RW test to learn the supplier failure modes.

The phase two smart stock module must be region aware. Demand for beras per RW in Java differs from Papua, and festival seasonality (Lebaran, Natal, Nyadran) shifts the basket. A national one size forecast will be wrong; the data model should partition by province and kabupaten.

---

## End to End Walkthrough: One RW, One Week

A concrete narrative of the MVP running, to make the system tangible.

Monday 08:00 WIB. Cron opens the order for RW 04 Kelurahan Mawar. The bot sends an approved template to the RW group: "Pesan bareng minggu ini buka. Balas 'beli beras_5kg 10' dan seterusnya. Tutup Jumat 18:00." Warung Bu Siti, who lost half her foot traffic to an Indomaret 50 meters away, replies "beli beras_5kg 8, minyak_2l 6, gula_1kg 5". The bot confirms and shows her running total.

Tuesday through Thursday. Other warungs add lines. The bot notifies the group when beras crosses the 20 bag threshold that unlocks distributor price, and again at 30 bags for an even better tier. Bu Siti sees her neighbors joining and adds 2 more bags. Peer momentum is the growth loop.

Friday 18:00. Cron locks the order. The engine aggregates: 34 beras, 52 minyak, 41 gula, 120 telur, 22 mie dus. It picks the distributor with the best quote meeting MOQ and posts the PO. The bot tells each warung what they owe and that the price is lower than last week. Bu Siti owes Rp 612.000 instead of her usual Rp 680.000 for the same basket, a Rp 68.000 save, about 11 percent.

Saturday 09:00. Supplier delivers to the RW drop point (the koperasi lot). Warungs collect. Each pays via the dynamic QRIS the bot sent. Settlement lands in Bu Siti's account the same or next day, separated from her personal e wallet, with a clean record she can show her husband or the koperasi.

All week. A regular customer, Pak Dodi, buys Rp 50.000 of daily needs and the bot accrues 5 points to his WhatsApp number. When he hits 50 points the bot nudges Bu Siti to offer him a Rp 5.000 discount, pulling him back from the Indomaret. The loyalty ledger is the minimarket member card, rebuilt free.

This is the whole product in one week. The software is modest. The coordination is the value.

---

## Message Template Catalog (WhatsApp)

The proactive messages must use Meta approved templates. A starter catalog:

- group_buy_open: "Pesan bareng RW {{rw_name}} minggu ini sudah buka. Balas 'beli <item> <jml>' sebelum Jumat 18:00." (weekly, proactive)
- price_unlock: "{{item}} RW {{rw_name}} sudah tembus harga grosir! Tambah pesanan sebelum tutup." (triggered, can ride session)
- order_locked: "Pesanan RW {{rw_name}} terkunci. Total Rp {{total}}, estimasi hemat {{save_pct}}%. Bayar via QRIS." (proactive, template)
- deliver_ready: "Pesanan datang di drop point {{drop_point}}. Ambil hari ini." (proactive, template)
- points_nudge: "Poin Anda {{points}}. Tukar Rp {{value}} di warung {{warung}}." (proactive, template, loyalty)

Each template must be submitted and approved in the Meta Business Manager before use. Rejection risk is real for templates that read as promotional; phrasing should be transactional and informative. This is an operational task, not a coding one, and it gates launch.

---

## Privacy Implementation Notes (UU PDP)

Indonesia's Personal Data Protection Law, Undang Undang No. 27 Tahun 2022, requires a lawful basis, purpose limitation, and data subject rights. For this toolkit:

- Consent capture. Before storing a customer's WhatsApp number for loyalty, send one plaintext consent message: "Untuk gabung poin di Warung Bu Siti, balas SETUJU. Data hanya untuk poin warung ini." Store the consent timestamp.
- Purpose limit. The customer's number and points are per warung. Do not cross reference customers across warungs without separate consent; the smart stock module should use aggregate, de identified demand, never the customer identity.
- Retention and deletion. Provide a "hapus data" command that deletes the customer's points row and the consent record. Set a default retention of, say, 24 months of inactivity.
- Breach notice. The system must be able to notify the warung owner and, if required, the regulator, of any unauthorized access. Keep the data store access logged.

This is not legal advice; the operator should confirm with a PDP competent advisor before launch (Komdigi guidance at https://www.komdigi.go.id, verify live).

---

## Frequently Asked Questions, Builder Edition

Why WhatsApp and not a dedicated app. Because the warung owner already lives in WhatsApp all day and will not install or open a second app. Distribution, onboarding, and support all collapse into one surface the owner trusts.

What if the supplier delivers short. The PO and the drop point receipt must be checked against the order. The toolkit should support a dispute flag that holds the warung's QRIS payment until resolved, and track supplier reliability so chronic short deliverers are dropped. Supplier SLA is the operational risk, so instrument it from week one.

What if only three warungs join. The MVP can still run at small scale; the thresholds simply may not unlock the best tier every week. The growth loop depends on showing a visible saving to the first adopters so they recruit neighbors. A champion per RW is the growth engine.

How is this different from a koperasi. It is the koperasi's missing digital coordination layer. It does not replace the cooperative legal form; it makes aggregation fast and transparent where the cooperative is slow and opaque. Partnering the koperasi is the recommended path, not competing with it.

Is the QRIS fee really zero. For micro merchants below the BI volume threshold, the MDR is waived, so acceptance is effectively free to the warung. The toolkit must confirm the warung qualifies and must re verify the threshold live, because policy can change. If the warung exceeds the threshold, a small MDR applies and the pricing story shifts.

---

## Appendix: Minimal SQLite Schema for the MVP

```
CREATE TABLE warung (
  id INTEGER PRIMARY KEY,
  wa_id TEXT UNIQUE,
  rw_id TEXT,
  merchant_id TEXT,
  joined_at TEXT DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE rw_group (
  id TEXT PRIMARY KEY,
  name TEXT,
  drop_point TEXT,
  supplier_id TEXT
);

CREATE TABLE customer (
  id INTEGER PRIMARY KEY,
  wa_id TEXT UNIQUE,
  consent_at TEXT
);

CREATE TABLE group_order (
  id INTEGER PRIMARY KEY,
  rw_id TEXT,
  status TEXT,
  opened_at TEXT,
  locked_at TEXT
);

CREATE TABLE order_line (
  id INTEGER PRIMARY KEY,
  order_id INTEGER,
  warung_id INTEGER,
  item TEXT,
  qty INTEGER
);

CREATE TABLE supplier (
  id TEXT PRIMARY KEY,
  name TEXT,
  moq_json TEXT,
  price_json TEXT
);

CREATE TABLE po (
  id INTEGER PRIMARY KEY,
  supplier_id TEXT,
  order_id INTEGER,
  total_qty_json TEXT,
  savings_pct REAL
);

CREATE TABLE ledger_entry (
  id INTEGER PRIMARY KEY,
  warung_id INTEGER,
  type TEXT,
  amount INTEGER,
  ref TEXT,
  at TEXT DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE points_balance (
  id INTEGER PRIMARY KEY,
  customer_wa_id TEXT,
  warung_id INTEGER,
  points INTEGER DEFAULT 0
);
```

This schema supports the pseudo code above and is enough to run the two week MVP without a heavy database. The three month product migrates to PostgreSQL and adds the sales_event table for forecasting.

---

## Operations Runbook for the Pilot Operator

The toolkit is a coordination business, not just software, so the human operator's weekly loop matters. A concrete runbook for a single operator running up to, say, 20 RWs:

- Monday. Confirm the supplier quote sheet is current. Open orders across all RWs via cron. Watch for RWs below the minimum item threshold and nudge the champion.
- Tuesday to Thursday. Answer warung questions in the groups. Resolve payment failures (a warung whose QRIS settlement bounced). Track which items are close to unlocking a better tier and broadcast the price unlock message to pull more volume.
- Friday. Lock all orders at 18:00. Confirm each PO is acknowledged by the supplier with a delivery window. If a supplier cannot meet an RW's volume, fall back to the second cheapest or split the order, and log the miss.
- Saturday. Confirm deliveries at drop points. Chase any no show delivery. Reconcile QRIS settlements against PO totals. Flag any warung that has not paid and follow up.
- Sunday. Review the savings report per RW and send it to champions. Identify the next RW to onboard from the waitlist.

The operator's leverage is coordination, not labor. Twenty RWs at this cadence is feasible for one person for the pilot. Past that, the engine must automate supplier negotiation and delivery tracking, which is the one month and three month work.

---

## Failure Mode Table

A blunt list of what kills the pilot and how the design defends against each.

| Failure mode | Symptom | Defense in design |
| --- | --- | --- |
| Supplier short delivery | Warung receives fewer bags than paid for | PO vs receipt check at drop point, dispute flag holds QRIS payout, supplier reliability score drops |
| Champion quits | RW group goes silent after two weeks | Make champion role transferable, recruit a deputy on day one, operator nudges weekly |
| QRIS settlement delay | Warung worries money missing | Settlement callback posts to ledger instantly, warung gets paid confirmation message, support command |
| Template rejection | Proactive message blocked by Meta | Phrase templates transactionally, pre submit and get approval before launch, ride sessions where possible |
| Low repeat rate | Warungs buy once then lapse | Show visible saving in week one, peer momentum in group, loyalty pull on the customer side |
| Cash only customers | QRIS unused | QRIS is an add, not a replacement; keep cash path working, reward QRIS use subtly |
| Data complaint | Customer objects to number stored | Plaintext consent before store, hapus data command, per warung isolation |
| Supplier price worse than agen | No saving realized | Engine compares distributor quote to the warung's known agen price; only lock if net positive after transport |

This table is the risk register. A pilot that survives the first two months without a supplier short delivery scandal and without a champion quitting is past the highest mortality risk.

---

## KPI Dashboard Specification (Operator View)

The operator needs a single screen. Fields per RW:

- Active warungs / total invited.
- This week pooled volume by item and total rupiah.
- Realized savings percent versus the warung's baseline agen price.
- Repeat order rate, trailing four weeks.
- QRIS adoption: share of warungs accepting, share of order value settled via QRIS.
- Loyalty: active customers, points issued, redemption rate.
- Supplier score: on time delivery rate, short delivery count, price competitiveness.
- Churn: warungs that have not ordered in two weeks.

A healthy RW dashboard shows active warungs at or above 60 percent of invited, savings above 8 percent on staples, repeat rate above 60 percent, and supplier on time delivery above 90 percent. Anything red on two of those four is a RW at risk and gets operator attention.

This dashboard is phase one operator aid; the three month product exposes a light version to champions so they self manage.

---

## Phased Rollout Plan by Geography

The launch sequence should follow pain and logistics, not ambition.

Phase 0, one RW proof. Pick one dense RW in a Java tier 2 city next to a new minimarket. Manual supplier, SQLite, single operator. Goal: prove the 8 percent plus saving and a 60 percent repeat rate. Two weeks.

Phase 1, one kelurahan cluster. Ten to twenty RWs in one kelurahan, one operator, automated weekly cron, one to two suppliers. Goal: operator runs the runbook smoothly, supplier reliability above 90 percent. One month.

Phase 2, one kota. Multiple kelurahan, two to three suppliers with price comparison, dynamic QRIS, basic dashboard, koperasi white label pilot. Goal: the engine, not the operator heroics, carries the load. Three months.

Phase 3, multi kota Java. Regional partitioning in the data model, festival seasonality handling, PPOB add on. Goal: a defensible regional footprint before any luar Jawa expansion.

Phase 4, luar Jawa selective. Only after Java unit economics are proven, run small single RW tests in Sulawesi, Sumatera, and Papua to learn supplier failure modes. Do not scale luar Jawa until the supplier SLA problem is solved, because the delivery risk there is the dominant killer.

This staged plan respects the vault's evidence first discipline. Each phase has a kill criterion tied to the KPI dashboard, so the build stops early if the saving or repeat rate does not hold.

---

## Koperasi Integration Detail

Partnering a koperasi is the recommended legal and trust path. The integration shape:

- The koperasi is the legal buyer. It places the PO in its name, which sidesteps the toolkit becoming a trading entity with licensing obligations. The toolkit is the technology provider and coordination layer.
- The koperasi provides the drop point and a trusted aggregator, often its own premise or a large warung it backs.
- The toolkit gives the koperasi a transparent view of pooled demand it never had, which strengthens the koperasi's own supplier negotiation and reporting to Dinas Koperasi.
- Revenue share: the toolkit can take a small technology fee from the saving it creates, with the koperasi taking a portion too, aligning the cooperative's incentive with adoption.

The risk is koperasi bureaucracy slowing the pilot. Mitigation: start with a single pragmatic koperasi champion who wants the digital layer, not with the full cooperative board. One willing kader is enough to launch.

---

## Financial Model, Three Scenarios

Illustrative arithmetic from stated assumptions, not observed financials. Verify with a real cohort.

Assumptions per RW: 30 warungs, Rp 1.500.000 weekly staples each, Rp 45.000.000 pooled weekly, 4.5 percent blended staple margin captured as toolkit value at 1.5 percent take rate.

Base case. 50 RWs after three months. Weekly pooled Rp 2.25 billion. Take rate 1.5 percent = Rp 33.75 million weekly, about Rp 135 million monthly gross. WhatsApp template cost at, say, Rp 300 per proactive block across 50 RWs weekly is trivial. Operator cost for 50 RWs at one operator per 20 RWs is three operators, roughly Rp 30 to 45 million monthly all in. Net before supplier rebates about Rp 90 to 105 million monthly. This is a real small business, not a unicorn thesis.

Conservative case. Only 15 RWs reach repeat, take rate 1.0 percent, saving thinner at 6 percent. Weekly pooled Rp 675 million. Take rate 1.0 percent = Rp 6.75 million weekly, about Rp 27 million monthly gross. One operator, roughly Rp 12 million cost. Net about Rp 15 million monthly. Still positive and worth running as a focused local business.

Upside case. 200 RWs, take rate 1.5 percent, plus QRIS rebate and PPOB cross sell adding 0.5 percent. Weekly pooled Rp 9 billion. Take rate 2.0 percent = Rp 180 million weekly, about Rp 720 million monthly gross. At this scale the engine is automated and operator cost is a fraction. This is the path that attracts outside capital, but it should not be the launch assumption.

The honest framing: this is a profitable local coordination business at modest scale, with a venture shaped upside only if the engine automates supplier negotiation. The vault documents it as the former, with the latter noted as a possible sequel.

---

## Adjacent Monetization: PPOB and Isi Ulang

Once the warung is a QRIS node and a WhatsApp hub, two cheap add ons follow:

- PPOB (titip bayar). Listrik PLN, pulsa, token, BPJS, PDAM, game voucher. The warung earns a small fee per transaction and pulls foot traffic. The toolkit adds a PPOB command to the same bot. Providers exist that white label PPOB APIs; integration is a few endpoints.
- Isi ulang and agen brankas. Cash in/out for e wallets and bank accounts, the Kudi style play, earns a per transaction fee and deepens the warung as the RW financial node.

These do not need the group buy to work; they ride the QRIS and WhatsApp foundation. They are listed as adjacent, not core, because the core wedge is procurement leverage. But they materially improve warung foot traffic, which is the entire game against the minimarket.

---

## Pre Launch Build Checklist

A concrete task list so the two week MVP is not vague.

- [ ] Register a WhatsApp Business Account and a Meta app; obtain the Cloud API token and webhook verification.
- [ ] Stand up FastAPI service on a small VPS; wire the webhook with HMAC signature verification.
- [ ] Provision a Postgres or SQLite store with the schema in the appendix.
- [ ] Integrate one QRIS aggregator SDK; mint a static QR per warung; confirm settlement callback fires.
- [ ] Implement the four commands: join, beli, qr, poin, plus help and hapus data.
- [ ] Write and submit the five WhatsApp templates; get approval before any proactive send.
- [ ] Build the cron that opens orders Monday 08:00 and locks Friday 18:00 WIB.
- [ ] Recruit one RW champion; onboard the first warungs by hand.
- [ ] Hand negotiate one supplier quote sheet for five staples; load into the supplier table.
- [ ] Draft the UU PDP consent message and the deletion command; log consent timestamps.
- [ ] Run one full weekly cycle manually with the operator in the loop; measure saving and repeat.
- [ ] Only after a positive week one, automate and add the second RW.

This checklist is deliberately boring. The risk in a build like this is over engineering the bot before a single warung has saved a rupiah. The MVP should be embarrassingly manual on the supplier side and crisp on the warung side.

---

## Open Questions for the Next Researcher

The gaps this document cannot close without field work or a working key:

- Real distributor pricing curve per commodity and per region (the headline unknown).
- Current BI QRIS MDR waiver threshold and rate (policy may have moved since the last confirmation; verify live at bi.go.id).
- WhatsApp Business Platform current template pricing per 24 hour conversation block (verify live at developers.facebook.com/docs/whatsapp).
- Koperasi legal form requirements for placing a PO as the buyer versus the toolkit (confirm with a cooperative law advisor).
- Supplier willingness to deliver to a neighborhood drop point rather than a single commercial address.
- Whether warung owners will trust a pooled payment model where they pay before delivery, versus cash on delivery at the drop point.
- Festival seasonality coefficients for the smart stock forecast, by province.

Whoever takes the next tick should pick the distributor pricing curve first, because it is the load bearing assumption of the entire model.

---

## Glossary

RW. Rukun Tetangga, the smallest neighborhood administrative unit, typically 30 to 50 households, the adoption unit for this toolkit.

Koperasi. Cooperative, a member owned legal entity; the recommended legal buyer and trust anchor for the pooled PO.

QRIS. Quick Response Code Indonesian Standard, Bank Indonesia's unified national QR payment standard; one code accepts all wallets and banks.

MDR. Merchant Discount Rate, the percentage fee on a QRIS transaction; waived by BI for micro merchants below a volume threshold.

Agen. Sub distributor or local wholesale intermediary that sells carton scale to warungs; the margin layer the pooled buy skips.

PO. Purchase Order, the locked bulk order sent to the supplier.

PPOB. Payment Point Online Bank, the titip bayar services (PLN, pulsa, BPJS, PDAM) a warung can offer as an add on.

UU PDP. Undang Undang Pelindungan Data Pribadi, Indonesia's Personal Data Protection Law, No. 27 of 2022.

BSP. Business Solution Provider, a Meta approved WhatsApp API partner (for example 360Dialog, Twilio) alternative to the Cloud API.

---

## Why This Fits the Vault Thesis

The vault's spine is Indonesian micro merchant pain converted into buildable, lightly technical opportunity one-pagers. This file sits naturally beside the warung micro fulfillment bottleneck, the COD settlement bottleneck (the QRIS layer this depends on), and the UMKM formalization gap (a formalized warung accesses supplier credit this toolkit surfaces). It is also a clean demonstration of the vault's self evolution rule: the original pain signal was mined in 03-id-business-trends, promoted through the 07 inbox, and here becomes a full opportunity with a concrete build path. The next tick should close the one remaining gap this document surfaces: the real distributor pricing curve, which only field work can fill.

---

## Next Research Step

The single biggest unknown is the real distributor and principal pricing curve at pallet scale versus the warung's current carton price, per commodity and per region. A field interview with two or three distributors in one kota, plus a quote sheet from one QRIS aggregator, would convert this one-pager from a research document into a buildable spec. That is the recommended follow up gap for the next tick.
