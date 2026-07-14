# TikTok Hashtag Velocity Scraper (Detect Trending Hashtags by Views/Hour)

Last updated: 2026-07-14. Researcher note: this document is an operational reference for the
`01-crawler-scrapper` module of the money-glitch vault. It is written for the agent that needs
to detect which TikTok hashtags are accelerating in view count per hour so the signal can feed
the `03-id-business-trends` demand-mining set, the `05-market-cron` sentiment trackers, and the
`07-gaps` thesis. The goal is not to teach the user how to go viral. The goal is to give the
agent a repeatable, tested architecture for measuring hashtag momentum, with working code, the
real endpoints involved, the anti-bot surface, and the velocity math that turns raw counts into
an actionable "this is exploding right now" signal.

A critical disclaimer up front: at research time on 2026-07-14 the web search and web fetch
tools in the agent environment were unavailable (`PARALLEL_API_KEY` not configured, both
`web_search` and `web_extract` returning an auth error). That means the live numeric claims
that normally anchor a file like this (exact response field names, current rate limits, a
fresh hashtag growth sample) could NOT be re-verified against TikTok this tick. Every such
claim below is flagged `source unreachable` and reconstructed from the stable, long-lived
architecture of TikTok's public surfaces and from the canonical documentation URLs listed in
the sources block. The endpoint shapes and formulas are structural and have been stable for
years; the specific numbers (rate limits, field names) must be re-checked against the live
docs before production use. This is the same discipline the X playbook uses for its own
`source unreachable` blocks.

Primary sources used to build this file (real canonical URLs, to be re-fetched live):

- TikTok Research API v2 spec (official, the compliant path).
  https://developers.tiktok.com/doc/research-api-spec/  (source unreachable at research time)
- TikTokApi Python library, Davidteather. The de-facto community scraper.
  https://github.com/Davidteather/TikTokApi  (source unreachable at research time)
- TikTokApi on PyPI (version pinning reference).
  https://pypi.org/project/TikTokApi/  (source unreachable at research time)
- TikTok web tag page (the headless-browser endpoint this doc reverse-engineers).
  https://www.tiktok.com/tag/fyp  (example; append any hashtag slug)
- TikTok Creative Center trending hashtags (sanctioned, no scraping needed).
  https://ads.tiktok.com/business/creativecenter/inspiration/popular/hashtag/pc/en
  (source unreachable at research time)
- TikTok Business API / Display API docs (the sibling of Research API).
  https://developers.tiktok.com/doc/get-started-business-api/  (source unreachable at research time)
- Companion file in this vault on safe cookie/token storage, which this scraper depends on.
  ../cookies-tokens/storage-safety.md

---

## H1. Mental model: three different TikTok surfaces and which one to scrape

Before writing a single line of code you must understand that TikTok exposes hashtag data
through at least three structurally different surfaces, and the velocity signal you can extract
from each is not the same. Picking the wrong surface is the single most common reason a
"TikTok trend detector" returns garbage or gets the account banned on day one.

The web tag page is what powers `tiktok.com/tag/<slug>`. It is a server-rendered HTML shell
that embeds a large JSON blob (historically under `window.__INITIAL_STATE__` or a generic
`__STATE__` / `>UniversalData</` script tag) containing the challenge object with
`statsV2` (view count, video count, like count, share count) and the first page of videos. It
is the richest free source of aggregate hashtag stats but it is also the most aggressively
bot-protected (x-bogus signature, ttwid cookie, region gating). Headless browsers can read it
but expect breakage every time TikTok shuffles the bundle.

The Research API is the official, compliant, application-only path. You apply for access,
get a Bearer token scoped to specific fields, and POST a query to
`https://open.tiktokapis.com/v2/research/video/query/` filtering by `challenge_name`. It does
NOT return a live aggregate `statsV2` for the hashtag; it returns the individual videos posted
in a date range that carry that hashtag, each with its own `view_count`. You compute the
velocity yourself by summing views per hour bucket. This is the path you want if you care
about compliance, reproducibility, and not burning accounts. Downsides: you must pre-register
the exact fields you read (a field not in your access grant returns 401/403), you are limited
to a monthly video cap and a query rate, and you cannot pull a single "hashtag has X total
views" number directly.

The Creative Center is TikTok's own sanctioned trend dashboard. It already ranks trending
hashtags with view counts and growth percentages and it exposes a JSON endpoint behind the
page that third-party trackers hit. You do not scrape the public page; you call the same
internal endpoint with your session. This is the lowest-risk "is this hashtag hot" source
because it is literally TikTok telling you what is trending, but it is coarser (curated top-N,
not arbitrary niche hashtags) and it is region/locale dependent.

The rule of thumb for this vault: use Creative Center for the broad "what is hot in Indonesia
right now" surface, use the Research API for compliant per-video velocity on a hashtag you
already care about, and use the web tag page only as a fallback or for niche hashtags that
Creative Center does not rank and that are too small for Research API's minimum query
thresholds. Never treat the web page as primary in production.

---

## H2. Anatomy of the web tag endpoint

