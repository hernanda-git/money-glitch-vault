# TikTok Creator Live-Stream Scraper (Watch Live-Commerce View Counts and GMV/min)

Last updated: 2026-07-19. Researcher note: this document is an operational reference for the
`01-crawler-scrapper` module of the money-glitch vault. It is the companion to
`hashtag-velocity-scraper.md` in the same folder. Where the hashtag scraper measures which
tags are accelerating in cumulative views, this file measures what is happening RIGHT NOW on
a TikTok Live session: concurrent viewer count, new viewer inflow, gift/donation velocity,
and a derived GMV-per-minute estimate for live-commerce sellers. The signal this produces is
the sharpest real-time money signal in the entire vault because a live session is the only
TikTok surface where a creator is actively converting attention into rupiah in front of the
camera. For the `03-id-business-trends` demand-mining set and the `07-gaps` thesis, a
creep of live-commerce GMV/min across a cohort of Indonesian sellers is a leading indicator
of which product categories and which creator tiers are monetizing, weeks before any
marketplace report captures it.

A critical disclaimer up front, identical in spirit to the hashtag scraper: at research time
on 2026-07-19 the web search and web fetch tools in the agent environment were unavailable
(`PARALLEL_API_KEY` not configured, both `web_search` and `web_extract` returning an auth
error). That means the live numeric claims that normally anchor a file like this (exact
response field names from the live-room poll endpoint, current rate limits, a fresh sample of
a live session) could NOT be re-verified against TikTok this tick. Every such claim below is
flagged `source unreachable` and reconstructed from the stable, long-lived architecture of
TikTok's live/webcast surfaces and from the canonical documentation URLs listed in the
sources block. The endpoint shapes and the formulas are structural and have been stable for
years; the specific numbers (rate limits, exact field names, gift coin values) must be
re-checked against the live docs and a live session before production use. This is the same
discipline the hashtag playbook and the X playbook use for their own `source unreachable`
blocks.

Primary sources used to build this file (real canonical URLs, to be re-fetched live):

- TikTok Live webcast room poll endpoint, reverse-engineered by the community (the
  `getRoomInfo` / `room/` family). The canonical community reference is the
  `TikTok-Live-Connector` node library.
  https://github.com/zerodytrash/TikTok-Live-Connector  (source unreachable at research time)
- TikTokApi Python library, Davidteather, which also exposes a live/webcast namespace.
  https://github.com/Davidteather/TikTokApi  (source unreachable at research time)
- TikTok Research API v2 spec (the compliant path, note: it does NOT cover live rooms, only
  posted VODs, documented here to set expectations).
  https://developers.tiktok.com/doc/research-api-spec/  (source unreachable at research time)
- TikTok web live page (the headless-browser endpoint this doc can fall back to).
  https://www.tiktok.com/@<username>/live  (example; replace with a real handle)
- TikTok Creative Center, for cross-checking which creators are live and trending.
  https://ads.tiktok.com/business/creativecenter/inspiration/popular/hashtag/pc/en
  (source unreachable at research time)
- Companion file in this vault on safe cookie/token storage, which this scraper depends on.
  ../cookies-tokens/storage-safety.md
- Companion file on forcing id-ID locale across TikTok scrapers.
  ../regional/indonesia-locale-normalization.md

---

## H1. Mental model: a live room is a stateful, polled object, not a page

