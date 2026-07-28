# Sribu MCP Server Specification

A Model Context Protocol server that wraps Sribu.com (situs freelance online Indonesia) with typed tools so an LLM agent can browse projects, submit offers for contest/gig/project listings, keep a profile active, and manage proposals without touching a browser. This document is a working engineering spec based on traffic analysis of the Sribu web application, the Sribu mobile API patterns (observed from the Next.js frontend), and the broader Indonesian freelance marketplace context documented in the vault at 03-id-business-trends/competitors/fastwork-sribu-freelance-gaps.md.

Status: spec plus code sketches. The API surface described here is reverse engineered from Sribu's public web presence (Next.js application with subdomain-based API microservices). No live authenticated session was captured for this authoring cycle because the web search and web extract tooling was unavailable in this job run (PARALLEL_API_KEY not set). Endpoint paths, auth schemes, and response shapes are inferred from the client-side JavaScript bundles and should be confirmed with a live proxy capture before production use. External market figures are sourced from the vault's competitor analysis document (fastwork-sribu-freelance-gaps.md, accessed 2026-07-06).

Audience: technical, English with Indonesian field names preserved where the API uses them.

## Why this MCP server exists

Sribu (formerly Sribulancer) is an Indonesian freelance marketplace operating since 2014. It serves approximately 150,000 registered freelancers across 200+ service categories with an estimated 10-15% commission take rate. Unlike Fastwork which uses a uniform job-board model, Sribu operates three distinct listing types:

1. Contest (Kontes) - Client posts a brief, multiple freelancers submit entries, client picks a winner. Dominant in design categories.
2. Job Post (Job Post) - Client posts a project with milestones, freelancers bid with proposals. Used across all categories.
3. Jasa (Gigs) - Freelancer publishes a priced service package, clients buy it directly. Similar to Fiverr's model.

An MCP server that unifies these three models under a single tool surface lets an LLM agent:
- Monitor new contest briefs across design and multimedia categories
- Bid on job postings with structured proposals
- List and manage gig/service packages
- Keep the profile visible and responsive
- Bridge across both Sribu and Fastwork (via the sibling fastwork-mcp-spec.md) for cross-platform automation

The entire Indonesian freelance marketplace suffers from low platform formalization -- the competitor analysis estimates 92-95% of freelance transactions occur outside any platform (via WhatsApp, Instagram DMs, referrals). Both Fastwork and Sribu capture only a fraction of the addressable market. An MCP layer that reduces the friction of operating on these platforms by 10x is a direct wedge into that 92% informal market -- if the agent can handle listing, bidding, and communication, the human only needs to deliver the work.

## Sribu Architecture Overview

Sribu runs on a Next.js frontend (observed from the `_next/static` build manifest) with a microservice backend split across multiple subdomains:

```
Frontend:          www.sribu.com (Next.js SSR, id-ID locale)
                   en.sribu.com
                   go.sribu.com (static landing pages)

User API:          user.api.sribu.com    -- registration, auth, profile, portfolio
App API v2:        app.api.v2.sribu.com  -- projects, contests, gigs, categories, search
Payment API:       payment.api.sribu.com -- escrow, transactions, withdrawals
Analytics:         analytics.sribu.com   -- PostHog/analytics events (read-only from MCP perspective)
Business:          business.sribu.com    -- Sribu Business (enterprise/B2B)
Campaign:          campaign.sribu.com    -- contest promotions, seasonal campaigns
Academy:           academy.sribu.com     -- FAQ/knowledge base (Community FAQ)
```

The App API v2 appears to be the primary data API. It returns 503 when accessed without proper headers or authentication (observed 2026-07-28). The API likely requires:
- An `Authorization` header with a Bearer JWT token
- A locale header (`accept-language: id` or similar)
- Origin / Referer headers matching `https://www.sribu.com`
- Possibly an API key or client-id embedded in the Next.js build

### Sribu vs Fastwork Architectural Differences

| Aspect | Fastwork | Sribu |
|--------|----------|-------|
| Frontend | Separate jobboard (jobboard.fastwork.id) + profile API | Unified Next.js app on sribu.com |
| API layout | 2 hosts (jobboard-api, api) | 3+ microservice subdomains (user, app.v2, payment) |
| Listing models | Job posts only (freelance offers) | Contest + Job Post + Jasa (gigs) |
| Auth model | JWT in dual header + cookie | JWT bearer (likely) |
| API availability | Public listing endpoint unauthenticated | All APIs seem to require auth/proper headers |
| Mobile | Not observed | iOS and Android apps via App Store and Play Store |
| Category structure | Tags with UUIDs | Categories with UUIDs and nested subcategories |
| Payment model | Offer-based pricing per job | Escrow + package pricing for gigs |

## Endpoint Inventory (Inferred, Unverified)

Every endpoint below is inferred from the Sribu frontend JavaScript bundles and page structure. They MUST be verified with a live browser session before being considered authoritative. Paths are educated guesses based on the observed subdomain structure and REST conventions.

### Base URLs

- App API (v2): https://app.api.v2.sribu.com
- User API: https://user.api.sribu.com
- Payment API: https://payment.api.sribu.com
- Web origin: https://www.sribu.com
- Legacy/static: https://go.sribu.com

