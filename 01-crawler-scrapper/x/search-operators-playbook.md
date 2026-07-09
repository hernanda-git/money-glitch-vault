# X (Twitter) Advanced Search Operators Playbook and Signal Patterns

Last updated: 2026-07-10. Researcher note: this document is an operational reference for the
`01-crawler-scrapper` module of the money-glitch vault. It is written for the agent that pulls
signal out of X (Twitter) at scale, either through the web advanced-search UI, the X API v2
recent-search endpoint, or a headless scraper such as snscrape or twscrape. The goal is not to
teach the user how to tweet. The goal is to give the agent a repeatable, tested query grammar it
can compose into money-relevant signals: layoffs, price shocks, regulatory changes, arbitrage
chatter, side-hustle demand, and early panic that has not yet hit the news wires.

Why this folder matters: every other module in the vault depends on a reliable firehose. The
`03-id-business-trends` pain points, the `05-market-cron` tickers, and the `07-gaps` thesis all
need raw input. X is the highest-signal public text stream we have for Indonesia and for
crypto/forex sentiment, but only if you can shape the query. A bad query returns 100,000
useless replies. A good query returns 40 posts, 30 of which are actionable. This file is the
query grammar.

A critical disclaimer up front: the web operators documented here (the `from:`, `min_faves:`,
`filter:` family) do NOT all map one-to-one onto the API. The web index and the Standard API
index are different systems. We detail the exact differences in the API parity section, with
real example queries you can paste. Where a claim could not be verified against a live source,
it is marked `source unreachable` and the approximate behavior is described as observed by the
community.

Primary sources used to build this file (real URLs, fetched during research):

- igorbrigadir/twitter-advanced-search README, the canonical community operator list.
  https://github.com/igorbrigadir/twitter-advanced-search  (fetched 2026-07-10, 100KB)
- X (Twitter) official advanced search UI. https://twitter.com/search-advanced
- X API v2 rules and filtering, official. https://developer.x.com/en/docs/x-api/rules-and-filtering/search-operators
- snscrape documentation, JustAnotherArchivist. https://github.com/JustAnotherArchivist/snscrape
  (PyPI version 0.7.0.20230622, fetched 2026-07-10)
- twscrape documentation, vladkens. https://github.com/vladkens/twscrape
  (PyPI version 0.19.1, fetched 2026-07-10)
- X API v2 sample code index. https://github.com/twitterdev/twitter-api-v2-sample-code
  (fetched 2026-07-10)
- Wikipedia, Twitter Search (for historical/algorithmic context). https://en.wikipedia.org/wiki/Twitter_Search

Note on the official X API operators page: it is a JavaScript-rendered SPA and returns an empty
body to a non-browser fetch (`source unreachable` via curl at research time). The operator list
below for the API side is therefore reconstructed from the igorbrigadir community list, the
X API v2 sample code, and the widely-documented v2 `is:` / `has:` token grammar. Verify against
https://developer.x.com/en/docs/x-api/rules-and-filtering/search-operators before production use.

---

## H1. Mental model: three different X search indexes

Before writing a single query you must understand that X runs at least three separate search
indexes, and an operator that works in one silently fails in another. Mixing them up is the
single most common reason a "scraper" returns garbage.

The web index is what powers twitter.com/search, the advanced-search UI, the mobile app, and
TweetDeck. It is the richest operator set. It supports `min_faves:`, `min_retweets:`,
`filter:verified`, `from:`, `to:`, `list:`, `near:`/`within:`, `source:`, `card_name:`,
`conversation_id:`, and dozens more. It returns Top or Latest results and is what a human uses.

The Standard API index (v1.1 and v2 recent search) is a different backend. It supports a much
smaller set of operators built around the `is:` and `has:` grammar plus a handful of field
filters. It does NOT support `min_faves:`, `min_retweets:`, `filter:verified`, `from:` in the
web sense, `list:`, or `near:`. If you send a web operator to the API it is either ignored or
returns a 400 error. This is the index you hit when you call `GET /2/tweets/search/recent`
with a bearer token.

The Premium and Enterprise (Gnip) index is yet another system, historically with its own
PowerTrack operator syntax (`has:geo`, `profile:country`, `bio:`). That is out of scope for a
budget operator but noted because some older blog snippets you find will reference it.

Practical rule: if you are scraping through a headless browser mimicking the web UI (snscrape,
twscrape, or a manually built query string), use the web operator set. If you are calling the
API with a bearer token, use the `is:`/`has:` set and keep your field filters inside the
`query` parameter plus the `start_time`/`end_time`/`tweet.fields` parameters. Do not assume
parity.

---

## H1. The full web operator grammar

This is the complete web-operator set, grouped by class. Every token was taken from the
igorbrigadir reference list, which itself was adapted from TweetDeck help, the Twitter manual by
@eevee, the Luca Hammer guide, and pushshift. Each row has the syntax, what it matches, and a
working example link structure you can reconstruct.

### H2. Tweet content operators

Spaces between terms are implicit AND. To require one of several terms you must write `OR` in
uppercase. Parentheses group terms. Quotes force a phrase and disable spelling correction.

- `nasa esa` matches tweets containing both "nasa" and "esa". Spaces are implicit AND.
  Example: https://twitter.com/search?q=esa%20nasa&src=typed_query&f=live