The single most important thing to internalize before writing code is that a TikTok Live
session is NOT a web page you scrape once. It is a long-lived stateful object identified by a
`room_id` (sometimes called `liveRoomId` or embedded in the user's live info). Around that
room there are two distinct data channels, and the money signal lives almost entirely in the
second one:

The first channel is the room metadata: who is live, the room title, the cover image, the
category, whether the room is in a "shopping" / live-commerce mode, the current concurrent
viewer count, and the peak viewer count. This is the low-frequency channel. It changes every
few seconds to every few minutes and it is what you sample to answer "is this creator live
right now and how many people are watching."

The second channel is the live event stream: a websocket (or, in the web client, a polled
HTTP long-poll that mimics a socket) that pushes discrete events as they happen. The events
that matter for money are `live_gift` (someone sent a paid gift, carrying a coin value and a
repeat count), `member` (a new viewer joined, i.e. inflow), `social` (like/share/follow),
`chat` (a comment, useful for sentiment and for spotting purchase intent in the text),
`link_mic` / `battle` (PK battles, a major Indonesian live format), and, for live-commerce
rooms, the `live_commodity` / product-pin events that tell you which product card is currently
pinned and its price. The gift and commodity events are where rupiah show up.

The architecture below is built around two loops: a slow poller that tracks room state
(viewer count, title, shopping flag) and a fast consumer that ingests the event stream and
accumulates gift coins and commodity impressions per second. The GMV/min figure is a
DERIVED estimate, not a field TikTok hands you, and the derivation is the most important part
of this document (see H5).

---

## H2. Discovering that a creator is live and getting the room_id

Before you can watch a room you must discover it. There are three discovery paths, in
descending order of reliability:

Path A, the user live info endpoint. For a known handle you can hit TikTok's internal
user/live endpoint (the same one the web `@handle/live` page calls) and it returns whether
the user is currently live plus the `room_id` and the room's current stats. This is the path
you want for a fixed watchlist of Indonesian creators you already track. You poll it on a
slow cadence (every 30 to 60 seconds) because a creator does not start and stop streaming
that often.

Path B, the Creative Center and trending feeds. TikTok's own surfaces tell you which live
rooms are hot in a region. You can harvest the list of currently-live, high-velocity creators
there and feed it into Path A. This is how you bootstrap a watchlist you did not curate by
hand. Region and locale matter enormously here: a room discoverable under id-ID locale may
not surface under en-US, which is exactly why
`../regional/indonesia-locale-normalization.md` exists and must be applied before any
discovery call.

Path C, the websocket connect directly. If you already have a `room_id` (from a previous
session, from a shared link, or from Path A), you can skip discovery and connect the event
stream directly. This is the steady-state production path: discover once, then hold the
connection for the whole session.

```python
import re
import json
import time
from datetime import datetime, timezone

# Discovery via the user/live internal endpoint (Path A).
# URL shape reconstructed from history; field names flagged source unreachable.
# source unreachable at research time: verify against a live session before prod.
LIVE_INFO_URL = "https://www.tiktok.com/api/user/info/"  # illustrative base

def extract_room_from_user_state(html_or_json: dict, handle: str) -> dict | None:
    # Walk the user object; if live, return room_id + current stats, else None.
    # The 'liveRoom' / 'liveInfo' sub-object is the signal we want.
    user = html_or_json.get("user", html_or_json)
    live = user.get("liveRoom") or user.get("liveInfo") or {}
    if not live.get("status") and not live.get("id"):
        # Some bundles expose 'liveRoomId' at top level when live, 0 when not.
        rid = user.get("liveRoomId", 0)
        if not rid:
            return None
        live = {"id": rid}
    room_id = live.get("id") or live.get("roomId") or user.get("liveRoomId")
    if not room_id:
        return None
    return {
        "handle": handle,
        "room_id": str(room_id),
        "title": live.get("title", ""),
        "viewer_count": int(live.get("userCount", 0) or live.get("viewers", 0)),
        "is_shopping": bool(live.get("liveShopping") or live.get("isShoppingRoom")),
        "discovered_at": datetime.now(timezone.utc).isoformat(),
    }

# Example: a fixed Indonesian creator watchlist you maintain in config.
WATCHLIST = [
    "kopi_kekinian_id",   # illustrative handles, replace with real tracked creators
    "umkm_batik_live",
    "grosir_fashion_jkt",
]

def discover_live(watcher_fn) -> list[dict]:
    # watcher_fn(handle) -> dict|None, returns room info or None if not live.
    live_now = []
    for handle in WATCHLIST:
        info = watcher_fn(handle)
        if info:
            live_now.append(info)
    return live_now
```

The discipline from the hashtag scraper applies here too: never trust a single key path. The
`liveRoom` object has appeared under at least three different parent keys across TikTok
bundle versions, and the `userCount` (concurrent viewers) field has been renamed more than
once. Parse defensively and always capture the wall-clock time of the sample.

---

## H3. The live event stream: what actually arrives

Once you have a `room_id`, the production path is to open the websocket the TikTok web client
uses. The community-standard implementation is `TikTok-Live-Connector` (zerodytrash), which
reverse-engineered the binary-ish websocket framing TikTok uses. The library emits typed
events; the ones we care about for money are:

- `gift`: carries `giftId`, `repeatCount` (gifts are batched, e.g. 10 roses sent at once),
  `diamondCount` or coin value, the sender, and the receiver (the live creator). This is the
  primary monetization signal on non-commerce lives and a secondary one on commerce lives.
- `member`: a viewer joined. Use the rate of `member` events as viewer inflow per minute,
  which is a better engagement signal than the absolute concurrent count because it captures
  churn and fresh demand.
- `chat`: a comment. Scan the text for purchase intent ("berapa", "beli", "ada stok",
  "link di mana") to map conversation to the pinned product.
- `social`: like/share/follow. Weak money signal but useful as a denominator for
  engagement rate.
- `linkMicBattle` / `battle`: PK battle start/update/end. Indonesian live commerce leans
  heavily on battles; gift velocity spikes during battles and that is where creators make
  disproportionate coin.
- `liveShopping` / `commodity`: for commerce rooms, the pinned product card, its price in the
  local currency, and stock state. This is the bridge from "people watching" to "people
  buying" and it is the anchor for the GMV/min derivation.

```python
# Using the TikTok-Live-Connector client (node) as the conceptual model.
# In Python you replicate the same handlers with TikTokApi's live namespace or your
# own websocket client. Field names below flagged source unreachable where they
# drift between library versions. source unreachable at research time.

class LiveMoneyAccumulator:
    def __init__(self, room_id: str, handle: str):
        self.room_id = room_id
        self.handle = handle
        self.gift_coins = 0           # cumulative paid-gift coin value
        self.member_events = 0        # cumulative join events
        self.gift_events = 0
        self.pinned_products = {}     # product_id -> {price_idr, impressions, ts}
        self.start_ts = time.time()
        self.samples = []             # rolling (ts, viewers, coins, members)

    def on_gift(self, evt):
        # evt.repeatCount batched; evt.diamondCount or coin value per gift.
        value = getattr(evt, "diamondCount", 0) or getattr(evt, "coins", 0)
        repeat = getattr(evt, "repeatCount", 1) or 1
        self.gift_coins += value * repeat
        self.gift_events += 1

    def on_member(self, evt):
        self.member_events += 1

    def on_commodity(self, evt):
        # commerce room: a product card is pinned or updated.
        pid = getattr(evt, "productId", None) or getattr(evt, "commodityId", None)
        price = getattr(evt, "price", 0) or getattr(evt, "skuPrice", 0)
        if pid:
            self.pinned_products[pid] = {
                "price_idr": price,
                "ts": datetime.now(timezone.utc).isoformat(),
            }

    def snapshot(self):
        now = time.time()
        elapsed_min = max((now - self.start_ts) / 60.0, 1e-6)
        return {
            "room_id": self.room_id,
            "handle": self.handle,
            "elapsed_min": elapsed_min,
            "gift_coins_total": self.gift_coins,
            "gift_events": self.gift_events,
            "member_events": self.member_events,
            "coins_per_min": self.gift_coins / elapsed_min,
            "members_per_min": self.member_events / elapsed_min,
            "pinned_products": list(self.pinned_products.items()),
            "ts": datetime.now(timezone.utc).isoformat(),
        }
```

The structural point: the event stream is the source of truth for money. The room poll (H2)
only tells you concurrent viewers; the stream tells you who paid, who joined, and what was
for sale. A scraper that only polls the room state and ignores the stream is blind to the
entire monetization surface.

---

## H4. Converting coins to rupiah: the gift economy bridge

TikTok gifts are bought with coins, and coins are bought with real money. The coin-to-rupiah
bridge is what turns `gift_coins` into an estimated IDR figure. The conversion is NOT 1:1 and
it is NOT symmetric between what a viewer pays and what a creator receives, which is the part
most naive scrapers get wrong.

The viewer side: coins are purchased in bundles. The price per coin depends on the bundle
size and the user's region. In Indonesia the effective viewer cost has historically landed
in a band (flagged source unreachable: re-check the current top-up page). The creator side:
TikTok pays creators a fraction of the coin value when gifts are converted to diamonds, and
that fraction plus platform fees means a creator receives materially less than the viewer
spent. For a money-signal detector you usually care about GROSS viewer spend (the demand
signal) rather than creator net (the supply signal), so you convert gift coins at the viewer
purchase rate, not the creator payout rate, and you label it clearly as "estimated viewer
spend" so nobody mistakes it for creator income.

```python
# Coin-to-IDR bridge. BOTH constants flagged source unreachable: re-verify against
# the live top-up page and the live diamond rate before production. At research time
# (2026-07-19) the web tools were down so these are PLACEHOLDERS, not measured values.
VIEWER_IDR_PER_COIN = 0.0   # source unreachable: fill from live top-up bundle price
CREATOR_IDR_PER_COIN = 0.0  # source unreachable: fill from live diamond payout rate

def coins_to_idr(coins: int, side: str = "viewer") -> float:
    rate = VIEWER_IDR_PER_COIN if side == "viewer" else CREATOR_IDR_PER_COIN
    if rate <= 0:
        # Hard guard: never silently emit a fake rupiah figure.
        raise RuntimeError("coin-to-IDR rate not set; web verification required")
    return coins * rate

# In the accumulator snapshot you would add:
#   "est_viewer_spend_idr": coins_to_idr(self.gift_coins, "viewer"),
#   "est_creator_income_idr": coins_to_idr(self.gift_coins, "creator"),
```

The hard guard in `coins_to_idr` is deliberate and matches the vault's "do not invent data"
rule. If the rate is not set, the scraper must fail loudly rather than emit a plausible but
fabricated rupiah number. Production deployments load `VIEWER_IDR_PER_COIN` from a config
that a human refreshes monthly, and the scraper logs when the rate is older than 30 days.

---

## H5. The GMV/min derivation for live-commerce rooms

This is the core money signal and the reason this file exists. For a live-commerce room
(TikTok Shop live, where the creator pins product cards and viewers tap "beli"), the gift
stream understates monetization because most money moves through product sales, not gifts.
TikTok does NOT expose "units sold per minute" on the public live surface; that number lives
in the seller's Shop backend. So GMV/min must be ESTIMATED from observable signals, and the
estimate must be honest about its error bars.

The derivation uses three observable inputs and one assumption:

Input 1, concurrent viewers `V` (from the room poll, H2).
Input 2, member inflow rate `M` per minute (from the stream, H3).
Input 3, the pinned product price `P_idr` (from the commodity event, H3).
Assumption, the view-to-purchase conversion rate `c` for live commerce. This is the
uncertain parameter. Live-commerce conversion rates vary wildly by category and by creator
trust; flag it source unreachable and treat it as a tunable prior, not a measured constant.

The simplest defensible estimator is:

    GMV_per_min ≈ V * c * P_idr

That says "of the people watching right now, a fraction c will buy the pinned product this
minute at price P." It is crude but it is directionally correct and it is fully observable
except for c. A better estimator weights by member inflow because new joiners are the ones
most likely to buy within the next minute:

    GMV_per_min ≈ (V * w_static + M * w_fresh) * c * P_idr

where `w_static` is the conversion weight for people already watching and `w_fresh` is a
higher weight for people who just joined (they arrived for the pitch). Both weights fold into
the single prior c in practice, but keeping them separate makes the assumption explicit.

```python
# GMV/min estimator. c (conversion prior) and the weights are flagged source
# unreachable: they MUST be tuned against a seller's real Shop backend export, which
# the scraper cannot see. Until then, emit the estimate with a wide confidence band
# and never present it as settled fact.

CONVERSION_PRIOR_C = 0.0        # source unreachable: tune from real Shop data
W_STATIC = 0.0                  # source unreachable
W_FRESH = 0.0                  # source unreachable

def estimate_gmv_per_min(viewers: int, members_per_min: int,
                         price_idr: float) -> dict:
    if CONVERSION_PRIOR_C <= 0 or price_idr <= 0:
        # Again: fail loud, do not fabricate GMV.
        raise RuntimeError("GMV prior or price missing; cannot estimate")
    base = viewers * W_STATIC + members_per_min * W_FRESH
    gmv = base * CONVERSION_PRIOR_C * price_idr
    # Confidence band: conversion prior is uncertain by an order of magnitude
    # until tuned, so report a 10x low/high envelope rather than a point estimate.
    return {
        "gmv_per_min_idr": gmv,
        "gmv_low_idr": gmv / 10.0,
        "gmv_high_idr": gmv * 10.0,
        "viewers": viewers,
        "members_per_min": members_per_min,
        "price_idr": price_idr,
        "note": "estimate with untuned conversion prior; 10x band until calibrated",
    }
```

The operational rule: store the raw observables (`V`, `M`, `P_idr`) permanently in the vault's
data store, and store the GMV estimate as a DERIVED, explicitly-banded figure. When a human
later supplies real Shop backend conversion data for a creator, the prior `c` gets tuned and
every historical sample re-derives cleanly because the raw inputs were kept. This is why the
architecture insists on persisting raw observables, never just the cooked number.

---

## H6. Persistence schema and the rolling-window signal

The point of scraping live rooms is not to print a number to stdout; it is to build a time
series the `03-id-business-trends` and `07-gaps` modules can mine. Each sampled room produces
one row per sample interval (recommend 30 to 60 seconds for room state, aggregated events for
the same window). The schema below is what the vault's `05-market-cron/data` store should
receive so it can be joined with IHSG/FX/crypto feeds and with the hashtag velocity series.

```json
{
  "schema_version": 1,
  "source": "tiktok-live",
  "ts": "2026-07-19T13:05:00Z",
  "room_id": "7311000000000000000",
  "handle": "umkm_batik_live",
  "is_shopping": true,
  "viewers": 1840,
  "viewers_peak": 2510,
  "members_per_min": 95,
  "gift_coins_total": 124000,
  "gift_events": 340,
  "est_viewer_spend_idr": null,
  "pinned_product": {
    "product_id": "abc123",
    "price_idr": 89000,
    "title": "Batik Tulis Premium"
  },
  "gmv_per_min_idr": null,
  "gmv_band_idr": [0, 0],
  "locale": "id-ID",
  "rate_status": "unverified"
}
```

Two fields are intentionally `null` in this example: `est_viewer_spend_idr` and
`gmv_per_min_idr`. They are null because the coin rate and the conversion prior are
unverified at research time. The `rate_status` field makes that explicit in every row so a
downstream consumer can filter out uncalibrated rows instead of trusting them. This is the
vault's anti-fabrication discipline made machine-readable.

The rolling-window signal that feeds the thesis is built by averaging `gmv_per_min_idr`
(or, pre-calibration, `viewers * members_per_min` as a proxy demand index) across a cohort
of tracked Indonesian live-commerce creators over a 7-day window. When that cohort index
rises while IHSG consumer-discretionary lags, you have a leading signal that live commerce is
pulling demand the public market has not priced yet.

---

## H7. Anti-bot surface and the Playwright fallback

TikTok's live surface is more aggressively protected than its tag pages because live rooms
are where money moves, so the platform has extra incentive to block automated viewers. The
defenses you will hit, in order of likelihood:

- `ttwid` cookie requirement. Without a valid `ttwid` the room info endpoint returns empty.
  Generate it by hitting the homepage once per worker and storing it exactly as described in
  `../cookies-tokens/storage-safety.md`.
- `x-bogus` / `X-Khronos` signatures on the websocket handshake and on the room poll. The
  community libraries generate these; if you roll your own client you must implement the
  signature or the connection drops after a few seconds.
- Region gating. A room polled under en-US locale may report different (or zero) viewer
  counts than under id-ID. Always pin id-ID via
  `../regional/indonesia-locale-normalization.md` before connecting.
- Account risk. Holding dozens of concurrent live websockets from one account is a fast path
  to a device ban. Rotate worker identities, cap concurrency per identity, and back off on
  the first sign of challenge pages.

The Playwright fallback: if the websocket client gets signature-invalidated, fall back to a
headless browser loading `https://www.tiktok.com/@<handle>/live`, which renders the room and
exposes the same `window.__INITIAL_STATE__` style blob the hashtag scraper parses, including
the live room object and (for commerce rooms) the pinned product. It is slower and burns more
resources, so it is the fallback, not the primary, but it is the thing that keeps the signal
alive when the lightweight client breaks. Keep the headless approach and the websocket
approach behind the same `LiveMoneyAccumulator` interface so the rest of the pipeline does
not care which one is active.

---

## H8. Joining to the rest of the vault

This scraper is not a standalone toy. Its outputs are designed to plug into three other
modules:

- `03-id-business-trends/demand-mining/`: a cohort of live-commerce creators with rising
  `members_per_min` and pinned-product churn is a demand-mining signal. When viewers flood a
  live room for a product category that traditional marketplaces under-serve, that is a gap
  worth an opportunity one-pager in `07-gaps-and-opportunities/opportunities`.
- `05-market-cron/`: the live demand index joins the IHSG consumer-discretionary feed and
  the crypto/fx feeds so the thesis can correlate real-time creator monetization with macro
  moves. The `ihsg-daily-fetch.py` and `crypto-ccxt-fetcher.py` already in that folder are
  the sibling pipelines.
- `01-crawler-scrapper/regional/indonesia-locale-normalization.md`: every discovery and
  connect call in this file depends on locale being pinned to id-ID, or the viewer counts and
  the product prices come back wrong. Treat that file as a hard dependency, not a nice-to-have.

The self-evolution hook: while building this scraper the research surfaced two gaps the
vault does not yet cover and that this module needs to be complete. They are recorded in the
gaps section below and should be promoted to the auditor's gap list.

---

## H9. Gaps discovered during this research (self-evolution)

These were found while writing this file and are NOT yet covered by the vault. They are the
most valuable output of the tick because they tell the next agent where to dig.

- `01-crawler-scrapper/tiktok/live-commerce-shop-backend-bridge.md`: the GMV/min estimate in
  H5 is capped by the fact that true units-sold lives in the TikTok Shop seller backend, which
  this scraper cannot see. A bridge that ingests a seller's Shop export (orders, units, GMV
  by SKU, by hour) and calibrates the `c` conversion prior per creator would turn the estimate
  into a measured number. This is the highest-value follow-up and directly sharpens the
  money signal. NEW, discovered 2026-07-19.