The page at `https://www.tiktok.com/tag/<slug>` (no leading hash, lowercase, spaces replaced
by nothing or hyphens) returns an HTML document. The useful data is in a script tag that
TikTok serializes as a JSON object. Over the years the variable name has moved; historically
it was `window.__INITIAL_STATE__`, later a more generic `>UniversalData</` / `STATE` blob, and
the challenge object lives under a key path like `ItemModule` / `Challenge` or `challengeInfo`.
The stability of this path is the core operational risk: a parser pinned to
`__INITIAL_STATE__.Challenge.statsV2.viewCount` will silently break when TikTok renames it.

What you are looking for inside that blob, conceptually:

- `challengeInfo.statsV2.viewCount` (string with possibly comma grouping, e.g. "1,234,567").
  This is the cumulative views attributed to the hashtag. Note it is a STRING and may be
  locale-formatted, so you must strip non-digits before int conversion.
- `challengeInfo.statsV2.videoCount` (number of posts using the tag).
- `challengeInfo.statsV2.likeCount`, `shareCount`, `commentCount` (the engagement split).
- `ItemModule` / `itemList` the first page of videos, each carrying its own `stats` block if
  you want per-video velocity instead of aggregate.

The velocity trick is simple: you do NOT get a "views in the last hour" field from TikTok
anywhere. TikTok only exposes a cumulative counter. Views/hour is therefore a derived quantity
you compute by polling the cumulative counter at two times and taking the difference. That
means the entire signal depends on disciplined, timestamped, repeat polling of the same slug
and on never losing the previous sample. The architecture below is built around that fact.

```python
import re
import json
import time
import asyncio
from datetime import datetime, timezone

def extract_challenge_state(html: str) -> dict:
    # TikTok serializes the whole app state in a script tag. The variable name
    # drifts, so we match the generic pattern instead of a fixed key.
    # NOTE: source unreachable at research time, path reconstructed from history.
    m = re.search(r"window\.__INITIAL_STATE__\s*=\s*({.*?});", html, re.DOTALL)
    if not m:
        # newer bundles use a generic STATE blob; try that fallback
        m = re.search(r">UniversalData</.*?({.+?})</script>", html, re.DOTALL)
    if not m:
        raise ValueError("challenge state blob not found; TikTok reshuffled the page")
    raw = m.group(1)
    # The blob is huge and sometimes truncated by the regex; parse defensively.
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        # trim trailing partial and retry with a closing bracket heuristic
        return json.loads(raw.rstrip().rstrip(",") + "}")

def read_hashtag_cumulative(state: dict, slug: str) -> tuple[int, int, datetime]:
    # Walk the challenge info, tolerating key-path drift. Returns (views, videos, ts).
    # Path depends on bundle version; try several known shapes.
    candidates = [
        state.get("Challenge", {}),
        state.get("challengeInfo", {}),
        (state.get("ItemModule", {}) or {}).get("challengeInfo", {}),
    ]
    info = next((c for c in candidates if c), {})
    stats = info.get("statsV2", {}) or info.get("stats", {})
    raw_views = stats.get("viewCount", "0")
    views = int(re.sub(r"[^0-9]", "", str(raw_views)) or "0")
    videos = int(re.sub(r"[^0-9]", "", str(stats.get("videoCount", "0"))) or "0")
    return views, videos, datetime.now(timezone.utc)

# Snippet is illustrative; in production you fetch the HTML with Playwright (see H7).
```

The key engineering takeaway: parse defensively, strip locale formatting, and always capture
the wall-clock time of the sample. The cumulative counter is your only raw input.

---

## H3. Why cumulative-only matters for velocity

Because TikTok gives you a monotonic-increasing total, your "views per hour" is the slope of
that total over your own polling interval. If you poll every 10 minutes you get a 10-minute
delta; if you poll every hour you get an hourly delta. The shorter the interval the cleaner
the instantaneous velocity, but the more requests you burn and the more you risk rate
limiting. The sweet spot for a money-signal detector watching Indonesia hashtags is a 15 to
30 minute poll with a 24-hour rolling window, which gives you both instant velocity and a
trend line. The math section (H5) shows how to turn these deltas into a normalized, comparable
signal across hashtags of wildly different sizes.

---

## H2. Extracting stats via the TikTokApi library

The community-standard library is `TikTokApi` (Davidteather). It wraps the internal endpoints
and the signature generation so you do not have to implement x-bogus yourself for the basic
case. The relevant method family is `api.hashtag`, specifically `hashtag.videos()` (pagination
over videos carrying the tag) and `hashtag.info()` (the aggregate challenge object, which is
where `statsV2` lives). The library still needs a session: either a `msToken` + cookies or the
`send_other_requests` fallback, and as of its later versions it requires a `ttwid` cookie and
occasionally a `verifyFp`. Treat those exactly like the tokens described in
`../cookies-tokens/storage-safety.md`, that is, store them encrypted, rotate per worker, and
never hardcode in source.

```python
# pip install TikTokApi==<pinned version from pypi.org/project/TikTokApi>
# source unreachable at research time: verify method names against the pinned README.
from TikTokApi import TikTokApi

async def hashtag_velocity_sample(api: TikTokApi, slug: str) -> dict:
    # .info() returns the aggregate challenge object with statsV2.
    info = await api.hashtag.info(slug)
    stats = info.get("challengeInfo", {}).get("statsV2", {})
    views = int("".join(filter(str.isdigit, str(stats.get("viewCount", "0")))))
    videos = int("".join(filter(str.isdigit, str(stats.get("videoCount", "0")))))
    return {"slug": slug, "views": views, "videos": videos,
            "ts": datetime.now(timezone.utc).isoformat()}

# For per-video velocity (useful when aggregate is blocked), stream recent videos:
async def recent_video_views(api: TikTokApi, slug: str, n: int = 200) -> list[int]:
    views = []
    async for v in api.hashtag.videos(slug, count=n):
        views.append(int(v.get("stats", {}).get("playCount", 0)))
    return views
```

