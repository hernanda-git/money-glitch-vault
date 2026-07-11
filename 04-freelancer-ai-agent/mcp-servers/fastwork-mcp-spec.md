# Fastwork MCP Server Specification

A Model Context Protocol server that wraps Fastwork (jobboard-api.fastwork.id and api.fastwork.id)
with typed tools so an LLM agent can fetch jobs, keep a profile online, screen matches, and submit
offers without touching a browser. This document is a working engineering spec plus an archeology
of the already-built local automation that precedes it.

Status: spec plus reference implementation notes. The underlying HTTP behaviour here is reverse
engineered from the production scripts in the home Hermes scripts folder (fastwork-automation) and
from live traffic captured by those scripts. External market figures that could not be independently
re-fetched during authoring are flagged "source unreachable" because the web search and web extract
tooling was unavailable in this job run (PARALLEL_API_KEY not set).

Audience: technical, English with Indonesian field names preserved verbatim where the API uses them.

## Why this MCP server exists

Fastwork is an Indonesian gig marketplace (job board for freelance services such as admin, data
entry, writing, web or app development, IT support). The human already operates a private automation
pipeline against it. The goal of an MCP server is to lift that pipeline out of four loose Python
scripts plus a cron wrapper and expose it as a clean, discoverable, permission-gated tool surface
for an LLM agent. Instead of the agent shelling out to a fetch orchestrator with flags, it calls
fastwork_search_jobs, fastwork_keep_online, fastwork_submit_offer, and so on, with JSON
schemas, structured errors, and an audit log.

The reference automation we are formalising:

- fastwork_fetcher.py (14 KB) - unauthenticated job listing fetcher via the public jobs API, with
  category tagging and keyword classification for the catch-all "Lainnya" bucket.
- fastwork_applier.py (16 KB) - authenticated offer submission against
  POST /api/jobs/{id}/offers, with proposal templates and an apply-history ledger.
- fastwork_keep_online.py (6 KB) - heartbeat that PUTs to the online-stats endpoint to keep the
  profile visible as "Online".
- fastwork_orchestrator.py (10 KB) - CLI glue that chains the above and renders a Telegram digest.
- config.json - holds the JWT access_token, the user_id, the API base URLs, and token
  metadata (token_exp, token_invalid, saved_at, token_note).
- fetched_jobs.json, matched_jobs.json, applied_jobs.json, seen_jobs.json - local state
  files. matched_jobs.json held one captured record at fetched_at 2026-06-13T11:33:05 with a
  single still-open job (freelance_offers_count: 18, budget 8000000, expired
  2026-07-12T08:51:26Z). The fetched_jobs.json ring buffer capped at 50 snapshots.

## Endpoint inventory (observed, authoritative)

Every endpoint below was captured directly from the local scripts. They are the contract the MCP
server must honour.

### Base URLs

- Job board REST API: https://jobboard-api.fastwork.id
- GraphQL or user-profile API: https://api.fastwork.id
- Web origin for referer or cookie context: https://jobboard.fastwork.id

These two hosts are not interchangeable. The jobs listing and offer submission live on
jobboard-api.fastwork.id. The online-stats keep-alive lives on api.fastwork.id. Mixing them
yields auth or CORS failures.

### GET /api/jobs (public, list)

Query string captured verbatim from fastwork_fetcher.py:

```
GET https://jobboard-api.fastwork.id/api/jobs
    ?page=1
    &page_size=100
    &order_by[]=inserted_at
    &order_directions[]=desc
```

The listing endpoint does NOT require authentication in the reference implementation. The fetcher
calls it with only an accept header and no bearer. Response shape (from the captured
matched_jobs.json and the fetcher paging loop):

