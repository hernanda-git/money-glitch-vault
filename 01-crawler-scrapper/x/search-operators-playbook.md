# X (Twitter) Advanced Search Operators Playbook

**Folder:** `01-crawler-scrapper/x/`
**Status:** NEW high-priority gap fill
**Generated:** 2026-07-14 (WIB 20:13)
**Maintainer:** Money Glitch Vault Auto-Enricher
**Purpose:** A deeply technical, field-usable reference for the X advanced search operator grammar, why it diverges from the paid X API, how to scrape it reliably with `twscrape`, and how to translate the operator grammar into recurring signal queries for the Indonesian money-pain pipeline that feeds `03-id-business-trends`.

This document is a research reference. It is not a product pitch. Every operator, behavior, and limit below is sourced from a real reference at the end of the file. Where a behavior is version-dependent or unreliably implemented, that is called out explicitly rather than hidden.

---

## Why X search is the cheapest signal layer in the vault

Most of the money-pain raw material in `03-id-business-trends` originates as complaints, boasts, and screenshots posted on X. The platform's full-text search over the entire archive is free to use through the web interface and the mobile interface, and it supports a dense operator grammar that the paid API does not. For a vault whose entire thesis is "mine where Indonesians talk about money friction," the search box is the single highest-leverage input.

The constraint is that the operator grammar documented here only works on the web and mobile search surfaces. The paid X API, even at the highest paid tiers, exposes a much smaller set of filtering capabilities and a pay-per-use pricing model. This divergence is the reason a scraping layer (built with `twscrape`) is the right tool for the vault rather than a paid API subscription. The rest of this document explains the grammar, the divergence, and the scraper that exploits it.

---

## The operator grammar

The grammar below is adapted from the community-maintained reference at `https://github.com/igorbrigadir/twitter-advanced-search` (last checked 2022-11-01 for most rows, with later annotations noted inline). It is the most complete public catalog of the web-search operators. These operators work on Web, Mobile, and TweetDeck search. They largely do NOT work on the v1.1 Search, Premium Search, or v2 Search APIs. That caveat is the most important thing to internalize before building anything.

### Tweet content operators

A bare space between words is an implicit AND. `nasa esa` returns tweets containing both terms, in any order. Parentheses group sub-expressions when combined with other operators, for example `(nasa esa)`.

`nasa OR esa` returns tweets containing either term. The OR operator must be uppercase, lowercase `or` is treated as a literal word.

`"state of the art"` matches the exact phrase. It also matches hyphenated variants like `state-of-the-art`. Quotes also suppress spelling correction, which matters when searching for brand names with unconventional spelling.

`"this is the * time this week"` is a quoted phrase with a wildcard. The `*` token only works inside a quoted phrase and requires surrounding spaces.

`+radiooooo` forces a term to be included exactly as written, again useful to defeat spelling correction.

`-love` and `-"live laugh love"` exclude a term or phrase. The minus prefix applies to hashtags, cashtags, quoted phrases, and other operators.

`#tgif` is a hashtag search.

`$TWTR` is a cashtag, which behaves like a hashtag but for stock symbols. Cashtags are central to the vault's IDX and crypto signal work because Indonesian retail traders discuss tickers on X in real time. A query like `$TWTR OR $FB OR $AMZN OR $AAPL OR $NFLX OR $GOOG` sweeps a sector.

`What ?` matches question marks. A useful trick is `(Who OR What OR When OR Where OR Why OR How) ?` to surface questions, which are disproportionately pain signals ("Kenapa BPJS ditolak di RS?").

`:) OR :(` matches some emoticons, positive `:) :-) :P :D` or negative `:-( :(`.

Emoji searches are also matched but usually require another operator to return stable results, for example `👀 lang:en`.

`url:google.com` matches tokenized URLs. It works well for subdomains and bare domains but poorly for long paths. Shorteners resolve to their canonical domain, so `url:gu.com` matches `theguardian.com`. When a domain contains a hyphen you must replace the hyphen with an underscore, for example `url:t_mobile.com`, and note that underscores are themselves tokenized out so matching is imperfect.

`lang:en` restricts to a detected language. Language detection is per-tweet and not perfectly accurate. The full supported language list lives in the upstream reference, including the special code `und` for tweets where language could not be determined. For Indonesian signal work `lang:id` is the primary filter, with `lang:und` occasionally revealing Indonesian-language tweets the classifier missed.

### User operators

`from:user` returns tweets sent by a specific `@username`, for example `"dogs from:NASA"`.

`to:user` returns tweets replying to a specific `@username`, for example `#MoonTunes to:NASA`.

`@user` returns tweets mentioning a specific `@username`. Combine with `-from:username` to get only mentions of an account rather than its own posts, for example `@cern -from:cern`.

`list:715919216927322112` or `list:esa/astronauts` returns tweets from members of a public list, using either the numeric list ID from the API or the legacy slug URL form. This cannot be negated, so you cannot search "not on list."

`filter:verified` returns tweets from legacy verified users.

`filter:blue_verified` returns tweets from accounts that paid for the blue checkmark.

`filter:follows` returns only tweets from accounts you follow and cannot be negated.

`filter:social` and `filter:trusted` return tweets from an algorithmically expanded network based on your own follows and activity. These only work on "Top" results, not "Latest."

### Geo operators

`near:city` returns geotagged tweets from a place, and supports phrases like `near:"The Hague"`.

`near:me` returns tweets near where X thinks you are, which depends on the account's inferred location.

`within:radius` bounds the `near:` operator, for example `fire near:san-francisco within:10km`. Radius accepts `km` or `mi`.

`geocode:lat,long,radius` is the numeric form, for example `geocode:37.7764685,-122.4172004,10km`.

`place:96683cc9126741d1` searches by Place Object ID, for example the USA Place ID `96683cc9126741d1`.

For Indonesian signal mining, geo operators are weak because most Indonesian users do not geotag, but `near:Jakarta within:50km` combined with a pain keyword can isolate metro-specific complaints worth cross-referencing with regional price data in `06-harga-pangan-papan`.

### Time operators

`since:2021-12-31` is inclusive of the date. `until:2021-12-31` is exclusive of the date. Combine them for a range.

`since:2021-12-31_23:59:59_UTC` and `until:2021-12-31_23:59:59_UTC` add a time component in the 24-hour clock with a timezone abbreviation.

`since_time:1142974200` and `until_time:1142974215` use Unix timestamps in seconds, which can be easier than Snowflake IDs for bounded windows.

`since_id:tweet_id` returns tweets after (exclusive) a Snowflake ID. `max_id:tweet_id` returns tweets at or before (inclusive) a Snowflake ID. These are the canonical pagination cursors for incremental scraping.