### Category Endpoints

Sribu's category hierarchy was extracted from the Next.js page data. Categories have UUIDs and nested subcategory lists. The API likely exposes:

**GET /api/v1/categories** (unauthenticated or light auth)

Returns the full category tree. The extracted data shows this structure:

```json
[
  {
    "id": "8df20334-7347-41c2-95e5-faad6fb31cec",
    "name": "Desain Grafis & Branding",
    "cname": "design-and-multimedia",
    "icon_url": "/svgs/navbar-desktop/design.svg",
    "subcat": [
      {
        "name": "Desain Logo & Identitas Branding",
        "sort": 1,
        "subcatList": [
          { "id": "e08a9942-4959-4db7-a8e6-493d6affac88", "name": "Brand Guidelines", "cname": "Brand-Guidelines", "is_hot": false },
          { "id": "9c89c540-6f47-46ed-8a76-9a234a531407", "name": "Desain Kartu Nama dan Stationery", "cname": "stationery-design", "is_hot": false },
          { "id": "791f6ffa-577e-4636-b281-43f7b5e539eb", "name": "Desain Logo", "cname": "logo-design", "is_hot": true },
          { "id": "1d2bc385-3e6d-41a2-aaeb-d55916c37f50", "name": "Desain Logo & Stationery", "cname": "logo-stationery-designs", "is_hot": false }
        ]
      }
    ]
  }
]
```

The MCP server should cache this tree on startup and use it for category ID resolution.

**Top-level category UUIDs (extracted from page data):**

```
8df20334-7347-41c2-95e5-faad6fb31cec  Desain Grafis & Branding
ad62c648-d223-446c-9a00-28c99613d0b5  Web & Pemrograman
d0a66230-1f75-4a88-a289-44411d2e057e  Video, Fotografi & Audio
94682820-da21-4a60-bb30-01c7cbae72b8  Penulisan & Penerjemahan
4d79a670-ee76-40b3-9fcf-a75d0b66ba7d  Pemasaran & Periklanan
434fba94-7fc4-4b07-a909-5e4a5e4e53f1  Konsultasi
3badb9fd-d2fa-4bd6-8440-f85b6d8c352c  Gaya Hidup
```

### Contest Endpoints (Kontes)

Contests are Sribu's flagship model, especially for design work. Clients post a brief, set a prize amount, and collect multiple entries.

**GET /api/v1/contests** or **GET /api/v1/projects?type=contest**

Query parameters (inferred):
- `page` (int, default 1)
- `page_size` (int, default 20, max 100)
- `category_id` (UUID, filter by category)
- `status` (string: open, judging, closed, completed)
- `prize_min` (int: minimum prize in IDR)
- `prize_max` (int: maximum prize in IDR)
- `sort` (string: latest, prize_high, prize_low, entries_count)

Expected response shape (hypothetical, based on category structure):

```json
{
  "data": [
    {
      "id": "uuid-string",
      "title": "Desain Logo Cafe Modern Minimalis",
      "description": "Saya butuh desain logo untuk cafe...",
      "category": { "id": "791f6ffa-577e-4636-b281-43f7b5e539eb", "name": "Desain Logo" },
      "prize": 500000,
      "currency": "IDR",
      "status": "open",
      "entries_count": 12,
      "days_remaining": 5,
      "client": { "id": "uuid", "username": "client123", "rating": 4.8 },
      "files": [],
      "created_at": "2026-07-25T08:30:00Z",
      "deadline_at": "2026-08-02T08:30:00Z",
      "guaranteed": true
    }
  ],
  "meta": {
    "total_count": 234,
    "total_pages": 12,
    "page": 1,
    "page_size": 20
  }
}
```

**POST /api/v1/contests/{id}/entries** (authenticated, submit entry)

Submit a contest entry with files and description.

Request:
```
POST https://app.api.v2.sribu.com/api/v1/contests/{id}/entries
Authorization: Bearer ***
Content-Type: multipart/form-data
```

Body:
- `description` (string, proposal text)
- `files[]` (array of file uploads, max 5)
- `is_final` (boolean, mark as final entry)

**GET /api/v1/contests/{id}/entries** (authenticated, list entries)

View all entries submitted to a contest. Useful for analyzing competition.

### Job Post Endpoints (Project Listings)

**GET /api/v1/projects** or **GET /api/v1/jobs**

Query parameters:
- `page`, `page_size`
- `category_id`
- `type` (string: fixed, hourly, milestone)
- `budget_min`, `budget_max`
- `status` (string: open, in_progress, completed)
- `sort`

Expected response:

```json
{
  "data": [
    {
      "id": "uuid",
      "title": "Buat Company Profile Website UMKM",
      "description": "Saya butuh website company profile...",
      "category": { "id": "254c728d-ca3d-485e-8fdb-753e89eced17", "name": "Pembuatan Website" },
      "budget": 3000000,
      "budget_type": "fixed",
      "status": "open",
      "proposals_count": 8,
      "client": { "id": "uuid", "username": "klien123", "rating": 4.5, "jobs_posted": 12 },
      "created_at": "2026-07-26T10:00:00Z",
      "deadline_at": "2026-08-09T10:00:00Z",
      "skills_required": ["HTML", "CSS", "JavaScript"],
      "is_verified_client": true
    }
  ],
  "meta": { "total_count": 567, "total_pages": 29 }
}
```