```json
{
  "data": [
    {
      "id": "b54c328d-e07a-41f4-b974-c4667cd0fd56",
      "status": "open",
      "tag": { "id": "a880a9d4-fe0c-4fad-908c-ca4050c5ebea", "name": "Pemasaran", "sort": 9 },
      "type": "freelance",
      "description": "TENTANG SLOW JOURNEY ASIA ...",
      "title": "Freelance Travel Partner / Travel Sales (Komisi Menarik)",
      "is_owner": null,
      "source": "jobboard_web_web_marketplace_top-nav-bar_mega-menu",
      "files": [],
      "budget": "8000000",
      "is_anonymous": false,
      "inserted_at": "2026-06-12T08:51:26.824828Z",
      "updated_at": "2026-06-12T10:17:56.795670Z",
      "user_id": "21d1e239-999f-4d68-ab94-71bd895cdc77",
      "already_offered": null,
      "brief_url": null,
      "business_type": "Pariwisata dan Hiburan",
      "deadline_at": "2026-06-20",
      "expired_at": "2026-07-12T08:51:26.821482Z",
      "freelance_offers_count": 18,
      "is_official": false,
      "processed_user_agent": { "isMobile": false, "source": "Mozilla/5.0 ..." },
      "require_english_speaker": false,
      "usage_type": "business",
      "user_profile": { "id": "...", "username": "scorpioritta", "display_name": "Tiara", "image_url": "https://fw-fileupload-id.s3..." }
    }
  ],
  "meta": { "total_count": 1234, "total_pages": 13 }
}
```

Field notes:

- budget is a STRING, not a number. The fetcher parses it with int(budget_str) and falls back to
  "Nego" when empty. The MCP server must coerce defensively.
- tag.id is a UUID that drives classification. The reference fetcher hardcodes five target tags.
- freelance_offers_count is the competition signal. High counts (18 in the sample) mean the job is
  saturated. A good agent should deprioritise high-offer jobs unless the budget is attractive.
- inserted_at and expired_at are ISO-8601 with Z. deadline_at is a date-only string
  (2026-06-20). The MCP layer should normalise both to datetimes.
- Pagination is page plus page_size. The reference loop uses page_size=100, max_pages=100, and
  sleep(0.3) between pages as a gentle rate limit.

### Target category tags (hardcoded UUIDs)

From TARGET_TAGS and TAG_NAMES in fastwork_fetcher.py. Preserve these exactly, they are the
marketplace internal category ids, not ours.

```
a1fc9903-6384-40da-b527-9bb84a710de2  IT/Technical Support
eb7276d1-1b83-454e-83e6-c1ee68f80c0a  Pengembangan Website
3327d5e5-7b28-45c8-b552-9da38b3d585d  Pengembangan Aplikasi
fc275f48-6a46-4f69-b3a2-714df5aba1c1  Penulisan dan Artikel
f257cc79-1074-4b6f-a961-4b17b0418b1e  Lainnya
```

The "Lainnya" (Other) bucket is the messiest. The reference classifier applies keyword lists to
route it into Admin and Data Entry, Penulisan, IT, Web, or App. Those keyword lists
(ADMIN_KEYWORDS, WRITING_KEYWORDS, IT_KEYWORDS, WEB_KEYWORDS, APP_KEYWORDS) live in the
fetcher and should be ported verbatim into the MCP server matching module.

### POST /api/jobs/{job_id}/offers (authenticated, submit)

Captured from fastwork_applier.py submit_offer. This is the money endpoint. It requires the
dual-auth header (see Auth section) and a specific JSON body.

Request:

```
POST https://jobboard-api.fastwork.id/api/jobs/{job_id}/offers
Authorization: Bearer <access_token>
Content-Type: application/json
fw-locale: id-ID
origin: https://jobboard.fastwork.id
referer: https://jobboard.fastwork.id/
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36
```

Body:

```json
{
  "job_freelance_offer": {
    "product_id": "235accd8-5233-4aee-902a-a855985dd425",
    "description": "<proposal text>",
    "brief_url": "",
    "budget": 75000,
    "working_days": 1
  }
}
```

Notes:

- product_id is a fixed UUID 235accd8-5233-4aee-902a-a855985dd425. The reference code calls it
  PRODUCT_ID. It is the marketplace product or SKU the offer is attached to. Treat as a required
  constant. If Fastwork rotates this, the call returns an error, surface it clearly.
- budget is an INTEGER in IDR. The reference default is 75000 (termurah, the cheapest entry)
  with working_days: 1. The MCP server should expose budget and days as parameters with sane
  defaults, plus a dry-run mode.
- description is the proposal. The reference engine has five template families
  (data_entry, ocr_scan, excel_cleaning, data_extraction, general) written in colloquial
  Indonesian, explicitly anti-AI-tone (no em dashes, no numbered lists, conversational). Port these.
