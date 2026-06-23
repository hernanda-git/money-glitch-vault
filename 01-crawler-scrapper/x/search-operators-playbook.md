# X / Twitter Search Operators Playbook

A deeply technical reference for mining money-relevant signals from X (formerly Twitter) using advanced search operators, API queries, and automated scraping pipelines. Targeted at the Indonesian market (IDX stocks, UMKM chatter, crypto trends, freelancer signals, consumer complaints).

## Table of Contents

- [Why X for Signal Mining?](#why-x-for-signal-mining)
- [Search Surface: Web vs API](#search-surface-web-vs-api)
- [Complete Operator Reference](#complete-operator-reference)
- [Boolean Logic & Query Construction](#boolean-logic--query-construction)
- [Query Length Limits & Availability](#query-length-limits--availability)
- [Indonesian Signal Patterns](#indonesian-signal-patterns)
- [Code: API Scrapers (Python)](#code-api-scrapers-python)
- [Code: Web Scrapers (Playwright)](#code-web-scrapers-playwright)
- [Signal Processing Pipeline](#signal-processing-pipeline)
- [Anti-Detection, Ethics & Legal (Indonesia)](#anti-detection-ethics--legal-indonesia)
- [Ready-to-Use Query Templates](#ready-to-use-query-templates)
- [References & Further Reading](#references--further-reading)

---

## Why X for Signal Mining?

X remains the highest-density real-time public signal source for the Indonesian market despite the rise of TikTok and Instagram. Here is why it matters for this vault:

| Signal Type | Why X Wins | Example Use Case |
|---|---|---|
| UMKM / Business complaints | Indonesian netizens vent about platform fees, blocked accounts, payment delays in real time | Track `fee tokopedia mahal` or `shopee blokir` sentiment |
| Crypto / NFT hype | X is the primary Indonesian crypto discussion hub (not Telegram, not Discord) | Detect `$BTC breakout` or `airdrop indo` trending |
| Stock market chatter | IDX retail investors discuss gorengan stocks, IHSG predictions | Monitor `BBCA goreng` or `IHSG bangkrut` panic |
| Freelancer / job signals | Fastwork, Sribu, Upwork links shared alongside payment complaints | Find `client kabur` or `freelance dibayar` |
| Consumer price complaints | Real-time price shock reactions (harga pangan, BBM, token listrik) | Track `cabai merah mahal` or `pertamax naik` spikes |
| Policy / regulation reaction | New Peraturan, PPN 12%, UU Cipta Kerja, QRIS issues | Catch `PPN 12%` trending before mainstream media |
| Competitor / brand monitoring | Public feedback about Gojek, Grab, Tokopedia, Shopee | Detect `Gojek error` or `Tokopedia scam` clusters |

Data from the X API is also structured (JSON with user profiles, engagement metrics, media, URLs, hashtags, mentions), making it far easier to process than unstructured web scraping from TikTok or Instagram.

---

## Search Surface: Web vs API

There are two fundamentally different ways to search X. Understanding the difference is critical.

### Web Search (x.com/search)

The public web search at `https://x.com/search-advanced` (or `https://x.com/search?q=<query>`) uses X's internal search stack. It has these characteristics:

- **Free, no API key needed** for manual/automated browser search.
- **Rich operator set** that is similar but not identical to the API operator set. Some operators work only on the web UI (e.g., `filter:`, `?`, advanced date pickers).
- **CAPTCHA & rate limits** after ~50 requests in a short window.
- **HTML output** varies; content is loaded via JavaScript. Requires Playwright/Puppeteer to render.
- **No structured data**; you must parse the DOM.
- **Useful for:** one-off investigations, manual research, small-scale scraping.

### API Search (api.twitter.com/2/tweets/search)

The official X API v2 provides two search endpoints:

| Endpoint | Description | Lookback | Cost |
|---|---|---|---|
| `/2/tweets/search/recent` | Recent search, last 7 days | 7 days | 100 req / 15 min (Essential) |
| `/2/tweets/search/all` | Full-archive search (Academic only) | Full history | 300 req / 15 min (Academic) |

- **Requires Developer Portal account** and a Project with Bearer Token or OAuth 2.0.
- **Structured JSON** response with tweet objects, user objects, media, context annotations.
- **Pay-per-use pricing** as of 2025-2026. Recent search costs $0.01 per 100 results via the pay-per-use model.
- **512 char query limit** (Essential/Elevated) or **1024 chars** (Academic Research).
- **Useful for:** production pipelines, automated crawling, bulk analysis.

### Hybrid Approach

The most effective setup for this vault uses both:

1. **API (recent search)** for routine daily signal collection on known keywords.
2. **Web scraping (Playwright)** for real-time monitoring of trending topics and advanced search UI features that the API does not expose (like `filter:verified`, date range picker in one query).

---

## Complete Operator Reference

This table covers all operators available in **X API v2 recent search** (Essential access level unless noted). The web UI supports a superset but is less documented.

### Keyword & Text Operators

| Operator | Type | Availability | Description | Example |
|---|---|---|---|---|
| `keyword` | Standalone | Essential | Tokenized match on the body of a Tweet. Tokens are split on punctuation, symbols, Unicode separators. Use double-quotes for phrases containing punctuation. | `pepsi OR cola` or `"coca cola"` |
| `"exact phrase"` | Standalone | Essential | Matches the exact phrase within the body. | `"Twitter API" -"recent search"` |
| `#hashtag` | Standalone | Essential | Exact match on a recognized hashtag entity. NOT a tokenized match, meaning `#thanku` will NOT match `#thankunext`. | `#thankunext #fanart` |
| `$cashtag` | Standalone | Elevated | Matches a cashtag symbol like `$TWTR`. Relies on entity extraction, not body text. | `$BBRI OR $BMRI` |
| `emoji` | Standalone | Essential | Matches an emoji in the body. Tokenized match. Wrap variants in double quotes. | `(😃 OR 😡) 😬` |

### User Operators

| Operator | Type | Availability | Description | Example |
|---|---|---|---|---|
| `@username` | Standalone | Essential | Matches a recognized mention entity (including the @). | `@twitterdev OR @twitterapi` |
| `from:` | Standalone | Essential | Matches tweets FROM a specific user. Use username (no @) or numeric user ID. Single user per operator. | `from:twitterdev` |
| `to:` | Standalone | Essential | Matches tweets IN REPLY to a specific user. Single user per operator. | `to:twitterdev` |
| `retweets_of:` | Standalone | Essential | Matches retweets of a specific user. Single user per operator. | `retweets_of:twitterdev` |
| `list:` | Standalone | Elevated | Matches tweets from members of a specific list (by List ID). Single list per operator. | `list:123456789` |

### Engagement / Content-Type Operators

| Operator | Type | Availability | Description | Example |
|---|---|---|---|---|
| `is:retweet` | Conjunction-required | Essential | Matches true Retweets (not Quote Tweets). | `data @twitterdev -is:retweet` |
| `is:reply` | Conjunction-required | Essential | Matches explicit replies. | `from:twitterdev is:reply` |
| `is:quote` | Conjunction-required | Essential | Returns Quote Tweets (Tweets with comments). | `"sentiment analysis" is:quote` |
| `is:verified` | Conjunction-required | Essential | Only tweets from verified authors. | `#nowplaying is:verified` |
| `-is:nullcast` | Conjunction-required | Elevated | Excludes ads-only tweets (must be negated). | `"mobile games" -is:nullcast` |

### Media & Link Operators

| Operator | Type | Availability | Description | Example |
|---|---|---|---|---|
| `has:hashtags` | Conjunction-required | Essential | Tweet contains at least one hashtag. | `from:twitterdev -has:hashtags` |
| `has:cashtags` | Conjunction-required | Elevated | Tweet contains a cashtag ($ symbol). | `#stonks has:cashtags` |
| `has:links` | Conjunction-required | Essential | Tweet contains links or media in the body. | `announcement has:links` |
| `has:mentions` | Conjunction-required | Essential | Tweet mentions another user. | `#nowplaying has:mentions` |
| `has:media` | Conjunction-required | Essential | Tweet contains a media object (photo, GIF, video). Not Periscope. | `(kittens OR puppies) has:media` |
| `has:images` | Conjunction-required | Essential | Tweet contains a recognized URL to an image. | `#meme has:images` |
| `has:video_link` | Conjunction-required | Essential | Tweet contains a native Twitter video. Not Periscope or external links. | `#icebucketchallenge has:video_link` |
| `has:geo` | Conjunction-required | Elevated | Tweet has specific geolocation data. | `recommend #paris has:geo` |
| `url:` | Standalone | Essential | Tokenized match on validly formatted URLs (matches both `url` and `expanded_url` fields). | `url:"https://developer.twitter.com"` |

### Temporal Operators

There is no dedicated `since:` or `until:` operator in API v2 query syntax. Instead, these are **parameters** passed with the request:

- `start_time` (ISO 8601: `2026-06-01T00:00:00Z`)
- `end_time` (ISO 8601)
- `max_results` (10-100 default, max 100 for recent search)

In the **web UI**, you can use the date picker in Advanced Search, or manually append to the URL:
- `since:2026-06-01` and `until:2026-06-23` work on the web search UI.

### Language Operator

| Operator | Type | Availability | Description | Example |
|---|---|---|---|---|
| `lang:` | Conjunction-required | Essential | Matches tweets classified as a specific language (BCP 47 code). Single lang per operator. | `lang:id` (Indonesian) or `lang:en` |

Indonesian BCP 47 codes: `id` (Indonesian), `en` (English), `jv` (Javanese), `su` (Sundanese). Most Indonesian tweets are classified as `lang:id`.

### Geo Operators

| Operator | Type | Availability | Description | Example |
|---|---|---|---|---|
| `place:` | Standalone | Elevated | Matches tweets at a specific place name or Twitter Place ID. Multi-word names need quotes. | `place:"new york city"` |
| `place_country:` | Standalone | Elevated | Matches tweets from a country by ISO alpha-2 code. Single code per operator. | `place_country:ID` |
| `point_radius:` | Standalone | Elevated | Matches tweets within [longitude latitude radius] radius in mi or km, max 25mi. | `point_radius:[106.8 -6.2 10km]` (Jakarta) |
| `bounding_box:` | Standalone | Elevated | Matches tweets within a bounding box [west_long south_lat east_long north_lat], max 25mi wide/tall. | `bounding_box:[106.6 -6.4 107.0 -6.0]` (Greater Jakarta) |

### Annotation / Context Operators

| Operator | Type | Availability | Description | Example |
|---|---|---|---|---|
| `context:` | Standalone | Essential | Matches a specific domain_id.entity_id pair (Twitter's content categorization). | `context:65.852262932607926273` (Pets domain) |
| `entity:` | Standalone | Essential | Matches a specific entity string value (person, place, etc.). Recent search only. | `entity:"Barcelona"` |
| `conversation_id:` | Standalone | Essential | Matches tweets sharing a common conversation ID. | `conversation_id:1334987486343299072` |
| `in_reply_to_tweet_id:` | Standalone | Essential | Matches replies to a specific Tweet ID. Also aliased as `in_reply_to_status_id:`. | `in_reply_to_tweet_id:1539382664746020864` |
| `retweets_of_tweet_id:` | Standalone | Essential | Matches native retweets of a specific original Tweet ID. | `retweets_of_tweet_id:1539382664746020864` |
| `quotes_of_tweet_id:` | Standalone | Essential | Matches Quote Tweets of a specific Tweet ID. | `quotes_of_tweet_id:1539382664746020864` |

---

## Boolean Logic & Query Construction

### AND Logic (implicit)

Separate operators with a space to require ALL conditions:

```
snow day #NoSchool
```
matches tweets containing BOTH `snow` AND `day` AND `#NoSchool`.

### OR Logic

Use `OR` (uppercase) between operators to require AT LEAST ONE condition:

```
grumpy OR cat OR #meme
```

### NOT Logic (negation)

Prepend a dash (`-`) to negate any operator:

```
cat #meme -grumpy
```
matches tweets with `cat` AND `#meme` but NOT `grumpy`.

The most common negations:
- `-is:retweet` (exclude retweets, keep original tweets + quote tweets + replies)
- `-is:reply` (exclude replies)
- `-is:nullcast` (exclude ad-only tweets, must be negated)
- `-filter:verified` (web UI, exclude verified users)
- `-has:links` (exclude tweets with links)

### Grouping

Use parentheses to group operators. ORs distribute over ANDs:

```
(grumpy cat) OR (#meme has:images)
```
returns tweets matching BOTH `grumpy` AND `cat`, OR tweets with BOTH `#meme` AND `has:images`.

### Order of Operations

1. ANDs are applied first.
2. ORs are applied second.

```
apple OR iphone ipad
```
evaluates as `apple OR (iphone ipad)`.

```
(apple OR iphone) ipad
```
evaluates as `(apple OR iphone) AND ipad`.

### Punctuation, Diacritics & Case Sensitivity

- All operators are **case-insensitive**: `cat` matches `CAT`, `Cat`, `cat`.
- Characters with diacritics (accents) match BOTH accented and unaccented forms: `cumpleaños` matches both `cumpleaños` and `cumpleanos`.
- This is critical for Indonesian: `shalat` will match `shalat`, `sholat`, and `shalat`.
- Punctuation tokens matter: `coca-cola` as a keyword will only match exact `coca-cola`. Use `"coca-cola"` (quoted) to match the phrase.

---

## Query Length Limits & Availability

| Access Level | Max Query Length | Operators Available |
|---|---|---|
| Essential (Free) | 512 characters | Core operators only |
| Elevated (Paid) | 512 characters | Core + some advanced |
| Academic Research | 1024 characters | All operators including advanced |

The character count includes ALL characters in the query: spaces, operators, punctuation, and the text itself.

**Tip:** Use acronyms and short keywords to stay under the limit. For Indonesian context, `UMKM` is better than `usaha mikro kecil menengah`. A single keyword like `happy` returns 200,000-300,000 tweets per day, so specificity is important for both signal quality and character budget.

---

## Indonesian Signal Patterns

This section provides battle-tested query patterns for mining Indonesian money-relevant signals. Each pattern includes both the API query and the equivalent web search URL.

### Pattern 1: UMKM Platform Fee Complaints

Track when sellers complain about Tokopedia, Shopee, or TikTok Shop fees:

```
(tokopedia OR shopee OR "tiktok shop") (fee OR komisi OR potongan OR mahal OR biaya) lang:id -is:retweet
```

Web URL:
```
https://x.com/search?q=(tokopedia%20OR%20shopee%20OR%20%22tiktok%20shop%22)%20(fee%20OR%20komisi%20OR%20potongan%20OR%20mahal%20OR%20biaya)%20lang%3Aid%20-is%3Aretweet&src=typed_query&f=live
```

### Pattern 2: Crypto / Airdrop Hype Detection

```
($BTC OR $ETH OR $SOL OR airdrop OR "token kripto") (rug OR pump OR dump OR "gas fee" OR listing) lang:id -is:retweet has:links
```

### Pattern 3: IDX Stock Chatter (Gorengan Stocks)

Monitor stocks frequently discussed by Indonesian retail investors:

```
(BBCA OR BBRI OR BMRI OR TLKM OR ASII OR GOTO) (goreng OR "harga turun" OR "naik" OR "cuan" OR rugi) lang:id -is:retweet
```

### Pattern 4: Freelancer Payment Problems

```
(freelance OR freelancer) (dibayar OR "gagal bayar" OR kabur OR wanprestasi OR "tidak dibayar") lang:id -is:retweet
```

### Pattern 5: Consumer Price Shocks

```
("cabai" OR "bawang" OR "minyak goreng" OR "beras" OR "telur") ("mahal" OR "naik" OR "melonjak" OR "inflasi") lang:id -is:retweet has:media
```

### Pattern 6: Gojek / Grab Service Complaints

```
(gojek OR grab) (tarif OR "driver batalkan" OR "aplikasi error" OR mahal OR "promo tipu") lang:id -is:retweet
```

### Pattern 7: QRIS & Digital Payment Issues

```
(qris OR "qris gagal" OR "edc" OR "transfer gagal" OR "mobile banking error") (dana OR tertahan OR gagal OR error OR "belum masuk") lang:id -is:retweet
```

### Pattern 8: PPN 12% & Tax Policy Reaction

```
("ppn 12%" OR "ppn 12" OR "pajak" OR "tarif pajak") (memberatkan OR protes OR demo OR "daya beli" OR mahal) lang:id -is:retweet
```

### Pattern 9: BPJS Kesehatan Complaints

```
(bpjs OR "bpjs kesehatan") (iuran OR naik OR defisit OR "tidak bisa" OR antrian) lang:id -is:retweet
```

### Pattern 10: Job Scam / Lowongan Palsu Detection

```
("lowongan palsu" OR "lowongan tipu" OR "penipuan kerja" OR "kerja scam" OR "fake job") lang:id -is:retweet has:links
```

### Pattern 11: Trending Topic Discovery (Broad)

```
"indonesia" lang:id -is:retweet min_faves:50
```

This catches tweets about Indonesia with at least 50 likes, filtering out noise. Adjust `min_faves` up for higher signal.

### Pattern 12: Influencer Discovery in Niche

Find verified users tweeting about a specific topic:

```
(qris OR "fintech" OR "bank digital") is:verified lang:id -is:retweet
```

### Pattern 13: Competitor Brand Crisis Detection

```
(tokopedia OR "tokopedia error" OR "tokopedia scam" OR "tokopedia down") has:media -is:retweet lang:id
```

### Pattern 14: Government Subsidy / BLT Chatter

```
("blt" OR "bansos" OR "subsidi" OR "bantuan sosial") (cair OR "belum cair" OR "tidak dapat" OR "dana") lang:id -is:retweet
```

### Pattern 15: Temu / Cina Produk Masuk Indonesia

```
(temu OR "temu.com" OR "shopee cina" OR "produk impor") (ancam OR "umkm" OR "murah" OR "hancur") lang:id -is:retweet
```

---

## Code: API Scrapers (Python)

### Setup: Twitter API v2 with Tweepy

```python
"""
twitter_api_scraper.py
X API v2 recent search wrapper for Indonesian signal mining.
Install: pip install tweepy python-dotenv
"""

import os
import json
import time
import logging
from datetime import datetime, timedelta, timezone
from typing import List, Dict, Optional

import tweepy
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)

class TwitterSignalScraper:
    """
    Production-grade scraper for X API v2 recent search.
    Handles rate limits, pagination, and structured output.
    """

    def __init__(self, bearer_token: Optional[str] = None):
        self.bearer_token = bearer_token or os.getenv("X_BEARER_TOKEN")
        if not self.bearer_token:
            raise ValueError(
                "X_BEARER_TOKEN not found. Set it in .env or pass bearer_token."
            )
        self.client = tweepy.Client(
            bearer_token=self.bearer_token,
            wait_on_rate_limit=True,  # auto-wait on 429
        )

    def search_recent(
        self,
        query: str,
        max_results: int = 100,
        start_time: Optional[datetime] = None,
        end_time: Optional[datetime] = None,
        expansions: Optional[List[str]] = None,
        tweet_fields: Optional[List[str]] = None,
        user_fields: Optional[List[str]] = None,
    ) -> List[Dict]:
        """
        Search recent tweets (last 7 days) with pagination.

        Args:
            query: Search query string (max 512 chars for Essential)
            max_results: Tweets per page (10-100)
            start_time: ISO 8601 datetime (must be within last 7 days)
            end_time: ISO 8601 datetime
            expansions: Additional data to include (author_id, geo.place_id, etc.)
            tweet_fields: Fields to include in tweet objects
            user_fields: Fields to include in user objects

        Returns:
            List of enriched tweet dictionaries
        """
        if expansions is None:
            expansions = ["author_id", "geo.place_id", "referenced_tweets.id"]
        if tweet_fields is None:
            tweet_fields = [
                "id", "text", "created_at", "author_id", "public_metrics",
                "lang", "source", "geo", "context_annotations",
                "referenced_tweets", "entities",
            ]
        if user_fields is None:
            user_fields = [
                "id", "name", "username", "verified", "public_metrics",
                "description", "location", "created_at",
            ]

        all_tweets = []
        next_token = None

        while True:
            try:
                response = self.client.search_recent_tweets(
                    query=query,
                    max_results=min(max_results, 100),
                    start_time=start_time,
                    end_time=end_time,
                    expansions=",".join(expansions),
                    tweet_fields=",".join(tweet_fields),
                    user_fields=",".join(user_fields),
                    next_token=next_token,
                )
            except tweepy.TweepyException as e:
                logger.error(f"API error: {e}")
                if "429" in str(e):
                    logger.warning("Rate limited. Sleeping 15 min...")
                    time.sleep(900)
                    continue
                break

            if not response.data:
                logger.info("No more tweets returned.")
                break

            # Build user lookup dict
            users = {}
            if response.includes and "users" in response.includes:
                for u in response.includes["users"]:
                    users[u.id] = u

            # Enrich each tweet
            for tweet in response.data:
                enriched = {
                    "id": tweet.id,
                    "text": tweet.text,
                    "created_at": tweet.created_at.isoformat(),
                    "author_id": tweet.author_id,
                    "lang": tweet.lang,
                    "source": tweet.source,
                    "public_metrics": tweet.public_metrics,
                }

                # Add user info
                if tweet.author_id and tweet.author_id in users:
                    user = users[tweet.author_id]
                    enriched["author"] = {
                        "username": user.username,
                        "name": user.name,
                        "verified": user.verified,
                        "followers_count": user.public_metrics.get("followers_count", 0),
                    }

                # Add entities (hashtags, mentions, urls)
                if tweet.entities:
                    enriched["entities"] = {
                        "hashtags": [h["tag"] for h in tweet.entities.get("hashtags", [])],
                        "mentions": [m["username"] for m in tweet.entities.get("mentions", [])],
                        "urls": [u["expanded_url"] for u in tweet.entities.get("urls", [])],
                    }

                # Add context annotations (for content categorization)
                if tweet.context_annotations:
                    enriched["context_annotations"] = [
                        {"domain": ca["domain"]["name"], "entity": ca["entity"]["name"]}
                        for ca in tweet.context_annotations
                    ]

                all_tweets.append(enriched)

            # Pagination
            next_token = response.meta.get("next_token") if response.meta else None
            if not next_token:
                break

            logger.info(f"Fetched {len(response.data)} tweets, total={len(all_tweets)}")

        return all_tweets

    def search_by_date_range(
        self, query: str, days_back: int = 1, **kwargs
    ) -> List[Dict]:
        """
        Convenience: search tweets from the last N days.
        The API limit is 7 days for recent search.
        """
        end_time = datetime.now(timezone.utc)
        start_time = end_time - timedelta(days=days_back)
        return self.search_recent(
            query=query,
            start_time=start_time,
            end_time=end_time,
            **kwargs,
        )


# Example usage
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    scraper = TwitterSignalScraper()

    # Search for UMKM platform fee complaints in the last 24 hours
    results = scraper.search_by_date_range(
        query="(tokopedia OR shopee) (fee OR komisi OR potongan OR mahal) lang:id -is:retweet",
        days_back=1,
        max_results=50,
    )

    print(f"Found {len(results)} tweets")
    for t in results[:5]:
        print(f"[{t['created_at']}] @{t['author']['username']}: {t['text'][:100]}...")
```

### Rate Limit Handling

The X API v2 Essential access has the following rate limits:

| Endpoint | Requests per 15-min window |
|---|---|
| `search/recent` | 100 (450 if using OAuth 1.0a User Context) |
| `search/all` | 300 (Academic Research only) |
| `tweets/lookup` | 300 |
| `users/lookup` | 300 |

The `wait_on_rate_limit=True` flag above handles 429 responses by sleeping until the window resets. For production, implement a token-bucket or sliding-window rate limiter:

```python
import time
from functools import wraps

def rate_limiter(max_per_window: int = 100, window_seconds: int = 900):
    """
    Decorator that limits calls to max_per_window per window_seconds.
    Sliding window implementation.
    """
    timestamps = []

    @wraps
    def decorator(func):
        def wrapper(*args, **kwargs):
            now = time.time()
            # Remove timestamps outside the window
            timestamps[:] = [t for t in timestamps if now - t < window_seconds]

            if len(timestamps) >= max_per_window:
                sleep_time = timestamps[0] + window_seconds - now
                if sleep_time > 0:
                    logger.warning(f"Rate limit: sleeping {sleep_time:.1f}s")
                    time.sleep(sleep_time)

            timestamps.append(time.time())
            return func(*args, **kwargs)
        return wrapper
    return decorator
```

### Response Storage (JSON Lines)

```python
def save_tweets(tweets: List[Dict], filename: str):
    """
    Save tweets as JSON Lines (.jsonl), one JSON object per line.
    This is append-friendly and grep-friendly.
    """
    with open(filename, "a") as f:
        for tweet in tweets:
            f.write(json.dumps(tweet, ensure_ascii=False) + "\n")
    logger.info(f"Saved {len(tweets)} tweets to {filename}")


def load_tweets(filename: str) -> List[Dict]:
    """Load tweets from JSON Lines file."""
    tweets = []
    with open(filename, "r") as f:
        for line in f:
            if line.strip():
                tweets.append(json.loads(line))
    return tweets
```

---

## Code: Web Scrapers (Playwright)

When the API is insufficient (e.g., you need web-only operators or real-time trending), use Playwright to automate the X web search interface.

### Setup

```bash
pip install playwright
playwright install chromium
```

### Basic Web Search Scraper

```python
"""
twitter_web_scraper.py
Playwright-based X web search scraper for when the API is not enough.
"""

import asyncio
import json
import logging
from datetime import datetime
from typing import List, Dict, Optional
from pathlib import Path

from playwright.async_api import async_playwright, Page, Browser

logger = logging.getLogger(__name__)

COOKIE_PATH = Path("x_cookies.json")


class XWebSearchScraper:
    """
    Automated X web search using Playwright.
    Requires a logged-in session for full access.
    """

    def __init__(self, headless: bool = True):
        self.headless = headless
        self.browser: Optional[Browser] = None

    async def __aenter__(self):
        self.playwright = await async_playwright().start()
        self.browser = await self.playwright.chromium.launch(
            headless=self.headless,
            args=[
                "--disable-blink-features=AutomationControlled",
                "--no-sandbox",
            ],
        )
        return self

    async def __aexit__(self, *args):
        if self.browser:
            await self.browser.close()
        if self.playwright:
            await self.playwright.stop()

    async def _get_context(self):
        """Create a browser context with stealth settings."""
        context = await self.browser.new_context(
            viewport={"width": 1280, "height": 720},
            user_agent=(
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/125.0.0.0 Safari/537.36"
            ),
            locale="id-ID",  # Set to Indonesian for localized results
            timezone_id="Asia/Jakarta",
        )

        # Load saved cookies if available
        if COOKIE_PATH.exists():
            with open(COOKIE_PATH) as f:
                cookies = json.load(f)
            await context.add_cookies(cookies)
            logger.info(f"Loaded {len(cookies)} cookies from {COOKIE_PATH}")

        return context

    async def search(
        self, query: str, max_scrolls: int = 10, is_advanced: bool = False
    ) -> List[Dict]:
        """
        Perform an X web search and extract tweets.

        Args:
            query: Search query string (raw, without URL encoding)
            max_scrolls: How many times to scroll for more results
            is_advanced: If True, use advanced search URL

        Returns:
            List of extracted tweet dicts
        """
        context = await self._get_context()
        page = await context.new_page()

        # Encode the query for URL
        import urllib.parse
        encoded_query = urllib.parse.quote(query, safe="")

        search_url = (
            f"https://x.com/search?q={encoded_query}&src=typed_query&f=live"
        )
        if is_advanced:
            search_url = f"https://x.com/search-advanced?lang=en&q={encoded_query}"

        logger.info(f"Navigating to: {search_url}")
        await page.goto(search_url, wait_until="domcontentloaded", timeout=30000)

        # Wait for tweets to load
        try:
            await page.wait_for_selector("article[data-testid='tweet']", timeout=15000)
        except Exception:
            logger.warning("No tweet articles found. Page may require login.")
            # Save screenshot for debugging
            await page.screenshot(path="debug_no_tweets.png")
            await context.close()
            return []

        tweets = []
        seen_ids = set()

        for scroll in range(max_scrolls):
            # Extract tweets currently in the DOM
            tweet_elements = await page.query_selector_all(
                "article[data-testid='tweet']"
            )

            for el in tweet_elements:
                try:
                    tweet_data = await self._extract_tweet(page, el)
                    if tweet_data and tweet_data["id"] not in seen_ids:
                        seen_ids.add(tweet_data["id"])
                        tweets.append(tweet_data)
                except Exception as e:
                    logger.debug(f"Error extracting tweet: {e}")

            logger.info(
                f"Scroll {scroll+1}/{max_scrolls}: {len(tweets)} unique tweets "
                f"({len(tweet_elements)} elements on page)"
            )

            # Scroll down to load more
            await page.evaluate("window.scrollBy(0, 1500)")
            await asyncio.sleep(2 + (scroll % 3))  # Randomize delay

        await context.close()
        return tweets

    async def _extract_tweet(self, page: Page, element) -> Optional[Dict]:
        """
        Extract structured data from a tweet article element.
        This relies on X's data-testid attributes which are relatively stable.
        """
        tweet_id = await element.get_attribute("data-tweet-id")
        if not tweet_id:
            # Try extracting from the tweet link
            link = await element.query_selector("a[href*='/status/']")
            if link:
                href = await link.get_attribute("href")
                if href and "/status/" in href:
                    tweet_id = href.split("/status/")[-1].split("?")[0]

        text_el = await element.query_selector("[data-testid='tweetText']")
        text = await text_el.inner_text() if text_el else ""

        # Extract user info
        user_el = await element.query_selector(
            "[data-testid='User-Name'] a[href*='/']:not([href*='status'])"
        )
        username = ""
        display_name = ""
        if user_el:
            href = await user_el.get_attribute("href")
            if href:
                username = href.strip("/").split("/")[-1] if href.count("/") <= 2 else ""
            display_name = await user_el.inner_text()

        # Extract timestamp
        time_el = await element.query_selector("time")
        timestamp = ""
        if time_el:
            timestamp = await time_el.get_attribute("datetime") or ""

        # Extract engagement metrics
        metrics = {}
        for metric_name, test_id in [
            ("replies", "reply"),
            ("retweets", "retweet"),
            ("likes", "like"),
            ("views", "view"),
        ]:
            metric_el = await element.query_selector(
                f"[data-testid='{test_id}']"
            )
            if metric_el:
                metric_text = await metric_el.inner_text()
                # Parse "1.2K" to 1200, "500" to 500
                metrics[metric_name] = self._parse_count(metric_text)

        # Extract media
        has_media = await element.query_selector(
            "[data-testid='tweetPhoto'], [data-testid='videoPlayer']"
        ) is not None

        return {
            "id": tweet_id,
            "text": text,
            "username": username,
            "display_name": display_name.strip(),
            "timestamp": timestamp,
            "metrics": metrics,
            "has_media": has_media,
            "scraped_at": datetime.utcnow().isoformat(),
        }

    @staticmethod
    def _parse_count(text: str) -> int:
        """Parse '1.2K' to 1200, '500' to 500."""
        text = text.strip()
        if not text:
            return 0
        text = text.replace(",", ".")
        if "K" in text:
            return int(float(text.replace("K", "")) * 1000)
        elif "M" in text:
            return int(float(text.replace("M", "")) * 1_000_000)
        try:
            return int(text)
        except ValueError:
            return 0


# Example usage
async def main():
    async with XWebSearchScraper(headless=True) as scraper:
        results = await scraper.search(
            query="(tolak OR protes OR demo) ppn 12% lang:id",
            max_scrolls=5,
        )
        print(f"Extracted {len(results)} tweets")
        for t in results[:3]:
            print(f"  @{t['username']}: {t['text'][:80]}... [{t['metrics'].get('likes', 0)} likes]")

    # Save results
    with open("x_web_results.jsonl", "w") as f:
        for t in results:
            f.write(json.dumps(t, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    asyncio.run(main())
```

### Cookie Persistence

To maintain session state across runs (avoiding repeated logins), save cookies after the first manual login:

```python
# After manual login, run once:
await context.storage_state(path=str(COOKIE_PATH))
```

And for the initial login on first run:

```python
async def login_first_time(context, username: str, password: str, email: str = ""):
    """Perform initial login to X and save cookies."""
    page = await context.new_page()
    await page.goto("https://x.com/login", wait_until="domcontentloaded")

    # Enter username
    await page.fill("input[autocomplete='username']", username)
    await page.click("//span[text()='Next']")
    await asyncio.sleep(2)

    # Sometimes X asks for email/phone
    email_input = await page.query_selector("input[autocomplete='email']")
    if email_input and email:
        await email_input.fill(email)
        await page.click("//span[text()='Next']")
        await asyncio.sleep(2)

    # Enter password
    await page.fill("input[autocomplete='current-password']", password)
    await page.click("//span[text()='Log in']")
    await asyncio.sleep(5)

    # Save cookies
    cookies = await context.cookies()
    with open(COOKIE_PATH, "w") as f:
        json.dump(cookies, f)
    logger.info(f"Saved cookies for @{username}")

    return cookies
```

### Anti-Detection Stealth

Modern X aggressively detects automated browsers. Add these stealth measures:

```python
# Before launching browser
stealth_args = [
    "--disable-blink-features=AutomationControlled",
    "--disable-automation",
    "--disable-infobars",
    "--no-sandbox",
    "--disable-dev-shm-usage",
    "--disable-web-security",
    "--disable-features=IsolateOrigins,site-per-process",
    "--disable-site-isolation-trials",
]

# In context creation, override navigator.webdriver
await context.add_init_script("""
    Object.defineProperty(navigator, 'webdriver', {
        get: () => undefined
    });
    // Override navigator.plugins to appear more human
    Object.defineProperty(navigator, 'plugins', {
        get: () => [1, 2, 3, 4, 5]
    });
    // Override chrome runtime
    window.chrome = {
        runtime: {},
        loadTimes: function() {},
        csi: function() {},
        app: {}
    };
""")
```

---

## Signal Processing Pipeline

Raw tweets are noisy. A production pipeline should classify, score, and alert.

### Classification

```python
"""
signal_classifier.py
Classify tweets into vault-relevant categories using keyword rules.
"""

SIGNAL_CATEGORIES = {
    "umkm_complaint": [
        "fee", "komisi", "potongan", "blokir", "suspend", "mahal",
        "tokopedia", "shopee", "tiktok shop", "biaya platform",
    ],
    "crypto_hype": [
        "$", "btc", "eth", "sol", "airdrop", "rug", "pump", "dump",
        "kripto", "crypto", "token", "nft",
    ],
    "stock_chatter": [
        "ihsg", "saham", "goreng", "cuan", "bbc", "bbri", "bmri",
        "tlkm", "asii", "goto",
    ],
    "freelancer_pain": [
        "freelance", "freelancer", "dibayar", "kabur", "wanprestasi",
        "client", "proyek", "upwork", "fastwork", "sribu",
    ],
    "price_shock": [
        "cabai", "bawang", "minyak goreng", "beras", "telur",
        "mahal", "naik", "melonjak", "inflasi",
    ],
    "platform_outage": [
        "error", "down", "maintenance", "gagal", "aplikasi error",
        "gojek", "grab", "tokopedia", "shopee",
    ],
    "policy_reaction": [
        "ppn", "pajak", "peraturan", "uu cipta kerja", "omnibus",
        "bpjs", "iuran", "blt", "bansos",
    ],
    "qris_payment": [
        "qris", "edc", "transfer gagal", "mobile banking", "gagal bayar",
        "dana tertahan",
    ],
}


def classify_tweet(text: str) -> List[str]:
    """Classify a tweet into signal categories. Returns list of matching categories."""
    text_lower = text.lower()
    matches = []
    for category, keywords in SIGNAL_CATEGORIES.items():
        for kw in keywords:
            if kw in text_lower:
                matches.append(category)
                break
    return matches


def score_urgency(tweet: Dict) -> float:
    """
    Score a tweet on a 0.0-1.0 urgency scale for alerting.
    Factors: engagement, verified author, recency, media, keywords.
    """
    score = 0.0
    metrics = tweet.get("public_metrics", tweet.get("metrics", {}))

    # Engagement factor (0-0.4)
    likes = metrics.get("likes", metrics.get("like_count", 0))
    retweets = metrics.get("retweets", metrics.get("retweet_count", 0))
    replies = metrics.get("replies", metrics.get("reply_count", 0))
    engagement_score = min((likes * 0.01 + retweets * 0.02 + replies * 0.03), 0.4)
    score += engagement_score

    # Verified author factor (0-0.2)
    if tweet.get("author", {}).get("verified", False):
        score += 0.2

    # Has media factor (0-0.1)
    if tweet.get("has_media", False):
        score += 0.1

    # Has links factor (0-0.1)
    entities = tweet.get("entities", {})
    if entities.get("urls"):
        score += 0.1

    # Recency factor (0-0.2)
    created_str = tweet.get("created_at", "")
    if created_str:
        try:
            created = datetime.fromisoformat(created_str.replace("Z", "+00:00"))
            hours_ago = (datetime.now(timezone.utc) - created).total_seconds() / 3600
            recency_score = max(0, 0.2 - hours_ago * 0.01)  # Decays over ~20 hours
            score += recency_score
        except ValueError:
            pass

    return min(score, 1.0)
```

### Alerting

```python
def should_alert(tweet: Dict, threshold: float = 0.5) -> bool:
    """Determine if a tweet should trigger an alert."""
    urgency = score_urgency(tweet)
    categories = classify_tweet(tweet.get("text", ""))
    return urgency >= threshold and len(categories) > 0


def format_alert(tweet: Dict) -> str:
    """Format a tweet for Telegram or other alerting channel."""
    categories = classify_tweet(tweet.get("text", ""))
    urgency = score_urgency(tweet)
    username = tweet.get("author", {}).get("username", tweet.get("username", "unknown"))
    text = tweet.get("text", "")[:200]
    link = f"https://x.com/{username}/status/{tweet['id']}"

    return (
        f"\U0001F514 *Signal Alert* (urgency: {urgency:.2f})\n"
        f"*Categories:* {', '.join(categories)}\n"
        f"*@{username}:* {text}\n"
        f"\U0001F517 {link}"
    )
```

### Full Pipeline Runner

```python
"""
run_pipeline.py
Daily pipeline: fetch, classify, save, and alert.
"""

import asyncio
import logging
from datetime import datetime, timezone

from twitter_api_scraper import TwitterSignalScraper
from signal_classifier import classify_tweet, score_urgency, should_alert, format_alert

logger = logging.getLogger(__name__)

# Predefined queries for daily signal collection
DAILY_QUERIES = [
    ("umkm_platform", "(tokopedia OR shopee) (fee OR komisi OR potongan) lang:id"),
    ("crypto_indonesia", "($BTC OR $ETH OR airdrop) lang:id"),
    ("ihsg_chatter", "(IHSG OR saham) (naik OR turun OR goreng) lang:id"),
    ("freelancer_pain", "(freelance OR freelancer) (dibayar OR kabur) lang:id"),
    ("harga_pangan", "(cabai OR bawang OR beras OR telur) mahal lang:id"),
    ("qris_issue", "qris (gagal OR error OR tertahan) lang:id"),
]

ALERT_THRESHOLD = 0.5


async def run():
    scraper = TwitterSignalScraper()
    all_alerts = []

    for label, query in DAILY_QUERIES:
        logger.info(f"Fetching signal: {label}")
        try:
            tweets = scraper.search_by_date_range(query, days_back=1, max_results=50)
        except Exception as e:
            logger.error(f"Failed to fetch {label}: {e}")
            continue

        for tweet in tweets:
            # Add classification
            tweet["_categories"] = classify_tweet(tweet.get("text", ""))
            tweet["_urgency"] = score_urgency(tweet)

            if should_alert(tweet, ALERT_THRESHOLD):
                all_alerts.append(tweet)

        logger.info(f"  Got {len(tweets)} tweets, {len([t for t in tweets if should_alert(t)])} above threshold")

    # Print alerts
    if all_alerts:
        print(f"\n=== {len(all_alerts)} Alerts ===")
        for tweet in sorted(all_alerts, key=lambda t: t["_urgency"], reverse=True)[:10]:
            print(format_alert(tweet))
    else:
        print("No alerts triggered today.")

    return all_alerts


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    )
    asyncio.run(run())
```

---

## Anti-Detection, Ethics & Legal (Indonesia)

### X's Anti-Scraping Measures (as of 2025-2026)

X has significantly hardened its anti-bot defenses since the 2023 API changes:

| Defense Mechanism | Impact | Mitigation |
|---|---|---|
| **Rate limiting** | ~50 web requests before temp block | Use API instead of web; rotate IPs |
| **CAPTCHA (hCaptcha)** | Triggers on rapid navigation, unusual user agents | Use residential proxies; randomize delays |
| **login_required walls** | Some searches require login for full results | Maintain persistent login session |
| **DOM randomization** | CSS classes change frequently | Use `data-testid` attributes instead of CSS classes |
| **X-Account-Headers** | Server-side detection of Playwright headless | Override `navigator.webdriver`; use stealth plugin |
| **IP reputation** | Datacenter IPs get stricter limits | Use residential proxies ($5-10/GB) |
| **Account suspension** | Repeat scraping from same account leads to suspension | Use burner accounts; rotate cookies |

### Recommended Anti-Detection Stack

1. **Playwright** with stealth patches (as shown above) instead of Selenium.
2. **BrightData / Oxylabs / Smartproxy** residential proxies for IP rotation.
3. **Multiple burner accounts** with distinct browsing patterns, rotated weekly.
4. **Randomized timing** between requests: Gaussian distribution with mean 3s, stddev 1s.
5. **Sessions limited to 30 min** per account to avoid detection.

### Legal Framework (Indonesia)

Scraping public data from X sits in a complex legal space. Key considerations:

**UU ITE (Undang-Undang Informasi dan Transaksi Elektronik)**
- Pasal 30: Prohibits unauthorized access to computer systems. Scraping publicly available data is generally not considered "unauthorized access" under Indonesian jurisprudence.
- Pasal 32: Prohibits altering, deleting, or transferring computer data without authorization. Read-only scraping does not violate this.
- Pasal 27: Prohibits distributing obscene content. If your scraper accidentally captures such content, you must filter it before storage.

**X / Twitter Terms of Service**
- X prohibits scraping "in violation of" their terms. The api.twitter.com terms strictly forbid data scraping via non-API methods.
- **Practical approach**: Use the official API for all production data collection. Use web scraping only for prototype/research or for data the API cannot access (trending topics, specific UI elements).
- Rate limit to avoid denial-of-service impact on X's infrastructure.

**UU Perlindungan Data Pribadi (PDP Law, effective 2024)**
- Public data from X is generally exempt from consent requirements under the "publicly available information" exemption.
- However, if you enrich scraped data with private information (e.g., phone numbers, addresses) or if you republish tweet content in a way that causes harm, you may be liable.
- **Recommendation:** Store tweet IDs and search queries, not full tweet texts, for archival purposes. Rehydrate from the API when needed.

**Practical Compliance Checklist**
- [ ] Use the official X API for production pipelines.
- [ ] Store only tweet IDs and metadata, not full content, for long-term storage.
- [ ] Set a `robots.txt`-respecting crawl delay (X's `robots.txt` disallows most scraping).
- [ ] Do not republish scraped content verbatim (data mining insights are fine, republishing tweet dumps is not).
- [ ] Filter and strip PII (phone numbers, emails, addresses) from stored data.
- [ ] Use burner accounts isolated from your main identity.
- [ ] Implement a kill switch: if you receive a cease-and-desist, stop immediately.

---

## Ready-to-Use Query Templates

This section provides copy-paste query strings for common Indonesian signal mining tasks. Each query is optimized for API v2 recent search (Essential access, 512 char limit).

### UMKM & E-commerce

```
# Seller complaints about platform fees (high signal)
(tokopedia OR shopee OR "tiktok shop") (fee OR komisi OR potongan OR mahal) lang:id -is:retweet

# Seller account blocks or suspensions (crisis signal)
(tokopedia OR shopee) (blokir OR suspend OR "akun ditutup" OR "tidak bisa login") lang:id -is:retweet has:media

# Promo complaints (fake discounts, inflated prices)
(tokopedia OR shopee OR lazada) (promo OR diskon OR cashback) (tipu OR bohong OR "tidak sesuai" OR gagal) lang:id -is:retweet
```

### Cryptocurrency

```
# Indonesian crypto community buzz
($BTC OR $ETH OR $SOL) (indonesia OR idr OR rupiah) lang:id -is:retweet

# Airdrop / free token hype
(airdrop OR "free token" OR "claim token") (indonesia OR indo) lang:id -is:retweet has:links

# Exchange issues (Indodax, Reku, Pintu)
(indodax OR reku OR pintu) (error OR down OR "gagal withdraw" OR "maintenance") lang:id -is:retweet
```

### Stock Market (IDX)

```
# IHSG daily sentiment
(IHSG OR "bursa efek" OR "idx composite") (naik OR turun OR "ditutup" OR rebound OR anjlok) lang:id -is:retweet

# Individual stock chatter
(BBCA OR BBRI OR BMRI OR TLKM OR ASII) (beli OR jual OR tahan OR goreng OR cuan) lang:id -is:retweet min_faves:5

# IPO buzz
(IPO OR "initial public offering" OR listing) (saham OR bursa) (beli OR allotment OR jatah) lang:id -is:retweet
```

### Freelance & Gig Economy

```
# Payment complaints
(freelance OR freelancer) (dibayar OR "gagal bayar" OR kabur OR "tidak dibayar" OR wanprestasi) lang:id -is:retweet

# Job scams
("lowongan palsu" OR "lowongan tipu" OR "penipuan kerja" OR "kerja scam") lang:id -is:retweet

# Fastwork / Sribu feedback
(fastwork OR sribu OR projects.co.id) (order OR proyek OR fee OR komisi OR pembayaran) lang:id -is:retweet
```

### Consumer & Price Signals

```
# Price shock for staple goods
(cabai OR bawang OR "minyak goreng" OR beras OR telur OR "daging sapi") (mahal OR naik OR melonjak OR "harga naik") lang:id -is:retweet

# Fuel price reaction
(pertalite OR pertamax OR solar OR "bbm naik" OR "harga bbm") (protes OR mahal OR demo OR "tidak mampu") lang:id -is:retweet

# Electricity token complaint
("token listrik" OR "pln token" OR "listrik padam") (mahal OR naik OR "beli token" OR error) lang:id -is:retweet
```

### Policy & Regulation

```
# PPN 12% reaction (if still active)
("ppn 12" OR "pajak 12%" OR "ppn naik") (protes OR demo OR berat OR "daya beli") lang:id -is:retweet

# BPJS Kesehatan crisis
(bpjs OR "bpjs kesehatan") (iuran OR defisit OR naik OR antrian OR "tidak bisa") lang:id -is:retweet

# BLT / Bansos distribution
(blt OR bansos OR "bantuan sosial" OR "bantuan langsung") (cair OR "belum cair" OR "tidak dapat") lang:id -is:retweet
```

### Crisis & Outage Detection

```
# Platform outage reports
(gojek OR grab OR tokopedia OR shopee OR "mobile banking") (error OR down OR crash OR "tidak bisa") lang:id -is:retweet has:media

# Natural disaster / emergency
(gempa OR banjir OR longsor OR "kebakaran") (indonesia OR jakarta OR jawa) lang:id -is:retweet has:geo
```

### Broad Trending Discovery

```
# High-engagement Indonesian tweets (general trend discovery)
lang:id -is:retweet min_faves:100

# Indonesian verified influencers posting about business
(bisnis OR "usaha" OR "modal" OR "investasi") is:verified lang:id -is:retweet

# Twitter Spaces about finance (audio signals)
(spaces OR "twitter space" OR "x space") (bisnis OR saham OR kripto OR investasi OR umkm) lang:id
```

---

## References & Further Reading

### Official Documentation

1. X API v2 Search Operators (via Wayback Machine, 2023 archive):
   - `https://developer.twitter.com/en/docs/twitter-api/tweets/search/integrate/build-a-query`
   - `https://developer.twitter.com/en/docs/twitter-api/tweets/search/integrate/operators`
2. X API v1.1 Search Operators (legacy, still useful for reference):
   - `https://developer.twitter.com/en/docs/twitter-api/v1/rules-and-filtering/search-operators`
3. X API v2 Recent Search Reference:
   - `https://developer.x.com/en/docs/x-api/tweets/search/api-reference/get-tweets-search-recent`
4. X API Rate Limits:
   - `https://developer.twitter.com/en/docs/twitter-api/rate-limits`
5. Tweepy Documentation:
   - `https://docs.tweepy.org/en/latest/`

### Practical Guides

6. Zapier guide to Twitter Advanced Search (2022, Melissa King):
   - `https://zapier.com/blog/twitter-advanced-search-guide/`
   - Covers the web UI, search fields, engagement filters, and practical examples.
7. Brandwatch Twitter Advanced Search Operators (blog):
   - `https://www.brandwatch.com/blog/twitter-advanced-search-operators/`
   - Comprehensive community-maintained list of operators.
8. Twitter Help Center: How to use X Search:
   - `https://help.twitter.com/en/using-x/x-search`
9. Social Media Examiner: Twitter Search Tips:
   - `https://www.socialmediaexaminer.com/twitter-advanced-search-tips/`

### Indonesia-Specific Sources

10. CNBC Indonesia (for trending business topics):
    - `https://www.cnbcindonesia.com/`
11. Katadata Insight Center (for data-driven Indonesian analysis):
    - `https://katadata.co.id/`
12. Celios (Center of Economic and Law Studies) research on UMKM:
    - `https://celios.co.id/`
13. OJK (Otoritas Jasa Keuangan) for regulatory signals:
    - `https://www.ojk.go.id/`
14. Bank Indonesia (BI) for payment system and QRIS updates:
    - `https://www.bi.go.id/`

### Technical References

15. Playwright Python Documentation:
    - `https://playwright.dev/python/docs/intro`
16. Playwright Stealth (anti-detection):
    - `https://github.com/AtuboDad/playwright_stealth`
17. X's robots.txt (scraping restrictions):
    - `https://x.com/robots.txt`
18. JSON Lines format (for tweet storage):
    - `https://jsonlines.org/`

### Legal References (Indonesia)

19. UU ITE (Undang-Undang Informasi dan Transaksi Elektronik), UU No. 1 Tahun 2024:
    - `https://peraturan.bpk.go.id/Details/282748/uu-no-1-tahun-2024`
20. UU PDP (Perlindungan Data Pribadi), UU No. 27 Tahun 2022:
    - `https://peraturan.bpk.go.id/Details/238238/uu-no-27-tahun-2022`
21. X Developer Terms (binding on API usage):
    - `https://developer.twitter.com/en/developer-terms`

---

*Generated: 2026-06-23 by Money Glitch Vault Auto-Enricher. Sources cited where possible; some URLs may have changed since X migrated from twitter.com to x.com domain.*