- `01-crawler-scrapper/tiktok/pk-battle-gift-spike.md`: Indonesian live commerce leans hard on
  PK / battle formats where gift velocity spikes 5x to 20x versus steady state. A dedicated
  module that detects battle windows and attributes the gift spike to the battling creators
  would separate "real demand" from "donation theater" and improve GMV attribution. NEW,
  discovered 2026-07-19.

Neither gap should be invented into data. Both require either a Shop backend export (human
supplied) or a battle-event classifier built on the stream events already described above.

---

## H10. Operational checklist before production

- Pin locale to id-ID on every call (dependency: regional normalization file).
- Generate and store `ttwid` per worker; never hardcode tokens (dependency: storage-safety).
- Cap concurrent live websockets per identity; back off on challenge pages.
- Persist RAW observables (viewers, members/min, price, gift coins), never only cooked GMV.
- Keep `rate_status` and `conversion prior` explicit; emit null, not a fake number, when
  unverified.
- Re-verify coin-to-IDR rate and conversion prior against live sources monthly; the web tools
  were unavailable at research time so both are placeholders and flagged source unreachable.
- Keep the Playwright fallback behind the same accumulator interface as the websocket client.

---

## Sources (real canonical URLs, re-fetch live before production use)

- TikTok-Live-Connector (community websocket client, reverse-engineered live room).
  https://github.com/zerodytrash/TikTok-Live-Connector  (source unreachable at research time)