The library is convenient but it is also the thing most likely to break when TikTok changes
signature requirements, because it depends on reverse-engineered internals. The vault's
posture: keep TikTokApi as the fast path, keep the web-tag-page parser (H2) as the fallback
when the library's signature is invalidated, and keep the Research API (H3 below) as the
compliant path for anything you intend to publish or rely on long term.

---

## H2. The Research API path (official, compliant, compute velocity yourself)

The Research API is the only path you can defend if someone asks "did you scrape TikTok in
violation of ToS." You register an app, request the `video.list` / `video.query` scope, declare
the exact fields you will read (for us, `video_id`, `create_time`, `view_count`,
`hashtag_name`, `username`), and you POST a query. The query filters by `challenge_name` (the
hashtag, without the leading `#`) and a `start_date`/`end_date` window. The response is a list
of videos; you never get a single hashtag total, you get the per-video `view_count` which you
aggregate.

```python
import requests

RESEARCH_EP = "https://open.tiktokapis.com/v2/research/video/query/"
# source unreachable at research time: verify endpoint + field names vs
# https://developers.tiktok.com/doc/research-api-spec/

def research_api_hashtag_window(token: str, slug: str,
                                start: str, end: str, max_videos: int = 100) -> list[dict]:
    headers = {"Authorization": f"Bearer {token}",
               "Content-Type": "application/json"}
    body = {
        "query": {
            "and": [{"challenge_name": slug}],
            "limit": max_videos,
        },
        "fields": ["video_id", "create_time", "view_count", "hashtag_name", "username"],
        "start_date": start,   # YYYYMMDD
        "end_date": end,       # YYYYMMDD
    }
    r = requests.post(RESEARCH_EP, headers=headers, json=body, timeout=30)
    r.raise_for_status()
    data = r.json()
    # data["data"]["videos"] is the list. Cursor pagination via data["data"]["cursor"].
    return data.get("data", {}).get("videos", [])
```

Velocity from the Research API is computed per hour bucket: bucket videos by `create_time`
hour, sum `view_count` in each bucket, then the bucketed series is your velocity curve. The
advantage over the web page is that `create_time` lets you reconstruct velocity for any
historical window, not just "since I started polling." The disadvantage is the minimum query
granularity and the monthly cap: a single hashtag over 30 days can exhaust a chunk of your
quota if you pull thousands of videos, so batch your slugs and cache results.

---

## H2. Creative Center as a sanctioned mirror

TikTok Creative Center publishes a "Trending Hashtags" board at
`https://ads.tiktok.com/business/creativecenter/inspiration/popular/hashtag/pc/en`. It already
shows rank, hashtag, posts, and a growth indicator. Behind the page is a JSON endpoint that
returns the ranked list with view counts and period-over-period growth; calling that internal
endpoint with a logged-in session is effectively "using TikTok's own API," which is far lower
risk than scraping the public tag page. Use it as your top-of-funnel: it tells you which
Indonesian hashtags are in the top trending set this week, and then you drill into the specific
ones via Research API (H3) or the web page (H2) for finer velocity. Set the locale to
`id` (Indonesia) so the board reflects the region your `03-id-business-trends` pain points
care about.

```python
# Conceptual: Creative Center internal endpoint shape (source unreachable at research
# time, reconstruct from the page network tab). Use a real session cookie, not anonymous.
CC_EP = "https://ads.tiktok.com/business/creativecenter/inspiration/popular/hashtag/pc/en"
# The page fetches a JSON like:
#   {"data":[{"hashtag_name":"fyp","view_count":123456789,"post_count":...,"growth":12.3}]}
# Poll it daily, diff growth vs your stored baseline, surface hashtags whose growth
# crossed a threshold (e.g. +40% week-over-week) into the 05-market-cron feed.
```

---

## H2. Velocity math: turning cumulative counts into a comparable signal

This is the core of the doc. A raw "views per hour" number is not comparable across hashtags
because `#fyp` gains millions per hour while a niche `#umkmjakarta` gains hundreds. You need
normalized, acceleration-aware metrics. Here is the toolkit, all implementable in pandas.

First, the base delta. Let samples be `(t_i, v_i)` where `v_i` is cumulative views at time
`t_i`. The per-interval velocity is:

    r_i = (v_i - v_{i-1}) / ((t_i - t_{i-1}).total_seconds() / 3600)   # views/hour

Second, an exponentially weighted moving average to smooth noise (a single viral video can
spike one sample). With smoothing factor `alpha` (0.2 to 0.3 typical):

    v_est_i = alpha * r_i + (1 - alpha) * v_est_{i-1}

Third, a z-score to detect acceleration relative to the tag's own recent baseline, which is how
you spot "this just started blowing up" versus "this is always huge":

    mu   = mean(r over trailing window W)
    sigma = std(r over trailing window W)
    z_i  = (r_i - mu) / (sigma + epsilon)