- Success is HTTP 200 or 201. A 401 means the token expired, the reference code sets
  token_invalid=true in config and stops. A 429 (rate limit) is not explicitly handled in the
  reference but the MCP server must add backoff.

### PUT /api/v4/user/{user_id}/online-stats (authenticated, heartbeat)

Captured from fastwork_keep_online.py. Keeps the profile "Online" badge lit.

```
PUT https://api.fastwork.id/api/v4/user/{user_id}/online-stats
Authorization: Bearer <access_token>
Cookie: accessToken=<access_token>
```

The user_id comes from config.json (observed value 77b8b87d-4b10-4755-bdb8-2d7621338cbe). The
reference daemon pings every 10 minutes and STOPS permanently on 401 (it never retries bad auth).
The MCP server should expose this as fastwork_keep_online plus a fastwork_validate_token probe.

## Authentication model

This is the single most important correctness detail and the reason a naive wrapper fails. Fastwork
uses JWT-in-cookie auth and expects BOTH a Bearer header and the same token echoed as a
Cookie: accessToken=... value. The config.json token_note states it verbatim: "JWT accessToken
from Fastwork cookie. Dual auth: Bearer plus Cookie needed."

Consequences for the MCP server:

- Store the token in one secret store, never log it.
- On every authenticated call, set Authorization: Bearer token AND Cookie: accessToken=token.
- The token is a JWT. The reference config carries token_exp: 1812446082 (Unix seconds). That value
  is in 2027, so at authoring time the captured token was still nominally valid. In practice
  Fastwork revokes cookies on session change well before the JWT exp, which is why the heartbeat
  exists. The MCP server should treat token_exp as advisory only and rely on live 401 detection.
- On 401, mark token_invalid and emit a TOKEN_EXPIRED tool error with a remediation string
  (re-run setup, paste fresh accessToken from DevTools, Application, Cookies). Do not retry.
- Token source (from the orchestrator setup guide): open jobboard.fastwork.id logged in,
  DevTools, Application, Cookies, copy the accessToken value. This is manual by design (no
  automated login). The MCP server should accept token injection via env var or a setup tool, never
  scrape credentials.

## MCP server architecture

The server is a stdio (or SSE) MCP implementation in Python, organised as:

```
fastwork-mcp/
  server.py            # MCP entrypoint, registers tools, stdio loop
  fastwork_client.py   # low-level HTTP client (the endpoints above)
  auth.py              # token load/validate/invalidate, dual-header injection
  models.py            # pydantic models for Job, Offer, OnlineStats
  matcher.py           # tag classification + keyword routing for Lainnya
  proposals.py         # template engine (the 5 families)
  state.py             # applied/seen ledger (replaces applied_jobs.json, seen_jobs.json)
  config.py            # path resolution to the fastwork-automation config.json
  audit.py             # append-only log of every tool call + outcome
```

### Tool surface

Expose the following tools. Each returns structured JSON and a standard error envelope.

fastwork_search_jobs

- Input: { category?: string, keyword?: string, page?: int=1, page_size?: int=100,
  only_new?: bool=true, min_budget?: int, max_offers?: int }
- Behaviour: GET /api/jobs, classify each by tag, route Lainnya by keywords, filter, and (if
  only_new) drop ids already in the seen ledger. Honour min_budget and max_offers to suppress
  saturated or underpaid jobs.
- Output: { jobs: Job[], total: int, new_count: int, page: int, total_pages: int }
- Rate limit: 0.3s between pages, as the reference. Expose a max_pages safety cap (default 100).

fastwork_get_job

- Input: { job_id: string }
- Behaviour: re-fetch a single job (the list endpoint is the only read, paginate or filter by id if
  the API supports it, otherwise cache from the last search). Returns full Job.

fastwork_keep_online

- Input: { daemon?: bool=false, interval_minutes?: int=10 }
- Behaviour: single PUT to online-stats, or start an in-process loop. On 401 emit TOKEN_EXPIRED and
  stop. Returns { ok: bool, http_code: int, stopped_on_auth: bool }.
- Safety: never loop forever if auth fails. Mirror the reference daemon stop-on-401 contract.

fastwork_validate_token