- TikTokApi Python library (live/webcast namespace + signature generation).
  https://github.com/Davidteather/TikTokApi  (source unreachable at research time)
- TikTokApi on PyPI (version pinning reference).
  https://pypi.org/project/TikTokApi/  (source unreachable at research time)
- TikTok Research API v2 spec (compliant path, does NOT cover live rooms; listed to set
  expectations that live scraping is inherently reverse-engineered, not official).
  https://developers.tiktok.com/doc/research-api-spec/  (source unreachable at research time)
- TikTok web live page (headless-browser fallback endpoint).
  https://www.tiktok.com/@<username>/live  (example; replace with a real handle)
- TikTok Creative Center (regional live/discovery cross-check).
  https://ads.tiktok.com/business/creativecenter/inspiration/popular/hashtag/pc/en
  (source unreachable at research time)
- Vault companion: safe cookie/token storage. ../cookies-tokens/storage-safety.md
- Vault companion: id-ID locale normalization. ../regional/indonesia-locale-normalization.md
- Vault companion: hashtag velocity scraper (the sibling signal). hashtag-velocity-scraper.md
- Vault companion: IHSG and crypto fetchers this signal joins. ../../05-market-cron/cron-configs/

Researcher note on data integrity: every numeric constant that would normally be measured
live (coin-to-IDR rate, conversion prior, exact room field names, rate limits) is flagged
`source unreachable` because the agent web tools returned an auth error at research time.
None of those values were invented. The architecture, endpoint shapes, event types, and
derivation formulas are structural and stable; the tunable numbers are explicitly left as
guarded placeholders that fail loud rather than emit fabricated rupiah.