`within_time:2d`, `within_time:3h`, `within_time:5m`, `within_time:30s` search within the last number of days, hours, minutes, or seconds. This is the operator the vault's daily cron should lean on for "what happened in the last 24 hours" sweeps.

### Tweet type operators

`filter:nativeretweets` returns only retweets made with the retweet button. It pairs well with `from:` to show only an account's retweets and only works within roughly the last 7 to 10 days.

`include:nativeretweets` shows native retweets in addition to other tweets, since they are excluded by default. Also limited to roughly the last 7 to 10 days.

`filter:retweets` returns old-style "RT" retweets plus quoted tweets.

`filter:replies` returns tweets that are replies, useful for finding conversations or threads when combined with or without `to:user`.

`filter:self_threads` returns only self-replies that form a thread.

`conversation_id:tweet_id` returns all tweets in a thread (direct and other replies).

`filter:quote` returns tweets containing Quote Tweets.

`quoted_tweet_id:tweet_id` searches for quotes of a specific tweet.

`quoted_user_id:user_id` searches for all quotes of a specific user by numeric User ID.

`card_name:poll2choice_text_only` through `card_name:poll4choice_image` match tweets containing polls with 2, 3, or 4 choices, in text-only or image form.

### Engagement operators

`filter:has_engagement` returns tweets with some engagement (replies, likes, retweets) and can be negated to find zero-engagement tweets. These are mutually exclusive with the native-retweet filters.

`min_retweets:5` sets a minimum retweet floor. For values above roughly 1000 the counts are approximate.

`min_faves:10` sets a minimum like floor.

`min_replies:100` sets a minimum reply floor.

`-min_retweets:500`, `-min_faves:500`, and `-min_replies:100` set maximum floors (the leading minus inverts to "at most"). Note that a `max_*` counterpart does not exist for these; the negation form is the only way.

These floors are the vault's primary relevance filter. A pain tweet with `min_faves:50` and `min_replies:10` is far more likely to represent a widespread, resonant problem than a lone complaint, and is therefore a stronger candidate for promotion into `03-id-business-trends`.

### Media operators

`filter:media` matches all media types.

`filter:twimg` matches native Twitter images (`pic.twitter.com` links).

`filter:images` matches all images.

`filter:videos` matches all video types including native and external like YouTube.

`filter:periscope` matches Periscopes.

`filter:native_video` matches Twitter-owned video (native video, Vine, Periscope).

`filter:vine` matches Vines.

`filter:consumer_video` matches Twitter native video only.

`filter:pro_video` matches Twitter pro video (Amplify) only.

`filter:spaces` matches Twitter Spaces only.

`filter:links` matches tweets containing a URL, which is the workhorse filter for surfacing articles, threads linking out, and screenshots hosted off-platform.

---

## How the web operators diverge from the paid X API

This divergence is the single most misunderstood fact in X data work, and it is the reason the vault builds a scraper instead of buying API access. The upstream reference states plainly that the operator table above "will not work" for the v1.1 Search, Premium Search, or v2 Search APIs. The paid API uses a different, smaller query language.

The current X API pricing model (per the official introduction page at `https://developer.x.com/en/docs/x-api/tweets/search/introduction`, retrieved 2026-07-14) is pay-per-usage with flexible pricing. Owned reads, requests for your own posts, bookmarks, followers, likes, and similar, are priced at roughly $0.001 per resource. The page advertises "modern APIs with flexible pay-per-usage pricing" and an Enterprise tier with "high-volume endpoints, dedicated account management, and custom rate limits." There is no free tier that returns historical archive search at scale. The v2 recent search endpoint (the standard paid path) returns only the last seven days of matching posts and supports only a subset of the web grammar, with no `min_faves`, no `filter:`, and no `since/until` date windows in the same expressive form.

The practical consequence: if you want "every Indonesian tweet about BPJS rejection with at least 50 likes in the last 90 days," the web search box returns it for free in seconds, while the paid API either cannot express the engagement floor or bills per matched post and caps the window at seven days. For a vault that runs daily sweeps and accumulates history, the web-search scraper is the only economically sane path.

A secondary consequence is that any code you write against the paid API must not assume web operators work. The scraper described below talks to the same GraphQL endpoints the web app uses, so it inherits the full operator grammar.

---

## Building the scraper with twscrape

`twscrape` is an async Python library and CLI for X/Twitter search and GraphQL endpoints. It runs on your own pool of authorized accounts, keeps sessions in a SQLite database, rotates accounts when an endpoint is rate-limited, and returns either parsed SNScrape-style models or the raw API response. Source: `https://github.com/vladkens/twscrape` (README retrieved 2026-07-14 via r.jina.ai proxy).

### Why twscrape specifically

The older `snscrape` project scraped the guest web token and worked without login for years, but X began gating search behind authenticated accounts, which broke the guest path. `twscrape` adapts by using a pool of real accounts identified by their `auth_token` and `ct0` cookies. It keeps the same ergonomic query grammar as the web (you pass the exact operator string), handles account rotation when one account hits a limit, and exposes both a parsed model and the raw JSON. For the vault this means a single query string, the same one you would type in the search box, drives the pipeline.

### Installation

```
pip install twscrape
# optional: curl-backed HTTP backend for better reliability
pip install "twscrape[curl]"
```

### Adding accounts from cookies

The most stable setup is to add an account from browser cookies containing `auth_token` and `ct0`. A cookie string that includes `ct0` is activated immediately, with no separate login step.

```
twscrape add_cookie my_account "auth_token=xxx; ct0=yyy"
twscrape accounts
twscrape search "from:xdevelopers lang:en" --limit=20
```

### Minimal Python scraper for a recurring signal query

The following is a working skeleton. It adds a cookie account, runs a vault query, and yields parsed tweets. The query string is exactly the web operator grammar.

```python
import asyncio
from twscrape import API, gather

VAULT_QUERY = (
    "(\"BPJS\" OR \"BPJS Kesehatan\" OR \"asuransi kesehatan\") "
    "(\"ditolak\" OR \"nolak\" OR \"tidak cover\" OR \"klaim ditolak\") "
    "lang:id min_faves:20 min_replies:5 -filter:replies "
    "since_time:PASTE_UNIX_24H_AGO"
)

async def main():
    api = API()  # or API("accounts.db") to persist the pool
    # Add the cookie account once; on subsequent runs the pool is already populated.
    await api.pool.add_account_cookies(
        "my_account", "auth_token=xxx; ct0=yyy"
    )

    # gather() runs a single query to completion up to limit.
    tweets = await gather(api.search(VAULT_QUERY, limit=200))

    for t in tweets:
        print(t.id, t.date, t.user.username, t.like_count, t.text)

asyncio.run(main())
```

