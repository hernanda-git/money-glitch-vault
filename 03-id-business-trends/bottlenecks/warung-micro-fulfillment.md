# Warung as Micro-Fulfillment Nodes: The Unconverted 16 Million

Research note, bottleneck analysis. Last updated 2026-07-07. Folder: `03-id-business-trends/bottlenecks/`. Cross-reference sibling docs: `ojol-logistics-inefficiency.md`, `umkm-npwp-registration-gap.md`, `ojol-address-normalization.md`.

This is a researcher's anatomy of a structural gap in Indonesian last-mile logistics. It is not a pitch. The thesis: Indonesia has roughly 16 to 21 million neighborhood warungs, a denser physical retail footprint than any modern-trade chain, yet almost none of them function as logistics nodes. They sell goods. They do not receive, store, or dispatch goods on behalf of a network. The gap is the absence of a systematic layer that converts a warung into a micro-fulfillment center (MFC) with inventory visibility, dispatch hooks, and trust rails. That layer does not exist as a product anyone has shipped at scale.

## The supply side: warungs are everywhere and they are not going away

A warung is a small, family-owned retail or food stall. The term covers a wide range: a front-room convenience shop, a pushcart under a tent (warung tenda), a floating boat warung, a rice-and-side-dish eatery (warung nasi), a basic-goods shop (warung sembako), a coffee stall (warung kopi), a general-goods kelontong, and the legacy communication stalls (wartel, warnet) that gave us the very wordplay. Wikipedia's Indonesian and English entries both describe the warung as "an essential part of daily life in Indonesia" and note that for most Indonesians it still means a small neighborhood convenience shop, often a front room or booth in a family home. Source: `https://id.wikipedia.org/wiki/Warung`, `https://en.wikipedia.org/wiki/Warung`.

The taxonomy of warung types is well documented by OttoPay, a payments and UMKM tooling company, in a long-form explainer. Their breakdown lists warung nasi (rice and lauk pauk, a kind of simple restaurant), warung sembako (daily necessities: cooking oil, instant noodles, rice, eggs), warung kopi (coffee and snacks), warung kelontong (broader than sembako: school supplies, household goods, snacks, cigarettes), warung internet (first established in Bogor in 1995), and warung telekomunikasi (wartel, coin-operated phone stalls from the pre-mobile era). The OttoPay piece makes one structural point worth quoting here: modern retail and pasar modern have not killed warungs. Owners adapt. "Beberapa pemilik warung membuat inovasi agar bisa mengikuti perkembangan zaman tanpa meninggalkan ciri khasnya." Source: `https://ottopay.id/blog/artikel/jenis-warung-tradisional-di-indonesia/`.

On scale, the widely cited industry figure is on the order of 16 to 21 million warungs nationwide. This number is repeated in platform investor decks, World Bank micro-retail work, and trade press, but there is no single clean public API that returns it. The closest anchored anchor is the UMKM count: KemenkopUKM and Bank Indonesia routinely cite ~64 million UMKM contributing the majority of employment and a large share of GDP. Wikipedia's Economy of Indonesia entry states micro, small, and medium enterprises "contribute around 61.7% of the economy." Source: `https://en.wikipedia.org/wiki/Economy_of_Indonesia`. The internet economy reached US$77 billion in 2022 per the same article. So the warung is the physical leaf node of a 64-million-strong informal retail tree that already accounts for the majority of economic activity. The fact that this leaf node is invisible to logistics networks is the gap.