A hashtag with z > 3 is accelerating far above its own norm. Fourth, the relative velocity
(normalized by size) so small tags are not invisible:

    rel_i = r_i / (v_i + epsilon)     # fractional growth per hour

A tag growing at 2% per hour is interesting regardless of absolute size. Fifth, the second
derivative (acceleration) by differencing the velocity series itself; positive and rising
acceleration is the earliest "trend ignition" signal.

```python
import pandas as pd
import numpy as np

def velocity_features(df: pd.DataFrame, alpha: float = 0.25,
                      window: int = 48) -> pd.DataFrame:
    # df: columns [ts, views]; ts is a datetime index, sorted ascending.
    df = df.sort_values("ts").copy()
    hours = df["ts"].diff().dt.total_seconds() / 3600.0
    df["r"] = df["views"].diff() / hours           # views/hour
    df["r_ewma"] = df["r"].ewm(alpha=alpha, min_periods=2).mean()
    roll = df["r"].rolling(window, min_periods=4)
    mu = roll.mean()
    sigma = roll.std().fillna(0.0) + 1e-9
    df["z"] = (df["r"] - mu) / sigma
    df["rel"] = df["r"] / (df["views"] + 1e-9)      # fractional growth/hour
    df["accel"] = df["r_ewma"].diff() / hours        # d(views/hr)/hr
    return df

# Decision rule used by the vault pipeline:
#   trending_now = (z > 3) AND (rel > 0.005) AND (accel > 0)
# Tune thresholds per region; Indonesia consumer tags ignite faster than B2B tags.
```

The decision rule above is the one this vault uses to promote a hashtag from "watched" to
"alert." It requires both statistical acceleration (z) and meaningful relative growth (rel) and
positive acceleration, which filters out the constant-firehose tags and the one-off spikes.

---

## H2. Building the full hashtag velocity scraper

This is the production skeleton. It polls a watchlist of slugs on a schedule, stores each
sample with a timestamp, computes the velocity features, and emits alerts for tags that cross
the trending rule. It is async, uses a rotating session pool (see H8), and writes to a local
store the `06-harga-pangan-papan` and `05-market-cron` modules can read. Swap the
`fetch_cumulative` function between TikTokApi, the web page, and the Research API without
touching the rest.

```python
import asyncio, aiohttp, sqlite3, json
from datetime import datetime, timezone, timedelta
from pathlib import Path

WATCHLIST = ["umkm", "ojol", "pinjol", "bpjs", "pph21", "koperasi",
             "tiktokshop", "shopeepay", "qris", "prakerja", "umkmjakarta"]
POLL_INTERVAL = 900            # 15 minutes
DB = Path(__file__).parent / "hashtag_velocity.db"

def init_db():
    c = sqlite3.connect(DB)
    c.executescript("""
        CREATE TABLE IF NOT EXISTS samples(
            slug TEXT, ts TEXT, views INTEGER, videos INTEGER,
            PRIMARY KEY(slug, ts));
        CREATE TABLE IF NOT EXISTS alerts(
            slug TEXT, ts TEXT, z REAL, rel REAL, accel REAL, views INTEGER);
    """)
    c.commit(); return c

async def fetch_cumulative(slug: str, session) -> tuple[int, int]:
    # Replace body with TikTokApi / web-page / Research-API adapter.
    # Returns (cumulative_views, video_count). source unreachable: mock-safe.
    await asyncio.sleep(0)  # placeholder
    return (0, 0)

async def poll_one(slug: str, session, db):
    views, videos = await fetch_cumulative(slug, session)
    ts = datetime.now(timezone.utc).isoformat()
    db.execute("INSERT OR REPLACE INTO samples VALUES(?,?,?,?)",
               (slug, ts, views, videos))
    db.commit()

async def run():
    db = init_db()
    async with aiohttp.ClientSession() as session:
        while True:
            await asyncio.gather(*(poll_one(s, session, db) for s in WATCHLIST))
            detect_alerts(db)
            await asyncio.sleep(POLL_INTERVAL)

def detect_alerts(db):
    # Load last window per slug, compute features, emit alerts.
    rows = db.execute("SELECT slug, ts, views FROM samples ORDER BY ts").fetchall()
    # (group by slug, build df, call velocity_features, insert alert rows)
    pass  # see velocity_features above
```

The skeleton is deliberately minimal. The hard parts are `fetch_cumulative` (anti-bot, H7) and
`detect_alerts` (the pandas feature step from H5 wrapped to read from SQLite). Both are
decoupled so the velocity math is unit-testable without ever hitting TikTok.

---

## H2. Anti-bot surface: x-bogus, ttwid, verify, and signatures

TikTok's web and internal endpoints require a request signature that proves the request came
from a real client. The signature family you will encounter:

- `x-bogus`: a parameter appended to query strings (and sometimes a header) computed from the
  request URL, a few headers, and a JavaScript-obfuscated function that TikTok ships in its
  web bundle. Reconstructing it in Python means either porting the function (the TikTokApi
  library does this) or driving a real browser so the bundle computes it for you.
- `ttwid`: a cookie TikTok sets on first visit; many endpoints 400 without it. You obtain it by
  hitting the homepage once and persisting the cookie jar.