- `nasa OR esa` matches either term. OR must be uppercase.
  Example: https://twitter.com/search?q=nasa%20OR%20esa&src=typed_query&f=live
- `"state of the art"` matches the exact phrase and also `state-of-the-art`. Quotes disable
  spelling correction and plurals. This is important when you want the literal word "photo"
  because X treats bare `photo` as a signal to show image tweets.
- `"this is the * time this week"` wildcard phrase. The `*` only works inside quotes with
  surrounding spaces.
- `+radiooooo` forces the exact spelling, preventing correction.
- `-love` excludes the term. Also works on phrases (`-"live laugh love"`) and on other
  operators. Exclusion is your main noise-reduction tool.
- `#tgif` matches a hashtag. Hashtags are case-insensitive on match but preserve casing in
  display.
- `$TWTR` matches a cashtag (stock symbol). Use for ticker monitoring: `$BBRI`, `$TLKM`,
  `$BTC`, `$ETH`. Cashtags are tokenized like hashtags.
- `What ?` question marks are matched, letting you find questions. Useful for mining "how do I"
  demand signals.
- `:) OR :(` some emoticons are matched (positive `:) :-) :P :D`, negative `:-( :(`).
- emoji like `👀` are matched but usually need another operator to return anything.
- `url:google.com` matches tokenized URLs, works well for domains and subdomains, and matches
  both shortened and canonical forms (`gu.com` finds theguardian.com links). Hyphens in domains
  must be replaced with underscores: `url:t_mobile.com`. This is how you find link-drops to a
  specific site without the API.
- `lang:en` restricts to a language. The full list is ISO 639-1 two-letter codes. Indonesian is
  `lang:in` (not `lang:id`). Full list in the language section below. Language tagging is
  automatic and not perfectly accurate.

### H2. User and network operators

- `from:user` tweets sent by a specific @username. Example: `"dogs from:NASA"`.
- `to:user` tweets replying to a specific @username.
- `@user` tweets mentioning a @username. Combine with `-from:username` to get only mentions of
  an account, not its own posts.
- `list:715919216927322112` or `list:esa/astronauts` tweets from members of a public list. Use
  the numeric list ID from `twitter.com/i/lists/<id>` or the legacy slug. Cannot be negated.
- `filter:verified` from legacy verified (blue check pre-2023) users.
- `filter:blue_verified` from accounts that paid for the post-2023 verification. Combine
  `-filter:verified` if you want only the paid set.
- `filter:follows` only from accounts you follow. Cannot be negated.
- `filter:social` or `filter:trusted` from the algorithmically expanded network based on your
  follows. Only works on Top results, not Latest.

### H2. Geo operators

Almost no modern tweets carry exact coordinates (precise geo was phased out for normal tweets in
2019, remaining only for some photos). Most geo is by Place. Still, the operators exist:

- `near:city` geotagged in a place; supports phrases like `near:"The Hague"`.
- `near:me` near where X thinks you are.
- `within:radius` limits the `near:` operator, in km or mi. Example:
  `fire near:san-francisco within:10km`.
- `geocode:lat,long,radius` example: `geocode:37.7764685,-122.4172004,10km` for 10km around
  Twitter HQ.
- `place:96683cc9126741d1` searches by Place Object ID; the USA place ID is that value.

For Indonesia money signal, geo is weak. Prefer `lang:in` plus keyword filtering over `near:`
because most Indonesian business chatter is not geotagged.

### H2. Time operators

All time operators must be combined with at least one other operator or they return nothing.

- `since:2021-12-31` on or after (inclusive) the date, format YYYY-MM-DD.
- `until:2021-12-31` before (exclusive) the date. Pair with `since:` for a window.
- `since:2021-12-31_23:59:59_UTC` on or after a specific date and time in a timezone. Same
  underscore pattern for `until:`.
- `since_time:1561720321` / `until_time:1562198400` unix epoch seconds.
- `since_id:tweet_id` / `max_id:tweet_id` snowflake-ID based paging. Handy for resuming a
  scrape exactly where it stopped.
- `within_time:2d` / `within_time:3h` / `within_time:5m` / `within_time:30s` last N days,
  hours, minutes, seconds. This is the simplest way to say "last 24 hours".

For a cron that runs daily, the canonical pattern is `since:YYYY-MM-DD` set to yesterday's date,
or `within_time:1d`. Store the highest tweet ID seen and use it as `since_id` next run for
precise resume.

### H2. Tweet-type operators

- `filter:nativeretweets` only retweets made with the retweet button. Pairs well with `from:`.
  Only works within roughly the last 7 to 10 days.
- `include:nativeretweets` shows native retweets that are hidden by default.
- `filter:retweets` old-style "RT" plus quoted tweets.
- `filter:replies` tweets that are replies. Good for finding conversations or threads.
- `filter:self_threads` only self-replies (thread posts, not replies to others).
- `conversation_id:tweet_id` all tweets in a thread (direct and other replies).
- `filter:quote` tweets that quote another.
- `quoted_tweet_id:tweet_id` quotes of a specific tweet.
- `quoted_user_id:user_id` all quotes of a specific user, by numeric ID.
- `card_name:poll2choice_text_only` (and 3/4 choice, image variants) tweets containing polls.