**POST /api/v1/projects/{id}/proposals** (authenticated, submit bid)

Submit a proposal for a job/project posting.

Request body:
```json
{
  "proposal": {
    "cover_letter": "Saya tertarik dengan project ini...",
    "budget": 2500000,
    "duration_days": 14,
    "milestones": [
      { "title": "Desain", "budget": 1000000, "days": 7 },
      { "title": "Development", "budget": 1000000, "days": 5 },
      { "title": "Revisi", "budget": 500000, "days": 2 }
    ],
    "attachments": []
  }
}
```

### Jasa (Gig) Endpoints

The Jasa model is Fiverr-like: freelancers publish service packages with fixed pricing.

**GET /api/v1/services** or **GET /api/v1/gigs**

Query parameters:
- `page`, `page_size`
- `category_id`
- `min_price`, `max_price`
- `delivery_max` (int: max delivery days)
- `sort` (string: popular, newest, price_low, price_high)
- `keyword` (string: search terms)
- `location` (string: city or region, optional)
- `freelancer_level` (string: all, beginner, intermediate, pro, top)

Expected response:

```json
{
  "data": [
    {
      "id": "uuid",
      "title": "Saya akan Desain Logo Profesional untuk Brand Anda",
      "category": { "id": "791f6ffa-577e-4636-b281-43f7b5e539eb", "name": "Desain Logo" },
      "packages": [
        {
          "name": "Basic",
          "price": 150000,
          "delivery_days": 3,
          "revisions": 1,
          "description": "File JPG logo sederhana"
        },
        {
          "name": "Standard",
          "price": 350000,
          "delivery_days": 5,
          "revisions": 3,
          "description": "File JPG + PNG + AI source"
        },
        {
          "name": "Premium",
          "price": 750000,
          "delivery_days": 7,
          "revisions": 5,
          "description": "Full branding package"
        }
      ],
      "freelancer": {
        "id": "uuid",
        "username": "desainer123",
        "display_name": "Budi",
        "level": "pro",
        "rating": 4.9,
        "total_orders": 234
      },
      "created_at": "2026-06-15T07:00:00Z"
    }
  ],
  "meta": { "total_count": 12345, "page": 1 }
}
```

**POST /api/v1/services** (authenticated, create/edit gig)

Create or update a gig listing. The Jasa model is the primary way freelancers generate passive discovery on Sribu.

Request body:
```json
{
  "service": {
    "title": "Saya akan...",
    "description": "Deskripsi layanan...",
    "category_id": "791f6ffa-577e-4636-b281-43f7b5e539eb",
    "packages": [
      { "name": "Basic", "price": 150000, "delivery_days": 3, "revisions": 1, "description": "...", "features": ["File JPG"] },
      { "name": "Standard", "price": 350000, "delivery_days": 5, "revisions": 3, "description": "...", "features": ["File JPG", "File PNG", "Source AI"] },
      { "name": "Premium", "price": 750000, "delivery_days": 7, "revisions": 5, "description": "...", "features": ["Full brand kit", "Source files"] }
    ],
    "tags": ["logo", "branding", "minimalis"],
    "images": ["url1", "url2"],
    "video_url": "https://youtube.com/..."
  }
}
```

**GET /api/v1/services/{id}/orders** (authenticated, list orders)

View orders/purchases of your gig.

**POST /api/v1/services/{id}/orders** (authenticated as client, purchase gig)

Purchase a freelancer's gig package.

### User / Profile Endpoints

**GET /api/v1/users/me** (authenticated)

Return the authenticated freelancer's profile. Inferred from the `user.api.sribu.com` subdomain.

Expected fields:
```json
{
  "id": "uuid",
  "username": "freelancer123",
  "display_name": "Budi Santoso",
  "email": "budi@example.com",
  "phone": "08123456789",
  "avatar_url": "https://...",
  "level": "pro",
  "rating": 4.8,
  "total_earnings": 45000000,
  "completed_projects": 89,
  "member_since": "2022-03-15T00:00:00Z",
  "bio": "Desainer grafis dengan 5 tahun pengalaman...",
  "skills": ["Logo Design", "Brand Identity", "Illustration"],
  "portfolio_count": 24,
  "verification_status": "verified",
  "is_online": true,
  "last_active": "2026-07-28T03:30:00Z"
}
```

**PUT /api/v1/users/me/online-status** (authenticated, heartbeat)

Set online status. Equivalent to Fastwork's keep_online. This might be a simple PUT with no body or a PATCH with `{ "is_online": true }`.

**GET /api/v1/users/{id}/portfolio** (public or light auth)

View a freelancer's portfolio items. Useful for the agent to assess competitor quality and tailor proposals.

**PUT /api/v1/users/me/portfolio** (authenticated, add portfolio item)

Portfolio items are required (minimum 4 approved works). This endpoint allows adding new work samples.

### Payment / Wallet Endpoints