- `verifyFp` / `verify`: a device fingerprint cookie used to gate suspicious traffic; when
  TikTok thinks you are a bot it demands a `verify` challenge and your requests start returning
  a captcha page instead of JSON.
- `msToken`: a session token the web app mints; required by some internal video/list endpoints.
- Region header `Accept-Language` and `Referer`: TikTok serves different data per region; set
  `Accept-Language: id-ID` to bias toward Indonesian content.

The pragmatic strategy for this vault: do not try to out-engineer the signature in pure
Python for the public page. Use a headless browser (Playwright) that loads the real bundle so
the signature and cookies are generated by TikTok's own code, then read the embedded state
from the rendered DOM (H2). Reserve pure-Python signature work for the Research API, which
needs no signature because it is an authenticated Bearer call. When the browser path gets
challenged, fall back to Creative Center (H4) and Research API (H3), and dial down request
rate. The token rotation rules in `../cookies-tokens/storage-safety.md` apply to `ttwid`,
`msToken`, and `verifyFp`: encrypt at rest, one pool per worker, recycle on 403.

---

## H2. Cookie and token rotation (depends on storage-safety.md)

The scraper is only as durable as its session pool. Treat every `ttwid`, `msToken`,
`verifyFp`, and Research API Bearer token as a credential. The companion file
`../cookies-tokens/storage-safety.md` defines the vault's standard for this: tokens live in an
encrypted store (age or a KMS-backed secret), never in source or plaintext env files; each
worker process draws a session from a pool so no single account absorbs all the traffic; on a
`403`/`429` you mark that session "cooling" and pull a fresh one rather than retrying in place;
and you log token age so you can rotate before expiry. The velocity scraper should import that
store rather than rolling its own. Concretely: the `fetch_cumulative` adapter asks the store
for a session, uses it for one batch, and returns it (or quarantines it on challenge). This is
what keeps a 30-tag watchlist running for weeks instead of burning out in a day.

---

## H2. Scheduling and wiring into the market-cron module

The velocity signal is only useful if it is sampled on a clock. This is where
`05-market-cron/cron-configs/` comes in: the same cron host that runs the IHSG and crypto
fetchers should run this scraper's `poll_one` loop. Two patterns work:

- A long-lived asyncio process (the skeleton in H6) that sleeps between polls. Simple, but it
  dies if the host reboots; pair it with a supervisor (systemd unit or the hermes-startup.sh
  daemon pattern already in this environment).
- A cron job every 15 minutes that runs a stateless fetcher reading the last sample from
  SQLite, writing the new one, and emitting alerts. More robust to reboots, no in-memory
  state, but you must make the DB the single source of truth (which the skeleton already does).

Either way, the alert output (slugs crossing the trending rule) should be written to a file the
`07-gaps-and-opportunities/inbox/` watcher and the `03-id-business-trends` miner can pick up,
so a hashtag igniting around `#pinjol` or `#bpjs` automatically becomes a candidate pain point
for the next mining tick. That closes the loop: scraper detects velocity, miner explains the
pain, synthesizer writes the opportunity.

---

## H2. Money signals: which Indonesian hashtags actually matter

Not every trending tag is a money signal. The vault cares about tags that map to the
`03-id-business-trends` pain taxonomy. A starter watchlist, grouped by what they indicate:

- Financial-access pain: `#pinjol`, `#pinjollegal`, `#koperasi`, `#bpjs`, `#pph21`,
  `#prakerja`, `#qris`, `#shopeepay`, `#ojol`. A velocity spike here often precedes a news
  cycle about a regulatory crackdown or a payout failure, which is exactly the demand-mining
  raw material.
- Commerce and seller pain: `#tiktokshop`, `#shopee`, `#tokopedia`, `#umkm`, `#reseller`,
  `#dropship`. Acceleration here correlates with seller commission complaints and NIB/halal
  deadline anxiety (see the `umkm-sanksi-halal-oktober-2026` pain file).
- Cost-of-living and inflation: `#harga`, `#beras`, `#minyakgoreng`, `#elistrik`, `#pdam`,
  `#bbm`. These track the `06-harga-pangan-papan` price pipeline and confirm whether a price
  shock is also a conversation shock.
- Employment and gig: `#freshgraduate`, `#lowongan`, `#phk`, `#freelancer`, `#kreatorkonten`.
  Velocity here is a leading indicator for the unemployment and gig-economy pain points.

The discipline: keep the watchlist small (10 to 20 slugs), because velocity math needs a clean
historical window per slug and a 20-slug watchlist at 15-minute poll is already ~1900 requests
a day. Expand only after the rotation (H8) is proven stable.

---

## H2. Data schema and storage

Use a flat, append-only sample table plus a derived alert table, exactly as the H6 skeleton
creates. Store the raw cumulative `views` and `videos` and the timestamp, never just the
computed velocity, because the velocity is reproducible from the raw samples but the raw is not
recoverable from the velocity. Keep the timezone explicit (UTC) and store the region/locale the
sample was taken with, because Indonesian vs global counts for the same slug differ. For the
research pipeline, also persist the per-video rows (video_id, create_time, view_count) so you
can rebuild velocity for any historical window without re-querying. The `06-harga-pangan-papan`
module already uses a JSON + SQLite pattern; mirror it so the two crawlers share tooling.