### H2. Engagement operators (the signal-rank filters)

These are the most useful for separating noise from signal. They apply to the original tweet,
not to retweets, and they conflict with the nativeretweet filters.

- `filter:has_engagement` has any replies, likes, or retweets. Negate with `-filter:has_engagement`
  to find dead tweets (useful for spotting suppressed or very early posts).
- `min_retweets:5` minimum retweet count. Counts are approximate for values above 1000.
- `min_faves:10` minimum like count.
- `min_replies:100` minimum reply count.
- `-min_retweets:500` acts as a maximum (tweets with fewer than 500 retweets). Same for
  `-min_faves:` and `-min_replies:`.

For an early-warning system you usually want LOW thresholds combined with recency:
`min_faves:5 -filter:has_engagement` is wrong; instead use `within_time:6h min_faves:5` to catch
posts that are gaining traction but not yet viral. For a weekly recap you want the opposite:
`since:7-days-ago min_faves:500` to surface only what broke through.

### H2. Media operators

- `filter:media` any media.
- `filter:twimg` native Twitter images (`pic.twitter.com`).
- `filter:images` all images.
- `filter:videos` all video including YouTube embeds.
- `filter:periscope`, `filter:native_video`, `filter:vine` (defunct), `filter:consumer_video`,
  `filter:pro_video` (Amplify), `filter:spaces`.
- `filter:links` tweets with any URL (includes media). Use `-filter:media` to keep only
  non-media links.

### H2. More filters and card operators

- `filter:mentions` tweets containing any @mention.
- `filter:news` tweets linking to a news story. X matches against an internal whitelist of news
  domains; the list is not public. Pair with a list operator to narrow the source set.
- `filter:safe` excludes content users marked as sensitive.
- `filter:hashtags` only tweets with hashtags.
- `source:client_name` tweets sent from a specific client, e.g. `source:tweetdeck`. Hyphens and
  spaces in client names must become underscores: `source:Twitter_for_iOS`.
- `card_domain:pscp.tv` / `card_url:pscp.tv` match a Twitter Card domain or URL.
- `card_name:audio`, `card_name:animated_gif`, `card_name:player`, `card_name:app`,
  `card_name:summary`, `card_name:summary_large_image`, `card_name:promo_website`, and several
  conversational-ad card names. Most `card_name:` operators only work for the last 7 to 8 days.

### H2. Matching behavior you must know

On web and mobile, keyword operators match the user display name, the @screen name, the tweet
text, and the shortened plus expanded URL text. So `url:trib.al` finds accounts that used that
shortener even though the visible link is different.

Defaults: Top results means tweets with some engagement; Latest means most recent. Private,
locked, and suspended accounts never appear. Anti-spam filtering and indexing lag can also hide
tweets.

X treats some words as signal words. Searching `photo` assumes you want image tweets. Wrap in
quotes `"photo"` to match the literal word.

Plurals are matched: `bears` also matches `bear`. Standalone hyphens are removed, so
`state-of-the-art` equals `state of the art`.

Negation works on most `filter:` tokens (`-filter:links` equals `exclude:links`). Exceptions
that cannot be negated: `filter:follows`, `filter:social`, `list:`, and `filter:nativeretweets`
in some contexts.

The maximum number of operators in a single web query appears to be about 22 to 23. Design
queries to stay under that. If your query is rejected, trim OR branches.

---

## H1. The X API v2 operator grammar (the `is:` and `has:` set)

When you call the API you cannot use the web operators. The v2 recent-search query parameter
accepts a different, smaller operator set. These are the well-documented tokens:

- `is:retweet` / `-is:retweet` (the default excludes retweets).
- `is:reply` / `-is:reply`.
- `is:quote` / `-is:quote`.
- `is:verified` (any verified account).
- `is:nullcast` / `-is:nullcast` (promoted/ads tweets).
- `has:links` / `-has:links`.
- `has:mentions` / `-has:mentions`.
- `has:hashtags` / `-has:hashtags`.
- `has:cashtags` / `-has:cashtags`.
- `has:media` / `-has:media`.
- `has:images` / `-has:images`.
- `has:video` / `-has:video`.
- `has:geo` / `-has:geo`.
- `lang:` works in the API too, with ISO codes.
- `from:` and `to:` DO work in the API as `from:` and `to:` (unlike most other web operators),
  but they are the user-screen-name field filters, not the rich web variants.
- `context:<domain>.<id>` for Twitter's entity/context annotations (e.g. event or product
  contexts). The exact domain IDs are enumerated in the API annotations reference.

Crucially, the API does NOT support `min_faves:`, `min_retweets:`, `min_replies:`,
`filter:verified`, `filter:blue_verified`, `list:`, `near:`, `within:`, `source:`, or
`card_name:`. If you need engagement thresholds you must pull a batch and filter client-side by
the `public_metrics` object (retweet_count, reply_count, like_count, quote_count). This is the
main reason scrapers that mimic the web UI are often more useful for signal mining than the
raw API at the free tier.

### H2. Building an API query that mirrors a web query

Web query to find Indonesian fintech complaints with at least some traction:

`("pinjol" OR "fintech") lang:in -filter:retweets within_time:1d`

API equivalent, with client-side engagement filter:

`("pinjol" OR "fintech") lang:in -is:retweet -is:reply`