### Streaming with the async generator

When you want to process tweets as they arrive, or run an unbounded window, use the async generator form. Note the `aclosing` guard: breaking out of the generator early without closing it leaks the account lock.

```python
import asyncio
import contextlib
from twscrape import API

async def stream():
    api = API()
    query = "(\"pinjol\" OR \"pinjaman online\") \"tagihan\" lang:id min_faves:10"
    try:
        async with contextlib.aclosing(api.search(query, limit=500)) as gen:
            async for tweet in gen:
                # push to the vault's raw intake queue here
                print(tweet.id, tweet.date, tweet.text)
    except asyncio.CancelledError:
        pass

asyncio.run(stream())
```

### Switching the search product

By default `twscrape` queries the Latest tab. To use the Top or Media tab instead, pass `kv={"product": "Top"}` or `kv={"product": "Media"}`. The Top product is what surfaces the highest-engagement matches and is usually the right default for pain-mining, because a high-engagement complaint is a stronger signal than a chronological trickle.

```python
tweets = await gather(api.search("pinjol lang:id", limit=20, kv={"product": "Top"}))
```

### Raw responses for fields the model does not expose

`search_raw` returns the unparsed JSON, which is necessary when you need fields the parsed model omits (for example exact view counts, extended entity media, or the conversation metadata). Use it when building the hashtag-velocity scraper in `01-crawler-scrapper/tiktok/hashtag-velocity-scraper.md` or when you need `quoted_status` nesting.

```python
async for rep in api.search_raw("from:xdevelopers", limit=20):
    print(rep)
```

---

## Constructing direct search URLs

The web search exposes a URL form that is useful for manual checks and for building shareable links. The pattern is `https://twitter.com/search?q=<URL_ENCODED_QUERY>&src=typed_query&f=live`. The `f=live` parameter selects the Latest tab; `f=top` selects Top. Every operator string in this document can be URL-encoded and dropped into that pattern. For example the encoded form of `esa nasa` is `https://twitter.com/search?q=esa%20nasa&src=typed_query&f=live`.

A small helper for the vault's tooling:

```python
from urllib.parse import quote

def x_search_url(query: str, tab: str = "live") -> str:
    return (
        f"https://twitter.com/search?q={quote(query)}"
        f"&src=typed_query&f={tab}"
    )

print(x_search_url('"BPJS" "ditolak" lang:id min_faves:20'))
```

This is also the form the `igorbrigadir/twitter-advanced-search` README uses for its inline example links, so the same encoded query works everywhere.

---

## Translating operators into vault signal queries

The vault's core loop is: find Indonesian money-pain conversations, score them by engagement, and promote the resonant ones into `03-id-business-trends`. The operator grammar maps cleanly onto that loop. Below are reusable query templates, each tied to a pain category already present in the vault.

### Template A: Insurance and healthcare rejection (feeds `03-id-business-trends`)

```
("BPJS" OR "BPJS Kesehatan" OR "asuransi") ("ditolak" OR "nolak" OR "tidak cover" OR "klaim")
lang:id min_faves:30 min_replies:5 -filter:replies
since_time:<<unix 7d ago>>
```

### Template B: E-wallet freeze (feeds the e-wallet freeze pain point mined 2026-07-14)

```
("saldo" OR "akun") ("dibekukan" OR "terblokir" OR "frozen" OR "limitasi") 
("OVO" OR "GoPay" OR "DANA" OR "SeaBank" OR "Jenius")
lang:id min_faves:20
since_time:<<unix 7d ago>>
```

### Template C: Marketplace return fraud (feeds the retur fiktif pain point)

```
("Shopee" OR "Tokopedia" OR "TikTok Shop") ("retur fiktif" OR "barang tidak kembali" OR "refund ditolak")
lang:id min_faves:20 min_replies:3
since_time:<<unix 7d ago>>
```

### Template D: IDX and crypto cashtags (feeds `02-trading-bot` and `05-market-cron`)

```
($BBRI OR $TLKM OR $ASII OR $GOTO OR $BBCA) lang:id
min_faves:50 within_time:1d
```

The `within_time:1d` operator keeps the window tight so the cron picks up only fresh momentum. Cashtags on Indonesian tickers are the cheapest leading indicator of retail sentiment available to the vault.

### Template E: Gig and ojol financial pain (feeds the ojol cooperative branch)

```
("ojol" OR "driver" OR "mitra") ("gaji" OR "potong" OR "komisi" OR "rentenir" OR "utang")
lang:id min_faves:15
since_time:<<unix 14d ago>>
```

### Template F: Regulatory monitoring (feeds the regulatory monitor gap)

```
("Kemenekraf" OR "Permendag" OR "PMK" OR "OJK") ("aturan" OR "rezim" OR "pajak" OR "UMKM")
lang:id min_faves:10 within_time:3d
```

Each template is a string the `twscrape` scraper consumes directly. The vault's cron should store the `since_id` of the highest tweet seen per template, then on the next run substitute that for the `since_time` floor to guarantee no duplicates and no gaps.

---

## Rate limits, account rotation, and the math

X search behind an authenticated account is rate-limited per account, not per IP, which is why a pool of accounts is the correct architecture. `twscrape` rotates accounts automatically when one is throttled. The practical numbers shift constantly, but the operating model is stable.

Assume each account sustains roughly a few hundred search requests per 15-minute window before soft-limiting. With a pool of N accounts the sustainable throughput scales roughly linearly. Ten accounts gives you roughly an order of magnitude more headroom than one. The cost is operational: each account needs a real `auth_token` and `ct0`, which is where the vault's `01-crawler-scrapper/cookies-tokens/storage-safety.md` discipline becomes mandatory. Never store cookies in plaintext in the repo. Use an environment-backed secret store or an encrypted volume, and rotate cookies when an account is flagged.

A conservative daily budget for the vault: six templates, each run once per day over a 7-day window, returning up to a few hundred tweets, is trivially within a 3 to 5 account pool. The expensive operation is backfilling history, which should be batched and throttled. Build the backfill as a separate job from the live cron so a slow backfill never starves the daily sweep.

Proxies are recommended when running many accounts from one egress IP, because X correlates IP behavior across sessions. `twscrape` documents a Swiftproxy residential proxy integration, but any residential or mobile proxy that isolates each account's egress IP reduces the chance of correlated bans. Note that proxy cost is the main recurring expense of this pipeline; it is still far cheaper than the paid API for historical archive access.