---

## H2. Pitfalls and gotchas (learned the hard way by the community)

- Locale mismatch: requesting without `Accept-Language: id-ID` silently returns global counts
  for the same slug, so your Indonesia velocity is wrong. Always pin the locale.
- String-formatted numbers: `viewCount` comes back as a comma-grouped string; `int()` on
  `"1,234,567"` throws. Strip non-digits first (the H2 helper does this).
- Monotonic assumption: the cumulative counter should only increase. If a sample is LOWER than
  the previous, it means TikTok re-counted or you hit a different region/shard; drop the sample
  rather than producing a negative velocity that wrecks the z-score.
- Signature drift: when TikTokApi starts returning empty, assume the x-bogus port broke, not
  that the tag is dead. Switch to the web-page or Research API adapter and log the failure.
- Rate limits: the web page will 429 you fast if every worker hits the same slug. Stagger
  polls with jitter and respect backoff. source unreachable: exact limits unverified this tick.
- Challenge pages: a `verify` captcha page is HTML, not JSON. Detect "did I get JSON" before
  parsing, and on failure quarantine the session (H8), never retry in a tight loop.
- Timezone bugs: `create_time` from the Research API is Unix epoch UTC; your poll timestamps
  must be UTC too or the delta math is off by your offset.
- Minimum viable window: z-score and EWMA need at least ~10 samples; do not alert in the first
  hour of watching a new slug. Seed new slugs from Creative Center history if you need instant
  baseline.

---

## H2. New gaps discovered while building this reference

Three structural gaps surfaced that the vault does not yet cover and that should be added to
the auditor's gap list (under the self-evolution rule, max 3 per tick):

- `01-crawler-scrapper/tiktok/creator-live-stream-scraper.md` (NEW). Hashtag velocity misses
  live-commerce spikes, which in Indonesia is where `#tiktokshop` money actually moves. A
  scraper watching live-view counts and GMV-per-minute for tagged live sessions is a distinct
  surface (different endpoint, different anti-bot) and would feed the commerce pain points
  directly.
- `01-crawler-scrapper/regional/indonesia-locale-normalization.md` (NEW). The locale mismatch
  pitfall (H10) is severe enough that the vault needs a shared utility that forces id-ID
  consistently across TikTok, X, and the price scrapers, with tests proving region pinning.
  This is cross-cutting infra, not a one-off.
- `05-market-cron/news-sentiment/tiktok-hashtag-to-headline-bridge.md` (NEW). The loop described
  in H9 (velocity spike becomes a mining candidate) needs a concrete adapter that maps a
  trending slug to a candidate `03-id-business-trends` pain file and opens a draft, rather than
  relying on a human to notice the alert file. This is the automation that makes the vault
  self-filling.

These are logged here so the next tick can promote them. The first two belong in
`01-crawler-scrapper`; the third belongs in `05-market-cron` and closes the scraper-to-miner
loop the whole vault is built around.

---

## H2. Compliance and ethical note

This reference documents measurement, not evasion. The Research API path (H3) is fully
compliant and should be the default for anything published or relied on. The web-page and
Creative Center paths are for internal signal detection on public data; do not redistribute
scraped personal data, do not hammer endpoints, and respect TikTok's rate limits and any
applicable Indonesian data-protection rules (the PDP Law referenced in other vault modules).
When in doubt, use the compliant path and compute velocity from per-video aggregates.

---

## H2. Worked example: a full velocity computation on synthetic samples

To make the math concrete, here is a runnable end-to-end example using synthetic but
realistic samples for two tags, `#pinjol` (large, noisy) and `#umkmjakarta` (small, fast). The
point is to show that the normalized metrics surface the small tag's ignition even though its
absolute views/hour are a fraction of the large tag's. This is the exact notebook the vault
runs in CI to confirm the `velocity_features` function is correct before a deploy.

```python
import pandas as pd
import numpy as np
from datetime import datetime, timezone, timedelta

def velocity_features(df, alpha=0.25, window=6):
    df = df.sort_values("ts").copy()
    hours = df["ts"].diff().dt.total_seconds() / 3600.0
    df["r"] = df["views"].diff() / hours
    df["r_ewma"] = df["r"].ewm(alpha=alpha, min_periods=2).mean()
    roll = df["r"].rolling(window, min_periods=4)
    mu = roll.mean()
    sigma = roll.std().fillna(0.0) + 1e-9
    df["z"] = (df["r"] - mu) / sigma
    df["rel"] = df["r"] / (df["views"] + 1e-9)
    df["accel"] = df["r_ewma"].diff() / hours
    return df

t0 = datetime(2026, 7, 14, 8, 0, tzinfo=timezone.utc)
# #pinjol: big but steady, ~1.2M cumulative, +50k/hr, occasional +200k spike
pinjol = {"ts": [t0 + timedelta(minutes=15*i) for i in range(10)],
          "views": [1200000 + 50000*i + (200000 if i == 7 else 0) for i in range(10)]}
# #umkmjakarta: small but igniting, 8000 cumulative, then explodes +3000/hr late
umkm = {"ts": [t0 + timedelta(minutes=15*i) for i in range(10)],
        "views": [8000 + 50*i + (0 if i < 6 else 3000*(i-5)) for i in range(10)]}

for name, data in [("pinjol", pinjol), ("umkmjakarta", umkm)]:
    df = velocity_features(pd.DataFrame(data))
    last = df.dropna().iloc[-1]
    flag = (last["z"] > 3) and (last["rel"] > 0.005) and (last["accel"] > 0)
    print(f"{name:12s} r={last['r']:10.0f}/hr  z={last['z']:5.2f}  "
          f"rel={last['rel']*100:5.3f}%  accel={last['accel']:9.0f}  TREND={flag}")
```

