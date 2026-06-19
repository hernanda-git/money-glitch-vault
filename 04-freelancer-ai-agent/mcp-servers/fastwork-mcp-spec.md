# Fastwork MCP Server Specification

## AI-Native Freelance Automation for the Indonesian Market

**Date:** 2026-06-19
**Author:** Money Glitch Vault Auto-Enricher
**Status:** Specification v1.0
**Target Platform:** Node.js / Python with Model Context Protocol (MCP) SDK
**Repository:** `money-glitch-vault/04-freelancer-ai-agent/mcp-servers/`

---

## Table of Contents

- [1. Background and Rationale](#1-background-and-rationale)
- [2. What is MCP?](#2-what-is-mcp)
- [3. Fastwork Platform Overview](#3-fastwork-platform-overview)
- [4. Reverse-Engineered API Surface](#4-reverse-engineered-api-surface)
- [5. MCP Server Architecture](#5-mcp-server-architecture)
- [6. Tool Definitions](#6-tool-definitions)
- [7. Resource Definitions](#7-resource-definitions)
- [8. Prompt Templates](#8-prompt-templates)
- [9. Authentication and Session Management](#9-authentication-and-session-management)
- [10. Rate Limiting and Error Handling](#10-rate-limiting-and-error-handling)
- [11. Security Considerations](#11-security-considerations)
- [12. Implementation Walkthrough (TypeScript)](#12-implementation-walkthrough-typescript)
- [13. n8n Integration Pattern](#13-n8n-integration-pattern)
- [14. Example Workflows](#14-example-workflows)
- [15. Testing and Deployment](#15-testing-and-deployment)
- [16. Future Extensions](#16-future-extensions)

---

## 1. Background and Rationale

### 1.1 The Freelancer Payment Pain

The vault has documented a critical pain point (Signal Strength 4/5): Indonesian freelancers frequently face non-payment after completing projects. The 2025 PayPal survey (via Kompas.com, 2026-06-18) found that 58% of Southeast Asian freelancers have experienced non-payment. In Indonesia, the problem is compounded by:

- Escrow costs that can reach 10-20% on platforms like Fastwork and Sribu (source: Fastwork fee structure, fastwork.id)
- The absence of legal frameworks for freelance contracts
- Systematic exclusion of gig workers from formal financial safety nets like BPJS Ketenagakerjaan

### 1.2 Why an MCP Server Changes This

An MCP (Model Context Protocol) server for Fastwork enables AI agents to:

1. Automate job discovery by continuously scanning for new projects matching a freelancer's skillset
2. Generate and submit tailored proposals with zero human latency
3. Monitor order status, incoming messages, and payment releases in real-time
4. Maintain a local database of proposal templates proven to convert (see prompts section)
5. Coordinate with other MCP servers (e.g., a WhatsApp MCP for client communication, a payment MCP for tracking escrow releases)

This is not a chatbot wrapper. This is a structured tool server that gives LLMs (like Claude, GPT-4, or local models) the capability to act as a semi-autonomous freelance assistant.

### 1.3 Target Users

| User Persona | Skill Level | Use Case |
|---|---|---|
| Freelancer AI | Advanced | Automate entire pipeline: search, bid, deliver, follow up |
| Freelance Marketplace Power User | Intermediate | Use AI to draft proposals, track orders, manage messages |
| Agency Owner | Expert | Deploy multi-agent system: one agent monitors jobboard, another manages client comms, a third handles payments |
| No-Code Builder | Intermediate | Connect Fastwork MCP to n8n/Node-RED to build visual automation |

---

## 2. What is MCP?

The Model Context Protocol (MCP) is an open standard developed by Anthropic that allows AI models to interact with external tools, data sources, and services through a structured JSON-RPC interface. It was announced in November 2024 and has since been adopted by Claude Desktop, Cline, and various open-source clients.

### 2.1 Core Concepts

MCP defines three primitives:

**Tools** -- Actions an AI model can invoke (functions with typed parameters). Examples: `search_freelancers`, `submit_proposal`, `send_message`.

**Resources** -- Structured data that can be read by the AI. Examples: `fastwork://user/profile`, `fastwork://orders/active`.

**Prompts** -- Pre-built templates for common tasks. Examples: `proposal-generator`, `search-builder`.

### 2.2 Transport Layer

MCP supports two transports:

- **stdio**: Server runs as a child process, communicates via stdin/stdout. Ideal for local Claude Desktop integration.
- **HTTP+SSE**: Server runs as a web service, communicates via Server-Sent Events. Ideal for n8n, cloud deployments, and multi-client access.

Our Fastwork MCP server will support both.

### 2.3 Why MCP over Raw API Wrappers

A raw API wrapper (e.g., a Python `fastwork_client` library) requires human developers to write integration code for every new client. MCP decouples the API integration from the client application. Any MCP-compatible client (Claude, Cline, n8n with MCP plugin, custom agent) can immediately use all Fastwork tools without writing Fastwork-specific code.

Reference: https://modelcontextprotocol.io/docs/learn/architecture (MCP official docs, 2025)

---

## 3. Fastwork Platform Overview

Fastwork is the largest freelance marketplace in Southeast Asia, operating in Indonesia (fastwork.id), Thailand (fastwork.co), and Vietnam (fastlance.vn). It was founded in Thailand in 2017 and expanded to Indonesia in 2019.

### 3.1 Key Platform Metrics (Indonesia)

- 150,000+ completed projects (as stated on fastwork.id homepage, 2026-06-19)
- 70+ service subcategories
- Categories include: AI Services, Design, Writing & Translation, Marketing, Video & Animation, Music & Audio, Programming & Tech, Business, Lifestyle
- AI Services subcategories include: AI Video, AI Photo, AI Voice, Prompt Engineering, AI Course, AI Consultation, Chatbot, AI Automation, AI Agent, Custom AI Development, AI Integration
- Payment via escrow system with Fastwork Guarantee (Jaminan Fastwork)
- Commission fee (komisi) charged per transaction

### 3.2 Technology Stack (Reverse-Engineered from Page Source)

Based on analysis of the Fastwork.id homepage and application bundle (retrieved 2026-06-19):

| Component | Technology | Details |
|---|---|---|
| Frontend | Next.js (React) | Server-side rendered, version 1.57.0 |
| Styling | Turbine CSS framework | Custom @fastwork/turbine v2.5.5 |
| API Gateway | api.fastwork.id / gateway.fastwork.id | RESTful, JWT-authenticated |
| Chat System | chat-api.fastwork.id | WebSocket-based (socket.io likely) |
| Search | Algolia | App key: F24LUZ3XRM, Index: products_prod |
| Secondary Search | MeiliSearch | Host: search.fastwork.co, Index: products_id_prod |
| Auth | OAuth2 server at auth.fastwork.id | Supports Google + Facebook OAuth |
| Payment | FastPay (checkout.fastwork.id) | Escrow-based payment processing |
| File Storage | AWS S3 | fastwork-public.s3.ap-southeast-1.amazonaws.com |
| Firebase | Google Firebase | Auth, Realtime DB, Storage, Remote Config |
| CDN | jsDelivr, Cloudflare | Static assets and fonts |
| AI Search | Custom AI-powered search | Enabled by FEATURES.AI_SEARCH flag |
| Job Board | jobboard.fastwork.id | Separate subdomain for job posting + bidding |

### 3.3 Business Model

Fastwork operates on a commission-based marketplace model:

- **Freelancers (Sellers)**: Pay a commission fee (komisi) on each completed transaction. The exact percentage varies by tier (Free, Specialist, Professional) and is estimated at 10-20% based on competitor analysis (Sribu 20%, Projects.co.id 15%, Fastwork likely 10-15% for standard tier).
- **Buyers (Clients)**: Pay the full project amount upfront into escrow (Jaminan Fastwork). Funds are released to the freelancer upon project approval.
- **Featured Listings / Ads**: Freelancers can pay to promote their services via the advertising system (Sistem Iklan).
- **Specialist Program**: Freelancers who pass a vetting process get a Specialist badge, higher visibility, and access to exclusive projects.

Reference: fastwork.id homepage footer, "Cara Penggunaan" section (retrieved 2026-06-19); also Fastwork blog at blog.fastwork.id.

---

## 4. Reverse-Engineered API Surface

The following endpoints were inferred from the Next.js runtime configuration and page source analysis. No official public API documentation exists for Fastwork as of June 2026 -- this is a reconstruction based on observed client-server communication patterns.

### 4.1 Authentication

```
POST https://auth.fastwork.id/oauth/authorize
  -- OAuth2 authorization endpoint
  -- Required: client_id, redirect_uri, response_type, scope
  -- Returns: authorization code or access token

POST https://auth.fastwork.id/v1/oauth/token
  -- Token exchange endpoint
  -- Required: grant_type, code, redirect_uri, client_id, client_secret
  -- Returns: { access_token, refresh_token, expires_in, token_type }

POST https://auth.fastwork.id/oauth/signout-device
  -- Device-level signout
  -- Required: valid session cookie

DELETE https://auth.fastwork.id/v1/oauth/session
  -- Session revocation
```

### 4.2 Core API

```
# Search (Algolia-based)
POST https://api.fastwork.id/search-api/search
  -- Headers: X-Algolia-Application-Id: F24LUZ3XRM, X-Algolia-API-Key: [redacted]
  -- Body: { query, hitsPerPage, page, facetFilters }
  -- Returns: { hits, nbHits, page, nbPages }

# Category and subcategory listing
GET https://api.fastwork.id/categories
GET https://api.fastwork.id/subcategories

# Product (service listing) endpoints
GET https://api.fastwork.id/products/{productId}
  -- Returns: { id, title, description, price, userId, ... }
GET https://api.fastwork.id/users/{username}/products
  -- List products by a specific freelancer

# User profile
GET https://api.fastwork.id/users/{username}
  -- Returns: { id, username, displayName, avatar, rating, ... }

# Orders and transactions
GET https://api.fastwork.id/orders
GET https://api.fastwork.id/orders/{orderId}
POST https://api.fastwork.id/orders
  -- Create new order (hire freelancer)
PATCH https://api.fastwork.id/orders/{orderId}
  -- Update order status (approve, cancel, request revision)

# Chat/Messaging
GET https://chat-api.fastwork.id/api/conversations
GET https://chat-api.fastwork.id/api/conversations/{conversationId}/messages
POST https://chat-api.fastwork.id/api/conversations/{conversationId}/messages
  -- WebSocket: wss://chat-api.fastwork.id/socket

# Wallet and payments
GET https://api.fastwork.id/wallet/balance
GET https://api.fastwork.id/wallet/transactions
POST https://api.fastwork.id/withdrawal/request
```

### 4.3 Job Board API (Separate Subdomain)

```
# FastMatch service (job board matching)
POST https://fh.fastwork.id/fh-management-service/api/v1/matches
  -- AI-powered matching between buyers and freelancers

# Job board listings
GET https://jobboard.fastwork.id/api/jobs
POST https://jobboard.fastwork.id/api/jobs/{jobId}/apply
```

### 4.4 Rate Limiting Observations

From the client-side configuration:
- API_TIMEOUT_MILLISECOND: 10000 (10 seconds)
- BIDDING_POLLING_MILLISECOND: 30000 (30 seconds for job board polling)
- Rate limiting is likely enforced via IP-based throttling on the gateway (gateway.fastwork.id)

---

## 5. MCP Server Architecture

### 5.1 High-Level Design

```
+---------------------------+       +----------------------------+
|   MCP Client (Claude,     |       |   MCP Client (n8n,         |
|   Cline, custom agent)    |       |   custom web app)          |
+------------+--------------+       +-------------+--------------+
             |                                      |
             |  JSON-RPC (stdio or HTTP+SSE)        |
             |                                      |
             +----------+---------------+-----------+
                        |
             +----------v---------------v-----------+
             |        Fastwork MCP Server            |
             |  (Node.js / Python)                   |
             |                                       |
             |  +---------------------------------+  |
             |  | Tool Layer                       |  |
             |  | - search_freelancers             |  |
             |  | - get_product_details            |  |
             |  | - submit_proposal                |  |
             |  | - send_message                   |  |
             |  | - create_order                   |  |
             |  | - resolve_escrow                 |  |
             |  +---------------------------------+  |
             |  +---------------------------------+  |
             |  | Resource Layer                   |  |
             |  | - fastwork://user/profile        |  |
             |  | - fastwork://orders/{id}         |  |
             |  | - fastwork://chat/{convId}       |  |
             |  | - fastwork://marketplace/search  |  |
             |  +---------------------------------+  |
             |  +---------------------------------+  |
             |  | Session Manager                  |  |
             |  | - OAuth2 token refresh            |  |
             |  | - Cookie persistence              |  |
             |  | - Rate limit queue                |  |
             |  +---------------------------------+  |
             |  +---------------------------------+  |
             |  | API Adapter                     |  |
             |  | - HTTP client (axios/fetch)     |  |
             |  | - WebSocket client              |  |
             |  | - Algolia search client         |  |
             |  +---------------------------------+  |
             +---------------------------------------+
                        |
             +-----------v------------+
             | Fastwork Platform       |
             | (api.fastwork.id,       |
             |  auth.fastwork.id,      |
             |  chat-api.fastwork.id)  |
             +------------------------+
```

### 5.2 Component Responsibilities

**Tool Layer**: Exposes MCP tool definitions. Each tool is a function that takes typed parameters, calls the API Adapter, transforms the response into a structured result, and handles errors according to MCP conventions.

**Resource Layer**: Exposes MCP resource URIs. Each resource is a data fetcher that reads from the API Adapter or a local cache and returns structured content (text, JSON, or binary).

**Session Manager**: Manages OAuth2 token lifecycle including automatic refresh before expiry. Stores tokens encrypted using Fernet (symmetric encryption) in a local SQLite vault. Handles concurrent session support for multi-user deployments.

**API Adapter**: Thin wrapper around HTTP/WebSocket clients. Handles request signing, header injection (User-Agent, Accept-Language), response parsing, and error classification. Implements a token-bucket rate limiter.

### 5.3 Technology Choices

| Component | Primary Choice | Alternative |
|---|---|---|
| Runtime | Node.js 20+ LTS | Python 3.11+ |
| MCP SDK | @modelcontextprotocol/sdk | mcp-python-sdk (community) |
| HTTP Client | undici (built into Node 20+) | axios, node-fetch |
| Search Client | algoliasearch | MeiliSearch JS client |
| WebSocket | ws | socket.io-client |
| Encryption | Node crypto (Fernet-compatible) | cryptography (Python) |
| State Store | better-sqlite3 | SQLite via sqlite3 |
| Config | dotenv + JSON schema | python-dotenv |

---

## 6. Tool Definitions

### 6.1 Tool Inventory

The MCP server exposes the following tools, grouped by domain:

#### Marketplace Tools

| Tool Name | Description | Parameters |
|---|---|---|
| `search_services` | Search for freelance services on Fastwork using keywords, category, price range, and rating filters | query, categorySlug, minPrice, maxPrice, minRating, sortBy, page, hitsPerPage |
| `get_service_details` | Get full details of a specific service listing | productId |
| `get_user_profile` | Get a freelancer or buyer's public profile | username |
| `list_categories` | List all available service categories and subcategories | none |
| `list_user_services` | List all services offered by a specific user | username, page |

#### Order Management Tools

| Tool Name | Description | Parameters |
|---|---|---|
| `create_order` | Hire a freelancer by creating an order for a specific service | productId, message, quantity, requiredDocuments |
| `get_order_status` | Get current status of an order | orderId |
| `list_orders` | List all orders (as buyer or seller) | role, status, page, limit |
| `approve_order` | Mark an order as complete and release escrow payment | orderId, rating, reviewText |
| `request_revision` | Request changes to delivered work | orderId, revisionNotes |
| `cancel_order` | Cancel an order before delivery | orderId, reason |

#### Communication Tools

| Tool Name | Description | Parameters |
|---|---|---|
| `send_message` | Send a message in an order conversation | orderId, messageText, attachmentUrls |
| `get_conversation` | Get message history for an order | orderId, limit, beforeId |
| `list_conversations` | List all active conversations | page, limit |

#### Wallet and Finance Tools

| Tool Name | Description | Parameters |
|---|---|---|
| `get_wallet_balance` | Get current wallet balance | none |
| `get_transaction_history` | Get recent transaction history | page, limit, fromDate, toDate |
| `request_withdrawal` | Request withdrawal to bank account | amount, bankAccountId |

#### Job Board Tools

| Tool Name | Description | Parameters |
|---|---|---|
| `search_jobs` | Search for posted jobs on the Fastwork Job Board | query, category, budgetMin, budgetMax, page |
| `get_job_details` | Get full details of a posted job | jobId |
| `submit_job_proposal` | Submit a proposal for a posted job | jobId, coverLetter, bidAmount, estimatedDays |

### 6.2 Tool Parameter Schemas (TypeScript)

```typescript
// -- Tool: search_services --

interface SearchServicesParams {
  query: string;              // Search keywords
  categorySlug?: string;      // Filter by category (e.g., "ai-agent", "graphic-design")
  minPrice?: number;          // Minimum price in IDR
  maxPrice?: number;          // Maximum price in IDR
  minRating?: number;         // Minimum seller rating (1-5)
  sortBy?: "relevance" | "price_asc" | "price_desc" | "rating" | "newest";
  page?: number;              // Page number (default: 1)
  hitsPerPage?: number;       // Results per page (default: 20, max: 100)
}

interface SearchServicesResult {
  hits: ServiceHit[];
  totalHits: number;
  page: number;
  totalPages: number;
}

interface ServiceHit {
  id: string;
  title: string;
  description: string;
  price: number;
  currency: "IDR";
  userId: string;
  username: string;
  sellerName: string;
  sellerAvatar: string;
  rating: number;
  reviewCount: number;
  category: string;
  subcategory: string;
  tags: string[];
  images: string[];
  deliveryTime: string;       // e.g., "1-3 hari"
  features: string[];         // Included features/bonuses
  isSpecialist: boolean;
  isProfessional: boolean;
  purchaseCount: number;
}


// -- Tool: create_order --

interface CreateOrderParams {
  productId: string;          // The service listing ID
  message: string;            // Initial message to the freelancer
  quantity?: number;          // Number of packages (default: 1)
  requiredDocuments?: string[]; // Any files or documents to attach
}

interface CreateOrderResult {
  orderId: string;
  status: "pending_payment" | "active";
  totalAmount: number;
  escrowAmount: number;
  feeAmount: number;
  createdAt: string;
  sellerUsername: string;
}


// -- Tool: submit_job_proposal --

interface SubmitJobProposalParams {
  jobId: string;
  coverLetter: string;       // Proposal letter (max 5000 chars)
  bidAmount: number;         // Your bid in IDR
  estimatedDays: number;     // Estimated completion time in days
  portfolioUrls?: string[];  // Links to relevant past work
}

interface SubmitJobProposalResult {
  proposalId: string;
  status: "submitted" | "accepted" | "rejected";
  submittedAt: string;
}
```

### 6.3 Tool Implementation Patterns

Every tool follows the same pattern:

```typescript
import { z } from "zod";
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";

// 1. Define Zod schema for parameter validation
const SearchServicesSchema = z.object({
  query: z.string().min(1).max(200),
  categorySlug: z.string().optional(),
  minPrice: z.number().positive().optional(),
  maxPrice: z.number().positive().optional(),
  minRating: z.number().min(1).max(5).optional(),
  sortBy: z.enum(["relevance", "price_asc", "price_desc", "rating", "newest"]).optional(),
  page: z.number().int().positive().default(1),
  hitsPerPage: z.number().int().min(1).max(100).default(20),
});

// 2. Register with MCP server
server.tool(
  "search_services",
  "Search for freelance services on Fastwork by keyword, category, price range, and rating.",
  SearchServicesSchema.shape,
  async (params) => {
    // 3. Authenticate
    const session = await sessionManager.getValidSession();

    // 4. Call API adapter
    const result = await apiAdapter.searchAlgolia({
      indexName: "products_prod",
      query: params.query,
      filters: buildFilters(params),
      page: params.page - 1, // Algolia is 0-indexed
      hitsPerPage: params.hitsPerPage,
    });

    // 5. Transform response
    return {
      content: [{
        type: "text",
        text: JSON.stringify({
          hits: result.hits.map(transformHit),
          totalHits: result.nbHits,
          page: params.page,
          totalPages: Math.ceil(result.nbHits / params.hitsPerPage),
        }, null, 2),
      }],
    };
  },
);
```

### 6.4 Error Response Convention

All tools return errors using MCP's structured error format:

```typescript
{
  content: [{
    type: "text",
    text: JSON.stringify({
      error: true,
      code: "AUTH_EXPIRED",
      message: "Session token has expired. Please re-authenticate.",
      recoverable: true,
    }),
  }],
  isError: true,
}
```

Standard error codes:
- `AUTH_EXPIRED` -- Token expired, needs refresh (recoverable)
- `AUTH_INVALID` -- Token invalid, needs re-login (recoverable through re-auth)
- `RATE_LIMITED` -- Too many requests, wait and retry (recoverable)
- `NOT_FOUND` -- Resource doesn't exist (not recoverable)
- `VALIDATION_ERROR` -- Invalid parameters (not recoverable)
- `PLATFORM_ERROR` -- Fastwork API returned an error (possibly recoverable)
- `NETWORK_ERROR` -- Connection issue (recoverable)

---

## 7. Resource Definitions

Resources provide structured access to data that the AI model can read.

### 7.1 Resource URI Scheme

```
fastwork://user/{username}/profile
fastwork://user/{username}/services
fastwork://orders/{orderId}
fastwork://orders?status=active
fastwork://chat/{conversationId}?limit=50
fastwork://wallet/balance
fastwork://wallet/transactions?limit=10
fastwork://marketplace/categories
fastwork://marketplace/search?q={query}
fastwork://jobboard/jobs?category={slug}
fastwork://jobboard/job/{jobId}
```

### 7.2 Resource Definitions

```typescript
// -- Profile Resource --

server.resource(
  "user-profile",
  "fastwork://user/{username}/profile",
  async (uri, { username }) => {
    const session = await sessionManager.getValidSession();
    const profile = await apiAdapter.getUserProfile(username);

    return {
      contents: [{
        uri: uri.href,
        mimeType: "application/json",
        text: JSON.stringify({
          username: profile.username,
          displayName: profile.displayName,
          avatar: profile.avatar,
          memberSince: profile.createdAt,
          rating: profile.rating,
          reviewCount: profile.reviewCount,
          responseTime: profile.responseTime,
          isSpecialist: profile.isSpecialist,
          isProfessional: profile.isProfessional,
          description: profile.description,
          skills: profile.skills,
          languages: profile.languages,
          education: profile.education,
          certificates: profile.certificates,
        }, null, 2),
      }],
    };
  },
);


// -- Order Resource --

server.resource(
  "order-detail",
  "fastwork://orders/{orderId}",
  async (uri, { orderId }) => {
    const session = await sessionManager.getValidSession();
    const order = await apiAdapter.getOrder(orderId);

    return {
      contents: [{
        uri: uri.href,
        mimeType: "application/json",
        text: JSON.stringify({
          id: order.id,
          status: order.status,
          createdAt: order.createdAt,
          serviceTitle: order.product.title,
          sellerName: order.seller.displayName,
          buyerName: order.buyer.displayName,
          price: order.price,
          fee: order.fee,
          totalAmount: order.totalAmount,
          escrowStatus: order.escrowStatus,
          milestones: order.milestones,
          deliveryDate: order.deliveryDate,
          messages: order.recentMessages?.slice(-5), // Last 5 messages preview
        }, null, 2),
      }],
    };
  },
);


// -- Conversation Resource (rendered as markdown for AI readability) --

server.resource(
  "conversation",
  "fastwork://chat/{conversationId}",
  async (uri, { conversationId }) => {
    const session = await sessionManager.getValidSession();
    const messages = await apiAdapter.getConversationMessages(conversationId);

    const markdown = messages.map(msg =>
      `**${msg.senderName}** (${new Date(msg.createdAt).toLocaleString("id-ID")}):\n${msg.text}`
    ).join("\n\n---\n\n");

    return {
      contents: [{
        uri: uri.href,
        mimeType: "text/markdown",
        text: markdown,
      }],
    };
  },
);
```

---

## 8. Prompt Templates

MCP prompts provide reusable templates that guide the AI on how to use the tools effectively. These are critical for consistent, high-quality output.

### 8.1 Proposal Generator Prompt

```typescript
server.prompt(
  "proposal-generator",
  "Generate a winning proposal for a Fastwork job posting based on the job details and your skills.",
  { jobId: "string", userSkills: "string" },
  async ({ jobId, userSkills }) => {
    // First fetch the job details using a resource
    // Then construct the conversation context
    return {
      messages: [{
        role: "system",
        content: {
          type: "text",
          text: `You are an expert freelance proposal writer for the Indonesian market.
            Your task is to write a compelling proposal for a job on Fastwork.id.

            RULES:
            - Write in Bahasa Indonesia unless the job posting is in English
            - Address the specific requirements in the job description
            - Reference relevant experience from the freelancer's skills
            - Include a clear timeline and price breakdown
            - Keep between 200-500 words
            - DO NOT use generic templates -- personalize for each job
            - End with a call to action (invite to chat)
            - Mention that Fastwork escrow protects both parties

            Based on the job details below and the freelancer's skills,
            generate a complete proposal ready to submit.`,
        },
      }, {
        role: "user",
        content: {
          type: "text",
          text: `JOB DETAILS:\n${JSON.stringify(jobDetails, null, 2)}\n\nFREELANCER SKILLS:\n${userSkills}`,
        },
      }],
    };
  },
);
```

### 8.2 Market Research Prompt

```typescript
server.prompt(
  "market-research",
  "Analyze the Fastwork marketplace to identify high-demand, low-competition service niches.",
  { categorySlug: "string" },
  async ({ categorySlug }) => {
    return {
      messages: [{
        role: "system",
        content: {
          type: "text",
          text: `You are a marketplace analyst for Fastwork Indonesia.
            Your job is to analyze the marketplace data for a given category
            and identify opportunities where demand exceeds supply.

            For each opportunity, provide:
            1. The specific subcategory or service type
            2. Estimated monthly searches (from Algolia search volume)
            3. Number of competing sellers
            4. Average price range
            5. Gap score (demand/supply ratio)
            6. Recommended entry strategy

            Use the search_services tool to gather data on multiple subcategories.`,
        },
      }],
    };
  },
);
```

### 8.3 Order Follow-Up Prompt

```typescript
server.prompt(
  "order-follow-up",
  "Send a professional follow-up message to a client about an active order.",
  { orderId: "string" },
  async ({ orderId }) => {
    return {
      messages: [{
        role: "system",
        content: {
          type: "text",
          text: `You are a professional freelance assistant on Fastwork.
            Generate a polite, professional follow-up message to a client.

            Guidelines:
            - Reference the specific order and project status
            - Be respectful of the client's time
            - Offer specific next steps
            - Keep it under 150 words
            - Write in the same language as previous messages in the conversation`,
        },
      }],
    };
  },
);
```

---

## 9. Authentication and Session Management

### 9.1 OAuth2 Flow

Fastwork uses OAuth2 with authorization code grant. The MCP server must handle the full flow:

```
Step 1: Redirect user to Fastwork auth URL
  https://auth.fastwork.id/oauth/authorize?
    client_id=076ba9d7-275f-4edd-b055-060f0547cf5e&
    redirect_uri=http://localhost:3456/auth/callback&
    response_type=code&
    scope=openid+profile+email

Step 2: User logs in and authorizes
Step 3: Fastwork redirects to redirect_uri with ?code={authCode}
Step 4: Exchange code for tokens:
  POST https://auth.fastwork.id/v1/oauth/token
  Body: {
    grant_type: "authorization_code",
    code: authCode,
    redirect_uri: "http://localhost:3456/auth/callback",
    client_id: "076ba9d7-...",
    client_secret: "..."  // NOTE: Client secret exposed in web bundle
  }
  Response: { access_token, refresh_token, expires_in, token_type }

Step 5: Store tokens encrypted, use access_token for API calls
Step 6: When access_token expires, use refresh_token to get new one
  POST https://auth.fastwork.id/v1/oauth/token
  Body: {
    grant_type: "refresh_token",
    refresh_token: "...",
    client_id: "076ba9d7-..."
  }
```

### 9.2 Encrypted Token Storage

```typescript
import { randomBytes, createCipheriv, createDecipheriv } from "node:crypto";
import Database from "better-sqlite3";

class SecureTokenStore {
  private db: Database.Database;
  private encryptionKey: Buffer;

  constructor(dbPath: string, masterKey: string) {
    this.db = new Database(dbPath);
    // Derive 256-bit key from master password using PBKDF2
    this.encryptionKey = crypto.pbkdf2Sync(
      masterKey,
      "fastwork-mcp-salt",
      100000,
      32,
      "sha256",
    );
    this.initialize();
  }

  private initialize() {
    this.db.exec(`
      CREATE TABLE IF NOT EXISTS sessions (
        id TEXT PRIMARY KEY,
        user_id TEXT NOT NULL,
        encrypted_tokens TEXT NOT NULL,
        created_at TEXT DEFAULT (datetime('now')),
        expires_at TEXT,
        is_active INTEGER DEFAULT 1
      )
    `);
  }

  async storeTokens(userId: string, tokens: Tokens): Promise<string> {
    const sessionId = randomUUID();
    const iv = randomBytes(16);
    const cipher = createCipheriv("aes-256-gcm", this.encryptionKey, iv);

    let encrypted = cipher.update(JSON.stringify(tokens), "utf8", "hex");
    encrypted += cipher.final("hex");
    const authTag = cipher.getAuthTag().toString("hex");

    const payload = JSON.stringify({ iv: iv.toString("hex"), data: encrypted, tag: authTag });

    this.db.prepare(`
      INSERT INTO sessions (id, user_id, encrypted_tokens, created_at, expires_at)
      VALUES (?, ?, ?, datetime('now'), datetime('now', '+30 days'))
    `).run(sessionId, userId, payload);

    return sessionId;
  }

  async retrieveTokens(sessionId: string): Promise<Tokens | null> {
    const row = this.db.prepare(
      "SELECT encrypted_tokens FROM sessions WHERE id = ? AND is_active = 1",
    ).get(sessionId) as { encrypted_tokens: string } | undefined;

    if (!row) return null;

    const { iv, data, tag } = JSON.parse(row.encrypted_tokens);
    const decipher = createDecipheriv("aes-256-gcm", this.encryptionKey, Buffer.from(iv, "hex"));
    decipher.setAuthTag(Buffer.from(tag, "hex"));

    let decrypted = decipher.update(data, "hex", "utf8");
    decrypted += decipher.final("utf8");

    return JSON.parse(decrypted);
  }
}
```

### 9.3 Session Manager with Auto-Refresh

```typescript
class SessionManager {
  private tokenStore: SecureTokenStore;
  private activeSession: Session | null = null;
  private refreshTimer: NodeJS.Timeout | null = null;

  async initialize(sessionId?: string) {
    if (sessionId) {
      const tokens = await this.tokenStore.retrieveTokens(sessionId);
      if (tokens) {
        this.activeSession = { sessionId, tokens };
        this.scheduleRefresh(tokens);
      }
    }
  }

  async getValidSession(): Promise<Session> {
    if (!this.activeSession) {
      throw new McpError(ErrorCode.InvalidRequest, "No active session. Use authenticate() first.");
    }

    // Check if token expires within 5 minutes
    const expiresAt = new Date(this.activeSession.tokens.expires_at).getTime();
    if (expiresAt - Date.now() < 5 * 60 * 1000) {
      await this.refreshSession();
    }

    return this.activeSession;
  }

  private async refreshSession() {
    try {
      const response = await fetch("https://auth.fastwork.id/v1/oauth/token", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          grant_type: "refresh_token",
          refresh_token: this.activeSession!.tokens.refresh_token,
          client_id: CLIENT_ID,
        }),
      });

      const newTokens = await response.json();
      this.activeSession!.tokens = newTokens;
      await this.tokenStore.updateTokens(this.activeSession!.sessionId, newTokens);
      this.scheduleRefresh(newTokens);
    } catch (error) {
      // Refresh failed -- mark session as expired, client needs re-auth
      this.activeSession = null;
      throw new McpError(ErrorCode.InvalidRequest, "Session expired. Please re-authenticate.");
    }
  }

  private scheduleRefresh(tokens: Tokens) {
    if (this.refreshTimer) clearTimeout(this.refreshTimer);
    // Refresh 10 minutes before expiry
    const expiresAt = new Date(tokens.expires_at).getTime();
    const refreshIn = Math.max(0, expiresAt - Date.now() - 10 * 60 * 1000);
    this.refreshTimer = setTimeout(() => this.refreshSession(), refreshIn);
  }
}
```

### 9.4 Authentication Tool

The MCP server exposes an `authenticate` tool that handles the OAuth2 flow:

```typescript
server.tool(
  "authenticate",
  "Start or resume authentication with Fastwork. If a sessionId is provided, resume that session. Otherwise, start a new OAuth2 flow.",
  {
    sessionId: z.string().optional(),
    authCode: z.string().optional(),
  },
  async ({ sessionId, authCode }) => {
    if (sessionId) {
      // Resume existing session
      await sessionManager.initialize(sessionId);
      return {
        content: [{
          type: "text",
          text: `Session resumed. Authenticated as user ${(await sessionManager.getValidSession()).userId}`,
        }],
      };
    }

    if (authCode) {
      // Complete OAuth2 flow with authorization code
      const tokens = await exchangeAuthCode(authCode);
      const newSessionId = await tokenStore.storeTokens(tokens.userId, tokens);
      await sessionManager.initialize(newSessionId);
      return {
        content: [{
          type: "text",
          text: `Authentication successful. Session ID: ${newSessionId}\nSave this session ID to resume without re-authenticating.`,
        }],
      };
    }

    // Start OAuth2 flow -- provide URL for user to visit
    const authUrl = buildAuthUrl();
    return {
      content: [{
        type: "text",
        text: `Please visit this URL to authorize Fastwork access:\n${authUrl}\n\nAfter authorizing, call authenticate() with the code parameter from the redirect URL.`,
      }],
    };
  },
);
```

---

## 10. Rate Limiting and Error Handling

### 10.1 Token-Bucket Rate Limiter

Fastwork's API endpoints have implicit rate limits (observed timeout: 10 seconds). The MCP server implements a token-bucket algorithm to stay within limits:

```typescript
class RateLimiter {
  private tokens: number;
  private lastRefill: number;
  private readonly maxTokens: number;
  private readonly refillRate: number; // tokens per second
  private readonly queue: Array<{ resolve: Function, reject: Function }> = [];

  constructor(maxRequestsPerSecond: number) {
    this.maxTokens = maxRequestsPerSecond;
    this.tokens = maxRequestsPerSecond;
    this.refillRate = maxRequestsPerSecond;
    this.lastRefill = Date.now();
  }

  async acquire(): Promise<void> {
    this.refill();

    if (this.tokens >= 1) {
      this.tokens--;
      return;
    }

    // Queue the request
    const waitTime = (1 - this.tokens) / this.refillRate * 1000;
    return new Promise(resolve => {
      setTimeout(() => {
        this.refill();
        this.tokens--;
        resolve();
      }, waitTime);
    });
  }

  private refill() {
    const now = Date.now();
    const elapsed = (now - this.lastRefill) / 1000;
    this.tokens = Math.min(this.maxTokens, this.tokens + elapsed * this.refillRate);
    this.lastRefill = now;
  }
}

// Rate limit configuration per endpoint group
const rateLimiters = {
  search: new RateLimiter(5),    // 5 search requests/second
  orders: new RateLimiter(3),    // 3 order requests/second
  chat: new RateLimiter(2),      // 2 chat requests/second
  auth: new RateLimiter(1),      // 1 auth request/second
};
```

### 10.2 Retry with Exponential Backoff

```typescript
async function withRetry<T>(
  fn: () => Promise<T>,
  options: { maxRetries?: number; baseDelayMs?: number } = {},
): Promise<T> {
  const { maxRetries = 3, baseDelayMs = 1000 } = options;
  let lastError: Error;

  for (let attempt = 0; attempt <= maxRetries; attempt++) {
    try {
      return await fn();
    } catch (error) {
      lastError = error as Error;

      // Don't retry non-recoverable errors
      if (error instanceof McpError && !error.recoverable) {
        throw error;
      }

      if (attempt < maxRetries) {
        const delay = baseDelayMs * Math.pow(2, attempt) + Math.random() * 1000;
        await new Promise(resolve => setTimeout(resolve, delay));
      }
    }
  }

  throw lastError!;
}
```

### 10.3 Error Classification

```typescript
function classifyApiError(statusCode: number, body: any): McpError {
  switch (statusCode) {
    case 401:
      return new McpError(
        ErrorCode.InvalidRequest,
        "Authentication failed. Token may be expired.",
        true, // recoverable
        "AUTH_EXPIRED",
      );
    case 429:
      return new McpError(
        ErrorCode.InvalidRequest,
        "Rate limited. Retry after the suggested delay.",
        true,
        "RATE_LIMITED",
      );
    case 404:
      return new McpError(
        ErrorCode.InvalidRequest,
        body?.error?.message || "Resource not found.",
        false,
        "NOT_FOUND",
      );
    case 422:
      return new McpError(
        ErrorCode.InvalidParams,
        body?.error?.message || "Validation failed.",
        false,
        "VALIDATION_ERROR",
      );
    case 500:
    case 502:
    case 503:
      return new McpError(
        ErrorCode.InternalError,
        "Fastwork platform error. Try again later.",
        true,
        "PLATFORM_ERROR",
      );
    default:
      return new McpError(
        ErrorCode.InternalError,
        `Unexpected API error (${statusCode})`,
        true,
        "NETWORK_ERROR",
      );
  }
}
```

---

## 11. Security Considerations

### 11.1 Credential Storage

- OAuth2 tokens are encrypted at rest using AES-256-GCM with a key derived from a master password via PBKDF2 (100,000 iterations).
- The master password is never stored on disk. It is provided via environment variable `FASTWORK_MCP_MASTER_KEY` at server startup.
- Session IDs are UUIDv4 and are the only identifier passed to the AI model. The model never sees raw tokens.
- Token refresh is automatic and transparent to the AI model.

### 11.2 Rate Limit Abuse Prevention

- The rate limiter uses a token-bucket algorithm with per-endpoint-group limits.
- AI models may attempt rapid-fire calls (e.g., searching 100 different queries). The rate limiter serializes these and delays excess requests.
- A circuit breaker pattern is implemented: if 5 consecutive requests to an endpoint fail with 5xx errors, the circuit opens for 30 seconds.

### 11.3 Data Privacy

- The MCP server never stores Fastwork user data beyond session tokens. All resource fetches are real-time API calls.
- Chat messages fetched via resources are cached in memory for at most 5 minutes (TTL cache).
- The server logs only anonymized request counts, never message content or user PII.
- When used as an HTTP server, TLS is mandatory (HTTPS). Self-signed certificates are acceptable for development but production deployments should use Let's Encrypt.

### 11.4 Client Secret Exposure Risk

The Fastwork OAuth2 client secret was observed in the client-side JavaScript bundle (runtime config). This means:

1. Anyone can technically authenticate to Fastwork's API as any user who consents via OAuth2.
2. The MCP server treats this as a known risk and implements additional security:
   - Each session is tied to a specific user's consent (delegated authorization).
   - The server cannot act on behalf of users who have not explicitly authorized it.
   - If Fastwork rotates their client secret, the server must be updated.

### 11.5 Secure Deployment Checklist

```
[ ] MCP server runs in a containerized environment (Docker)
[ ] Environment variables loaded from .env file (gitignored)
[ ] Production deployments use HTTPS (TLS 1.3)
[ ] Logging level set to WARN or ERROR in production (not DEBUG)
[ ] Master encryption key stored in secrets vault (e.g., HashiCorp Vault, AWS Secrets Manager)
[ ] Network egress restricted to fastwork.id and auth.fastwork.id only
[ ] Rate limiting enabled and tuned per deployment scale
[ ] Session token database backed up to encrypted storage
```

---

## 12. Implementation Walkthrough (TypeScript)

### 12.1 Project Structure

```
fastwork-mcp-server/
  package.json
  tsconfig.json
  .env.example
  .gitignore
  Dockerfile
  docker-compose.yml
  src/
    index.ts              # Entry point, server initialization
    config.ts             # Environment configuration
    server.ts             # MCP server setup and tool registration
    session-manager.ts    # OAuth2 authentication and token management
    secure-store.ts       # Encrypted SQLite token storage
    api-adapter.ts        # Fastwork HTTP API client
    algolia-client.ts     # Algolia search integration
    rate-limiter.ts       # Token-bucket rate limiter
    tools/
      marketplace.ts      # search_services, get_service_details, etc.
      orders.ts           # create_order, get_order_status, etc.
      communication.ts    # send_message, get_conversation, etc.
      wallet.ts           # get_wallet_balance, etc.
      jobboard.ts         # search_jobs, submit_job_proposal, etc.
    resources/
      user.ts             # User profile resource
      orders.ts           # Order resources
      chat.ts             # Conversation resources
      marketplace.ts      # Search resource
    prompts/
      proposal-generator.ts
      market-research.ts
      order-follow-up.ts
```

### 12.2 Main Server Entry Point

```typescript
// src/index.ts

import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { SSEServerTransport } from "@modelcontextprotocol/sdk/server/sse.js";
import express from "express";
import { loadConfig } from "./config.js";
import { SessionManager } from "./session-manager.js";
import { ApiAdapter } from "./api-adapter.js";
import { registerMarketplaceTools } from "./tools/marketplace.js";
import { registerOrderTools } from "./tools/orders.js";
import { registerCommunicationTools } from "./tools/communication.js";
import { registerWalletTools } from "./tools/wallet.js";
import { registerJobBoardTools } from "./tools/jobboard.js";
import { registerUserResources } from "./resources/user.js";
import { registerOrderResources } from "./resources/orders.js";
import { registerChatResources } from "./resources/chat.js";
import { registerPrompts } from "./prompts/index.js";

async function main() {
  const config = loadConfig();

  // Initialize dependencies
  const sessionManager = new SessionManager(config);
  const apiAdapter = new ApiAdapter(config, sessionManager);

  // Create MCP server
  const server = new McpServer({
    name: "fastwork-mcp-server",
    version: "1.0.0",
    description: "MCP server for Fastwork.id, the Indonesian freelance marketplace. Enables AI agents to search services, manage orders, submit proposals, and communicate with clients.",
  });

  // Register all tools, resources, and prompts
  registerMarketplaceTools(server, apiAdapter);
  registerOrderTools(server, apiAdapter);
  registerCommunicationTools(server, apiAdapter, sessionManager);
  registerWalletTools(server, apiAdapter);
  registerJobBoardTools(server, apiAdapter);
  registerUserResources(server, apiAdapter);
  registerOrderResources(server, apiAdapter);
  registerChatResources(server, apiAdapter);
  registerPrompts(server, apiAdapter);

  // Choose transport based on configuration
  if (config.transport === "stdio") {
    const transport = new StdioServerTransport();
    await server.connect(transport);
    console.error("Fastwork MCP server running on stdio transport");
  } else if (config.transport === "sse") {
    // HTTP+SSE transport for n8n and remote access
    const app = express();
    const transports: Map<string, SSEServerTransport> = new Map();

    app.get("/sse", async (req, res) => {
      const transport = new SSEServerTransport("/messages", res);
      transports.set(transport.sessionId, transport);
      res.on("close", () => {
        transports.delete(transport.sessionId);
      });
      await server.connect(transport);
    });

    app.post("/messages", (req, res) => {
      const sessionId = req.query.sessionId as string;
      const transport = transports.get(sessionId);
      if (transport) {
        transport.handlePostMessage(req, res);
      }
    });

    app.listen(config.port, () => {
      console.error(`Fastwork MCP server running on http://localhost:${config.port}/sse`);
    });
  }
}

main().catch(console.error);
```

### 12.3 Configuration

```typescript
// src/config.ts

import { z } from "zod";

const ConfigSchema = z.object({
  transport: z.enum(["stdio", "sse"]).default("stdio"),
  port: z.coerce.number().int().positive().default(3456),
  fastworkClientId: z.string().default("076ba9d7-275f-4edd-b055-060f0547cf5e"),
  fastworkAuthUrl: z.string().default("https://auth.fastwork.id"),
  fastworkApiUrl: z.string().default("https://api.fastwork.id"),
  fastworkChatApiUrl: z.string().default("https://chat-api.fastwork.id"),
  algoliaAppId: z.string().default("F24LUZ3XRM"),
  algoliaApiKey: z.string().default(process.env.ALGOLIA_API_KEY || ""),
  masterKey: z.string().min(8, "Master encryption key must be at least 8 characters"),
  dbPath: z.string().default("./data/fastwork-sessions.db"),
  logLevel: z.enum(["debug", "info", "warn", "error"]).default("info"),
});

export type Config = z.infer<typeof ConfigSchema>;

export function loadConfig(): Config {
  return ConfigSchema.parse({
    transport: process.env.MCP_TRANSPORT,
    port: process.env.MCP_PORT,
    masterKey: process.env.FASTWORK_MCP_MASTER_KEY,
    dbPath: process.env.FASTWORK_DB_PATH,
    logLevel: process.env.LOG_LEVEL,
    algoliaApiKey: process.env.ALGOLIA_API_KEY,
  });
}
```

### 12.4 API Adapter (Core HTTP Client)

```typescript
// src/api-adapter.ts

import { SessionManager } from "./session-manager.js";
import { RateLimiter } from "./rate-limiter.js";
import { Config } from "./config.js";

interface RequestOptions {
  method?: string;
  headers?: Record<string, string>;
  body?: any;
  retry?: boolean;
}

export class ApiAdapter {
  private rateLimiters = {
    search: new RateLimiter(5),
    orders: new RateLimiter(3),
    chat: new RateLimiter(2),
    default: new RateLimiter(4),
  };

  constructor(
    private config: Config,
    private sessionManager: SessionManager,
  ) {}

  private getRateLimiter(endpoint: string): RateLimiter {
    if (endpoint.includes("search")) return this.rateLimiters.search;
    if (endpoint.includes("order")) return this.rateLimiters.orders;
    if (endpoint.includes("chat")) return this.rateLimiters.chat;
    return this.rateLimiters.default;
  }

  async request<T = any>(
    endpoint: string,
    options: RequestOptions = {},
  ): Promise<T> {
    const rateLimiter = this.getRateLimiter(endpoint);
    await rateLimiter.acquire();

    const session = await this.sessionManager.getValidSession();
    const url = `${this.config.fastworkApiUrl}${endpoint}`;

    const response = await fetch(url, {
      method: options.method || "GET",
      headers: {
        "Content-Type": "application/json",
        "Authorization": `Bearer ${session.tokens.access_token}`,
        "Accept-Language": "id",
        "User-Agent": "FastworkMCP/1.0",
        ...options.headers,
      },
      body: options.body ? JSON.stringify(options.body) : undefined,
    });

    if (!response.ok) {
      const body = await response.json().catch(() => ({}));
      throw classifyApiError(response.status, body);
    }

    return response.json();
  }

  // Convenience methods
  async get<T>(endpoint: string): Promise<T> {
    return this.request<T>(endpoint, { method: "GET" });
  }

  async post<T>(endpoint: string, body: any): Promise<T> {
    return this.request<T>(endpoint, { method: "POST", body });
  }

  async patch<T>(endpoint: string, body: any): Promise<T> {
    return this.request<T>(endpoint, { method: "PATCH", body });
  }

  // Algolia search
  async searchAlgolia(params: {
    indexName: string;
    query: string;
    filters?: string;
    page?: number;
    hitsPerPage?: number;
  }) {
    // Algolia uses a different auth mechanism
    const url = `https://${this.config.algoliaAppId}.algolia.net/1/indexes/${params.indexName}/query`;
    const response = await fetch(url, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-Algolia-Application-Id": this.config.algoliaAppId,
        "X-Algolia-API-Key": this.config.algoliaApiKey,
      },
      body: JSON.stringify({
        query: params.query,
        filters: params.filters,
        page: params.page || 0,
        hitsPerPage: params.hitsPerPage || 20,
      }),
    });

    if (!response.ok) {
      throw new McpError(ErrorCode.InternalError, "Algolia search failed", true);
    }

    return response.json();
  }
}
```

### 12.5 Docker Compose

```yaml
# docker-compose.yml

version: "3.8"

services:
  fastwork-mcp:
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - "3456:3456"
    environment:
      - MCP_TRANSPORT=sse
      - MCP_PORT=3456
      - FASTWORK_MCP_MASTER_KEY=${FASTWORK_MCP_MASTER_KEY}
      - ALGOLIA_API_KEY=${ALGOLIA_API_KEY}
      - LOG_LEVEL=info
    volumes:
      - ./data:/app/data  # Persist encrypted session tokens
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:3456/sse"]
      interval: 30s
      timeout: 10s
      retries: 3
```

---

## 13. n8n Integration Pattern

### 13.1 n8n MCP Node Configuration

n8n can connect to MCP servers via the community "MCP Client" node or via the HTTP Request node pointed at the SSE endpoint.

**Option A: Using n8n MCP Client Node (if available)**

```
Node type: MCP Client
Configuration:
  - Server URL: http://localhost:3456/sse
  - Transport: SSE
  - Authentication: None (or API key if configured)
  - Tools: [Select which tools to expose as n8n actions]
```

**Option B: Using HTTP Request Node**

```
Node type: HTTP Request
Method: POST
URL: http://localhost:3456/messages?sessionId={sessionId}
Headers:
  Content-Type: application/json
Body (JSON-RPC):
  {
    "jsonrpc": "2.0",
    "id": 1,
    "method": "tools/call",
    "params": {
      "name": "search_services",
      "arguments": {
        "query": "AI Agent",
        "categorySlug": "ai-agent",
        "page": 1,
        "hitsPerPage": 10
      }
    }
  }
```

### 13.2 Pre-Built n8n Workflow: Auto-Bidder

A complete n8n workflow that polls Fastwork's job board for new AI-related jobs and auto-submits proposals:

```
[Schedule] --(every 4 hours)--> [MCP: search_jobs]
  --> [Code: Filter by relevance]
  --> [MCP: get_job_details]
  --> [HTTP: LLM API - Generate proposal using proposal-generator prompt]
  --> [MCP: submit_job_proposal]
  --> [Slack: Notify freelancer "Proposal submitted"]
```

Workflow export would be at `04-freelancer-ai-agent/n8n-workflows/job-fetch-pipeline.json` (see future work).

### 13.3 n8n Workflow: Order Monitor

```
[MCP: list_orders (role=seller, status=active)]
  --> [Loop over orders]
  --> [MCP: get_conversation]
  --> [AI: Classify if client message needs response]
  --> [If "needs response": MCP: send_message]
  --> [If "overdue": MCP: send_message with polite reminder]
```

---

## 14. Example Workflows

### 14.1 Automated Proposal Submission

```
Scenario:
  - Freelancer: AI developer with Fastwork profile "ai-agent-pro"
  - Job: "Butuh AI Chatbot untuk customer service WhatsApp"
  - Budget: Rp 3,000,000 - Rp 8,000,000

AI Agent Execution:

1. TOOL: search_jobs(query="AI Chatbot WhatsApp", budgetMin=3000000, budgetMax=8000000)
   RESULT: [jobId: "job-abc123", title: "AI Chatbot WhatsApp Integrasi", budget: 5000000]

2. RESOURCE: fastwork://jobboard/job/job-abc123
   RESULT: Full job details including requirements, company info, deadline

3. PROMPT: proposal-generator(jobId="job-abc123", userSkills="5 years AI/ML, 3 chatbots deployed, Fastwork 5-star rating")
   RESULT: AI-generated proposal in Bahasa Indonesia

4. TOOL: submit_job_proposal(
     jobId="job-abc123",
     coverLetter="<generated proposal>",
     bidAmount=4500000,
     estimatedDays=7
   )
   RESULT: { proposalId: "prop-xyz", status: "submitted" }

5. TOOL: send_message(
     orderId="job-abc123",
     messageText="Halo! Saya sudah submit proposal untuk project AI Chatbot Anda. Saya punya pengalaman dengan integrasi WhatsApp Business API dan bisa mulai minggu ini. Silakan review proposal saya. Terima kasih!"
   )
```

### 14.2 Escrow Dispute Assistance

```
Scenario:
  - A client requests unreasonable revisions after delivery
  - Freelancer needs to negotiate professionally

1. RESOURCE: fastwork://orders/order-456
   RESULT: { status: "revision_requested", revisionNotes: "I want a completely different design style" }

2. RESOURCE: fastwork://chat/conv-789?limit=20
   RESULT: Full conversation context showing scope was agreed upon

3. TOOL: send_message(
     orderId="order-456",
     messageText="Hai [Client Name], saya paham Anda ingin perubahan gaya desain. Sesuai kesepakatan awal di chat, project ini sudah mencakup 3x revisi dengan ruang lingkup yang sudah disepakati. Perubahan gaya ini masuk ke ruang lingkup baru. Saya bisa membantu dengan biaya tambahan Rp 200,000 untuk desain ulang. Atau jika ada bagian spesifik yang kurang sesuai, saya siap memperbaikinya dalam revisi yang tersisa. Terima kasih!"
   )

4. TOOL: list_conversations() -- Verify client response
```

### 14.3 Cross-Platform Freelancer Dashboard

When combined with other MCP servers (WhatsApp, GoPay, Tokopedia), this creates a unified dashboard:

```
MCP Workflow:

1. fastwork-mcp: list_orders(role=seller, status=active)     -> Active projects
2. fastwork-mcp: get_wallet_balance()                         -> Pending payments
3. whatsapp-mcp: get_unread_messages()                        -> Client inquiries
4. gopay-mcp: get_transaction_history()                       -> Received payments
5. Combine into daily briefing for the freelancer
```

---

## 15. Testing and Deployment

### 15.1 Local Development

```bash
# Install dependencies
npm install

# Build TypeScript
npm run build

# Create .env file with your master key
echo "FASTWORK_MCP_MASTER_KEY=changeme-local-dev-key-123456" > .env
echo "ALGOLIA_API_KEY=" >> .env  # Optional, read-only search without it

# Run with stdio transport (for Claude Desktop)
npm start

# Or with SSE transport (for n8n integration)
MCP_TRANSPORT=sse MCP_PORT=3456 npm start
```

### 15.2 Testing with MCP Inspector

```bash
npx @modelcontextprotocol/inspector node dist/index.js

# Then visit http://localhost:5173 to test tools interactively
```

### 15.3 Integration Test Suite

```typescript
// tests/tools.test.ts

import { describe, it, expect, beforeAll } from "vitest";
import { FastworkMCPTestHarness } from "./test-harness";

describe("Fastwork MCP Server", () => {
  let harness: FastworkMCPTestHarness;

  beforeAll(async () => {
    harness = new FastworkMCPTestHarness();
    await harness.start();
  });

  describe("search_services", () => {
    it("should return results for 'AI Agent' query", async () => {
      const result = await harness.callTool("search_services", {
        query: "AI Agent",
        categorySlug: "ai-agent",
        hitsPerPage: 5,
      });

      const parsed = JSON.parse(result.content[0].text);
      expect(parsed.totalHits).toBeGreaterThan(0);
      expect(parsed.hits[0]).toHaveProperty("title");
      expect(parsed.hits[0]).toHaveProperty("price");
    });

    it("should handle empty queries gracefully", async () => {
      const result = await harness.callTool("search_services", {
        query: "zzzz_not_a_real_search_2024",
      });

      const parsed = JSON.parse(result.content[0].text);
      expect(parsed.totalHits).toBe(0);
      expect(parsed.hits).toHaveLength(0);
    });
  });

  describe("authentication", () => {
    it("should reject unauthenticated order requests", async () => {
      await expect(
        harness.callTool("get_order_status", { orderId: "test-123" }),
      ).rejects.toThrow("No active session");
    });
  });
});
```

### 15.4 Production Deployment

```bash
# Build Docker image
docker build -t fastwork-mcp-server:latest .

# Run with Docker Compose
docker-compose up -d

# Verify health
curl http://localhost:3456/sse

# Check logs
docker-compose logs -f
```

### 15.5 Claude Desktop Integration

Add to your Claude Desktop configuration (`claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "fastwork": {
      "command": "node",
      "args": ["/path/to/fastwork-mcp-server/dist/index.js"],
      "env": {
        "FASTWORK_MCP_MASTER_KEY": "your-master-key",
        "ALGOLIA_API_KEY": "your-algolia-key",
        "LOG_LEVEL": "info"
      }
    }
  }
}
```

---

## 16. Future Extensions

### 16.1 Immediate Gaps (Next Tick)

- **04-freelancer-ai-agent/n8n-workflows/job-fetch-pipeline.json**: Export the complete n8n workflow for automated job fetching (2-3 hours of work).
- **04-freelancer-ai-agent/prompts/proposal-template-bank.md**: A repository of proven proposal templates for different service categories, with conversion rate data.
- **04-freelancer-ai-agent/mcp-servers/sribu-mcp-spec.md**: MCP server for Sribu.com (another major Indonesian freelance platform), giving cross-platform automation.

### 16.2 Medium-Term Additions

- **WebSocket Event Listener**: Connect to `wss://chat-api.fastwork.id/socket` for real-time message events. This would allow the MCP server to push notifications when new messages arrive, rather than polling.
- **Multi-Account Support**: Manage multiple freelancer profiles from a single MCP server instance. Useful for agencies operating multiple Fastwork accounts.
- **Proposal A/B Testing**: Track which proposal templates convert at the highest rate, using order acceptance as the success metric.
- **Sentiment Analysis Integration**: Score client messages for satisfaction level. Flag accounts where the client sentiment is declining for proactive intervention.

### 16.3 Cross-Folder Integration

This MCP server connects to three other vault folders:

1. **03-id-business-trends/demand-mining/freelancer-gagal-dibayar-klien-wanprestasi.md**: The payment pain point that this MCP server directly addresses through automated escrow management and professional communication tools.
2. **01-crawler-scrapper/cookies-tokens/storage-safety.md**: The encryption patterns in the SecureTokenStore follow the same Fernet-compatible principles documented in the cookie storage safety guide.
3. **07-gaps-and-opportunities/opportunities/whatsapp-financial-inclusion-ecosystem.md**: The cross-platform dashboard vision (Section 14.3) directly connects to the WhatsApp financial inclusion thesis, creating a bridge between the freelance AI agent infrastructure and the broader financial inclusion opportunity.

---

## References

1. Fastwork.id homepage and runtime configuration, retrieved 2026-06-19 from https://fastwork.id
2. Model Context Protocol official documentation, Architecture overview, https://modelcontextprotocol.io/docs/learn/architecture (accessed 2026-06-19)
3. MCP Specification GitHub repository, https://github.com/modelcontextprotocol/specification (accessed 2026-06-19)
4. Fastwork blog (technical category information), https://blog.fastwork.id (retrieved 2026-06-19)
5. Fastwork ID job board, https://jobboard.fastwork.id (retrieved 2026-06-19)
6. PayPal survey on SE Asia freelancer non-payment, cited via Kompas.com, 2026-06-18
7. Fastwork fee structure and terms of service, https://fastwork.id (footer links, retrieved 2026-06-19)
8. Indonesien Freelancer Market: Sribu, Projects.co.id competitor fee analysis, various sources 2025-2026
9. Token bucket rate limiting algorithm, https://en.wikipedia.org/wiki/Token_bucket (general reference)
10. Algolia search API documentation, https://www.algolia.com/doc/ (general reference for search integration pattern)