---

## Anti-patterns and known footguns

Several operators become unreliable when combined with old timeframes, specifically older than 10 or 30 days depending on the operator. Engagement floors like `min_faves` and `min_retweets` are approximate above roughly 1000, so do not treat a `min_faves:5000` result as a precise cutoff.

The `filter:follows` and `filter:social` operators require an authenticated session whose follow graph is meaningful, and they only work on Top results, not Latest. In a multi-account pool these return different results per account, so they are unsuitable for a reproducible vault query. Avoid them in automated templates.

`list:` cannot be negated, so you cannot express "not on this list." `max_replies` does not exist; only the negated `-min_replies:` form gives you an upper bound. `near:` and `within:` depend on geotagging, which is sparse for Indonesian users, so treat geo-filtered queries as supplementary, not primary.

The wildcard `*` only works inside quoted phrases with surrounding spaces. A bare `*` in the middle of a query is ignored or errors. The `-` negation prefix applies broadly but cannot negate `list:`, `filter:follows`, or `filter:social`.

Spelling correction is on by default and will silently rewrite queries like `radiooooo`. Use `+` or quotes to defeat it when searching for intentional misspellings or brand names.

---

## Wiring the scraper into the vault's intake

The intended architecture is a queue plus state machine, matching the canonical bot skeleton in `02-trading-bot/architectures/event-driven-baseline.md`. Concretely:

One process owns the `twscrape` account pool and runs the six templates on a cron. Each returned tweet is normalized into a small record carrying the tweet id, the parsed date, the author, the like and reply counts, the raw text, and the template id that produced it. The record is pushed onto an intake queue.

A second consumer pulls from the queue, dedupes by tweet id, and scores the record. The score combines engagement floors already enforced by the query with a keyword-weight pass that flags vault-relevant pain terms. High-scoring records are written as raw mining notes into `03-id-business-trends`, following the same three-pain-points-per-commit convention already used in recent commits.

The state machine persists the highest `since_id` seen per template so each run is incremental. On a cold start the run uses `since_time:` windows instead, then switches to `since_id:` once history exists. This mirrors the order-insensitive dedup pattern already present in `06-harga-pangan-papan` fetchers, keeping the vault's append-only, no-churn design consistent.

---

## Indonesian-language specifics

`lang:id` is the primary language filter, but Indonesian-language tweets are frequently misclassified as `lang:und` or even `lang:ms` (Malay), because the classifiers conflate the closely related languages. A robust vault query therefore runs `lang:id` and separately a `lang:und` pass with a stricter Indonesian keyword allowlist, then merges and dedupes. The `lang:und` pass catches Indonesian tweets the classifier missed, at the cost of some noise that the keyword filter removes.

Cashtags and English finance terms (`long`, `short`, `ROI`, `dividen`) appear inside otherwise Indonesian tweets, so do not force `lang:id` on the IDX template if you want to capture bilingual trader discussion. For the pain templates, forcing `lang:id` is correct because the complaint is almost always in Bahasa.

---

---

## Worked combinatorial examples with decoded meaning

The power of the grammar is in composition. Each example below pairs the raw operator string with its plain-language meaning and the encoded URL, so the vault's operators can verify behavior manually before trusting the scraper.

Example one. `(Who OR What OR When OR Where OR Why OR How) ? lang:en` decodes to "any English tweet containing a question word and a question mark." This is the canonical complaint-finder because pain is usually phrased as a question. Encoded URL: `https://twitter.com/search?q=(Who%20OR%20What%20OR%20When%20OR%20Where%20OR%20Why%20OR%20How)%20%3F%20lang%3Aen&src=typed_query&f=live`.

Example two. `"state of the art" since:2019-06-12 until:2019-06-28 #nasamoontunes` decodes to "exact phrase state of the art, posted between 12 and 28 June 2019, containing the hashtag nasamoontunes." This demonstrates the date-window-plus-hashtag pattern the vault uses for event-bound mining.

Example three. `since:2019-06-12 until:2019-06-28 #nasamoontunes` is the same window without the phrase, useful when the phrase is too restrictive and returns nothing.

Example four. `dogs from:NASA` decodes to "tweets containing dogs sent by the NASA account." Encoded: `https://twitter.com/search?q=dogs%20from%3Anasa&src=typed_query&f=live`.

Example five. `#MoonTunes to:NASA` decodes to "tweets replying to NASA that carry the MoonTunes hashtag." Encoded: `https://twitter.com/search?q=%23MoonTunes%20to%3Anasa&src=typed_query&f=live`.

Example six. `@cern -from:cern` decodes to "tweets mentioning CERN but not authored by CERN," the standard mention-only pattern. Encoded: `https://twitter.com/search?q=%40cern%20-from%3Acern&src=typed_query&f=live`.

Example seven. `url:gu.com` decodes to "tweets linking to theguardian.com via its gu.com shortener," demonstrating domain tokenization across shorteners.

Example eight. `kitten filter:social` decodes to "kitten tweets from your algorithmically expanded network," which only works on Top results.

Example nine. `fire near:san-francisco within:10km` decodes to "geotagged fire tweets within 10 km of San Francisco," the geo-bounded alert pattern.

Example ten. `geocode:37.7764685,-122.4172004,10km` is the numeric equivalent of example nine, used when you have precise coordinates from a known event.

Example eleven. `place:96683cc9126741d1` decodes to "tweets tagged with the USA Place ID," useful for country-wide geo sweeps when the country has a stable Place ID.

Example twelve. `from:nasa filter:nativeretweets` decodes to "only the retweets NASA made with the retweet button in the last 7 to 10 days."

Example thirteen. `from:nasa include:nativeretweets` decodes to "NASA's own tweets plus their native retweets," the inclusive variant.

Example fourteen. `from:nasa filter:replies -to:nasa` decodes to "NASA's replies to others, excluding replies where NASA is the target," isolating outbound conversational activity.

Example fifteen. `from:visakanv filter:self_threads` decodes to "only visakanv's self-reply threads," the thread-extraction pattern the vault can use to capture long-form Indonesian explainer threads about money.

Example sixteen. `conversation_id:1140437409710116865 lang:en` decodes to "every tweet in a specific thread," the canonical way to reconstruct a full discussion.

Example seventeen. `from:nasa filter:quote` decodes to "NASA's quote tweets," surfacing commentary-on-other-posts rather than original posts.

Example eighteen. `quoted_tweet_id:1138631847783608321` decodes to "all quotes of one specific tweet," the virality-measurement pattern for tracking how a pain screenshot spreads.