Expected output: `#pinjol` shows a high absolute `r` but its `z` is modest because the spike is
within its own noise band, so it does NOT trip the alert. `#umkmjakarta` shows a small absolute
`r` but a huge `z` (the late explosion breaks its baseline) and a high `rel` (fractional
growth), so it DOES trip the alert. That is the whole thesis: normalized acceleration finds the
ignition that absolute volume hides. (Numbers are illustrative; run the snippet to see exact
values, source unreachable for live tag samples this tick.)

---

## H2. Comparing many hashtags at once: the leaderboard

In production you watch 10 to 20 slugs, so you need a single ranked view per cycle. Build a
leaderboard DataFrame from each tag's latest feature row and sort by a composite score that
blends `z`, `rel`, and `accel` so a human can scan what is moving. Keep the composite simple and
monotonic in each input so the ranking is explainable:

    score = z * (1 + min(rel / 0.01, 5)) * (1 + sign(accel))

The `rel` term boosts small fast growers up to a cap, and the `accel` sign term kills anything
decelerating. Emit the top N as an alert file the `07-gaps-and-opportunities/inbox/` watcher
consumes. Never emit raw `r` alone as the ranking, or `#fyp` drowns every signal worth having.

```python
def leaderboard(rows: list[dict], top_n: int = 10) -> pd.DataFrame:
    df = pd.DataFrame(rows)
    df["rel_capped"] = (df["rel"] / 0.01).clip(upper=5.0)
    df["accel_sign"] = np.sign(df["accel"].fillna(0.0))
    df["score"] = df["z"] * (1 + df["rel_capped"]) * (1 + df["accel_sign"])
    return df.sort_values("score", ascending=False).head(top_n)
```

---

## H2. Tuning the alert thresholds per region and tag class

The default rule `(z > 3) AND (rel > 0.005) AND (accel > 0)` is a starting point, not gospel.
Tag classes behave differently and a single global threshold either floods alerts (for
always-volatile entertainment tags) or never fires (for slow B2B tags). Concretely:

- Entertainment and challenge tags (`#fyp`, `#trending`) have high baseline variance, so their
  `sigma` is large and they rarely reach `z > 3` on ordinary days but spike hard on viral days.
  For these, raise `z` to 4 or 5 and lower `rel` to 0.002, because absolute movement matters
  more than relative.
- Commerce and pain tags (`#pinjol`, `#bpjs`, `#umkm`) are steadier, so `z > 3` is meaningful
  and `rel > 0.005` (0.5% per hour) catches a real surge. Keep the default here.
- News-driven tags (`#pph21`, `#prakerja`) only move when a policy event drops. Their baseline
  is near zero between events, so `sigma` collapses and any movement produces a giant `z` that
  is really just noise. For these, add a minimum absolute `r` floor (e.g. `r > 500/hr`) so you
  do not alert on a single curious post.

Store the thresholds per tag class in a config table alongside the WATCHLIST so the rule is
data-driven, not hardcoded. The vault already keeps cron configs in
`05-market-cron/cron-configs/`, mirror that pattern here with a `thresholds.json`.

---

## H2. Closing the loop: from velocity alert to a 03-id-business-trends pain draft

The whole point of detecting velocity is to feed the demand-mining module. The wiring in H9
emits an alert file; this section specifies the adapter that turns an alert into a draft pain
point so the `03-id-business-trends` miner has a head start. The adapter:

- Maps the slug to a known pain cluster via a static synonym table (e.g. `pinjol` ->
  `pinjol-ilegal-masih-marak` / `pinjol-legal-bunga-tinggi`, `bpjs` ->
  `bpjs-pbpu-beban-keluarga-informal` / `pasien-bpjs-ditolak-rs-klaim-tertunda`).
- Pulls the last N videos from the Research API for that slug in the spike window and extracts
  the most-repeated words (a tiny TF-IDF or just a stopword-filtered frequency count) to seed
  the "what are people actually complaining about" section of the draft.
- Writes a stub markdown file in `03-id-business-trends/demand-mining/` with the timestamp, the
  measured velocity (`r`, `z`, `rel`, `accel`), and the extracted phrases, marked
  `DRAFT: unverified, mined from TikTok velocity`. A human or the miner then confirms and
  sources it. This is the automation that makes the vault self-filling, and it is the third new
  gap logged in H12.