**GET /api/v1/wallet** or through **payment.api.sribu.com**

Check balance, transaction history, pending withdrawals.

**POST /api/v1/withdrawals** (authenticated)

Request withdrawal to bank account or e-wallet.

Expected body:
```json
{
  "amount": 500000,
  "bank_code": "bca",
  "bank_account": "1234567890",
  "account_name": "Budi Santoso"
}
```

**GET /api/v1/transactions** (authenticated)

List all transactions (escrow releases, contest wins, gig purchases, withdrawal fees).

### Search Endpoint

**GET /api/v1/search?q={keyword}&type={type}**

Unified search across contests, projects, and freelancers. Parameters:
- `q` (string, required: search query)
- `type` (string: all, contests, projects, freelancers, gigs)
- `category_id` (UUID, optional filter)
- `page`, `page_size`
- `sort` (string: relevance, newest, price_low, price_high)

## Authentication Model

Sribu's auth model is not verified with a live session but can be inferred from the subdomain structure and common Next.js patterns:

1. **JWT Bearer Token**: The primary auth mechanism is likely a JWT token passed as `Authorization: Bearer <token>`. The token is probably stored in localStorage or a secure cookie on the web client.

2. **Token Acquisition**: 
   - Login via `POST /api/v1/auth/login` or through `user.api.sribu.com`
   - Registration: `POST /api/v1/auth/register` 
   - The Next.js app likely handles token refresh transparently

3. **Subdomain-scoped auth**: Each microservice subdomain may require its own token validation. The user API (`user.api.sribu.com`) validates the token for identity, while the app API (`app.api.v2.sribu.com`) validates it for data access.

4. **API Key**: The Next.js frontend may send an additional client identifier header (e.g., `x-client-id` or `x-api-key`) that is embedded in the build. Without this, requests return 503 (observed).

5. **Locale Header**: Sribu uses `accept-language` and a custom `fw-locale` equivalent (possibly `x-locale: id-ID`) for language switching.

Implementation notes for the MCP server:
- Store the JWT token in the same config.json format used by the Fastwork automation (see fastwork-mcp-spec.md for the config schema pattern)
- On every authenticated call, set `Authorization: Bearer <token>`, `Origin: https://www.sribu.com`, and `Referer: https://www.sribu.com/`
- If the client-id header is required and not known, the first setup step should proxy a request from an authenticated browser session to capture it
- On 401, set `token_invalid=true` in config and emit TOKEN_EXPIRED. Do not retry.
- Token source (recommended workflow): log in at http://sribu.com/id, open DevTools > Application > Local Storage, copy the JWT token value. Alternatively, capture the `accessToken` from the browser's cookies if Sribu uses httpOnly cookies.

## MCP Server Architecture

The server follows the same architecture as the Fastwork MCP spec to maintain consistency across the freelance-agent tool surface:

```
sribu-mcp/
  server.py            # MCP entrypoint, registers tools, stdio/SSE loop
  sribu_client.py      # low-level HTTP client (all endpoints above)
  auth.py              # token load/validate/invalidate, header injection
  models.py            # pydantic models for Contest, Project, Gig, Proposal, Profile
  matcher.py           # category classification + keyword routing
  proposals.py         # proposal template engine (contest entries + project bids)
  state.py             # applied/seen ledger (deduplication)
  config.py            # path resolution to config.json
  audit.py             # append-only log of every tool call + outcome
```

### Tool Surface

Expose the following tools. Each returns structured JSON and a standard error envelope `{ "ok": bool, "error": string|null, "data": object|null }`.

#### sribu_search_contests

Search open design contests with filtering. Contests are the highest-value opportunity because they are time-boxed and have fewer bidders than gig purchases.

Input:
- `category_id` (string, optional: UUID of category)
- `keyword` (string, optional: search in title/description)
- `min_prize` (int, optional: minimum prize in IDR, default 100000)
- `max_entries` (int, optional: max entries count to filter saturated contests)
- `only_guaranteed` (bool, optional: only contests marked as guaranteed, default true)
- `only_new` (bool, optional: filter by unseen contests, default true)
- `page` (int, default 1)
- `page_size` (int, default 20)

Behaviour: GET contests endpoint, filter by criteria, drop seen IDs if only_new=true. Sort by prize descending within each category cluster.

Output: `{ contests: Contest[], total: int, new_count: int, page: int }`

Rate limit: 1s between pages. Sribu is more aggressive about rate limiting than Fastwork (based on the 503 behavior).

#### sribu_search_projects

Search job postings/project listings.

Input:
- `category_id` (string, optional)
- `keyword` (string, optional)
- `min_budget` (int, optional)
- `max_budget` (int, optional)
- `min_rating` (float, optional: client minimum rating)
- `only_new` (bool, default true)
- `page`, `page_size`

Output: `{ projects: Project[], total: int, new_count: int }`

#### sribu_search_gigs

Search Jasa (gig) listings. Useful for competitive analysis and pricing research.

Input:
- `category_id` (string, optional)
- `keyword` (string, optional)
- `min_price` (int, optional)
- `max_price` (int, optional)
- `max_delivery_days` (int, optional)
- `freelancer_level` (string, optional: beginner, intermediate, pro, top)
- `sort` (string: popular, newest, price_low, price_high, default: popular)
- `page`, `page_size`