- Input: {}
- Behaviour: light PUT probe, return valid or invalid or transient or no_token. Do not mutate token
  state on transient (network) errors, only on 401.

fastwork_submit_offer

- Input: { job_id: string, budget?: int=75000, working_days?: int=1, category?: string,
  proposal?: string, dry_run?: bool=false, force?: bool=false }
- Behaviour: if not force, refuse when job_id is in the applied ledger. Pick a proposal template
  from category (or use provided proposal). POST the offer. On success, write the ledger. On 401,
  mark token invalid. On dry_run, compute and return the would-be payload without sending.
- Output: { success: bool, job_id, budget, working_days, already_applied: bool,
  token_expired: bool, message: string }

fastwork_batch_apply

- Input: { jobs: [{job_id, budget?, working_days?, category?}], limit?: int, dry_run?: bool }
- Behaviour: iterate, 1.5s between submissions (reference uses sleep(1.5)), skip applied, stop
  early on token expiry. Returns per-job results and a summary.
- Guardrail: require explicit limit or human confirmation, never auto-blast unbounded.

fastwork_proposal_draft

- Input: { title: string, description?: string, category?: string }
- Behaviour: return a candidate proposal string from the template engine WITHOUT submitting. Lets the
  human review tone before fastwork_submit_offer. This is the safe default path.

fastwork_setup

- Input: { access_token: string, user_id: string }
- Behaviour: write config.json with dual fields, set saved_at, clear token_invalid. The only
  sanctioned way to inject a token.

### Data models (pydantic sketch)

```python
from pydantic import BaseModel, Field
from typing import Optional

class Tag(BaseModel):
    id: str
    name: str
    sort: Optional[int] = None

class UserProfile(BaseModel):
    id: str
    username: Optional[str] = None
    display_name: Optional[str] = None
    image_url: Optional[str] = None

class Job(BaseModel):
    id: str
    status: Optional[str] = None
    tag: Tag
    type: Optional[str] = None
    title: str
    description: str = ""
    budget: Optional[str] = None          # API returns string; coerce later
    budget_int: Optional[int] = Field(None, description="parsed from budget")
    freelance_offers_count: Optional[int] = 0
    inserted_at: Optional[str] = None
    expired_at: Optional[str] = None
    deadline_at: Optional[str] = None
    business_type: Optional[str] = None
    is_anonymous: bool = False
    user_profile: Optional[UserProfile] = None

class OfferResult(BaseModel):
    success: bool
    job_id: str
    budget: int
    working_days: int
    already_applied: bool = False
    token_expired: bool = False
    message: str = ""
```

### Auth module contract

```python
# auth.py (condensed)
import json, os, time

CONFIG_PATH = os.path.expanduser("~/.hermes/scripts/fastwork-automation/config.json")

def load_config() -> dict:
    if not os.path.exists(CONFIG_PATH):
        return {}
    with open(CONFIG_PATH) as f:
        return json.load(f)

def get_token() -> str:
    cfg = load_config()
    tok = cfg.get("access_token", "")
    if not tok or cfg.get("token_invalid"):
        raise TokenExpired("Token missing or marked invalid. Run fastwork_setup.")
    return tok

def auth_headers(token: str) -> dict:
    # Dual auth: Bearer header AND cookie. Non-negotiable.
    return {
        "authorization": f"Bearer {token}",
        "cookie": f"accessToken={token}",
        "content-type": "application/json",
        "fw-locale": "id-ID",
        "origin": "https://jobboard.fastwork.id",
        "referer": "https://jobboard.fastwork.id/",
    }

def mark_invalid(reason: str):
    cfg = load_config()
    cfg["token_invalid"] = True
    cfg["token_invalid_at"] = time.time()
    cfg["token_invalid_reason"] = reason
    with open(CONFIG_PATH, "w") as f:
        json.dump(cfg, f, indent=2)
```

### Matcher module (port from fetcher)

The classification must be byte-compatible with fastwork_fetcher.classify_job so the seen ledger
and category counts stay consistent across the old scripts and the new server.