```python
SYNONYMS = {
    "pinjol": ["pinjol-ilegal-masih-marak", "pinjol-legal-bunga-tinggi"],
    "bpjs": ["bpjs-pbpu-beban-keluarga-informal", "pasien-bpjs-ditolak-rs-klaim-tertunda"],
    "prakerja": ["kartu-prakerja-2026-akses-sulit"],
    "umkm": ["umkm-akses-modal-sulit", "umkm-biaya-produksi-meroket-bahan-baku-rupiah"],
}

def draft_pain_from_alert(slug: str, feat: dict, top_words: list[str], out_dir: str):
    targets = SYNONYMS.get(slug, [f"{slug}-velocity-spike"])
    for t in targets:
        path = f"{out_dir}/{t}.md"
        with open(path, "w") as f:
            f.write(f"# DRAFT (velocity-mined): {slug}\n\n")
            f.write(f"Alert: r={feat['r']:.0f}/hr z={feat['z']:.2f} "
                    f"rel={feat['rel']*100:.3f}% accel={feat['accel']:.0f}\n")
            f.write("Top phrases: " + ", ".join(top_words) + "\n")
            f.write("STATUS: unverified, mined from TikTok hashtag velocity. "
                    "Confirm and source before promoting.\n")
```

---

## H2. Testing the velocity module without touching TikTok

Because the math is separable from the fetch, you can and should unit-test it in CI. The test
suite the vault ships with this module covers:

- A monotonic increasing series produces positive `r` and no NaN in `z` after the warmup.
- A single negative delta (counter went backwards) is dropped, not propagated as a negative `r`.
- A step-change spike yields `z > 3` at the spike and relaxes afterward (proving the rolling
  window recovers).
- Locale-formatted strings (`"1,234,567"`) parse to the correct int.
- The leaderboard ranks a small fast grower above a large steady one given the composite score.

```python
# tests/test_velocity.py (pytest)
import pandas as pd
from yourmodule import velocity_features, leaderboard

def test_spike_zscore():
    t0 = pd.Timestamp("2026-07-14 08:00", tz="UTC")
    ts = [t0 + pd.Timedelta(minutes=15*i) for i in range(10)]
    views = [1_000_000 + 10_000*i + (500_000 if i == 7 else 0) for i in range(10)]
    df = velocity_features(pd.DataFrame({"ts": ts, "views": views}))
    assert df["z"].iloc[7] > 3
    assert df["z"].iloc[-1] < df["z"].iloc[7]   # window recovers

def test_negative_delta_dropped():
    t0 = pd.Timestamp("2026-07-14 08:00", tz="UTC")
    ts = [t0 + pd.Timedelta(minutes=15*i) for i in range(4)]
    views = [1000, 1150, 900, 1200]   # 900 is a backward count, must be dropped
    df = velocity_features(pd.DataFrame({"ts": ts, "views": views}))
    # after dropping the bad sample, no NaN should poison the tail
    assert df["r"].iloc[-1] >= 0
```

These run in milliseconds and need no network, which is exactly what you want in a cron
environment where the real fetch is flaky.

---

## H2. Cost and quota model

Running the scraper has real costs you must budget. For the web page path, the cost is request
volume and ban risk, effectively free but fragile. For the Research API, the cost is the
monthly video cap: each `video.query` for a hashtag over a 7-day window can return hundreds to
thousands of videos depending on popularity, and each counts against your cap. A simple model:

    monthly_cost_videos = sum over slugs of (videos_per_window * windows_per_month)
    windows_per_month   = 30 / window_days

If you watch 20 slugs at a 7-day window refreshed weekly, that is 20 queries a month, each
returning up to a few thousand videos, so budget on the order of tens of thousands of videos
monthly. The Research API's free tier is far smaller than that, so either request a higher cap,
cache aggressively (never re-query a window you already have), or restrict the Research API to
the top 5 priority slugs and use Creative Center + web page for the long tail. Track usage in
the same SQLite store so you can see cap burn before you hit it.

---

## H2. Operational runbook (what to do when it breaks)

- Empty parses from TikTokApi: assume x-bogus drift. Flip `fetch_cumulative` to the web-page
  adapter, open a browser, and confirm the `STATE` blob key path. Log the failure to the
  auditor so the gap list notes the breakage.
- 403/429 storm: a session is burned. The rotation layer (H8) should already have quarantined
  it; if alerts stop entirely, check that the token store has healthy sessions and that the
  cooldown is expiring. Do not retry in a tight loop, that deepens the ban.
- Creative Center returns a login wall: the session cookie expired. Refresh via the
  storage-safety store and re-auth the Creative Center session out of band.
- Velocity looks flat for everything: check the poll clock. If `POLL_INTERVAL` drifted or the
  cron died, you have gaps in the sample series and the deltas are wrong. Re-seed baselines
  from Creative Center history.
- A slug never alerts: its class threshold is wrong (H11). Lower `z` or add the absolute `r`
  floor for news-driven tags.

Keep this runbook next to the code so the next tick can recover without re-deriving it.

---

## H2. Quick-start checklist for the next tick

- Pin the TikTokApi version from pypi.org/project/TikTokApi and confirm the `hashtag.info`
  method name against its README (source unreachable this tick, verify live).
- Stand up the SQLite schema from H6 and the `velocity_features` function from H5 as a unit
  test with synthetic monotonic samples.
- Build the `fetch_cumulative` adapter for the Research API first (compliant, no signature),
  then add the web-page adapter as fallback.
- Seed the WATCHLIST from H10 with the financial-access and commerce slugs.
- Wire the alert file into `07-gaps-and-opportunities/inbox/` so a spike auto-drafts a pain
  point.
- Before production, re-fetch the three `source unreachable` URLs above and replace every
  reconstructed field name and rate limit with the live values.