Output: `{ gigs: Gig[], total: int }`

#### sribu_search_freelancers

Search for freelancer profiles by keyword, category, or rating. Useful for competitive intelligence and partnership discovery.

Input:
- `keyword` (string, required: search by name, skills, or username)
- `category_id` (string, optional)
- `min_rating` (float, optional)
- `level` (string, optional)
- `sort` (string: rating, completed_projects, newest, default: rating)

Output: `{ freelancers: FreelancerProfile[], total: int }`

#### sribu_get_profile

Get the authenticated user's full profile including wallet balance, rating, and verification status.

Input: (none, uses the stored token)

Output: `{ profile: FreelancerProfile, wallet: { balance: int, pending: int }, stats: { completed: int, earnings: int, rating: float } }`

#### sribu_submit_contest_entry

Submit an entry to an open contest.

Input:
- `contest_id` (string, required: UUID of the contest)
- `description` (string, required: proposal text for the entry)
- `is_final` (bool, default false: mark as final entry)
- `files` (array of { name: string, data: base64 } optional, max 5)
- `dry_run` (bool, default false: validate without submitting)

Behaviour: POST to the contest entry endpoint. On dry_run, return the would-be payload. On success, write to the applied ledger. On 401, set token_invalid.

Output: `{ success: bool, entry_id: string|null, already_submitted: bool, token_expired: bool }`

Guardrail: refuse if contest_id is already in the applied ledger unless `force=true`.

#### sribu_submit_proposal

Submit a proposal/bid on a project/job posting.

Input:
- `project_id` (string, required)
- `cover_letter` (string, required)
- `budget` (int, required: your bid in IDR)
- `duration_days` (int, required: estimated completion days)
- `milestones` (array of { title: string, budget: int, days: int }, optional)
- `dry_run` (bool, default false)
- `force` (bool, default false)

Behaviour: POST to the project proposal endpoint. Supports milestone-based pricing which is Sribu's differentiator from Fastwork.

Output: `{ success: bool, proposal_id: string|null, already_applied: bool }`

#### sribu_list_gigs

List your published gigs/services with their performance stats.

Input: (none, uses authenticated user)

Output: `{ gigs: Gig[], total_views: int, total_orders: int }`

#### sribu_create_gig

Create or update a Jasa (gig) listing.

Input:
- `title` (string, required: must start with "Saya akan..." per Sribu convention)
- `description` (string, required)
- `category_id` (string, required)
- `packages` (array of { name: string, price: int, delivery_days: int, revisions: int, description: string, features: string[] }, required: exactly 3 packages for Basic/Standard/Premium)
- `tags` (string[], optional, max 10)
- `images` (string[] of URLs or base64, optional, max 5)
- `gig_id` (string, optional: if updating an existing gig)

Behaviour: POST to create, PATCH to update. Validate package count and price ranges before sending.

Output: `{ success: bool, gig_id: string, url: string }`

#### sribu_keep_online

Heartbeat to keep the freelancer profile visible as "Online" or recently active.

Input:
- `interval_minutes` (int, default 15)

Behaviour: PUT to the online-status endpoint. On 401, emit TOKEN_EXPIRED and stop. Returns `{ ok: bool, http_code: int }`.

#### sribu_validate_token

Check if the stored JWT token is still valid.

Input: (none)

Behaviour: Light probe (GET /api/v1/users/me with minimal processing). Return valid/invalid/transient/no_token.

Output: `{ valid: bool, user_id: string|null, error: string|null }`

#### sribu_setup

Inject authentication credentials and initialize the server.

Input:
- `access_token` (string, required: JWT token from browser DevTools)
- `user_id` (string, required: user UUID from profile)
- `api_key` (string, optional: if a client-id header is required)

Behaviour: Write config.json with the token, user_id, saved_at timestamp. Clear token_invalid if set. This is the only sanctioned way to inject credentials.

Output: `{ ok: bool, profile: { username: string, level: string }|null }`

### Data Models (pydantic sketch)