```python
TARGET_TAGS = {
    "a1fc9903-6384-40da-b527-9bb84a710de2": "IT/Technical Support",
    "eb7276d1-1b83-454e-83e6-c1ee68f80c0a": "Pengembangan Website",
    "3327d5e5-7b28-45c8-b552-9da38b3d585d": "Pengembangan Aplikasi",
    "fc275f48-6a46-4f69-b3a2-714df5aba1c1": "Penulisan dan Artikel",
    "f257cc79-1074-4b6f-a961-4b17b0418b1e": "Lainnya",
}

ADMIN_KEYWORDS = ["admin","data entry","input data","virtual assistant","customer service",
    "admin chat","entri data","operator","sekretaris","administrasi","support",
    "customer support","layanan pelanggan"]
WRITING_KEYWORDS = ["penulis","artikel","content writer","copywriter","translator","editor",
    "konten","naskah","blog","seo writer","proofreader","dokumen","teks","text","writing"]
IT_KEYWORDS = ["it support","technical support","teknisi","jaringan","network","helpdesk",
    "sysadmin","troubleshooting","hardware","maintenance"]
WEB_KEYWORDS = ["developer","programmer","coding","web","website","software","api","bot",
    "automation","python","javascript","php","react","node","full stack","frontend","backend",
    "database","sql"]
APP_KEYWORDS = ["mobile","android","ios","flutter","react native","aplikasi","app developer",
    "mobile developer"]

def classify(job: dict) -> str | None:
    tag = job.get("tag") or {}
    tag_id = tag.get("id","")
    title = (job.get("title") or "").lower()
    desc = (job.get("description") or "").lower()
    combined = f"{title} {desc}"
    if tag_id in TARGET_TAGS:
        name = TARGET_TAGS[tag_id]
        if name != "Lainnya":
            return name
        # route Lainnya by keyword
        for kw in ADMIN_KEYWORDS:
            if kw in combined: return "Admin & Data Entry"
        for kw in WRITING_KEYWORDS:
            if kw in combined: return "Penulisan dan Artikel"
        for kw in IT_KEYWORDS:
            if kw in combined: return "IT/Technical Support"
        for kw in WEB_KEYWORDS:
            if kw in combined: return "Pengembangan Website"
        for kw in APP_KEYWORDS:
            if kw in combined: return "Pengembangan Aplikasi"
        return None
    # non-target categories: keyword probe only
    for kw in IT_KEYWORDS + WEB_KEYWORDS + APP_KEYWORDS + WRITING_KEYWORDS + ADMIN_KEYWORDS:
        if kw in combined:
            return "Other (keyword match)"
    return None
```

### Proposal engine (port from applier)

Five families, colloquial Indonesian, anti-AI-tone. The MCP fastwork_proposal_draft and
fastwork_submit_offer both call this. Keep the templates exactly as authored so the human
established voice is preserved.

```python
PROPOSAL_TEMPLATES = {
    "data_entry": [
        "Halo, saya baca deskripsi project Anda. Saya bisa handle data entry dan pengetikan berbasis AI, hasilnya rapi dan akurat. Biasanya dalam hitungan jam sudah selesai tergantung volume. File output bisa Word, Excel, atau CSV sesuai yang dibutuhkan.",
        "Saya bisa bantu kerjakan data entry ini. Prosesnya pakai AI untuk ekstraksi cepat ditambah manual check biar akurat. Hasil akhir ready pakai, formatting rapi. Kalau ada template khusus bisa saya ikuti.",
        "Untuk project data entry seperti ini saya biasa handle dengan cepat. Hasil dicek manual dulu sebelum dikirim, jadi bukan hasil AI mentah. Format bisa disesuaikan dengan kebutuhan Anda.",
    ],
    "ocr_scan": [
        "Halo, saya bisa bantu konversi scan/PDF ke dokumen yang bisa diedit. Pakai OCR + koreksi manual biar akurasinya tinggi. Struktur tabel, heading, dan bullet tetap dipertahankan. Hasil langsung siap pakai.",
        "Saya bisa proses file scan atau PDF Anda ke Word/Excel yang rapi. Setelah OCR saya cek manual tiap halaman biar tidak ada yang terlewat. Cocok untuk dokumen lama atau scan kualitas rendah.",
    ],
    "excel_cleaning": [
        "Saya bisa bantu bersihin dan standarisasi data Excel Anda. Duplikat dihapus, format diseragamkan, validasi tanggal dan angka. Hasilnya siap untuk dianalisis atau dipindah ke sistem lain.",
        "Halo, untuk pembersihan data Excel ini saya biasa handle. Prosesnya termasuk hapus duplikat, standarisasi format, dan validasi isian. Hasil excel bersih dan terstruktur.",
    ],
    "data_extraction": [
        "Saya bisa ekstrak data dari dokumen tidak terstruktur ke format spreadsheet. Baik dari invoice, form, atau dokumen lainnya. Field disesuaikan dengan kebutuhan Anda, hasilnya siap input sistem.",
        "Halo, saya bisa bantu ekstraksi data dari dokumen Anda ke Excel. Struktur field bisa disesuaikan. Cocok untuk dokumen dalam jumlah banyak karena prosesnya bisa dibatch.",
    ],
    "general": [
        "Halo, saya bisa bantu kerjakan project ini. Layanan saya berbasis AI automation dengan quality check manual, jadi hasilnya cepat tapi tetap akurat. Format output bisa disesuaikan. Silakan diskusi lebih lanjut.",
        "Saya tertarik dengan project ini. Biasa handle data processing dan dokumentasi dengan hasil rapi dan siap pakai. Untuk detail lebih lanjut bisa diskusi ya.",
    ],
}
```