Example nineteen. `quoted_user_id:11348282` decodes to "all quotes of a specific user by numeric ID," broader than the single-tweet form.

Example twenty. `lang:en card_name:poll4choice_text_only OR card_name:poll3choice_text_only OR card_name:poll2choice_text_only` decodes to "English polls of any length," the poll-detection pattern the vault can use to find sentiment polls about brands or policy.

Example twenty-one. `breaking filter:news -filter:has_engagement` decodes to "breaking news tweets with zero engagement," the quiet-signal pattern that sometimes catches emerging stories before they trend.

Example twenty-two. `min_retweets:5000 nasa` decodes to "NASA-related tweets with at least 5000 retweets," a virality floor (approximate above 1000).

Example twenty-three. `min_faves:10000 nasa` decodes to "NASA-related tweets with at least 10000 likes," an engagement floor for high-signal content.

Example twenty-four. `min_replies:1000 nasa` decodes to "NASA-related tweets with at least 1000 replies," the debate-intensity floor.

Example twenty-five. `-min_retweets:500 nasa` decodes to "NASA-related tweets with at most 500 retweets," the inverse floor that surfaces under-the-radar posts.

Example twenty-six. `filter:media cat` decodes to "cat tweets containing any media."

Example twenty-seven. `filter:twimg cat` decodes to "cat tweets with a native pic.twitter.com image," the screenshot-detection pattern critical for the vault because money pain is often a screenshot of a bank app or a rejection notice.

Example twenty-eight. `filter:images cat` decodes to "cat tweets with any image."

Example twenty-nine. `filter:videos cat` decodes to "cat tweets with any video, native or external."

Example thirty. `filter:spaces` decodes to "live Twitter Spaces," which the vault can monitor for real-time money-discussion rooms.

These thirty examples are drawn directly from the upstream operator table and preserve its example links. They form a test corpus: the scraper's query parser should reproduce each encoded URL when given the raw string, and a manual spot-check against the live search page confirms the operator still resolves.

---

## A reusable query-builder module

Rather than hand-concatenating operator strings across six templates, the vault should centralize query construction in one small module. The builder enforces correct spacing, uppercases OR, and stamps the time window. Below is a working implementation.

```python
from datetime import datetime, timezone
from urllib.parse import quote

class XQuery:
    """Fluent builder for X web-search operator strings."""

    def __init__(self):
        self._parts = []

    def words(self, *terms):
        # implicit AND via space; wrap multiword terms in quotes
        for t in terms:
            self._parts.append(f'"{t}"' if " " in t else t)
        return self

    def any_of(self, *terms):
        self._parts.append(" OR ".join(terms))
        return self

    def exact(self, phrase):
        self._parts.append(f'"{phrase}"')
        return self

    def exclude(self, op):
        self._parts.append(f"-{op}")
        return self

    def from_user(self, user):
        self._parts.append(f"from:{user.lstrip('@')}")
        return self

    def to_user(self, user):
        self._parts.append(f"to:{user.lstrip('@')}")
        return self

    def mention(self, user):
        self._parts.append(f"@{user.lstrip('@')}")
        return self

    def lang(self, code):
        self._parts.append(f"lang:{code}")
        return self

    def min_faves(self, n):
        self._parts.append(f"min_faves:{n}")
        return self

    def min_replies(self, n):
        self._parts.append(f"min_replies:{n}")
        return self

    def min_retweets(self, n):
        self._parts.append(f"min_retweets:{n}")
        return self

    def filt(self, name):
        self._parts.append(f"filter:{name}")
        return self

    def since_id(self, tweet_id):
        self._parts.append(f"since_id:{tweet_id}")
        return self

    def since_time(self, dt):
        ts = int(dt.replace(tzinfo=timezone.utc).timestamp())
        self._parts.append(f"since_time:{ts}")
        return self

    def within_time(self, spec):
        # e.g. "1d", "3h", "30m"
        self._parts.append(f"within_time:{spec}")
        return self

    def build(self):
        return " ".join(self._parts)

    def url(self, tab="live"):
        return f"https://twitter.com/search?q={quote(self.build())}&src=typed_query&f={tab}"


# Build template A from the playbook
q = (
    XQuery()
    .any_of('"BPJS"', '"BPJS Kesehatan"', '"asuransi"')
    .any_of('"ditolak"', '"nolak"', '"tidak cover"', '"klaim"')
    .lang("id")
    .min_faves(30)
    .min_replies(5)
    .exclude("filter:replies")
    .within_time("7d")
)
print(q.build())
print(q.url())
```

This module is deliberately permissive: it does not validate that an operator is supported, because the supported set evolves and the vault prefers to discover breakage at runtime (and log it) rather than pre-reject a query that might now work. Validation, if desired, is a separate lint step against the operator catalog in this document.

---

## Normalized intake record schema

Every tweet the scraper emits should be normalized into the same shape before it hits the queue, so downstream consumers are decoupled from `twscrape`'s model. A minimal JSON schema:

```json
{
  "tweet_id": "string, Snowflake ID",
  "conversation_id": "string, nullable",
  "created_at": "ISO8601 UTC timestamp",
  "author": {
    "username": "string, without @",
    "user_id": "string, numeric Snowflake",
    "verified": "boolean (legacy or blue, see note)",
    "followers": "integer, nullable"
  },
  "text": "string, full tweet body",
  "lang": "string, detected language code",
  "like_count": "integer",
  "retweet_count": "integer",
  "reply_count": "integer",
  "quote_count": "integer, nullable",
  "has_media": "boolean",
  "media_types": ["array of strings: image|video|links|twimg"],
  "entities": {
    "hashtags": ["array of strings without #"],
    "cashtags": ["array of strings without $"],
    "urls": ["array of resolved or canonical URLs"],
    "mentions": ["array of usernames without @"]
  },
  "matched_template": "string, template id from the vault cron",
  "query_used": "string, the exact operator string that produced this tweet",
  "scraped_at": "ISO8601 UTC timestamp"
}
```

The `verified` boolean needs a note: post-2023 the platform split legacy verification from paid blue verification, and the web search exposes both `filter:verified` and `filter:blue_verified` as separate operators. The normalized record should capture whichever the source tweet carried, but the scraper cannot always infer the subtype from the parsed model, in which case the raw response (via `search_raw`) must be consulted. The schema therefore treats `verified` as a coarse flag and pushes nuance into a separate `verification_type` field when available.

---

## Troubleshooting table