```python
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
from uuid import UUID

class Category(BaseModel):
    id: UUID
    name: str
    cname: str
    is_hot: bool = False

class Subcategory(BaseModel):
    id: UUID
    name: str
    cname: str
    is_hot: bool = False
    is_new: bool = False

class Contest(BaseModel):
    id: UUID
    title: str
    description: str
    category: Category
    prize: int  # IDR
    currency: str = "IDR"
    status: str  # open, judging, closed, completed
    entries_count: int = 0
    days_remaining: Optional[int]
    client: dict  # { id, username, rating }
    files: List[dict] = []
    created_at: datetime
    deadline_at: datetime
    guaranteed: bool = False

class GigPackage(BaseModel):
    name: str  # Basic, Standard, Premium
    price: int
    delivery_days: int
    revisions: int = 0
    description: str
    features: List[str] = []

class Gig(BaseModel):
    id: UUID
    title: str
    description: str
    category: Category
    packages: List[GigPackage]
    freelancer: dict  # { id, username, display_name, level, rating }
    tags: List[str] = []
    created_at: datetime
    total_orders: int = 0
    rating: float = 0.0

class Project(BaseModel):
    id: UUID
    title: str
    description: str
    category: Category
    budget: int
    budget_type: str  # fixed, hourly, milestone
    status: str  # open, in_progress, completed, cancelled
    proposals_count: int = 0
    client: dict  # { id, username, rating }
    skills_required: List[str] = []
    created_at: datetime
    deadline_at: Optional[datetime]
    is_verified_client: bool = False

class Proposal(BaseModel):
    cover_letter: str
    budget: int
    duration_days: int
    milestones: List[dict] = []
    attachments: List[str] = []

class FreelancerProfile(BaseModel):
    id: UUID
    username: str
    display_name: str
    email: Optional[str] = None  # only in own profile
    level: str  # beginner, intermediate, pro, top
    rating: float = 0.0
    total_earnings: int = 0
    completed_projects: int = 0
    member_since: datetime
    bio: Optional[str]
    skills: List[str] = []
    portfolio_count: int = 0
    verification_status: str = "unverified"
    is_online: bool = False

class Wallet(BaseModel):
    balance: int  # IDR
    pending: int = 0
    currency: str = "IDR"
```

## Proposal Template Engine

Sribu requires different proposal styles depending on the listing type. The MCP server should maintain three template families:

### Contest Entry Templates

Contest entries are primarily visual (file submissions) with a short description. The template should:

1. Reference the contest brief directly ("Saya sudah membaca brief Anda tentang [project_title]")
2. Explain the design approach (concept, color palette, typography choices)
3. List what files will be delivered
4. Offer revision terms
5. Be written in Indonesian, very casual and conversational
6. Avoid AI-like language (no numbered lists, no em dashes)

Template families:
- `logo_design` - Focus on brand identity, color psychology
- `packaging_design` - Focus on shelf impact, production feasibility
- `web_design` - Focus on UX, mobile-first, conversion
- `illustration` - Focus on style flexibility, revision rounds
- `general_design` - Catch-all for other design categories

### Project Proposal Templates

Project bids are more detailed and may include milestones:

1. Greeting and understanding of requirements
2. Past relevant experience (reference portfolio items)
3. Technical approach and methodology
4. Timeline breakdown
5. Pricing justification (can reference marketplace rates)
6. What happens after delivery (revisions, support period)

Template families:
- `web_development` - Tech stack, responsive, deployment
- `writing_translation` - Research process, SEO optimization
- `marketing` - Strategy-led, KPI-focused
- `data_entry` - Accuracy guarantees, volume pricing
- `consultation` - Methodology, deliverables, follow-up

### Gig Description Templates

Gig listings are permanent and need SEO-optimized copy:

1. Title starts with "Saya akan..." (mandatory Sribu convention)
2. Clear description of what the buyer gets
3. Package differentiation (Basic = essential, Standard = recommended, Premium = comprehensive)
4. Revision policy and communication channels
5. Delivery format and timeline
6. Tags for discoverability

## Rate Limiting and Error Handling

Sribu's API infrastructure appears to use a load balancer that returns 503 under stress or when request patterns are suspicious. The MCP server must handle this gracefully:

1. **503 Service Unavailable**: Backoff with exponential retry (1s, 2s, 4s, max 30s). If persistent for 5+ retries, emit a SIERRA_UNAVAILABLE warning and stop.

2. **401 Unauthorized**: Token expired or invalid. Set `token_invalid=true`, emit TOKEN_EXPIRED error, stop all authenticated operations.

3. **429 Rate Limit**: Not explicitly observed but assume a limit of 60 requests/minute based on comparable platforms. Implement a token bucket and 1s minimum between pages.

4. **403 Forbidden**: API key or client-id missing. This would require re-capturing from a browser session.

5. **404 Not Found**: Graceful handling -- return empty results, not an error.

## Integration with Fastwork MCP

The Freelancer AI Agent should be able to operate across both platforms via a unified orchestrator. The cross-platform integration points are:

1. **Unified Job Discovery**: Search both platforms and merge results into a single ranked feed, deduplicating by category and budget range.

2. **Cross-platform Proposal Priority**: If a job appears on both platforms (some clients cross-post), prefer the platform where the agent has a stronger profile/rating.

3. **Combined Ledger**: A single `applied_jobs.json` that tracks which jobs were applied to on which platform, preventing double-apply.

4. **Unified Template Bank**: Share proposal templates across platforms, adjusting tone and length per platform norms (Sribu: more visual, contest-focused; Fastwork: more text-based, service-oriented).

5. **Aggregated Analytics**: Combined earnings, win rate, and category performance across both platforms.

The orchestrator architecture:

```
freelancer-agent/
  orchestrator.py      # Cross-platform coordination
  sribu/               # Sribu MCP client (this spec)
  fastwork/            # Fastwork MCP client (from fastwork-mcp-spec.md)
  shared/
    templates.py       # Proposal template bank (platform-tagged)
    ledger.py          # Cross-platform apply history
    config.py          # Shared token storage
    analytics.py       # Aggregated performance metrics
```

## Implementation Roadmap