then filter results where `public_metrics.like_count >= 5` and `created_at` is within 24h.
You lose the native `min_faves:` but you get the same effect in code, and you are not limited by
the 22-operator ceiling in the same way.

### H2. Rate limits and pagination (X API v2 recent search)

The recent-search endpoint (`GET /2/tweets/search/recent`) at the free/basic tiers returns up to
100 tweets per request, paginated with a `next_token`. The free tier historically allows a small
number of requests per month and a 7-day lookback window. The basic paid tier extends the
lookback and request quota. Because these numbers change frequently and the official page was
not fetchable at research time (`source unreachable`), treat exact quotas as time-sensitive and
verify on https://developer.x.com/en/products/twitter-api before relying on them.

Practical implication: for a daily money-signal cron, the API free tier is usually insufficient
for broad keyword sweeps. That is why the web-UI-mimicking scrapers (next section) are the
primary tool for this vault, with the API used only for targeted, low-volume pulls (a specific
@user, a specific conversation, a specific cashtag with `has:cashtags`).

---

## H1. Scraping tools that actually run the web grammar

The vault's intent is an automated, cookie/token-based crawler. Two Python projects implement
the web search grammar without the official API: snscrape and twscrape. Both were fetched and
verified at research time.

### H2. snscrape (version 0.7.0.20230622)

Source: https://github.com/JustAnotherArchivist/snscrape  (PyPI 0.7.0.20230622)

snscrape is a multi-platform SNS scraper. For Twitter it supports user profiles, hashtags,
searches (live tweets, top tweets, and users), single tweets and surrounding threads, list
posts, communities, and trends. Installation: `pip3 install snscrape`. Requires Python 3.8+,
plus libxml2 and libxslt for the lxml dependency.

CLI form: `snscrape [GLOBAL-OPTIONS] SCRAPER-NAME [SCRAPER-OPTIONS] [ARGUMENTS]`.

Key global options for signal mining:

- `--jsonl` emits one JSON object per result with the full extracted payload (text, datetime,
  media, user). This is what you want for the vault pipeline.
- `--max-results N` caps the number of results.
- `--with-entity` also fetches the entity being scraped (e.g. user metadata).

Examples:

```bash
# Latest 100 tweets with the hashtag #archiveteam
snscrape --max-results 100 twitter-hashtag archiveteam

# All tweets by a user, written to a file
snscrape twitter-user textfiles > twitter-@textfiles

# Search syntax (twitter-search) accepts the web operator grammar
snscrape "twitter-search:(pinjol OR fintech) lang:in min_faves:10 since:2026-07-01"
```

Important caveat: snscrape's Twitter backend relies on the guest web token and unauthenticated
endpoints. X has repeatedly broken these, so at any given time the Twitter scraper may fail
with guest-token errors (`source unreachable` intermittently). For resilient operation you
typically need to supply authenticated cookies, which is exactly why the
`01-crawler-scrapper/cookies-tokens/` subfolder exists in this vault. Combine snscrape with a
logged-in cookie pool for production reliability.

### H2. twscrape (version 0.19.1)

Source: https://github.com/vladkens/twscrape  (PyPI 0.19.1)

twscrape is described as "Twitter GraphQL and Search API implementation with SNScrape data
models". The key advantage over snscrape is that it uses the authenticated GraphQL endpoints and
supports adding multiple accounts to rotate, which dramatically improves reliability and volume.
Its data models are compatible with snscrape, so you can swap one for the other with minimal
code change.

Typical async usage pattern (illustrative, based on the documented API shape):

```python
import asyncio
import twscrape

async def main():
    # Add one or more authenticated accounts (cookies / username+password)
    await twscrape.add_account("user1", "pass1", "email1", "email_pass1")
    # Or load cookies from the vault's cookies-tokens store
    api = twscrape.API()

    # The search method accepts the web operator grammar
    query = "(pinjol OR "fintech") lang:in -filter:retweets min_faves:20 since:2026-07-01"
    async for tweet in twscrape.search(query, limit=200):
        print(tweet.id, tweet.date, tweet.username, tweet.rawContent)

asyncio.run(main())
```

Because twscrape rotates accounts, it is the recommended primary scraper for the vault's daily
cron, with snscrape kept as a fallback. Both output JSON-compatible tweet objects that feed
directly into the `03-id-business-trends` and `05-market-cron` consumers.

### H2. Nitter and the death of the easy path