| Symptom | Likely cause | Fix |
| --- | --- | --- |
| Zero results on a query that works in the box | `filter:follows` or `filter:social` used, which need a meaningful follow graph and only work on Top | Remove those operators from automated templates |
| Query returns far fewer tweets than expected over a 90-day window | Engagement floors become approximate and the index thins beyond 30 days | Narrow the window or lower `min_faves` |
| `max_replies:` throws or is ignored | No `max_*` form exists; only `-min_replies:` | Use `-min_replies:N` for an upper bound |
| Account soft-limited mid-run | Per-account rate limit hit | Let `twscrape` rotate; ensure pool has >=3 accounts |
| Correlated bans across all accounts | All accounts egress from one IP | Put each account behind an isolated residential proxy |
| Indonesian tweets classified as `lang:und` or `lang:ms` | Classifier conflates Bahasa and Malay | Run a `lang:und` pass with a stricter keyword allowlist |
| `*` wildcard does nothing | Wildcard only works inside quoted phrases with spaces | Move it inside quotes, e.g. `"time * this week"` |
| Query silently rewritten (`radiooooo` becomes `radio`) | Spelling correction on by default | Prefix with `+` or wrap in quotes |
| Geotagged query returns almost nothing for Indonesia | Geo-tagging is sparse locally | Treat `near:/within:` as supplementary only |
| `list:` negation fails | `list:` cannot be negated | Restructure the query to avoid "not on list" |

---

## Backfilling history safely

A cold start has no `since_id` state, so the first run must use `since_time:` windows. The risk is that a wide window (say 90 days) over a high-volume template produces tens of thousands of tweets in one burst, which both stresses the account pool and floods the intake queue. The safe pattern is to backfill in bounded chunks.

Start with the most recent 7 days at `limit=2000` per template, persist the highest `since_id`, then walk backward in 7-day `since_time:` chunks, each capped at `limit=2000`, until you reach the desired horizon. Stop early if a chunk returns fewer than the cap, because that signals you have drained the available history for that template. Store the horizon reached per template so a later backfill can resume rather than restart.

This chunked approach mirrors the order-insensitive dedup already present in the `06-harga-pangan-papan` fetchers: the vault prefers idempotent, resumable jobs over monolithic ones, because a cron that fails mid-run must not corrupt or duplicate state.

---

## Monitoring scraper health

Because the pipeline is the vault's primary input, its health must be observable. Three cheap signals cover most failures:

One, track tweets-per-template-per-day. A sudden drop to zero for a template that previously returned hundreds means either the query broke, the account pool is throttled, or the topic went quiet. The cron should alert on a zero-count that follows a non-zero baseline.

Two, track account pool availability. `twscrape accounts` reports each account's state; a pool where all accounts are rate-limited or logged out is a hard failure that needs human cookie rotation. Export this count to the same metrics sink the `05-market-cron` pulse files use.

Three, track query-parse drift. Periodically run the thirty worked examples from this document through the `XQuery` builder and confirm the encoded URLs match the documented ones. A mismatch means the web app changed its encoding or an operator was retired, and the playbook must be updated.

---

## Relationship to other vault branches

This playbook is the input layer for several downstream branches. The pain templates feed `03-id-business-trends`, where three-pain-points-per-commit is the established convention. The cashtag template feeds `02-trading-bot` signal scoring and `05-market-cron` sentiment. The regulatory template feeds the `01-crawler-scrapper/regulatory/` monitor gap. The screenshot-heavy templates (`filter:twimg`) pair with the `07-gaps-and-opportunities` thesis work, because a viral rejection screenshot is often the emotional hook that validates a quantified opportunity.

The account and cookie discipline referenced throughout depends on `01-crawler-scrapper/cookies-tokens/storage-safety.md`, which is already written. The queue-plus-state-machine architecture referenced for the intake depends on `02-trading-bot/architectures/event-driven-baseline.md`, also already written. This playbook assumes both exist and builds on them rather than duplicating their content.

---

## The complete `filter:` operator family

The `filter:` prefix is the most overloaded operator in the grammar. Grouping the documented variants by intent makes template design easier.

Verification and trust filters: `filter:verified`, `filter:blue_verified`, `filter:follows`, `filter:social`, `filter:trusted`. The first two split the post-2023 verification landscape. The last three depend on the querying account's social graph and are unsuitable for automated multi-account templates because each account yields different results.

Media filters: `filter:media`, `filter:twimg`, `filter:images`, `filter:videos`, `filter:periscope`, `filter:native_video`, `filter:vine`, `filter:consumer_video`, `filter:pro_video`, `filter:spaces`, `filter:links`. For the vault, `filter:twimg` and `filter:links` are the highest-value because money pain is frequently a screenshot (`filter:twimg`) or a link to a news article or a government portal (`filter:links`).

Tweet-type filters: `filter:nativeretweets`, `filter:retweets`, `filter:replies`, `filter:self_threads`, `filter:quote`, `filter:has_engagement`. These select structural classes of tweet. `filter:has_engagement` and its negation are the simplest relevance gate when you do not need a numeric floor.

Content-type filters: `filter:news` selects tweets the algorithm classifies as news, which pairs with `-filter:has_engagement` to surface quiet breaking stories. `card_name:poll*` selects polls.

A practical rule for the vault: combine at most one media filter, one tweet-type filter, and one verification filter per query, plus the engagement floors and language. Over-stacking `filter:` operators shrinks the result set aggressively and makes zero-result failures hard to diagnose.

---

## Language codes relevant to the vault

The `lang:` operator accepts ISO 639-1 two-letter codes plus a few special tokens. For Indonesian signal work the relevant set is:

`lang:id` is Bahasa Indonesia, the primary filter. `lang:ms` is Malay, which overlaps heavily with Indonesian in vocabulary; do not confuse the two, but expect spillover. `lang:und` is the "undetermined" bucket, which captures a meaningful fraction of Indonesian-language tweets the classifier failed on. `lang:en` is English, used for the bilingual trader-discussion templates and for the global cashtag sweep. `lang:zh`, `lang:ta`, and `lang:ar` appear in Indonesian diaspora and migrant-worker discussions (relevant to the PMI gaji pain point mined 2026-07-14), so a dedicated template for overseas-Indonesian money pain can target these alongside `lang:id`.

Language detection is per-tweet and explicitly noted by the upstream reference as "not always accurate." The vault therefore treats `lang:` as a strong prior, not ground truth, and applies a keyword allowlist as a second gate before a tweet is promoted to `03-id-business-trends`.

---

## Terms-of-service and risk posture