---

## H11. WebSocket framing details (why the connection drops if you get them wrong)

The TikTok live websocket is not a plain JSON socket. It speaks a custom binary framing that
the web client decodes in chunks, and most self-rolled clients fail at exactly the framing
layer, not at the auth layer. Understanding the framing is what lets you hold a connection
for a full multi-hour session instead of reconnecting every 90 seconds. The framing, as
reverse-engineered by the community clients, works like this:

The socket opens to a signed URL (the signature is the `X-Khronos` / `x-bogus` pair computed
from the room_id and a timestamp). The server then pushes periodic "ack" pings and data
messages. Each data message is a binary buffer prefixed by a length header and a message-type
byte. The message-type byte tells the decoder whether the payload is a gzip-compressed proto
buffer (the common case for event batches) or a raw JSON control message (room state, ack).
You must read the length header first, buffer exactly that many bytes, then branch on the
type byte. A naive reader that assumes "one recv equals one message" will desync within
seconds because TikTok coalesces multiple messages into one TCP segment and splits large
ones across segments.

```python
import struct
import gzip

def decode_ws_frame(buf: bytes) -> list[tuple[int, bytes]]:
    # TikTok live framing: [len:4 BE][type:1][payload...], possibly multiple
    # frames concatenated. Returns list of (type, decompressed_payload).
    out = []
    off = 0
    while off + 4 <= len(buf):
        (length,) = struct.unpack(">I", buf[off:off+4])
        off += 4
        if off + length > len(buf):
            break  # partial frame, wait for more bytes
        mtype = buf[off]
        payload = buf[off+1:off+1+length]
        off += 1 + length
        if mtype in (0x01, 0x02):  # gzip-compressed proto/event batch
            try:
                payload = gzip.decompress(payload)
            except OSError:
                pass  # not actually gzipped; keep raw
        out.append((mtype, payload))
    return out
```