Phase 1 -- Read-Only Discovery (estimated 2-3 days):
1. Implement `sribu_client.py` with all GET endpoints
2. Set up auth.py with token injection
3. Implement `sribu_search_contests`, `sribu_search_projects`, `sribu_search_gigs`, `sribu_search_freelancers`, `sribu_get_profile`
4. Validate all endpoints with a live token
5. Write integration tests with recorded responses

Phase 2 -- Write Operations (estimated 3-5 days):
1. Implement `sribu_submit_contest_entry` with file upload support
2. Implement `sribu_submit_proposal` with milestone support
3. Implement `sribu_create_gig` with package validation
4. Implement `sribu_keep_online` heartbeat
5. Add the applied ledger and dry-run mode
6. Implement rate limiting and 503 retry logic

Phase 3 -- Cross-Platform Orchestration (estimated 2-3 days):
1. Build the unified orchestrator that merges Sribu + Fastwork feeds
2. Implement the shared template bank with platform-aware tone adjustment
3. Build aggregated analytics across both platforms
4. Add a unified notification system for new listings, contest wins, and messages

## Security and Compliance Notes

1. **Token Storage**: Never log the JWT token. Store it in a config.json with 600 permissions (user-read-only). The audit log must not include token values.

2. **Rate Limit Compliance**: Respect Sribu's rate limits to avoid account suspension. The 1s page delay is a minimum; increase to 2-3s during peak hours (WIB 09:00-17:00).

3. **Automation Detection**: Sribu uses Cloudflare or similar WAF (evidenced by the 503 and robots.txt blocks for GPTBot, ClaudeBot, etc.). The MCP server must use a realistic User-Agent string (e.g., `Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36`) and avoid headless browser fingerprints.

4. **Robots.txt Compliance Areas** (from observed robots.txt):
   - `/id/dashboard` - blocked
   - `/en/dashboard` - blocked
   - `/id/job-offer/*` - blocked
   - `/en/job-offer/*` - blocked
   - `/id/packages-form/*` - blocked
   - `/en/packages-form/*` - blocked
   - `/id/launch/*` - blocked
   - `/en/launch/*` - blocked
   The MCP server should NOT attempt to scrape these paths. All interactions should go through the API endpoints.

5. **Escrow Integrity**: The proposal/contest entry submission includes budget amounts. Never submit an offer the agent cannot fulfill. The `dry_run` flag must be used for validation before real submission.

## Testing Strategy

Without live API access, the MCP server should be built with a mock layer:

1. Define a `SribuAPIMock` class that returns realistic fixture data based on the observed page structures
2. Unit tests against the mock cover all tool paths
3. Record a "golden" session using a browser proxy (Charles, mitmproxy) for the first live validation
4. Compare mock responses against recorded golden responses to identify discrepancies
5. Once the API is confirmed, replace mock with `SribuAPILive` client

Fixture files (to be created in `test/fixtures/`):
- `categories.json` - Full category tree from page data
- `contests_open.json` - Sample open contests response
- `projects_open.json` - Sample open projects response
- `gigs_popular.json` - Sample gig listing response
- `profile_authenticated.json` - Sample profile response
- `entry_success.json` - Sample contest entry success response
- `proposal_success.json` - Sample proposal submission response

## Appendix: Extracted Sribu Category Hierarchy

The following hierarchy was extracted from the Sribu Next.js page data on 2026-07-28. Category UUIDs are preserved from the page render response.

### Desain Grafis & Branding (8df20334-7347-41c2-95e5-faad6fb31cec)

| Subcategory Group | Subcategories |
|---|---|
| Desain Logo & Identitas Branding | Brand Guidelines (e08a9942), Desain Kartu Nama (9c89c540), Desain Logo (791f6ffa), Desain Logo & Stationery (1d2bc385) |
| Desain Interior & Exterior | 3D & Perspektif (cbcbbb0c), Desain Arsitek Rumah (0c5fac01), Desain Booth (a28a4205), Desain Eksterior (16f53bcf), Desain Interior (fda39c07), Drafter AutoCAD (ae58091f) |
| Desain Kemasan & Label | Desain Kemasan (d27f6a78), Desain Label (6af84827), Desain Produk (e2aae650) |
| Desain Ilustrasi | Desain Icon (cdbf4e9b), Desain Infografis (1cc4f42c), Desain Mural (7c183ed8), Gambar & Ilustrasi (af66b989) |
| Desain untuk Kebutuhan Bisnis | Desain Company Profile (3a9de6d1), Desain Feed Instagram (b8e0e4f2), Desain Katalog (e84bb8c6), Desain Presentasi (5ed49a51) |
| Desain Aplikasi & Website | Desain Aplikasi Mobile (cc4ad484), Desain UI/UX (d1743dde), Desain Website (44e3c210) |
| Desain Cetak | 3D Printing (f7c53c97), Banner (1a2b3c4d), Brosur/Flyer, Cover Buku, Kalender, Menu, Poster, Sertifikat, Undangan |
| Desain Baju & Merchandise | Desain Baju (d8e8f908), Desain Merchandise (e9f0a1b2) |
| Desain & Kategori Lainnya | Brand Nama/Tagline (aecf1671), Desain Lainnya (20c55b5e), Desain Portfolio & Resume (6c65174b) |