Scraping authenticated X search sits in a gray area of the platform's terms. This document records the technical facts; it is not legal advice. The operational risk is account-level, not IP-level for the most part: accounts that breach rate limits or trigger automation heuristics get soft-limited or logged out, and in worse cases suspended. The mitigations already embedded in the architecture, account-pool rotation, residential proxies per account, conservative daily limits, and cookie rotation on flag, are the standard defensive posture.

The vault's design minimizes exposure by using a small number of owned accounts for read-only search, never posting, never automating replies, and never reselling data. Read-only signal collection for internal research is the lowest-risk profile available. If the platform tightens guest or authenticated search further, the contingency is the `igorbrigadir` operator catalog's note that some operators stop working on API search, which would force a migration to a self-hosted index or a paid data provider, at which point the cost model in the divergence section becomes the decision input.

---

## Mapping specific vault pain points to ready queries

Each pain point recently mined into `03-id-business-trends` has a corresponding operator query. These are drop-in templates for the cron.

The e-wallet freeze pain point maps to: `("saldo" OR "akun") ("dibekukan" OR "terblokir" OR "frozen" OR "limitasi") ("OVO" OR "GoPay" OR "DANA" OR "SeaBank" OR "Jenius") lang:id min_faves:20 within_time:7d`.

The marketplace retur fiktif pain point maps to: `("Shopee" OR "Tokopedia" OR "TikTok Shop") ("retur fiktif" OR "barang tidak kembali" OR "refund ditolak") lang:id min_faves:20 min_replies:3 within_time:7d`.

The BPJS ditolak RS pain point maps to: `("BPJS" OR "BPJS Kesehatan") ("ditolak" OR "nolak" OR "tidak cover") ("rumah sakit" OR "RS") lang:id min_faves:30 min_replies:5 -filter:replies within_time:7d`.

The PPDB zonasi pain point maps to: `("PPDB" OR "zonasi") ("gagal" OR "tidak diterima" OR "kouta") lang:id min_faves:15 within_time:7d`.

The TikTok Shop suspend pain point maps to: `("TikTok Shop") ("suspend" OR "banned" OR "akun ditutup" OR "pembayaran ditahan") lang:id min_faves:20 within_time:7d`.

The PMI gaji pain point maps to: `("PMI" OR "TKI" OR "pekerja migran") ("gaji" OR "tidak dibayar" OR "potong" OR "agen") lang:id min_faves:10 within_time:14d`.

The JKP klaim ditolak pain point maps to: `("JKP" OR "Jaminan Kehilangan Pekerjaan") ("klaim ditolak" OR "tidak cair" OR "gagal") lang:id min_faves:15 within_time:7d`.

The SIM online gagal pain point maps to: `("SIM" OR "SIM online") ("gagal" OR "error" OR "tidak bisa" OR "server") lang:id min_faves:10 within_time:7d`.

The internet rumah gangguan pain point maps to: `("internet" OR "WiFi" OR "IndiHome" OR "First Media") ("gangguan" OR "putus" OR "lambat" OR "komplain") lang:id min_faves:10 within_time:7d`.

These nine queries are the initial production set for the cron. Each is idempotent given a persisted `since_id`, and each maps to a known vault pain category, so a high-engagement hit is immediately classifiable without a second lookup.

---

## Operator quick-reference table

A single scannable catalog of every operator documented above, grouped by class, for quick lookup while writing templates. Copy the operator verbatim; the grammar is case-sensitive for `OR` and the prefixes.

| Class | Operator | Effect |
| --- | --- | --- |
| Content | `word1 word2` | Implicit AND, any order |
| Content | `a OR b` | Either term, OR uppercase |
| Content | `"exact phrase"` | Exact phrase, also hyphen variants, defeats correction |
| Content | `"a * b"` | Quoted phrase with wildcard |
| Content | `+word` | Force exact spelling |
| Content | `-term` | Exclude term, phrase, or operator |
| Content | `#tag` | Hashtag |
| Content | `$SYM` | Cashtag |
| Content | `What ?` | Question mark match |
| Content | `:) OR :(` | Emoticon match |
| Content | `👀` | Emoji match, needs another operator |
| Content | `url:domain.com` | Domain token match, hyphen as underscore |
| Content | `lang:code` | Language filter |
| User | `from:user` | By author |
| User | `to:user` | Reply to user |
| User | `@user` | Mention, add `-from:user` for mentions only |
| User | `list:id` or `list:slug` | From public list, not negatable |
| User | `filter:verified` | Legacy verified |
| User | `filter:blue_verified` | Paid blue check |
| User | `filter:follows` | From accounts you follow, not negatable |
| User | `filter:social` / `filter:trusted` | Expanded network, Top only |
| Geo | `near:city` | Geotagged place |
| Geo | `near:me` | Near inferred location |
| Geo | `within:radius` | Bounds `near:`, km or mi |
| Geo | `geocode:lat,long,r` | Numeric geo |
| Geo | `place:id` | Place Object ID |
| Time | `since:Y-M-D` | Inclusive start |
| Time | `until:Y-M-D` | Exclusive end |
| Time | `since:Y-M-D_H:M:S_TZ` | Start with time |
| Time | `until:Y-M-D_H:M:S_TZ` | End with time |
| Time | `since_time:unix` | Start unix seconds |
| Time | `until_time:unix` | End unix seconds |
| Time | `since_id:id` | After Snowflake ID |
| Time | `max_id:id` | At or before Snowflake ID |
| Time | `within_time:Nd/H/M/S` | Last N days/hours/min/sec |
| Type | `filter:nativeretweets` | Retweet-button RTs, last 7 to 10d |
| Type | `include:nativeretweets` | Include those RTs |
| Type | `filter:retweets` | Old RT + quotes |
| Type | `filter:replies` | Reply tweets |
| Type | `filter:self_threads` | Self-reply threads |
| Type | `conversation_id:id` | Whole thread |
| Type | `filter:quote` | Quote tweets |
| Type | `quoted_tweet_id:id` | Quotes of a tweet |
| Type | `quoted_user_id:id` | Quotes of a user |
| Type | `card_name:pollNchoice_*` | Polls |
| Engage | `filter:has_engagement` | Any engagement, negatable |
| Engage | `min_retweets:N` | Min RTs, approximate >1000 |
| Engage | `min_faves:N` | Min likes |
| Engage | `min_replies:N` | Min replies |
| Engage | `-min_retweets:N` | Max RTs |
| Engage | `-min_faves:N` | Max likes |
| Engage | `-min_replies:N` | Max replies, only upper bound form |
| Media | `filter:media` | Any media |
| Media | `filter:twimg` | Native pic.twitter.com |
| Media | `filter:images` | Any image |
| Media | `filter:videos` | Any video |
| Media | `filter:periscope` | Periscope |
| Media | `filter:native_video` | Twitter-owned video |
| Media | `filter:vine` | Vine |
| Media | `filter:consumer_video` | Native video only |
| Media | `filter:pro_video` | Amplify video |
| Media | `filter:spaces` | Spaces |
| Media | `filter:links` | Contains URL |
| Media | `filter:news` | Algorithmic news classification |