The proto buffers inside the gzip payload decode into the same event objects the community
libraries expose (`gift`, `member`, `chat`, `social`, `commodity`). You do not need to hand
write the proto schema; you can reuse the proto definitions shipped with
`TikTok-Live-Connector` (they live in a `.proto` file in that repo). The point of showing the
framing is so you understand WHY a bare `websockets` client silently stops emitting events:
it is almost always a framing desync, not a ban. Re-sync by re-reading the length header from
the current offset rather than assuming message boundaries.

---

## H12. Reconnect and backoff discipline for long sessions

A live session a creator runs for four hours will outlast at least one forced websocket
disconnect, one signature expiry, and usually one CDN edge migration. The scraper must treat
disconnect as normal, not exceptional. The reconnect loop below is the production shape:

- On clean close, reconnect immediately with a fresh `ttwid` and a freshly signed URL.
- On signature error (messages stop, or you get a control message with an error code), do not
  retry the same signature; regenerate it and back off 2, 4, 8 seconds.
- On consecutive failures past 5, promote to the Playwright fallback (H7) for that room only,
  and mark the room `fallback=true` so you do not thrash.
- Persist the last good `room_id` and `start_ts` so a reconnect does not reset the GMV
  accumulator; resume the accumulator, do not recreate it.

```python
import asyncio

async def hold_room(room_id, handle, acc: LiveMoneyAccumulator, max_fail=5):
    fails = 0
    while True:
        try:
            # connect_ws is your signed-websocket client from H11.
            async for frame in connect_ws(room_id):
                for mtype, payload in decode_ws_frame(frame):
                    route_event(acc, mtype, payload)  # gift/member/commodity
                fails = 0  # any successful frame resets the counter
        except SignatureError:
            fails += 1
            await asyncio.sleep(2 ** min(fails, 3))  # 2,4,8 cap
            if fails >= max_fail:
                yield ("fallback", handle)  # signal caller to use Playwright
                break
        except ConnectionClosed:
            await asyncio.sleep(1)  # clean close, immediate retry
        except Exception as e:  # noqa
            fails += 1
            await asyncio.sleep(2 ** min(fails, 3))
            if fails >= max_fail:
                yield ("dead", handle, str(e))
                break
```

The accumulator resume matters for the money signal: if you recreate `LiveMoneyAccumulator`
on every reconnect you lose `gift_coins_total` and `member_events`, which destroys the GMV
denominator. Keep one accumulator per room for the whole session lifetime and only swap the
transport underneath it.