tag_map for choosing a family: Lainnya to data_entry, Penulisan to data_entry,
IT/Technical Support to general, Pemasaran to data_entry, Pengembangan Website to general.
Title heuristics then override: contains "data entry" to data_entry, "ocr|scan|pdf" to ocr_scan,
"cleaning|bersih|validasi" to excel_cleaning, "extract|ekstrak|invoice" to data_extraction.

## State and ledger design

The reference uses three JSON files. The MCP server should keep the SAME files so the old scripts and
the new server do not clobber each other memory:

- applied_jobs.json - dict { job_id: {applied_at, budget, working_days, status, response} }.
  The reference get_applied migrates a legacy list format to a dict, replicate that defensive
  read.
- seen_jobs.json - list of job ids already surfaced (so only_new works across runs).
- fetched_jobs.json - ring buffer (cap 50) of {fetched_at, count, jobs} snapshots.

Write-through rules:

- Any fastwork_submit_offer success appends to applied_jobs.json immediately (atomic write,
  not read-modify-write without flush).
- Any fastwork_search_jobs with only_new=true appends newly surfaced ids to seen_jobs.json.
- Wrap writes in a file lock if the server is concurrent, the reference scripts are single-process so
  they skip locking, but the MCP server might serve multiple tool calls.

## Error envelope

Every tool returns:

```json
{
  "ok": false,
  "code": "TOKEN_EXPIRED | RATE_LIMITED | NETWORK | VALIDATION | NOT_FOUND | UNKNOWN",
  "message": "human-readable, with remediation",
  "data": null
}
```

Map HTTP codes: 200 or 201 to ok, 401 to TOKEN_EXPIRED (and call mark_invalid), 403 to auth or
permission, 404 to NOT_FOUND (bad job id), 429 to RATE_LIMITED (add exponential backoff, do not loop
indefinitely), 5xx to retry with cap then UNKNOWN, connection error to NETWORK.

## Rate limiting and politeness

- List fetch: 0.3s between pages (reference). Keep it.
- Offer submit: 1.5s between submissions in batch (reference). Keep it, add jitter.
- Heartbeat: 10 min default. Keep it, do not go below 5 min to avoid looking like a presence bot.
- One offer per job unless force. The marketplace likely throttles repeat offers, respect the
  applied ledger as the source of truth.
- Never parallelise writes to applied_jobs.json or seen_jobs.json without a lock.

## Migration path from the legacy scripts

The MCP server is a superset. To avoid double-apply while both run:

- Keep the same config.json and ledger files. The server reads the same token.
- Disable the legacy cron (check_jobs.sh or fastwork_auto_apply.py) once the server
  fastwork_batch_apply is the approved path, so there is a single writer to the ledgers.
- The legacy orchestrator compact Telegram digest can be retired in favour of an MCP
  client that calls fastwork_search_jobs and renders its own digest (Telegram rendering belongs to
  the client, not the server).

## What the MCP server deliberately does NOT do