A note on sourcing rigor: the precise 16 million warung figure could not be pinned to a single primary government API during this research pass (the BPS open API returned 403, and Google cache / World Bank blog fetches 404'd). It is therefore treated here as an industry estimate, not a verified census figure. Any deck built on top of this note should footnote it as such.

## The bottleneck: why warungs are not yet fulfillment nodes

The physical density exists. The conversion to logistics function does not. The reasons are structural, not accidental.

### Fragmented ownership and zero network effect

Each warung is an independent micro-firm. There is no shared identity, no shared inventory ledger, no shared replenishment cadence. A logistics operator who wants to use warungs as nodes must onboard and manage each one as a bespoke counterparty. Compare this to a modern-trade chain where one master agreement covers thousands of stores. The onboarding cost per node is the single largest barrier. For a network effect to emerge, the marginal cost of adding node N must fall below the marginal value, and today it does not, because every warung carries its own bank account (or none), its own trust graph, its own operating hours, and its own level of digital literacy.

### No inventory visibility

A warung knows what it has on its shelves only through memory and a paper notebook, if that. OttoPay itself sells a "Catat Transaksi Digital" and "OttoKasir" product precisely because analog bookkeeping is the default. Source: `https://ottopay.id/blog/artikel/jenis-warung-tradisional-di-indonesia/`. Without a live inventory signal, a fulfillment network cannot know whether a given warung can accept a drop, hold a SKU, or serve a pickup. The node is blind.

### Cash-first, manual operations

Most warung transactions are cash. Non-cash acceptance is improving (QRIS penetration is real and the government pushed it hard), but reconciliation, float management, and settlement at warung scale remain manual. A fulfillment layer needs programmatic settlement per node. That plumbing mostly does not exist for the long tail.

### No cold chain and limited storage

Warungs are not built to hold temperature-sensitive goods or to stage parcels. Converting one into a true MFC implies shelving, maybe a chest freezer, and a secure locker. That is capex the warung owner will not self-fund without a clear per-parcel or per-month incentive.

### Trust and geographic friction

The same address-normalization problem documented in `ojol-address-normalization.md` applies here. A warung in a Tier 2/3 city may not appear correctly on any map, so a routing engine cannot reliably send a driver to it. And the trust problem is reciprocal: a warung owner will not hold strangers' goods without assurance about theft, damage, and payment.

## Existing attempts, and why they stopped short of fulfillment

Several well-funded players touched this space. None shipped "warung as a networked fulfillment node" as a durable product. Understanding their trajectories is the core of the gap analysis.

### Mitra Bukalapak

Bukalapak built "Mitra Bukalapak," an agent network that turned warungs and small shops into service points for PPOB (phone credit, bill payment), logistics drop points, and govcr-related services. Bukalapak is publicly listed (BUKA on IDX) and reported very large agent networks in its early public filings. The model was adjacency: warungs became payment and top-up agents and parcel pickup points, not inventory-holding fulfillment nodes. Over time Bukalapak's strategy retrenched toward profitability and virtual products rather than physical fulfillment. The lesson: the agent model is viable as a financial-services attachment but does not by itself create a goods-fulfillment mesh.

### GrabKios, Kudo, and WARUNG (Yummy Corp)

Grab acquired Kudo, an Indonesian O2O agent-network startup, in 2017, and later acquired Yummy Corp (the parent of Warung Pintar) in 2021. Warung Pintar was a "smart warung" concept: a tech-enabled, branded physical stall with digital payments, inventory support, and a franchise-like operating model. It raised significant venture capital (East Ventures was an early backer) and expanded, then contracted. Multiple trade reports from 2022 to 2023 described layoffs and a strategic pivot after the Grab acquisition, with the smart-warung footprint wound down in favor of integrating capabilities into Grab's broader merchant and delivery network. The post-mortem is instructive: a vertically owned, branded, capex-heavy warung model struggled to reach unit economics, whereas using existing warungs as lightweight nodes (GrabMart, GrabExpress) proved more scalable. Source note: specific headcount and closure figures were not verifiable from primary sources in this pass; treat the pivot as reported, not audited.

### Shopee Mitra / Agen Shopee

Shopee operates "Mitra Shopee," an agent app for warungs and counter outlets covering PPOB, top-up, and logistics. Like Bukalapak Mitra, it is an adjacency play: the warung becomes a cash-in/cash-out and parcel point, not a stocked node.

### Gojek / GoFood / GoShop / GoTo

Gojek (now part of GoTo after the May 2021 Gojek-Tokopedia merger; Gojek was Indonesia's first unicorn and later decacorn, with ~170 million users across Southeast Asia per Wikipedia) runs GoFood (food delivery from warung and restaurant merchants) and GoShop/GoSend. Source: `https://en.wikipedia.org/wiki/Gojek`. Crucially, on GoFood the warung is a merchant whose goods Gojek's drivers pick up and deliver. That is the inverse of fulfillment: the warung is a source, not a node that receives and holds network inventory. GoTo's strength is the demand app and the driver fleet, not a warung-owned storage mesh.

### B2B procurement: seleraku and similar

A separate cluster of startups (seleraku being the most cited) attacked the warung supply side: digitizing the warung's restocking from distributors, giving owners a mobile app to order inventory at wholesale prices with credit. This is the "inventory in" half of the problem. It is necessary but not sufficient for fulfillment, because fulfillment also needs the "inventory out" and "hold for network" half. The procurement players rarely also run a delivery network that would use the warung as a drop node.

### What all of these share

Every attempt optimized one slice: payments (Mitra, Shopee Mitra), branded capex warungs (Warung Pintar), merchant delivery (GoFood), or procurement (seleraku). Nobody shipped the integrating layer: a system of record for warung nodes, a live inventory and capacity signal per node, a dispatch protocol that routes parcels or goods through nodes, and a trust-and-settlement rail that pays the owner per action. That integrating layer is the wedge-shaped gap.

## The technical architecture that does not exist yet

Below is a concrete design for the missing layer, written as a researcher's reference architecture rather than a product pitch. It is the kind of system a team would build to turn a warung into a node.

### Data model: the warung node

A fulfillment network needs a canonical node record. A minimal schema:

```json
{
  "warung_id": "WNG-32719",
  "owner": {
    "name": "Ibu Siti",
    "phone_wa": "62812xxxxxxx",
    "ktp_hash": "sha256:...",
    "npwp": null
  },
  "location": {
    "lat": -6.2001,
    "lon": 106.8163,
    "normalized_address": "Jl. Mawar No. 14, RT 003/RW 002, Kel. Sukamaju",
    "geohash": "qqzpv",
    "map_confidence": 0.42,
    "address_source": "owner_voice_note_transcribed"
  },
  "capabilities": {
    "holds_parcels": true,
    "cold_chain": false,
    "secure_locker": false,
    "max_parcel_dim_cm": [40, 30, 30],
    "daily_capacity_parcels": 15,
    "operating_hours": {"open": "07:00", "close": "21:00", "tz": "Asia/Jakarta"}
  },
  "inventory": {
    "tracked": false,
    "skus": [],
    "restock_days": ["mon", "thu"]
  },
  "payments": {
    "qris_enabled": true,
    "bank_account": "BCA ****1234",
    "settlement_t_plus": 1
  },
  "trust": {
    "rating": 4.8,
    "completed_holds": 312,
    "disputes": 1,
    "onboarded_at": "2026-03-12"
  }
}
```

The `map_confidence` and `address_source` fields are not decoration. They directly encode the address-normalization gap from `ojol-address-normalization.md`: in Tier 2/3 cities Google Maps coverage is roughly half, so a node's location must carry its own confidence score and provenance, and the dispatch system must degrade gracefully when confidence is low (e.g., send the driver a WhatsApp voice pin from the owner).

### Inventory and capacity sync

The node must broadcast what it can accept. A lightweight webhook or polling endpoint:

```python
# node_capacity.py - runs on a cheap Android at the warung or in the cloud
from dataclasses import dataclass, asdict
import json, time

@dataclass
class Capacity:
    warung_id: str
    free_slots: int
    cold_chain_free: int
    next_open_slot: str  # ISO timestamp
    updated_at: float

def publish_capacity(warung_id, free_slots, cold_chain_free):
    cap = Capacity(warung_id, free_slots, cold_chain_free,
                   next_open_slot="2026-07-07T14:00:00+07:00",
                   updated_at=time.time())
    # In production push to an MQTT topic or a signed REST endpoint.
    # The dispatcher subscribes and maintains a live availability index.
    return json.dumps(asdict(cap))
```

The dispatcher maintains an in-memory or Redis index keyed by geohash so that a parcel bound for a neighborhood can be matched to the nearest node with free capacity in milliseconds.

### Dispatch and routing through nodes

A naive but effective assignment is a capacitated nearest-node matching. Real systems would layer in driver routes from `ojol-logistics-inefficiency.md`, but the node-matching core is:

```python
import heapq

def assign_parcel(parcel, nodes_index, max_radius_km=1.5):
    # nodes_index: geohash bucket -> list of (warung_id, lat, lon, free_slots)
    candidates = []
    for node in nodes_index.near(parcel.lat, parcel.lon, max_radius_km):
        if node.free_slots <= 0:
            continue
        if parcel.needs_cold and not node.cold_chain:
            continue
        dist = haversine(parcel.lat, parcel.lon, node.lat, node.lon)
        heapq.heappush(candidates, (dist, node.warung_id, node))
    if not candidates:
        return None  # no node in radius, fall back to hub or direct
    dist, wid, node = heapq.heappop(candidates)
    return wid

def haversine(lat1, lon1, lat2, lon2):
    from math import radians, sin, cos, asin, sqrt
    R = 6371.0
    dlat, dlon = radians(lat2 - lat1), radians(lon2 - lon1)
    a = sin(dlat/2)**2 + cos(radians(lat1))*cos(radians(lat2))*sin(dlon/2)**2
    return 2*R*asin(sqrt(a))
```

The matching is the easy part. The hard part is the operating agreement with the owner: who is liable if a parcel is lost, how fast settlement happens (QRIS T+0 or T+1), and what the per-parcel fee is. Those are the trust rails, and they are where every prior attempt spent its political capital.

### Settlement and trust rail

Each completed hold or handoff triggers a micro-payment to the warung owner. Using QRIS with a programmable backend (see `digital-credit-scoring-umkm-qris.md` in `07-gaps-and-opportunities/opportunities/` for the QRIS context), the flow is:

```python
# On successful parcel pickup by end customer at warung node:
def settle_node_fee(warung_id, parcel_id, fee_idr=1500):
    # Call PJP (payment gateway / QRIS acquirer) payout API.
    # In practice this is a batch disbursement to the warung's account,
    # not per-parcel real-time, to keep interchange costs sane.
    batch.add(Disbursement(warung_id, fee_idr, ref=parcel_id))
    ledger.record(warung_id, "node_fee", fee_idr, parcel_id)
```

The fee math matters. If a network pays IDR 1,000 to 1,500 per parcel held and a warung can hold 15 parcels a day, that is IDR 15,000 to 22,500 of incremental daily income, roughly IDR 450,000 to 675,000 a month, before any restocking or PPOB commission. That is material to a warung whose net margin may be a few tens of thousands of rupiah a day. The incentive is real; the operational reliability is the blocker.

### Cold chain feasibility

Most warungs lack refrigeration. For grocery or pharmacy fulfillment, a chest freezer or insulated box at the node is required. The capex (a small chest freezer runs roughly IDR 1 to 2 million) is only justified if parcel or grocery volume is predictable. A phased approach: start with non-cold parcels (the bulk of e-commerce returns, COD, and Click-and-Collect), prove volume, then subsidize cold-capable nodes in dense areas. This sequencing is exactly what Warung Pintar skipped by going capex-heavy from day one.

## Unit economics sketch

The numbers below are a researcher's sketch, not a validated model. They illustrate why the gap is wedge-shaped.

Inputs:
- Warung node capex to enable: IDR 0 (parcels, no cold) to IDR 2,000,000 (cold).
- Incremental owner income per parcel held: IDR 1,000 to 1,500.
- Parcels per node per day at steady state: 5 to 15.
- Network saves on last-mile: a driver dropping 10 parcels at one node instead of 10 homes cuts roughly 40 to 60 percent of last-mile distance in dense areas.

Outputs (mid-case, 10 parcels/day, IDR 1,200 fee):
- Owner incremental income: IDR 12,000/day = IDR 360,000/month.
- Network cost per parcel to node: IDR 1,200 fee + driver drop cost (amortized, low because bundled).
- Network saving vs door-to-door: the bundled drop avoids 9 separate residential stops.

The wedge: the owner gets meaningful incremental income, the network cuts last-mile cost, and the end customer gets a walkable pickup point. The reason it has not happened at scale is not economics, it is the integration cost (onboarding, inventory signal, trust, settlement) that no one has productized as a shared layer.

## Integration with the rest of the vault

This bottleneck is not isolated. It plugs into three sibling analyses.

One, `ojol-logistics-inefficiency.md` documents why door-to-door last-mile is structurally broken outside Java's major metros: failed deliveries, address gaps, and driver unprofitability. Warung nodes are the proposed fix on the demand side, a walkable, always-open anchor that absorbs the "last 200 meters." Two, `ojol-address-normalization.md` provides the location primitives (geohash, confidence, voice-pin) that a node record needs. Three, `umkm-npwp-registration-gap.md` explains why many warung owners lack NPWP, which blocks formal bank accounts and clean settlement; a node-enabling layer must offer a lightweight onboarding that works around the NPWP gap or helps close it. The QRIS-enabled settlement described here is the practical workaround because QRIS onboarding has a lower identity bar than a corporate bank account.

## Open data and API gaps

There is no public registry of warungs. BPS publishes UMKM statistics at aggregate level but not a geocoded warung directory. The modern-trade and F&B chains have store locators; the informal warung network does not, because it is millions of unregistered micro-firms. This is itself a gap: a "warung graph" (nodes, capabilities, hours, capacity) does not exist as open or commercial data. Whoever builds the node-enabling layer simultaneously builds the only real-time warung graph in the country. That data asset may be more valuable than the fulfillment margins.

The BPS open API (`api.bps.go.id`) returned 403 to unauthenticated requests during this research, so aggregate UMKM figures could not be pulled programmatically here. The 64 million UMKM figure is cited from secondary encyclopedic sources and KemenkopUKM's widely reported statements. Source: `https://en.wikipedia.org/wiki/Economy_of_Indonesia`.

## Risks and failure modes

The Warung Pintar / Yummy Corp story is the cautionary tale. A vertically integrated, branded, capex-heavy smart-warung model carries real estate, staffing, and inventory risk per location. When capital tightened, the fixed-cost base became unsustainable and the footprint was wound down after acquisition. The durable pattern is the opposite: asset-light, use existing warungs, pay per action, layer capabilities incrementally. The risk in the asset-light model is quality control. A warung that loses a parcel or closes early breaks the promise to the end customer. Mitigations are operational, not technical: rating systems, deposit or insurance pools, and dense enough node coverage that a single failure is absorbed by neighbors.

Another risk is platform dependency. Warung owners already fear being locked into a single super-app. A node layer that is single-platform (say, only usable by Grab) repeats the "digitalisasi paksa platform" pain documented in `03-id-business-trends/demand-mining/umkm-digitalisasi-paksa-platform-ekosistem.md`. An open or multi-tenant node standard would reduce that risk and is itself a gap.

## What a minimal viable version looks like

A first version does not need cold chain, does not need full inventory, and does not need a branded stall. It needs four things: a node record with a confidence-scored location, a capacity signal (free slots), a dispatch match, and a per-action settlement. Start with Click-and-Collect and COD parcels for one e-commerce or logistics partner in one city. Prove that a warung can reliably hold N parcels a day and that customers will walk to it. Then expand SKUs (grocery top-up, pharmacy) and capabilities (cold). The sequencing respects the unit economics and avoids the Warung Pintar trap.

Concretely, the MVP's daily loop is:

```text
Morning: warung owner opens app, sets "I can hold 10 parcels today."
Network: dispatcher indexes node with 10 free slots.
Day: parcels bound for the neighborhood are routed to the node.
Driver: drops bundled parcel batch, scans each, owner confirms receipt.
Customer: gets WhatsApp "your parcel is at Warung Ibu Siti, open till 21:00."
Evening: customer picks up, owner scans handover, settlement batched to owner.
```

The whole loop is buildable on off-the-shelf parts: a mobile app or WhatsApp bot for the owner, a Redis-backed capacity index for the dispatcher, an existing QRIS acquirer for settlement, and the geohash primitives from the address-normalization work. The missing piece is the product that wires them together and the operational playbook that keeps node quality high. That product does not exist today, which is the gap.

## Adjacent and confirming signals

The persistence of warungs against modern retail, documented by OttoPay, is the demand-side insurance for this thesis: warungs are not a dying format that needs saving, they are a stable, adapting institution. Source: `https://ottopay.id/blog/artikel/jenis-warung-tradisional-di-indonesia/`. The Gojek/GoTo scale (170 million users, decacorn) shows the demand app and driver fleet already exist; what is missing is the neighborhood node that those drivers drop into. Source: `https://en.wikipedia.org/wiki/Gojek`. The 61.7 percent of the economy from MSMEs shows the prize is large. Source: `https://en.wikipedia.org/wiki/Economy_of_Indonesia`.

## Prior-attempt comparison, in one table

The fragmentation of prior attempts is easier to see side by side. None combined node record, capacity signal, dispatch, and settlement into one shared layer.

| Player | Model | Warung role | Held inventory? | Network effect | Outcome |
|--------|-------|-------------|----------------|----------------|---------|
| Mitra Bukalapak | Agent network, PPOB + parcel point | Service/pickup point | No | Per-agent onboarding, no mesh | Retrenched to virtual products |
| GrabKios / Kudo | O2O agent top-up | Top-up + paypoint | No | Agent list, not fulfillment | Folded into Grab ecosystem |
| Warung Pintar (Yummy/Grab) | Branded capex smart stall | Owned node | Partial (retail stock) | Vertically owned, not open | Wound down post-2021 acquisition |
| Shopee Mitra | Agent app, PPOB | Cash-in/out + parcel | No | Per-agent, no mesh | Adjacency to e-commerce |
| GoFood / GoShop | Merchant delivery | Source of goods | N/A (sells own) | Strong demand app | Warung is pickup origin, not node |
| seleraku (B2B) | Procurement digitization | Buyer of restock | "In" only | Supplier side | No delivery network use |

The empty cells in the "Held inventory?" and "Network effect" columns are the gap. Every player solved a slice and stopped. The integrating layer sits in the intersection and has no occupant.

## A fuller dispatcher implementation

The matching sketch above is toy-grade. A production dispatcher is a small service that maintains a live capacity index, accepts parcel assignments, and emits driver routes. Below is a reference implementation in Python using Redis for the live index and a simple HTTP surface. It is illustrative, not production-hardened.

```python
# dispatcher.py - reference architecture for warung-node parcel routing
import json, math, time, redis, geojson
from flask import Flask, request, jsonify

app = Flask(__name__)
r = redis.Redis(host="redis", port=6379, db=0)

CAP_KEY = "warung:cap:{warung_id}"          # hash: free_slots, cold, lat, lon, owner_wa
IDX_KEY = "warung:geo"                       # geohash bucket -> set of warung_ids

def haversine(lat1, lon1, lat2, lon2):
    R = 6371.0
    dlat, dlon = math.radians(lat2-lat1), math.radians(lon2-lon1)
    a = (math.sin(dlat/2)**2 +
         math.cos(math.radians(lat1))*math.cos(math.radians(lat2))*math.sin(dlon/2)**2)
    return 2*R*math.asin(math.sqrt(a))

def geohash_bucket(lat, lon, precision=6):
    # 6-char geohash ~ 1.2km x 0.6km, good for neighborhood matching
    import geohash2
    return geohash2.encode(lat, lon, precision)

@app.route("/node/heartbeat", methods=["POST"])
def node_heartbeat():
    # Called by the warung app when it opens, sets capacity, refreshes TTL
    d = request.json
    wid = d["warung_id"]
    pipe = r.pipeline()
    pipe.hset(CAP_KEY.format(warung_id=wid), mapping={
        "free_slots": d["free_slots"],
        "cold": int(d.get("cold", False)),
        "lat": d["lat"], "lon": d["lon"],
        "owner_wa": d["owner_wa"],
        "ts": int(time.time()),
    })
    pipe.expire(CAP_KEY.format(warung_id=wid), 86400)  # stale if no heartbeat 24h
    bucket = geohash_bucket(d["lat"], d["lon"])
    pipe.sadd(IDX_KEY, wid)
    pipe.sadd(f"warung:bucket:{bucket}", wid)
    pipe.execute()
    return jsonify({"ok": True})

@app.route("/assign", methods=["POST"])
def assign():
    d = request.json
    plat, plon = d["lat"], d["lon"]
    need_cold = d.get("need_cold", False)
    radius = d.get("radius_km", 1.5)
    # Expand bucket search outward until candidates or max radius
    candidates = []
    checked = set()
    for bucket in expanding_buckets(geohash_bucket(plat, plon), max_steps=3):
        for wid in r.smembers(f"warung:bucket:{bucket}"):
            if wid in checked:
                continue
            checked.add(wid)
            cap = r.hgetall(CAP_KEY.format(warung_id=wid))
            if not cap or int(cap.get(b"free_slots", 0)) <= 0:
                continue
            if need_cold and not int(cap.get(b"cold", 0)):
                continue
            wlat, wlon = float(cap[b"lat"]), float(cap[b"lon"])
            dist = haversine(plat, plon, wlat, wlon)
            if dist <= radius:
                candidates.append((dist, wid, cap))
    if not candidates:
        return jsonify({"assigned": False, "reason": "no_node_in_radius"})
    candidates.sort(key=lambda x: x[0])
    dist, wid, cap = candidates[0]
    r.hincrby(CAP_KEY.format(warung_id=wid), "free_slots", -1)
    # Notify owner via WhatsApp (see owner bot section)
    notify_owner(cap[b"owner_wa"], f"Parcel inbound, {dist:.2f}km away")
    return jsonify({"assigned": True, "warung_id": wid, "dist_km": round(dist, 3)})

def expanding_buckets(gh, max_steps=3):
    # yield neighbor buckets at increasing precision steps
    yield gh
    import geohash2
    for step in range(1, max_steps+1):
        for nb in geohash2.neighbors(gh[:max(1, len(gh)-step)]):
            yield nb

def notify_owner(wa, msg):
    # In production call an official WA Business API provider (WATI, 360dialog)
    # or a self-hosted baileys client. Pseudocode:
    # whatsapp_client.send(to=wa, text=msg)
    pass

if __name__ == "__main__":
    app.run(port=5000)
```

The design choices worth noting: capacity is a decrementing counter with a daily TTL so a warung that goes silent cannot hold phantom capacity forever. Bucketing by geohash avoids scanning all 16 million nodes for every parcel. The assignment is greedy nearest with capacity, which is fine because the hard routing (driver multi-stop tours) happens after node assignment, in the layer described in `ojol-logistics-inefficiency.md`.

## Owner-side interaction: the WhatsApp-first bot

Warung owners are not going to install and learn a complex app. The onboarding and daily loop should run on WhatsApp, which they already use. A minimal bot flow:

```text
Owner: (types) "BUKA 10"
Bot:    "Terima kasih Ibu Siti. Warung WNG-32719 buka hari ini, kuota 10 paket.
         Saya kabari kalau ada paket masuk. Jam tutup pukul 21:00 ya."

[later, driver drops batch]

Bot:    "Ada 3 paket masuk dari kurir. Scan barcode masing-masing ya.
         Paket A: AMAN, Paket B: AMAN, Paket C: AMAN."
Owner:  (scans) "A B C"
Bot:    "Terkonfirmasi 3 paket tersimpan. Estimasi pendapatan +Rp4.500."

[customer arrives]

Bot:    "Paket A diambil oleh pembeli. +Rp1.500 lunas ke rekening besok pagi."
```

The bot is the trust surface. Every state transition is confirmed by the owner so there is no ambiguity about custody. The message templates above are the contract. Underneath, each confirmation writes a ledger entry and a custody event. The bot can be built on the official WhatsApp Business API or a self-hosted client; for cost at warung scale, a shared multi-tenant client per region is the realistic pattern.

## Settlement and the dispute/insurance pool

Per-action settlement needs a backstop for loss or damage. A simple pooled model:

```python
# ledger.py - node fee ledger + insurance pool
from dataclasses import dataclass
from enum import Enum

class CustodyEvent(Enum):
    DROPPED = "dropped"          # driver -> node
    CONFIRMED = "confirmed"      # node acknowledged
    PICKED_UP = "picked_up"      # customer -> left node
    LOST = "lost"                # dispute opened

@dataclass
class LedgerEntry:
    warung_id: str
    parcel_id: str
    event: CustodyEvent
    fee_idr: int
    ts: float

INSURANCE_RATE = 0.02  # 2% of node fee goes to a shared loss pool

def on_confirmed(warung_id, parcel_id, base_fee=1500):
    fee = base_fee
    pool_contrib = int(fee * INSURANCE_RATE)
    # At batch settlement: pay (fee - pool_contrib) to owner, add pool_contrib to pool
    return LedgerEntry(warung_id, parcel_id, CustodyEvent.CONFIRMED, fee, time.time())

def resolve_dispute(parcel_id, at_fault: str):
    # at_fault in {"node", "driver", "customer", "force_majeure"}
    if at_fault == "node":
        # owner liable up to pool coverage; deduct from future payouts
        compensate_customer_from_pool(parcel_id)
    elif at_fault == "driver":
        charge_courier_partner(parcel_id)
    # force_majeure: split between pool and customer, per T&C
```

The 2 percent insurance skim is the cost of trust at scale. Without it, a single lost-parcel dispute can poison the relationship between owner and network. With it, the pool absorbs shocks and the owner's payout is predictable. This is the kind of operational detail that the branded-capex players under-built.

## Regional variation: one model does not fit all 17,000 islands

The warung node thesis behaves very differently by region, and the address-normalization gap compounds it.

Java and Bali: dense, high e-commerce volume, decent maps. Warung nodes here are the easiest win. A kelurahan with 30 warungs and 2,000 parcels a month can absorb Click-and-Collect immediately. The constraint is operational quality, not geography.

Sumatra, Sulawesi, Kalimantan: medium density, weaker maps, longer driver distances. Nodes here save more per parcel because the last mile is longer, so the economic wedge is actually larger. But map confidence is lower, so the geohash-plus-voice-pin pattern from `ojol-address-normalization.md` is mandatory, not optional.

Eastern Indonesia (Maluku, Papua, NTT): sparse, expensive logistics, few modern retail competitors. A warung node here can double as the only reliable parcel access point for a village. The social value is highest and the commercial margin thinnest, which points to a subsidy or CSR/public-private model rather than pure commercial rollout.

The rollout order is therefore not "biggest city first" by vanity, but "densest parcel-to-warung ratio first," which is Java and Bali, then the long-last-mile secondary cities where the savings per parcel are largest.

## The warung graph as the real asset

Whoever runs the node layer accumulates, as a side effect, a live graph of every participating warung: location (with confidence), capabilities, hours, capacity utilization, and throughput. No such dataset exists today. BPS can tell you there are tens of millions of UMKM; it cannot tell you which warung on Jl. Mawar is open at 8pm and can hold a frozen parcel. That gap in the public data is itself a moat.

The graph has uses beyond fulfillment:
- Micro-targeted procurement: a B2B supplier can see real demand density per kelurahan.
- Credit scoring: node throughput is a cash-flow signal usable by the QRIS credit-scoring model in `07-gaps-and-opportunities/opportunities/digital-credit-scoring-umkm-qris.md`.
- Disaster logistics: in a flood or eruption, the warung graph is a ready distribution mesh.
- Public policy: governments trying to reach warungs with subsidies (like the rice or cooking-oil programs) currently have no addressable list.

The governance question (new gap, recorded below) is whether this graph should be open, platform-locked, or regulated as a public utility. The pattern from `umkm-digitalisasi-paksa-platform-ekosistem.md` warns that platform lock-in is the likely default unless an open standard is deliberately built.

## Worked example: one kelurahan, 20 warungs, 200 parcels a day

Assume a kelurahan with 20 warungs onboarded, each holding up to 10 parcels/day, and 200 parcels/day destined for the area.

- Without nodes: 200 residential drops, average 1.2km between stops in dense lanes, driver does ~25 stops/hour effective (parking, walk-up). Needs ~8 driver-hours.
- With nodes: parcels routed to the 20 warungs by nearest-capacity. A driver drops batches of ~10 at each of 20 nodes = 20 stops instead of 200. At 20 stops/hour, ~1 driver-hour for the drop phase, plus customers self-collect on foot (zero driver cost).
- Saving: ~7 driver-hours/day for this one kelurahan, roughly an 85 percent reduction in last-mile driver time for the parcels routed through nodes.
- Owner income: 200 parcels x IDR 1,200 = IDR 240,000/day split across 20 owners = IDR 12,000/owner/day, IDR 360,000/month.

The example is deliberately conservative (only 10 parcels/node, IDR 1,200 fee). At 15 parcels and IDR 1,500 the owner income reaches the IDR 675,000/month figure from the unit-economics sketch. The driver-time saving is the network's reason to pay; the owner income is the owner's reason to participate. Both are positive simultaneously, which is why the gap is wedge-shaped rather than a subsidy sink.

## Phased rollout and the KPIs that prove it works

Phase 0, single city, Click-and-Collect only, no cold: prove that owners reliably hold parcels and customers walk to them. KPI: hold accuracy > 99 percent, pickup rate > 90 percent within 24h, owner churn < 10 percent/month.

Phase 1, add COD and returns: warungs become cash-handling and return nodes. KPI: cash reconciliation error < 0.5 percent, return processing time < 10 min.

Phase 2, multi-tenant: the same node serves more than one logistics or e-commerce partner, proving the open-standard thesis and reducing platform-lock risk. KPI: node revenue per day rises with each added partner.

Phase 3, cold-capable nodes in dense areas: grocery and pharmacy fulfillment. KPI: cold-chain incident rate < 1 percent, cold-node utilization > 50 percent.

Each phase has a kill criterion. If Phase 0 hold accuracy or pickup rate misses, the model is broken at the foundation and no amount of later features fixes it. The Warung Pintar failure was effectively skipping Phase 0 economics by going capex-heavy; this sequencing is the explicit correction.

## Why the super-apps have not just done this

A fair objection: GoTo and Grab already have drivers, customers, and merchant relationships. Why have they not turned warungs into nodes? Three reasons. One, their incentive is to keep volume inside their own app and driver fleet, not to create a shared neutral layer that competitors could also use. Two, node quality control is operational pain they have historically pushed onto merchants (GoFood ratings) rather than solved as infrastructure. Three, the marg-incremental per-parcel node fee is small relative to their core take rates, so it ranks low against other roadmap bets. That is exactly the opening: a neutral, multi-tenant node layer is something the super-apps are structurally unlikely to build because it commoditizes their last-mile advantage.

## The Warung Pintar post-mortem, in detail

Warung Pintar (under Yummy Group / Yummy Corp) is the closest historical precedent to a capex warung node, and its trajectory is the single most important cautionary data point for this thesis. Understanding precisely what broke matters more than the headline "it shut down."

What Warung Pintar got right: it recognized that warungs are the densest retail footprint in the country and that digitizing them creates leverage. It built a branded, tech-enabled stall with a point-of-sale, digital payments, inventory suggestion, and a franchise operating model. It attracted real capital and credible backers and expanded across Jabodetek and other cities.

What broke: the unit economics of an owned-and-operated physical retail node are brutal. Each location carried rent or build cost, staffing, inventory, and technology. To make a single node profitable you need either high throughput (many transactions) or high margin (value-added services), and a newly built smart warung in a random corner does not start with either. The model also competed with the very warungs it could have partnered with, doubling its own capex instead of leveraging existing infrastructure. When macro capital tightened in 2022 to 2023 and Grab (which acquired Yummy Corp in 2021) prioritized profitability over footprint, the smart-warung network was a natural place to cut. Multiple trade reports described layoffs and a strategic wind-down, with capabilities folded into Grab's broader merchant and delivery ecosystem rather than maintained as standalone branded stalls.

The lesson for the node-layer thesis is precise and counterintuitive: do not own the warung, use it. Asset-light, pay-per-action, incremental-capability is the only version with a shot at the 16 million scale. The node layer should be software and operations on top of existing warungs, not real estate. This is the central design constraint that separates a viable wedge from a closed experiment.

## Regulatory and compliance surface

Turning a warung into a node is not purely a software problem. It creates a compliance surface that nobody has mapped cleanly.

Storage and logistics liability. A warung holding a third party's parcel is, functionally, a temporary warehouse. Indonesian logistics and consumer-protection rules around lost, damaged, or late goods may attach. The node operator needs a standard custody agreement with each owner and a clear allocation of fault (node, driver, customer, force majeure), which is exactly what the insurance-pool code above models.

Personal data. When a customer's parcel is routed to "Warung Ibu Siti," the customer's name, address fragment, and phone may transit through the node owner's phone or app. That is personal data under the PDP Law (Undang-Undang Pelindungan Data Pribadi, effective 2022, with implementing regulations rolling out through 2024 to 2026). The node layer must minimize what the owner sees (e.g., a pickup code, not a full address) and document a lawful basis for any personal data the owner handles. This is a regtech gap in its own right, captured in the new gaps below.

Tax and formalization. As noted in `umkm-npwp-registration-gap.md`, many warung owners lack NPWP. Node income paid to them needs a reporting path. QRIS-based settlement lowers the identity bar and creates a clean transaction trail, which paradoxically helps formalization, but the operator still needs to handle 23 percent final-income-tax withholding (PPh 23) mechanics for non-NPWP vs NPWP owners or route through a PJP that handles it. The compliance plumbing is non-trivial at 16 million nodes.

Local trading and zoning. Some kelurahans restrict non-residential activity in residential zones. A warung is already a business, but a high-traffic parcel hub may draw complaints. Early engagement with local government (kelurahan, camat) is part of the rollout, not an afterthought.

## Cold chain and IoT: extending the node schema

For grocery and pharmacy fulfillment, the node needs to prove temperature integrity. The node schema from the architecture section extends with an IoT device record:

```json
{
  "cold_unit": {
    "present": true,
    "type": "chest_freezer_100L",
    "iot_sensor": "ESP32-Therm-0001",
    "temp_c_current": -4.2,
    "temp_c_min_24h": -1.0,
    "temp_c_max_24h": 6.5,
    "last_telemetry_ts": "2026-07-07T13:55:00+07:00",
    "breach_count_30d": 0
  }
}
```

The telemetry is the trust signal for cold SKUs. A pharmacy or grocery partner will only route temperature-sensitive goods to a node whose `breach_count_30d` stays near zero. The sensor can be a sub-IDR 200,000 ESP32 with a DS18B20 probe reporting over the owner's phone hotspot or a cheap SIM. The capex is small; the financing of it is the separate gap recorded below (warung-cold-chain-capex).

## Inventory sync protocol (the "inventory out" half)

Procurement players (seleraku and peers) solve "inventory in" (restocking the warung). Fulfillment needs "inventory out" and "hold for network." A minimal sync protocol, polled or pushed, looks like:

```json
{
  "warung_id": "WNG-32719",
  "ts": "2026-07-07T14:00:00+07:00",
  "network_stock": [
    {"sku": "PARCEL-AX12", "state": "held", "since": "2026-07-07T13:10:00+07:00"},
    {"sku": "PARCEL-BZ09", "state": "held", "since": "2026-07-07T13:12:00+07:00"}
  ],
  "network_capacity": {"free_slots": 8, "cold_free": 2},
  "own_stock_flag": false
}
```

The `own_stock_flag` is important: the node layer should not, in Phase 0, try to manage the warung's own retail inventory. That is the procurement players' domain and a much harder problem (per-SKU, per-expiry, per-supplier). The node layer only tracks network-owned items (parcels, held goods) and capacity. Keeping the scope narrow is what makes Phase 0 achievable. Later phases can optionally ingest the owner's own stock for grocery top-up fulfillment, but that is an explicit later bet, not the foundation.

## Driver app: batch drop and route building

On the driver side, the node assignment changes the route shape from many small residential stops to few large node drops. A batch-drop route builder:

```python
# driver_route.py - build a node-batch route from assigned parcels
def build_node_drops(assignments):
    # assignments: list of (parcel_id, warung_id, lat, lon)
    from collections import defaultdict
    by_node = defaultdict(list)
    for p in assignments:
        by_node[p.warung_id].append(p)
    # Order nodes by a traveling-salesman-ish greedy over node centroids
    nodes = [(wid, sum(p.lat for p in ps)/len(ps), sum(p.lon for p in ps)/len(ps), ps)
             for wid, ps in by_node.items()]
    route = greedy_tsp(nodes)   # returns ordered list of (wid, parcels)
    return [{"warung_id": wid, "parcels": [p.parcel_id for p in ps],
             "scan_all": True} for wid, _, _, ps in route]

def greedy_tsp(nodes, start=(DRIVER_LAT, DRIVER_LON)):
    remaining = list(nodes)
    cur = start
    route = []
    while remaining:
        remaining.sort(key=lambda n: haversine(cur[0], cur[1], n[1], n[2]))
        nxt = remaining.pop(0)
        route.append(nxt)
        cur = (nxt[1], nxt[2])
    return route
```

This is the mirror image of the residential route. Instead of 200 stops, the driver does ~20 node stops and scans a batch at each. The parcel-to-customer last 200 meters is handled by the customer walking in. The driver's effective throughput jumps because parking and walk-up time per parcel collapses.

## Adoption barriers by owner persona

Not every warung owner will say yes. Segmenting the long tail by persona clarifies the go-to-market.

The "already-digital" owner (Mitra Bukalapak / Shopee Mitra agent, uses QRIS, has a smartphone): easiest. They already earn from adjacencies and understand the model. Target these first; they are reference cases.

The "cash-only" owner (no smartphone literacy beyond WhatsApp, cash-first): reachable via WhatsApp bot and a family member who helps set up. The bot must be voice-friendly and Bahasa, not app-heavy.

The "skeptic" owner (burned by a prior scheme, distrusts platforms): needs trust proof, perhaps a cooperative or local-government endorsement, and a no-capex promise. The `umkm-digitalisasi-paksa-platform-ekosistem.md` pain is concentrated here.

The "too-busy" owner (warteg, high foot traffic, no spare attention): only works if the node interaction is seconds, not minutes. Scan-and-go, no paperwork. This persona caps node throughput by attention, not space, which the capacity signal must respect (lower `daily_capacity_parcels`).

The segmentation matters because the onboarding cost per persona differs by an order of magnitude, and the rollout should sequence by lowest-friction first to build proof before chasing the hard segments.

## Instrumentation and the metrics that detect failure early

A node layer lives or dies on instrumentation. The minimum event stream:

- `node_heartbeat`: owner opens, sets capacity. Detects silent nodes (no heartbeat 24h = capacity auto-zeroed).
- `parcel_dropped`: driver scans at node. Detects drop-side failures.
- `parcel_confirmed`: owner acknowledges. Detects custody gaps.
- `parcel_picked_up`: customer collects. Detects pickup-rate decay.
- `parcel_expired`: not picked up in SLA. Detects bad node placement or poor customer comms.
- `dispute_opened` / `dispute_resolved`: trust health.

Dashboards should surface, per kelurahan: hold accuracy, 24h pickup rate, owner churn, dispute rate, and average parcels per node per day. The kill criteria from the phased-rollout section are computed from exactly these. Without this instrumentation, a node network fails silently, which is the failure mode that killed several informal logistics experiments that never published their numbers.

## OpenAPI-style node service contract

For teams building the integrating layer, a minimal service contract helps. In OpenAPI-ish form:

```yaml
openapi: 3.0.0
info:
  title: Warung Node Fulfillment API
  version: 0.1.0
paths:
  /node/heartbeat:
    post:
      summary: Owner opens node, declares capacity
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                warung_id: {type: string}
                free_slots: {type: integer}
                cold: {type: boolean}
                lat: {type: number}
                lon: {type: number}
                owner_wa: {type: string}
  /assign:
    post:
      summary: Route a parcel to nearest capable node
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                lat: {type: number}
                lon: {type: number}
                need_cold: {type: boolean}
                radius_km: {type: number}
      responses:
        '200':
          description: Assignment result
  /node/{warung_id}/parcels:
    get:
      summary: List network-held parcels at a node
```

This contract is intentionally small. The temptation in any platform play is to over-specify. The node layer should expose just enough for a dispatcher and a driver app to function, and resist feature creep until Phase 0 proves out.

## Comparison to models outside Indonesia

The warung-node idea is not unique to Indonesia, which is reassuring. Convenience-store networks as parcel points (7-Eleven, FamilyMart in Japan, Thailand, and the Philippines) and "click and collect" at neighborhood shops (InPost lockers in Europe, Amazon Hub in the US) prove the pattern works where density and trust exist. The Indonesian twist is that the node is an informal micro-merchant, not a corporate chain, so the trust and settlement rails must be rebuilt for a low-formalization counterparty. That rebuild is the actual innovation, and it is where the prior Indonesian attempts under-invested. The global precedent de-risks the consumer behavior (people will walk to a shop to collect a parcel); the local work is the counterparty formalization.

## Financing the node enablement: who pays for the enablement capex

Even the asset-light model has capex somewhere: a smartphone mount or second phone, a parcel locker or shelf, maybe a chest freezer for cold. The question of who funds it is a distinct bottleneck.

Self-funded by owner. Works only for the "already-digital" persona with spare cash. Excludes the long tail.

Revenue-share lease. The operator provides the locker/freezer and recovers cost from node fees over N months. Aligns incentives (operator only earns if node earns) but ties up operator capital at 16 million scale, which is why it must be phased (cold only after non-cold proves volume).

Cooperative pool. A warung koperasi (relevant given the koperasi gaps in `03-id-business-trends/bottlenecks/koperasi-simpan-pinjam-ojol.md`) fronts the capex and owns the asset, renting it to members. This is culturally familiar in Indonesia and de-risks the owner, but needs a functioning cooperative, which is itself a gap in many areas.

Vendor financing from a B2B supplier. The seleraku-style procurement player already wants the warung stocked; it can bundle node enablement as a loyalty investment. This is the most natural fit because the supplier already has the relationship and the restock cadence to amortize the capex against procurement volume.

The financing mechanism is recorded as a separate gap (warung-cold-chain-capex) because it is the gating constraint for Phase 3 cold nodes, and none of the prior players solved it cleanly (Warung Pintar tried to own it and it became a cost center).

## Mock operating dashboard: what healthy looks like

A kelurahan operations view, mid-rollout, might read:

```
Kelurahan Sukamaju - Node Network (2026-Q3)
-------------------------------------------
Warungs onboarded:        34 / ~210 estimated
Active today (heartbeat): 31 (91%)
Avg parcels/node/day:     9.4
Hold accuracy (30d):      99.3%
24h pickup rate:          94.1%
Owner churn (30d):        4.2%
Dispute rate:             0.3%
Cold nodes:               3 (pilot)
Parcel driver-hours saved/day: ~11 (vs door-to-door)
Est. owner incremental income/mo: IDR 338,000 avg
```

The dashboard is the early-warning system. If "Active today" drops below 85 percent, onboarding or app friction is the problem. If "24h pickup rate" falls below 90 percent, node placement or customer communication is wrong. If "dispute rate" rises above 1 percent, the insurance pool is under-funded or custody UX is broken. These thresholds are the kill/continue criteria made operational.

## Deep failure-mode analysis

Beyond the Warung Pintar capex trap, several failure modes deserve explicit callouts because they are silent.

The "ghost node" failure. A warung signs up, gets the onboarding incentive, then goes silent. Without the 24h heartbeat TTL auto-zeroing capacity (as coded), the network keeps routing parcels to a dead node and customers never get them. The TTL and active-rate metric are the specific defense.

The "over-subscribed node" failure. A popular corner warung gets assigned 40 parcels when its declared capacity was 10. The owner cannot physically hold them, parcels pile up, pickup rate collapses. The decrementing counter and a hard reject when `free_slots <= 0` prevent this; the dispatcher must never over-assign.

The "last-200-meters-unwalked" failure. Customers used to doorstep delivery will not walk to a warung unless the incentive (faster, cheaper, or COD convenience) is clear. This is a communications problem, solved by a crisp WhatsApp notification with the warung name, a landmark, and a pickup code. Underestimating customer behavior change is how many Click-and-Collect experiments died in Western markets too.

The "platform-lock revenge" failure. If the node layer becomes extractive (low fees, punitive penalties, exclusive clauses), owners churn to a competitor or revert to pure cash. The `umkm-digitalisasi-paksa-platform-ekosistem.md` pain is the warning. A neutral, multi-tenant standard is the structural antidote.

The "data-honeypot" failure. The warung graph becomes so valuable that the operator monetizes it against the owners (selling location and throughput to their suppliers at the owners' expense). This is the governance gap. An open or cooperative-held graph prevents it.

## Why this is a bottleneck and not just an opportunity

The vault separates "bottlenecks" (structural frictions) from "opportunities" (one-pagers for ventures). This note belongs in bottlenecks because the core finding is a missing layer, a friction, not a company. The friction is: a 16-million-node physical network that is invisible and unusable to logistics because no one has built the record-plus-signal-plus-dispatch-plus-settlement integration. That is a classic infrastructure bottleneck. It may spawn opportunities (a node-layer startup, an open warung graph, a compliance SaaS), and those would be logged in `07-gaps-and-opportunities/` once the bottleneck is understood. The bottleneck analysis comes first because it explains why the opportunity, if attempted, fails at the integration step rather than the idea step.

## Synthesis: the node layer as connective tissue for the vault

Read across the vault, the warung-node idea is the connective tissue between several threads. It is the demand-side fix for `ojol-logistics-inefficiency.md` (the walkable anchor that absorbs the last 200 meters). It consumes the location primitives from `ojol-address-normalization.md`. It routes around the formalization cliff in `umkm-npwp-registration-gap.md` via QRIS settlement. It reuses the QRIS credit signal from `digital-credit-scoring-umkm-qris.md`. It is threatened by the platform-lock pattern in `umkm-digitalisasi-paksa-platform-ekosistem.md`. And it could be financed by the cooperative model in `koperasi-simpan-pinjam-ojol.md`. No single opportunity file captures this web; the bottleneck note is where the threads meet, which is why it earns its place in `03-id-business-trends/bottlenecks/`.

## Node onboarding runbook (operational, not theoretical)

The integration cost lives mostly in onboarding. A concrete runbook for bringing one warung online, low-friction:

1. Discovery. Walk or ride the kelurahan, photograph each warung, note operating hours from the physical sign. This bootstraps the warung graph where maps are weak, directly addressing `ojol-address-normalization.md`.
2. First contact. Explain in Bahasa, with a neighbor as translator if needed: "Terima kasih, Bu. Kami bantu warung dapat penghasilan tambahan dari menerima paket tetangga. Tidak keluar modal." The no-capex promise is the hook.
3. Identity. Capture owner name, WhatsApp number, and a photo of KTP (hashed, not stored in clear). NPWP if present; if absent, note it and route settlement via QRIS to avoid the formalization cliff.
4. Location. Owner sends a WhatsApp live location pin, plus a voice note describing the landmark ("sebelah musholla, pojok jalan"). Transcribe to `normalized_address` with a `map_confidence` score. Low confidence triggers the voice-pin fallback at dispatch time.
5. Capacity. Owner declares `daily_capacity_parcels` (start conservative, e.g., 5). This is tuned up as throughput proves out.
6. Payments. Link a QRIS string or bank account. For unbanked owners, a nearby BPR or e-wallet agent cash-out is arranged.
7. Go live. Owner texts "BUKA N" daily; the heartbeat sets capacity. First parcels routed next day.
8. First-week handholding. A human checks in twice the first week to fix UX frictions before they cause churn.

The runbook is deliberately human-heavy at the start and automates only after the pattern is proven. Over-automating onboarding is how platforms scale churn instead of nodes.

## Data model for the warung graph (the asset, formalized)

If the node layer is the product, the warung graph is the moat. A normalized schema for the graph:

```json
{
  "graph_meta": {"version": "0.1", "generated": "2026-07-07", "coverage_kelurahan": "Sukamaju"},
  "nodes": [
    {
      "warung_id": "WNG-32719",
      "type": "warung_sembako",
      "centroid": {"lat": -6.2001, "lon": 106.8163, "geohash": "qqzpv", "confidence": 0.42},
      "footprint_m2": 12,
      "operating_hours": {"open": "07:00", "close": "21:00"},
      "capabilities": {"parcel_hold": true, "cold": false, "ppob": true, "qris": true},
      "throughput_30d": {"parcels_held": 280, "parcels_picked_24h_pct": 94.1},
      "owner": {"digital_tier": "already_digital", "npwp": false}
    }
  ]
}
```

This graph lets a B2B supplier see real demand density, a credit model see cash flow (feeding `digital-credit-scoring-umkm-qris.md`), and a disaster agency see distribution nodes. No equivalent open dataset exists. The governance decision (open vs locked) is the recorded gap; the technical ability to build it is the moat.

## Moat timing: why now and not five years ago

Three shifts make the node layer viable now where it was not before. QRIS reached near-ubiquitous acceptance, so settlement to an informal merchant is finally clean. Smartphone penetration among warung owners is high enough that a WhatsApp bot is a real interface, not a dream. And e-commerce parcel volume in Indonesia crossed the threshold where door-to-door last-mile is genuinely unprofitable in dense areas, creating pull from logistics players rather than requiring the node layer to manufacture demand. The Warung Pintar era (2017 to 2021) had none of these tailwinds fully in place; it was early. The 2026 window is materially different, which is why the bottleneck is ripe to be solved now rather than re-attempted and abandoned.

## Tier-by-tier numerical comparison

The savings from node routing scale with last-mile difficulty. A rough model across tiers, holding parcel volume constant at 1,000 parcels/day for a delivery zone:

| Tier | Avg stop spacing | Effective stops/hr (door) | Driver-hrs door-to-door | Nodes used | Node stops | Driver-hrs via nodes | Saved hrs | Saved % |
|------|-----------------|---------------------------|-------------------------|------------|-----------|----------------------|-----------|---------|
| Java dense (Jakarta/Bandung) | 0.4 km | 28 | 35.7 | 40 | 40 | 1.4 | 34.3 | 96% |
| Java secondary (Cirebon) | 0.7 km | 22 | 45.5 | 30 | 30 | 1.1 | 44.4 | 98% |
| Sumatra medium (Palembang) | 1.1 km | 16 | 62.5 | 22 | 22 | 0.8 | 61.7 | 99% |
| Eastern sparse (Kupang) | 2.0 km | 9 | 111.1 | 12 | 12 | 0.4 | 110.7 | 99.6% |

Two things jump out. One, door-to-door driver-hours explode as spacing widens, which is exactly the geography of outside-Java Indonesia, so the node wedge is largest precisely where logistics is worst. Two, the node model's driver-hours are nearly flat across tiers because they depend on node count, not parcel geography. This is why a neutral node layer is strategically most valuable in the regions super-apps serve worst, and why those same super-apps are unlikely to build it (low absolute volume, high complexity). The table is a researcher's estimate using assumed stop rates; the directional conclusion (savings rise with last-mile difficulty) is robust even if the absolute numbers shift.

## Gaps this research opens (recap)

This note discovered three new gaps, recorded as inbox/bottleneck items in the CHANGELOG and intended for the auditor gap list:

1. `07-gaps-and-opportunities/inbox/2026-07-07-warung-graph-open-data.md` - There is no geocoded, capability-tagged warung registry (public or commercial). The node-layer builder becomes the owner of the country's only real-time warung graph; the open-vs-locked governance question is itself a gap.
2. `03-id-business-trends/bottlenecks/warung-cold-chain-capex.md` - Cold-capable nodes need capex (chest freezer, insulated box) justified only by predictable grocery/pharmacy volume. The financing mechanism (vendor financing, revenue-share lease, cooperative pool) is undefined and is a distinct bottleneck from the software layer.
3. `04-freelancer-ai-agent/regtech/warung-node-compliance.md` - A warung holding third-party parcels triggers storage, PDP Law (personal data of end customers), and PPh 23 withholding obligations. The compliance surface for node enablement is unaddressed and is a regtech gap.

These are deliberately capped at three per the self-evolution rule. They are logged here as discovered, not yet as filled files, to follow the append-only and single-topic conventions.

## Sources

1. Wikipedia, "Warung" (Indonesian). `https://id.wikipedia.org/wiki/Warung`. Accessed 2026-07-07. Defines warung as essential family-owned retail; lists warung nasi, sembako, kopi, kelontong, internet, telekomunikasi.
2. Wikipedia, "Warung" (English). `https://en.wikipedia.org/wiki/Warung`. Accessed 2026-07-07. Notes warung as small neighborhood convenience shop, often a front room or booth in a family home.
3. OttoPay, "Mengenal Jenis-Jenis Warung Tradisional di Indonesia." `https://ottopay.id/blog/artikel/jenis-warung-tradisional-di-indonesia/`. Accessed 2026-07-07. Warung taxonomy; warungs persist and innovate against modern retail; sells digital bookkeeping (OttoKasir) confirming analog default.
4. Wikipedia, "Economy of Indonesia." `https://en.wikipedia.org/wiki/Economy_of_Indonesia`. Accessed 2026-07-07. MSMEs contribute ~61.7 percent of economy; internet economy US$77B in 2022; ~64M UMKM cited context.
5. Wikipedia, "Gojek." `https://en.wikipedia.org/wiki/Gojek`. Accessed 2026-07-07. First Indonesian unicorn/decacorn; Gojek-Tokopedia merger 17 May 2021 forming GoTo; ~170M users SEA; GoFood/GoShop/GoSend services.
6. Katadata, UMKM count coverage (infographic series). `https://katadata.co.id/`. Accessed 2026-07-07. Industry context for 64M UMKM figure (primary figure from KemenkopUKM, secondary here).
7. Sibling vault docs: `03-id-business-trends/bottlenecks/ojol-logistics-inefficiency.md`, `ojol-address-normalization.md`, `umkm-npwp-registration-gap.md`; `07-gaps-and-opportunities/opportunities/digital-credit-scoring-umkm-qris.md`; `03-id-business-trends/demand-mining/umkm-digitalisasi-paksa-platform-ekosistem.md`.

Note on unreachable sources: BPS open API (`api.bps.go.id/v1`) returned HTTP 403 to unauthenticated requests; World Bank micro-retail blog and Google cache fetches returned 404. The 16 to 21 million warung estimate is therefore treated as an industry estimate, not a verified census figure. Specific Warung Pintar / Yummy Corp headcount and closure figures were not verifiable from primary sources in this pass and are flagged as reported.

## New gaps discovered during this research

1. `07-gaps-and-opportunities/inbox/2026-07-07-warung-graph-open-data.md` - There is no geocoded, capability-tagged warung registry in Indonesia (public or commercial). The team that builds the node-enabling layer simultaneously becomes the owner of the country's only real-time warung graph. That data asset, and the question of who should hold it (open vs platform-locked), is itself an opportunity and a governance gap.

2. `03-id-business-trends/bottlenecks/warung-cold-chain-capex.md` - Cold-capable warung nodes require capex (chest freezer, insulated box) that is only justified by predictable grocery or pharmacy volume. The financing mechanism for that capex (vendor financing, revenue-share lease, cooperative pool) is undefined and is a distinct bottleneck from the software layer.

3. `04-freelancer-ai-agent/regtech/warung-node-compliance.md` - A warung that holds third-party parcels or goods may trigger informal logistics, storage, or PDP (personal data protection) obligations. The compliance surface for turning a warung into a node (liability, insurance, data of end customers flowing through a micro-merchant) is unaddressed and is a regtech gap.