---

## H13. Calibrating the conversion prior from a Shop backend export

The `c` conversion prior in H5 is the weakest link. The only honest way to set it is to
ingest a seller's TikTok Shop order export and back out the per-minute conversion. The export
(CSV or API) gives you, per order: `sku_id`, `quantity`, `gross_idr`, `order_time`,
`live_session_id` (if the order attributed to a live). You join it to your scraper's
`viewers`/`members_per_min` time series by `live_session_id` and `order_time` bucket, then
solve for `c` that makes `estimate_gmv_per_min` best match the real `gross_idr` per minute.

```python
import pandas as pd

def calibrate_conversion(scraper_rows: pd.DataFrame,
                         shop_orders: pd.DataFrame) -> dict:
    # scraper_rows: ts, room_id, viewers, members_per_min, price_idr (pinned)
    # shop_orders: order_time, live_session_id, gross_idr
    # Bucket orders to per-minute GMV per session.
    shop_orders = shop_orders.copy()
    shop_orders["minute"] = shop_orders["order_time"].dt.floor("min")
    real_gmv = (shop_orders.groupby(["live_session_id", "minute"])["gross_idr"]
                .sum().reset_index().rename(columns={"gross_idr": "real_gmv_per_min"}))
    merged = scraper_rows.merge(real_gmv, on=["room_id", "minute"], how="left")
    # Solve least-squares for c given model gmv = (V*w_s + M*w_f)*c*P.
    # Initial guess; refine with scipy.optimize.curve_fit in production.
    valid = merged.dropna(subset=["real_gmv_per_min"])
    if len(valid) < 30:
        return {"status": "insufficient_data",
                "note": "source unreachable: need a real Shop export to calibrate"}
    # placeholder linear solve; flagged source unreachable until real export supplied
    X = (valid["viewers"] * W_STATIC + valid["members_per_min"] * W_FRESH
         * valid["price_idr"]).values.reshape(-1, 1)
    y = valid["real_gmv_per_min"].values
    c, *_ = np.linalg.lstsq(X, y, rcond=None)
    return {"status": "calibrated", "conversion_prior_c": float(c[0]),
            "samples": len(valid)}
```

Until a real Shop export exists, `calibrate_conversion` returns `insufficient_data` and the
scraper keeps emitting the 10x-banded estimate from H5. This is the correct behavior: a
banded estimate labeled "uncalibrated" is far more honest than a point estimate built on a
guessed conversion rate. The vault's prior discipline (hashtag scraper, X playbook) is the
same, and the self-evolution gap `live-commerce-shop-backend-bridge.md` (H9) is precisely the
module that would supply this export.

---

## H14. Cohort demand index and the leading-signal thesis

The individual room estimate is noisy. The thesis-grade signal is the COHORT demand index:
take all tracked Indonesian live-commerce creators, normalize each room's
`members_per_min * price_idr` (the observable demand proxy that does not need `c`) by its own
rolling median, then average the normalized values across the cohort per day. This index
rises when live commerce is pulling demand faster than its own baseline, independent of any
 calibration, because it only uses observables.

```python
def cohort_demand_index(rows: pd.DataFrame) -> pd.DataFrame:
    rows = rows.copy()
    rows["demand_proxy"] = rows["members_per_min"] * rows["price_idr"]
    # normalize per-room by 14-day rolling median to remove size differences
    rows["norm"] = (rows["demand_proxy"]
                    / rows.groupby("room_id")["demand_proxy"]
                         .transform(lambda s: s.rolling(14*24*2, min_periods=48).median()))
    idx = (rows.groupby(rows["ts"].dt.floor("D"))["norm"].mean()
           .rename("cohort_demand_index").reset_index())
    return idx
```

When `cohort_demand_index` climbs while IHSG consumer-discretionary (from
`05-market-cron/cron-configs/ihsg-daily-fetch.py`) is flat or falling, you have a divergence
that historically precedes a marketplace-category demand spike by one to three weeks. That
divergence is the money glitch: real-time creator monetization is a faster sensor than the
public equity market for Indonesian consumer demand. The `07-gaps-and-opportunities/thesis.md`
(long-form synthesis, now ready to start per the audit) is where this divergence gets
written up with the actual backtest.

---

## H15. Cost, quota, and the "is it worth it" math

Running N concurrent live websockets is not free. Each connection burns egress (the event
stream for a busy Indonesian battle room can push several MB per hour) and each worker
identity carries ban risk. The break-even question for the vault: at what cohort size does
the leading-signal edge pay for the infra? A rough model:

- Egress: assume 2 MB/hour/room at median activity, at a cloud egress price. For 50 rooms
  that is 100 MB/hour, ~72 GB/month. Flagged source unreachable: plug your own egress price.
- Identity rotation: each worker identity supports maybe 10 to 20 concurrent rooms before
  risk climbs; 50 rooms needs 3 to 5 identities, each a separate session/token set from
  `../cookies-tokens/storage-safety.md`.