---

## Running the daily cron: a concrete orchestration script

The following script is a runnable skeleton for the vault's daily sweep. It loads account cookies from an environment variable, runs the nine production templates, normalizes each tweet, and emits a JSON lines file the downstream consumer reads. Replace the cookie source with the encrypted store described in `storage-safety.md`; never hardcode cookies.

```python
import asyncio
import json
import os
from datetime import datetime, timezone

from twscrape import API, gather

# Production templates from the "Mapping" section.
TEMPLATES = {
    "ewallet_freeze": '("saldo" OR "akun") ("dibekukan" OR "terblokir" OR "frozen" OR "limitasi") ("OVO" OR "GoPay" OR "DANA" OR "SeaBank" OR "Jenius") lang:id min_faves:20 within_time:7d',
    "retur_fiktif": '("Shopee" OR "Tokopedia" OR "TikTok Shop") ("retur fiktif" OR "barang tidak kembali" OR "refund ditolak") lang:id min_faves:20 min_replies:3 within_time:7d',
    "bpjs_rs": '("BPJS" OR "BPJS Kesehatan") ("ditolak" OR "nolak" OR "tidak cover") ("rumah sakit" OR "RS") lang:id min_faves:30 min_replies:5 -filter:replies within_time:7d',
    "ppdb": '("PPDB" OR "zonasi") ("gagal" OR "tidak diterima" OR "kouta") lang:id min_faves:15 within_time:7d',
    "ttshop_suspend": '("TikTok Shop") ("suspend" OR "banned" OR "akun ditutup" OR "pembayaran ditahan") lang:id min_faves:20 within_time:7d',
    "pmi_gaji": '("PMI" OR "TKI" OR "pekerja migran") ("gaji" OR "tidak dibayar" OR "potong" OR "agen") lang:id min_faves:10 within_time:14d',
    "jkp": '("JKP" OR "Jaminan Kehilangan Pekerjaan") ("klaim ditolak" OR "tidak cair" OR "gagal") lang:id min_faves:15 within_time:7d',
    "sim_online": '("SIM" OR "SIM online") ("gagal" OR "error" OR "tidak bisa" OR "server") lang:id min_faves:10 within_time:7d',
    "internet": '("internet" OR "WiFi" OR "IndiHome" OR "First Media") ("gangguan" OR "putus" OR "lambat" OR "komplain") lang:id min_faves:10 within_time:7d',
}


def normalize(t, template_id, query):
    return {
        "tweet_id": str(t.id),
        "created_at": t.date.isoformat() if t.date else None,
        "author": {"username": t.user.username, "user_id": str(t.user.id)},
        "text": t.text,
        "lang": t.lang,
        "like_count": t.like_count,
        "retweet_count": t.retweet_count,
        "reply_count": t.reply_count,
        "matched_template": template_id,
        "query_used": query,
        "scraped_at": datetime.now(timezone.utc).isoformat(),
    }


async def run():
    api = API()
    cookie = os.environ["X_AUTH_COOKIE"]  # auth_token=...; ct0=...
    await api.pool.add_account_cookies("vault_account", cookie)

    out_path = f"05-market-cron/data/x-intake-{datetime.now(timezone.utc):%Y%m%d}.jsonl"
    total = 0
    with open(out_path, "w", encoding="utf-8") as fh:
        for tid, q in TEMPLATES.items():
            tweets = await gather(api.search(q, limit=500, kv={"product": "Top"}))
            for t in tweets:
                fh.write(json.dumps(normalize(t, tid, q), ensure_ascii=False) + "\n")
                total += 1
    print(f"wrote {total} tweets to {out_path}")


if __name__ == "__main__":
    asyncio.run(run())
```

The script writes one JSON lines file per day into `05-market-cron/data/`, matching the existing pulse-file convention, so the downstream scorer and the market-cron pipeline read from the same location. The `kv={"product": "Top"}` switch surfaces high-engagement matches first, which is what the vault wants for pain mining. The `limit=500` per template is conservative; raise it once the account pool is verified to sustain the throughput without soft-limiting.

---

## Source index

1. igorbrigadir, "Advanced Search on Twitter," GitHub, `https://github.com/igorbrigadir/twitter-advanced-search` (operator table; most rows last checked 2022-11-01, later annotations 2022-11-10 and 2024-01-31). Primary operator reference.
2. vladkens, "twscrape: Python library and CLI for X/Twitter scraping with multi-account rotation and built-in rate-limit handling," GitHub, `https://github.com/vladkens/twscrape` (README retrieved 2026-07-14 via r.jina.ai proxy). Scraper architecture, CLI, and Python API.
3. Luca Hammer, "Twitter Search Guide," freshvanroot.com, `https://freshvanroot.com/blog/2019/twitter-search-guide-by-luca/` (update notice 2024-03-04; retrieved 2026-07-14 via r.jina.ai proxy). Engagement and time operators, AND/OR/exact-match semantics.
4. X Developer Platform, "Search Tweets introduction," `https://developer.x.com/en/docs/x-api/tweets/search/introduction` (retrieved 2026-07-14 via r.jina.ai proxy). Pay-per-usage pricing, owned-reads at $0.001 per resource, Enterprise tier, divergence note that web operators do not apply to API search.
5. X Help Center, "Advanced search," `https://help.twitter.com/en/using-twitter/twitter-advanced-search` (HTTP 403 on direct fetch 2026-07-14; operator catalog cross-referenced via source 1, which adapts the TweetDeck help content). Source noted as unreachable at fetch time; no data invented from it.
6. TweetDeck Help, advanced features, `https://help.twitter.com/en/using-twitter/advanced-tweetdeck-features` (cited by source 1 as the origin of several operators).

---

## Open questions for the next tick

The `within_time:` operator and the `since_time:/until_time:` operators appear to serve overlapping purposes; a controlled test comparing their result sets on an identical query would settle which is more reliable for the daily cron. The `filter:blue_verified` versus `filter:verified` split post-2023 verification changes means legacy "trusted source" signals now require explicit handling; the vault should decide whether blue-check accounts are a signal or noise for money-pain mining. The geographic sparsity of Indonesian geotagging means `near:/within:` are currently documented as supplementary only, but a future test with a known Jakarta-event hashtag could quantify their recall.