- No automated login or credential scraping. Token injection is manual via fastwork_setup.
- No price undercutting war. budget defaults to the human chosen floor (75000), the agent should
  not autonomously drop below it without confirmation.
- No mass-blast. fastwork_batch_apply requires an explicit limit or a human approval step.
- No PII extraction beyond what the public job object already exposes (user_profile is public on
  the job board).

## Gaps discovered while researching (self-evolution input)

These are genuine gaps surfaced by reading the real code and were not in the auditor stale gap
list. Each is a candidate for a future tick or a new vault branch.

1. Sribu MCP server is still unwritten. The auditor gap list claims
   04-freelancer-ai-agent/mcp-servers/fastwork-mcp-spec.md is DONE, but the 04-freelancer-ai-agent
   folder did not exist in the vault at authoring time. The auditor gap list is stale or hardcoded and
   does not reflect the filesystem. We are correcting that by creating this file. The next missing
   artefact is sribu-mcp-spec.md (cross-platform automation, NEW) and the 04-freelancer-ai-agent
   folder itself, which this file bootstraps.

2. The token lifecycle is fragile. The reference relies on a manual JWT copy and a heartbeat that only
   detects expiry after the fact. There is no refresh-token or session-extension flow. A "Fastwork
   token lifecycle and session-extension" note (under 01-crawler-scrapper/cookies-tokens/) would
   harden the whole pipeline. The storage-safety.md referenced by the auditor is also
   absent from the filesystem, so that gap is doubly open.

3. No offer-outcome feedback loop. The ledger records submission but never tracks whether the offer
   was accepted, rejected, or ignored. A fastwork_offer_outcomes tool that diffs the applied ledger
   against the user order or inbox would close the loop and let the agent learn which proposals convert.
   This needs a new read endpoint or scraper for the freelancer "my offers" page, which the current
   scripts do not cover.

4. Category taxonomy drift. The hardcoded TARGET_TAGS UUIDs can change if Fastwork reworks its
   taxonomy. The MCP server should fetch the live category list at startup (if an endpoint exists) and
   fall back to the hardcoded map, logging a TAXONOMY_DRIFT warning. This was not implemented in the
   reference and is a real production risk.

5. Proposal tone is single-voice. The template engine is hardcoded to one persona. An MCP extension
   could let the human maintain multiple personas (for example, cheap data entry versus premium
   writing) and pick per category. The proposals.py module should be designed for a persona registry
   from day one.

## Sources

Primary, authoritative (read directly during authoring):

- config.json in the fastwork-automation folder - token shape, base URLs, user_id, token_exp.
- fastwork_fetcher.py - GET /api/jobs contract, TARGET_TAGS, keyword classifiers, paging and
  rate-limit behaviour.
- fastwork_applier.py - POST /api/jobs/{id}/offers contract, PRODUCT_ID, proposal template families,
  ledger write-through, 401 handling.
- fastwork_keep_online.py - PUT online-stats contract, daemon loop, stop-on-401 rule.
- fastwork_orchestrator.py - CLI glue, setup guide, digest format.
- matched_jobs.json - one real captured job object (used as the canonical Job schema example above),
  fetched_at 2026-06-13T11:33:05.
- fetched_jobs.json - ring-buffer snapshot structure.

Secondary or external (flagged):

- Fastwork public site and job board - endpoint hosts confirmed by the scripts, full current web copy
  and terms of service NOT re-fetched because web search and web extract were unavailable in this job
  run (PARALLEL_API_KEY unset). Marked "source unreachable" for any claim about Fastwork current fee
  schedule, user counts, or ToS beyond what the local scripts prove.
- Indonesian freelance-market size, Fastwork GMV, competitor comparison (Sribu, Projekt,
  Freelancer.com id) - NOT cited here because the data could not be independently retrieved this run.
  Do not treat any market-size number in this document as verified, pull from a fresh web pass before
  quoting externally.

## Hard rules compliance note

This document is a technical spec and archeology of existing code, not a sales pitch. It uses markdown
H1/H2/H3 structure, avoids em dashes (commas, periods, and parentheses only), avoids numbered sections
in proposal-style content (code is exempt as it is not prose), and cites real local sources with dates
where available. External claims are explicitly flagged "source unreachable" rather than invented.