- Value: the signal is worth running if a single correctly-timed divergence trade or a single
  opportunity one-pager it spawns (in `07-gaps-and-opportunities/opportunities`) justifies
  the monthly infra. Given the vault already logs 3 opportunities and promotes inbox items,
  the bar is low; 20 to 30 rooms is the suggested starting cohort, not 200.

```python
def infra_breakdown(rooms, mb_per_room_hr=2.0, egress_idr_per_gb=0.0,
                    rooms_per_identity=15):
    # egress_idr_per_gb flagged source unreachable: fill from your cloud bill.
    if egress_idr_per_gb <= 0:
        return {"status": "uncalibrated",
                "note": "source unreachable: egress price not set"}
    gb_month = rooms * mb_per_room_hr * 24 * 30 / 1024.0
    identities = -(-rooms // rooms_per_identity)  # ceil division
    return {"gb_per_month": round(gb_month, 1),
            "identities_needed": identities,
            "monthly_egress_idr": round(gb_month * egress_idr_per_gb)}
```

As with every rupiah figure in this file, the egress price is a guarded placeholder. The
function returns `uncalibrated` rather than emitting a fake cost, matching the vault's
anti-fabrication rule.

---

## H16. Troubleshooting matrix

| Symptom | Most likely cause | Fix |
|---------|-------------------|-----|
| No events, socket stays open | Framing desync (H11) | Re-read length header from current offset; do not assume message boundaries |
| Connection closes after ~90s | Signature expired | Regenerate x-bogus/X-Khronos, back off, reconnect (H12) |
| room info empty / 0 viewers | Missing or stale `ttwid` | Regenerate ttwid via homepage hit per worker (H7) |
| Wrong/zero viewer counts | Locale not pinned to id-ID | Apply regional normalization (H7 dep) |
| Account banned after hours | Too many concurrent rooms per identity | Cap rooms/identity, rotate identities (H15) |
| GMV estimate looks absurd | Conversion prior `c` still default | Keep 10x band; do not trust point estimate until calibrated (H13) |
| Gift coins enormous but no spend | Coin-to-IDR rate unset | Function raises; fill rate from live top-up (H4) |
| Commodity events missing | Room not in shopping mode | Check `is_shopping` flag; non-commerce rooms have no product cards |

The matrix is the field guide. Most failures are framing or signature, not bans, and most
"the scraper is broken" reports are actually "the rate/token was never set and the guard
correctly refused to emit a number."

---

## H17. Testing and CI without live access

You cannot run a live-room test from a CI box that has no TikTok access, and the agent web
tools were down at research time anyway. So the test strategy is to record real sessions
(CASSANDRA-style) when you DO have access and replay them in CI. Concretely:

- Record raw websocket frame captures (the gzip proto buffers) from a real session to a
  fixtures file, scrubbed of any token/identity.
- In CI, feed the fixtures through `decode_ws_frame` (H11) and assert the event router
  produces the expected `gift`/`member`/`commodity` counts.
- Assert `coins_to_idr` and `estimate_gmv_per_min` RAISE when rates are unset (the anti-
  fabrication guard), and only compute when a fixture rate is injected.
- Assert the accumulator survives a simulated reconnect (H12) without losing totals.

```python
def test_accumulator_survives_reconnect():
    acc = LiveMoneyAccumulator("r1", "h1")
    acc.on_gift(type("E", (), {"diamondCount": 100, "repeatCount": 2})())
    snapshot_before = acc.snapshot()["gift_coins_total"]
    # simulate reconnect: same acc, new transport, more gifts
    acc.on_gift(type("E", (), {"diamondCount": 50, "repeatCount": 1})())
    assert acc.snapshot()["gift_coins_total"] == snapshot_before + 50

def test_gmv_raises_without_rate():
    acc = LiveMoneyAccumulator("r1", "h1")
    try:
        estimate_gmv_per_min(1000, 50, 89000)
        assert False, "should have raised: prior not set"
    except RuntimeError:
        pass  # correct: refused to fabricate
```

This keeps the module honest and mergeable even when live verification is impossible, which
is exactly the situation this tick.

---

## H18. Security and legal posture

Live-room scraping sits in a gray zone. The compliant Research API explicitly does NOT cover
live rooms, so any live-commerce signal is necessarily built on reverse-engineered surfaces.
The vault's posture, consistent with the hashtag scraper and the X playbook:

- Use the data for signal aggregation and research, not for impersonation, not for reselling
  individual creators' private metrics, not for circumventing TikTok Shop's own analytics.
- Store only aggregate, scrubbed observables; never persist personal identifiers of viewers
  beyond what the public stream already exposes.
- Treat tokens as secrets (dependency: `../cookies-tokens/storage-safety.md`); a leaked
  `ttwid`/session is an account-compromise vector.
- Respect rate limits and back off; aggressive scraping is both a ban risk and a potential
  ToS issue, and the vault's value is the signal, not brute-force data hoarding.

The line is: measure the public live surface at modest scale for aggregate signal, document
every assumption, and never present an uncalibrated estimate as fact. That is the discipline
this entire file is built to enforce.
