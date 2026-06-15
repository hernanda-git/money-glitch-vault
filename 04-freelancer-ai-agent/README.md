# 🤖 04 — Freelancer AI Agent

An AI agent (or fleet) that follows a pipeline from job-source → proposal → delivery → payout. Built on MCP, n8n, or any orchestrator you can wire.

## Pipeline (canonical)

```
Job board (Fastwork/Upwork/Fiverr/Glints)
  → filter (budget, skill, recency)
  → score (win-probability heuristic)
  → draft proposal (RAG over your past wins + portfolio)
  → human-approve (Telegram ping)
  → submit
  → on-accept: spawn delivery agent
  → deliver + invoice
  → follow-up review request
```

## Sub-folders

- `mcp-servers/` — custom MCP servers for each job platform
- `n8n-workflows/` — exported JSON workflows
- `prompts/` — proposal templates, scoring prompts, delivery prompts
- `proposals-history/` — what was sent, win/loss, edits made
- `portfolio-snippets/` — your best work, indexed for RAG
- `pricing-models/` — how to price against ID/SEA/US/UK markets
- `agents/` — per-task agent definitions (proposal-writer, code-builder, etc.)

## Tech stack to evaluate

- **Orchestrator:** n8n (self-host), Make, LangGraph, CrewAI
- **LLM:** Claude / GPT-4o / OSS via Ollama for cost
- **Browser automation:** Playwright (with your real cookies)
- **Storage:** Obsidian vault + Qdrant for RAG
- **Notifications:** Telegram bot

## First milestone

- [ ] Fastwork scraper that watches 5 keywords, pings Telegram on new high-budget jobs
- [ ] Proposal drafter that produces 3 variants in your voice
- [ ] Win-rate dashboard (manual: mark win/loss, agent learns)