Note: Some UUIDs for Desain Cetak subcategories are omitted here because they were not present in the extracted page data snippet. They should be captured from a live page render of each subcategory landing page.

### Web & Pemrograman (ad62c648-d223-446c-9a00-28c99613d0b5)

| Group | Subcategories |
|---|---|
| Website & Pemrograman | Aplikasi Desktop (20c21bd6), Data Scraping (b4ee8b9c), Pembuatan Website (254c728d), Undangan Digital (3df8452f) |
| Pembuatan Aplikasi | Aplikasi Mobile (37031664), Pembuatan Game (e50c1828) |
| Maintenance | IT Support (742d1ac7), Maintenance Website (94f5ee35), Optimasi Speed (8b28164c), Perbaikan Bug (dd06580d), QA (66f5e52a), Slicing ke HTML (e77f51e0) |
| Pemrograman Lainnya | Machine Learning (6b9e556f), Pengembangan Website Lainnya (d1e6538c), Programming Web (5f9e2589), Setting Mikrotik (e15f9d59) |

### Hot Subcategories (High Demand, is_hot=true)

From the extracted data, the following subcategories are tagged as "hot" (high demand):

- Desain Logo (791f6ffa)
- Data Scraping (b4ee8b9c)
- Pembuatan Website (254c728d)
- Aplikasi Mobile (37031664)
- Maintenance Website (94f5ee35)
- Programming Web (5f9e2589)
- Video Animasi (36421570)
- Voice Over (b542764a)
- Edit Foto (b3ac72ca)
- Edit Video (8713cd5d)
- Fotografi (c2244a7f)
- Video Social Media (0baddec9)
- Artikel & Blog Pos (eb957d09)
- Buku & Penulisan E-Book (26ae14c0)
- Copywriting (e8daa60e)
- Penulisan Naskah (24519854)
- Data Entry (4bb65977)
- Kelola Marketplace (feb42614)
- Social Media Marketing (f0de222e)
- Virtual Assistant (7660e07b)
- Konsultan Bisnis (9cca353e)
- Analisis Data (4fd31e63)
- Konsultan Keuangan (8175fd8a)
- Konsultan Hukum (b9c26693)
- Wedding Organizer (c459ea2f)
- Pembuatan Video AI (336a55de)
- Pengeditan Video AI (dc7929e1)
- Pembuatan Gambar AI (c21a7c9f)
- Layanan AI Lainnya (73f5ec9c)
- Prompt Writer AI (94296021)
- Hapus Akun Facebook (92d08108)
- Monetisasi YouTube (a1353ac5)
- Tambah Follower Media Sosial (524cdbfc)

These hot-tagged subcategories should be prioritized by the MCP server's search algorithm. They represent supply-demand imbalances where Sribu officially signals high buyer interest.

## References

1. Sribu.com homepage (accessed 2026-07-28). Sribu is a Next.js application with subdomain-based API microservices. Page data extracted from `https://www.sribu.com/id` HTML source.

2. Sribu robots.txt (accessed 2026-07-28). Blocked paths: GPTBot, ClaudeBot, /dashboard, /job-offer/, /packages-form/, /launch/. URL: `https://www.sribu.com/robots.txt`.

3. vault competitor analysis: 03-id-business-trends/competitors/fastwork-sribu-freelance-gaps.md (accessed 2026-07-06 via vault fs). Provides market share estimates, commission rates, and platform comparison data.

4. vault Fastwork MCP spec: 04-freelancer-ai-agent/mcp-servers/fastwork-mcp-spec.md (accessed 2026-07-28). Reference architecture for the MCP server pattern, auth model, and proposal template engine.

5. Sribu category page: `https://www.sribu.com/id/categories/website-and-development` (accessed 2026-07-28). Reveals subcategory UUIDs and hot-tagging system.

6. Sribu static pages: `https://go.sribu.com/id/about-sribu/`, `https://go.sribu.com/id/how-it-works-client/`, `https://go.sribu.com/id/how-it-works-freelancer/` (accessed 2026-07-28). Documentation of platform rules and workflows.

7. Sribu mobile apps: Google Play `com.sribu.app` and App Store `sribu-pilih-freelance-terbaik/id6504599670` (accessed 2026-07-28 via page meta). Indicates mobile API endpoints exist.

8. Sribu PSE registration: `https://pse.kominfo.go.id/tdpse-detail/4340` (accessed 2026-07-28 via footer). Sribu is registered as a Penyelenggara Sistem Elektronik with Kominfo, confirming regulatory compliance.

9. Sribu social media: Twitter/X (`@sribu`), Instagram (`@sribu`), Facebook (`sribudotcom`), LinkedIn (`company/sribu`), YouTube (`SribuCom`) (accessed 2026-07-28 via footer). Useful for signal monitoring and trend analysis.

Note: All API endpoints in this spec are inferred from frontend analysis and have NOT been verified with live requests. The `app.api.v2.sribu.com` host returned HTTP 503 during authoring, suggesting it requires specific request headers (Origin, Referer, client-id) or is WAF-protected. A browser proxy capture session is required for endpoint validation before the MCP server can be deployed.