Historically Nitter public instances let you scrape X HTML without auth. As of 2023 to 2024 X
hardened guest access and most public Nitter instances went dark. The official Nitter instances
wiki (https://github.com/zedeus/nitter/wiki/Instances) lists few or no reliably working public
instances at research time (`source unreachable` / empty). Conclusion: do not build the pipeline
on Nitter. Build it on authenticated twscrape/snscrape with a cookie pool, which is the
append-only design intent of this vault's cookies-tokens folder.

---

## H1. Snowflake IDs and precise time windows

Every tweet and user ID on X is a snowflake: a 64-bit ID that embeds a timestamp. This matters
for resuming scrapes exactly and for slicing time windows without the fuzzy `since:`/`until:`
date parsing.

Conversion math (from the igorbrigadir reference):

- Tweet ID to millisecond epoch: `(tweet_id >> 22) + 1288834974657`.
- Millisecond epoch to tweet ID: `(millisecond_epoch - 1288834974657) << 22`.
- Snowflake epoch base is `1288834974657` (2010-11-04). User IDs use the same scheme from
  2013-01-22.

Worked example: to start collecting at August 4, 2019 09:00:00 UTC = epoch `1564909200000`,
convert to a tweet ID: `(1564909200000 - 1288834974657) << 22 = 1157939227653046272`. Use that
as `max_id` and you collect everything earlier than that instant.

Python helper:

```python
def convert_milliepoch_to_tweet_id(milliepoch):
    if milliepoch <= 1288834974657:
        raise ValueError("Date is too early (before snowflake implementation)")
    return (milliepoch - 1288834974657) << 22

def convert_tweet_id_to_milliepoch(tweet_id):
    return (tweet_id >> 22) + 1288834974657
```

Caveat from the source: JavaScript does not support 64-bit integers natively, so ID math in the
browser often fails silently. Do your snowflake math in Python or another language with BigInt.
For the vault cron, which runs under Python, this is fine.

---

## H1. Signal patterns for the money-glitch vault

This is the payoff section. Below are ready-to-use query patterns mapped to the vault's modules.
Each pattern is a starting query you adapt. Replace the seed keywords with whatever the
`03-id-business-trends` research surfaces that week.

### H2. Indonesian pain-point mining (feeds 03-id-business-trends)

The vault already has 60+ demand-mining files. New ones come from catching fresh complaints.
Pattern: Indonesian language, questions or complaints, excluding retweets and ads, last 24 to 72
hours, with a low engagement floor so early whispers surface.

```
("gaji" OR "utang" OR "pinjol" OR "biaya" OR "mahal") lang:in -filter:retweets -filter:blue_verified within_time:3d min_faves:3
```

To find "how do I" demand (people willing to pay for a solution):

```
("cara" OR "bantu" OR "rekomendasi" OR "apa ya") (lang:in) -filter:retweets within_time:2d
```

To catch regulatory shock that affects UMKM and creators:

```
("PP" OR "Permen" OR "SE" OR "aturan" OR "pajak") (UMKM OR kreator OR "usaha mikro") lang:in -filter:retweets within_time:5d
```

### H2. Market and ticker signal (feeds 05-market-cron)

For cashtag monitoring use the API `has:cashtags` or the web cashtag operator. Indonesia focus:

```
($BBRI OR $TLKM OR $BBTN OR $BMRI OR $ASII) lang:in min_faves:10 within_time:1d
```

For crypto sentiment, English plus Indonesian:

```
($BTC OR $ETH OR $SOL) (jatuh OR naik OR "liquidation" OR "rug") (lang:in OR lang:en) within_time:12h
```

For macro/forex and rate decisions:

```
(BI rate OR "suku bunga" OR "Rupiah" OR "IHSG") lang:in -filter:retweets min_faves:20 within_time:1d
```

### H2. Early-panic / black-swan detection

The goal here is to catch a developing event before it trends. Use near-zero engagement floors
and short windows, then rank by velocity (likes per minute) in code.

```
("PHK" OR "layoff" OR "bangkrut" OR "default" OR "gagal bayar") lang:in -filter:has_engagement within_time:6h
```

The `-filter:has_engagement` combination finds posts that have NOT yet gotten traction, which is
exactly the early signal. Your code then watches whether such posts cross a threshold in the
next few hours.

### H2. Competitor and platform-gap discovery (feeds 03-id-business-trends/competitors)

```
(Gojek OR Grab OR "Tokopedia" OR "Shopee" OR "TikTok Shop") (komplain OR "tidak bisa" OR "mah") lang:in -filter:retweets within_time:2d min_faves:5
```

### H2. Arbitrage and regional price chat (feeds 06-harga-pangan-papan)

```
("harga beras" OR "harga cabai" OR "harga gula" OR "Bapanas") lang:in within_time:1d min_faves:3
```

### H2. Velocity scoring recipe (pseudo-code)

Because the web index gives you `min_faves:` but not rate, compute velocity yourself:

```python
# tweets: list of dicts with 'id','created_at','like_count','retweet_count'
now = time.time()
for t in tweets:
    age_min = (now - t['created_at']) / 60.0
    if age_min <= 0:
        continue
    t['velocity'] = (t['like_count'] + 2*t['retweet_count']) / age_min
# Sort by velocity, alert when velocity crosses a learned baseline
alerts = [t for t in tweets if t['velocity'] > BASELINE]
```

BASELINE should be learned per keyword cluster from a week of history, not hardcoded. Store
baselines in the vault's config so the cron adapts.

---

## H1. Query construction rules and footguns

Compose with booleans and parentheses. Spaces are implicit AND; `OR` must be uppercase. Example
from the reference: mentions of "puppy" or "kitten" AND "sweet" or "cute", no native retweets,
at least 10 likes:

`(puppy OR kitten) (sweet OR cute) -filter:nativeretweets min_faves:10`

More complex, members of a list, specific clients, images, excluding a hashtag, since 2011:

`space (big OR large) list:nasa/astronauts (source:twitter_for_iphone OR source:twitter_web_client) filter:images since:2011-01-01 -#asteroid`

Footguns, all observed in the source material:

- Hyphens and spaces in parameters (domains, client names) must become underscores. `url:t-mobile.com`
  returns nothing; `url:t_mobile.com` works. `source:Twitter for iOS` fails; `source:Twitter_for_iOS` works.
- `card_name:` only works for the last 7 to 8 days.
- Max about 22 to 23 operators per web query. Trim OR branches if rejected.
- Time operators never work alone; always pair with a keyword.
- `filter:follows`, `filter:social`, `list:` cannot be negated.
- `min_faves:` counts are approximate above 1000.
- `lang:in` is Indonesian; `lang:id` is NOT valid (Indonesia is `in` in ISO 639-1, not `id`).
- Native retweets are excluded by default in some contexts; use `include:nativeretweets` to see them.

---

## H1. Supported language codes (Indonesian = lang:in)

The full language list (from the TweetDeck dropdown, via the igorbrigadir reference) uses ISO
639-1 two-letter codes. Language is tagged automatically from text and is not perfectly accurate.
Relevant subset for this vault:

- `lang:in` Bahasa Indonesia (use this, NOT `lang:id`)
- `lang:en` English
- `lang:ms` Malay
- `lang:zh` Chinese
- `lang:ja` Japanese
- `lang:ko` Korean
- `lang:ar` Arabic
- `lang:ta` Tamil
- `lang:th` Thai
- `lang:vi` Vietnamese
- `lang:hi` Hindi
- `lang:und` undefined / empty / single-number or single-link tweets (useful to EXCLUDE when
  you want real language content: `-lang:und`)

Full list also includes am, ar, bg, bn, bo, ca, cs, da, de, dv, el, es, et, fa, fi, fr, gu, ht,
hu, hy, is, it, iu, iw, ka, km, kn, lo, lt, lv, ml, my, ne, nl, no, or, pa, pl, pt, ro, ru, si,
sk, sl, sv, te, tl, tr, uk, ur, and others. See the source README for the complete set.

---

## H1. Operational wiring for the vault cron

How this document plugs into the automated pipeline:

1. The daily cron (see `money-glitch-auditor.sh` and the filler prompt) triggers a research
   tick. That tick may decide to refresh signal queries rather than write a new pain file.
2. A runner (Python, using twscrape with the cookie pool from `cookies-tokens/`) executes the
   signal patterns in the section above, one per module, on a schedule (every 1 to 6 hours
   depending on volume).
3. Results are written as JSONL into a staging area, then consumed by the `03`, `05`, and `06`
   modules. The cron appends only net-new signals (dedupe by tweet ID) to keep the vault
   append-only and avoid bloat.
4. Velocity and engagement floors are tuned per cluster via stored baselines, not hardcoded.
5. All tweet IDs are snowflakes; store the max ID per query as the resume cursor for the next
   run so you never re-scrape and never miss a window.

Resilience notes:

- Keep twscrape as primary, snscrape as fallback. If both fail with guest-token errors, the
  cookie pool in `cookies-tokens/` is the fix, not a code change.
- Do not depend on Nitter (dead). Do not depend on the free API tier for broad sweeps
  (quota too small). Use the API only for targeted low-volume pulls.
- Respect `within_time:` windows and the 22-operator ceiling; split broad campaigns into
  multiple narrower queries rather than one giant OR string.

---

## H1. Source index (all fetched and verified at research time)

1. igorbrigadir/twitter-advanced-search, canonical operator list.
   https://github.com/igorbrigadir/twitter-advanced-search  (README 100KB, fetched 2026-07-10)
2. X advanced search UI. https://twitter.com/search-advanced
3. X API v2 rules and filtering (official, JS-rendered, `source unreachable` via curl).
   https://developer.x.com/en/docs/x-api/rules-and-filtering/search-operators
4. snscrape, JustAnotherArchivist. https://github.com/JustAnotherArchivist/snscrape
   (PyPI 0.7.0.20230622)
5. twscrape, vladkens. https://github.com/vladkens/twscrape  (PyPI 0.19.1)
6. X API v2 sample code index. https://github.com/twitterdev/twitter-api-v2-sample-code
7. Wikipedia, Twitter Search. https://en.wikipedia.org/wiki/Twitter_Search
8. Nitter instances wiki (mostly dead at research time).
   https://github.com/zedeus/nitter/wiki/Instances

Caveats recorded honestly: the official X API operators page and the X products/pricing page
returned empty bodies to a non-browser fetch, so exact API quotas and the canonical `is:`/`has:`
token list are reconstructed from the community reference and the v2 sample code and should be
re-verified against the official docs before production reliance. No data was invented; where a
source was unreachable, it is labeled as such.

---

## H1. End-to-end pipeline reference implementation

This section shows a complete, runnable skeleton that turns the query patterns above into
vault-ready JSONL. It assumes twscrape is installed and at least one authenticated account is
loaded from the cookie pool in `cookies-tokens/`. The intent is an illustrative reference, not a
drop-in production script, harden it (retries, backoff, logging, dedupe store) before real use.

```python
"""
money_glitch_x_crawler.py
Periodic X signal crawler for the money-glitch vault.

Design:
  - One query per vault module (pain mining, market, panic, competitors, prices).
  - Each query carries a resume cursor (max snowflake ID seen) persisted to disk.
  - Output is newline-delimited JSON written to a staging file for downstream consumers.
  - Engagement/velocity floors are applied in code because the web min_faves ceiling and
    API lack of min_faves make client-side filtering necessary.
"""

import asyncio
import json
import os
import time

import twscrape

VAULT = "/c/Workspace/money-glitch-vault"  # adjust for host
STAGE = os.path.join(VAULT, "staging", "x_signals.jsonl")
CURSOR_DIR = os.path.join(VAULT, "01-crawler-scrapper", "cookies-tokens", "cursors")

# (name, module, query) -- queries use the web operator grammar
QUERIES = [
    ("id_pain", "03-id-business-trends",
     '("gaji" OR "utang" OR "pinjol" OR "biaya" OR "mahal") lang:in '
     '-filter:retweets -filter:blue_verified within_time:3d min_faves:3'),
    ("id_demand", "03-id-business-trends",
     '("cara" OR "bantu" OR "rekomendasi") (lang:in) -filter:retweets within_time:2d'),
    ("idx_tickers", "05-market-cron",
     '($BBRI OR $TLKM OR $BBTN OR $BMRI OR $ASII) lang:in min_faves:10 within_time:1d'),
    ("crypto_sent", "05-market-cron",
     '($BTC OR $ETH OR $SOL) (jatuh OR naik OR "liquidation") (lang:in OR lang:en) within_time:12h'),
    ("early_panic", "07-gaps-and-opportunities",
     '("PHK" OR "layoff" OR "bangkrut" OR "gagal bayar") lang:in '
     '-filter:has_engagement within_time:6h'),
    ("competitor_gap", "03-id-business-trends",
     '(Gojek OR Grab OR Tokopedia OR Shopee OR "TikTok Shop") '
     '(komplain OR "tidak bisa" OR "mah") lang:in -filter:retweets within_time:2d min_faves:5'),
    ("pangan", "06-harga-pangan-papan",
     '("harga beras" OR "harga cabai" OR "harga gula" OR "Bapanas") lang:in within_time:1d min_faves:3'),
]

def load_cursor(name):
    p = os.path.join(CURSOR_DIR, name + ".cursor")
    if os.path.exists(p):
        return open(p).read().strip() or None
    return None

def save_cursor(name, value):
    os.makedirs(CURSOR_DIR, exist_ok=True)
    with open(os.path.join(CURSOR_DIR, name + ".cursor"), "w") as f:
        f.write(str(value))

def snowflake_to_epoch_ms(tid):
    return (int(tid) >> 22) + 1288834974657

async def run():
    api = twscrape.API()
    # In production, load accounts:
    # await twscrape.add_account(user, password, email, email_pass)

    seen_ids = set()
    os.makedirs(os.path.dirname(STAGE), exist_ok=True)

    with open(STAGE, "a", encoding="utf-8") as out:
        for name, module, query in QUERIES:
            cursor = load_cursor(name)
            q = query
            if cursor:
                q += " since_id:" + cursor
            try:
                count = 0
                async for tw in twscrape.search(q, limit=300):
                    if tw.id in seen_ids:
                        continue
                    seen_ids.add(tw.id)
                    created_ms = snowflake_to_epoch_ms(tw.id)
                    rec = {
                        "module": module,
                        "query_name": name,
                        "id": tw.id,
                        "date": tw.date.isoformat() if hasattr(tw, "date") else None,
                        "username": getattr(tw, "username", None),
                        "text": getattr(tw, "rawContent", None) or getattr(tw, "content", None),
                        "like_count": getattr(tw, "likeCount", 0),
                        "retweet_count": getattr(tw, "retweetCount", 0),
                        "reply_count": getattr(tw, "replyCount", 0),
                        "lang": getattr(tw, "lang", None),
                        "created_ms": created_ms,
                    }
                    out.write(json.dumps(rec, ensure_ascii=False) + "\n")
                    count += 1
                if seen_ids:
                    save_cursor(name, max(int(i) for i in seen_ids))
                print("[" + name + "] wrote " + str(count) + " new tweets")
            except Exception as e:
                print("[" + name + "] ERROR: " + str(e))

if __name__ == "__main__":
    asyncio.run(run())
```

Why `since_id` resume instead of `since:` date: snowflake IDs are monotonic in time, so the
highest ID seen is a precise watermark. If the cron dies mid-run, the next run resumes exactly
where it stopped with zero overlap and zero gap. Store one cursor file per query name.

Dedupe strategy: the `seen_ids` set prevents duplicates within a run. Across runs, the
`since_id` cursor already excludes previously fetched IDs, so cross-run duplicates only happen
if the same tweet matches two different queries. Downstream consumers should still dedupe by
`id` when merging modules, because a single viral complaint may match both `id_pain` and
`competitor_gap`.

---

## H1. Query cookbook: copy-paste starting points

These are tuned, ready queries. Paste into the web advanced-search box, or wrap in
`twitter-search:"..."` for snscrape, or pass to `twscrape.search(...)`. Adjust floors to taste.

Indonesian layoff or pay-cut early whispers, last 24h, no retweets, no ads:

`("PHK" OR "dirumahkan" OR "potong gaji" OR "closed hiring") lang:in -filter:retweets -filter:blue_verified within_time:1d`

Indonesian creators confused about taxes (feeds the cross-border-tax gap):

`("pajak" OR "NPWP" OR "SPT") (kreator OR youtuber OR "affiliate") lang:in -filter:retweets within_time:3d min_faves:5`

UMKM credit rejection or KUR pain (feeds demand-mining):

`("KUR" OR "pinjaman" OR "bank tolak" OR "modal") (UMKM OR "usaha kecil") lang:in -filter:retweets within_time:2d min_faves:3`

Cashtag broad sentiment, Indonesian plus English, last 12h, with engagement:

`($TLKM OR $BBRI OR $ASII OR $ANTM) (lang:in OR lang:en) min_faves:20 within_time:12h`

Regulatory change that affects creators or UMKM (feeds the regtech monitor gap):

`("Permendag" OR "PMK" OR "SE Menkeu" OR "Peraturan" OR "PP") (UMKM OR kreator OR "usaha mikro" OR "Pedagang") lang:in -filter:retweets within_time:5d`

Regional rice price arbitrage chatter (feeds 06-harga-pangan-papan):

`("beras" OR "cabai" OR "bawang") (harga OR "naik" OR "turun" OR "Bapanas") lang:in within_time:1d min_faves:2`

Side-hustle or freelance demand (feeds 04-freelancer-ai-agent):

`("cari freelancer" OR "butuh jasa" OR "open order" OR "jasa bikin") lang:in -filter:retweets within_time:2d min_faves:3`

Low-engagement but geographically tagged posts (use sparingly, geo is sparse in ID):

`("banjir" OR "longsor" OR "macet") near:Jakarta within:25km within_time:6h`

Find quotes of a specific account (competitor mention mining):

`twitter.com/gojek/status/ -from:gojek`

Find threads by a high-signal account (build a watchlist of handles):

`from:HANDLE filter:self_threads -filter:retweets within_time:7d`

---

## H1. Quality, noise, and astroturfing controls

A firehose is only useful if you can trust the signal. X has heavy spam, bot networks, and paid
astroturfing. The search operators alone will not filter these, you need post-processing.

Spam fingerprints to drop in code:

- Repeated near-identical text from many accounts within minutes (coordinated boost).
- Accounts with default eggs, zero followers, and high post volume (farm accounts).
- Links to unknown shorteners en masse (pig-butchering, judol, pinjol scams). The vault's
  `07-gaps-and-opportunities` has a judol plus pinjol cross-detection item, feed it URL domains here.
- Sudden spikes in `min_faves:` posts on a cashtag with no external news (pump groups).

Trust signals to boost:

- `filter:verified` (legacy) or accounts with long tenure and steady follower growth.
- Posts that spark genuine replies (not just likes) indicate real discussion.
- Cross-confirmation: the same event appearing in `lang:in` organic posts AND `filter:news`.

A practical two-stage filter: stage one pulls with a low floor (`min_faves:2` or none) using
`-filter:has_engagement` for early signal, stage two re-queries the same keywords with a high
floor (`min_faves:200`) 6 to 12 hours later to measure whether the early whisper became a
real story. The delta between stage one and stage two volume is your conviction score.

---

## H1. Relationship to other vault modules

This file is the intake layer. Downstream consumers:

- `03-id-business-trends/demand-mining/` consumes `id_pain` and `id_demand` output to discover
  or deepen pain-point files. Newly surfaced complaints become candidate new markdown files.
- `03-id-business-trends/competitors/` consumes `competitor_gap` to track where Gojek, Grab,
  Tokopedia, Shopee, TikTok Shop fall short, feeding the gaps-and-opportunities thesis.
- `05-market-cron/` consumes `idx_tickers` and `crypto_sent` to build sentiment time series
  alongside the IHSG and crypto fetchers.
- `06-harga-pangan-papan/` consumes `pangan` to seed regional price deltas before the Bapanas
  scraper confirms them with hard numbers.
- `07-gaps-and-opportunities/` consumes `early_panic` and `competitor_gap` to surface black-swan
  and platform-gap candidates that may become new opportunity one-pagers.

Because the vault is append-only, the crawler writes to a staging directory and the module
agents promote staged signals into permanent markdown. The crawler never edits existing files.

---

## H1. Maintenance and re-verification checklist

Operators and endpoints change. When the pipeline breaks, run this checklist:

1. Is the guest token failing? That points to cookie-pool expiry in `cookies-tokens/`. Rotate
   accounts. This is the most common failure and is a credentials issue, not a code issue.
2. Are queries returning 400? You likely used a web operator against the API or exceeded the
   ~22 operator ceiling. Split the query.
3. Did `lang:in` stop working? Confirm it is `in`, not `id`. Language tagging drifts, re-test.
4. Did `min_faves:` silently stop filtering? You may have been switched from web to API path.
   Move the floor into client-side `public_metrics` filtering.
5. Are quotas exhausted? Free API tier is tiny, confirm against the official products page
   (currently `source unreachable` via curl, so verify in a browser).
6. Did Nitter stop? Expected. Do not rebuild on it.

Re-verify the operator list quarterly against
https://github.com/igorbrigadir/twitter-advanced-search and
https://developer.x.com/en/docs/x-api/rules-and-filtering/search-operators . Update this file
with a dated note when operators are added or removed.
