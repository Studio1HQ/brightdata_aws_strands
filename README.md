<div align="center">

<img src="https://raw.githubusercontent.com/Studio1HQ/Studio1HQ/main/assets/banners/brightdata_aws_strands.webp" alt="Strands Agents with Bright Data MCP: Autonomous competitive intelligence agents on Strands and Bright Data MCP" width="100%" />

<br />
<br />

# Strands Agents with Bright Data MCP

### Autonomous competitive intelligence agents on Strands and Bright Data MCP

Three Python demos where a Strands agent backed by Claude picks Bright Data MCP tools on its own to run market analysis, competitor analysis and a multi-step research workflow.

<br />

[![Built by Studio1](https://img.shields.io/badge/Built_by_Studio1-f97316?style=for-the-badge&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNjAgMTYwIiBmaWxsPSJub25lIj48cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTAgMzVDMCAxNi42ODA3IDE0LjA3NDQgMS42NDg0NCAzMiAwLjEyNjk1M1YxNDFINTEuMDUyM0M1Mi40MzA4IDEzNy4zNDQgNTQuNzQ0NiAxMzMuNjg5IDU3Ljk5MzggMTMwLjAzM0M2MS4xNDQ2IDEyNi41MDggNjQuNjg5MiAxMjMuNDQgNjguNjI3NyAxMjAuODI5QzcyLjU2NjIgMTE4LjM0OSA3Ni4zNTY5IDExNi43ODIgODAgMTE2LjEyOVY4Ni43NTQ0Qzc1LjQ3MDggODcuOTI5MiA3MS4zODQ2IDg5LjY5MTkgNjcuNzQxNSA5Mi4wNDE1QzY0IDk0LjUyMjUgNjAuNzUwOCA5Ny40NiA1Ny45OTM4IDEwMC44NTRDNTYuNTM0NSAxMDIuNzIgNTUuMjU0NSAxMDQuNjU5IDU0LjE1MzkgMTA2LjY3MVYwSDEyNUMxNDQuMzMgMCAxNjAgMTUuNjY5OSAxNjAgMzVWMTI1QzE2MCAxNDQuMzMgMTQ0LjMzIDE2MCAxMjUgMTYwSDEyNFYxOEgxMDQuOTQ4QzEwMy41NjkgMjEuNjgxNiAxMDEuMjU1IDI1LjM2MjggOTguMDA2MiAyOS4wNDQ0Qzk0Ljg1NTQgMzIuNTk0MiA5MS4zMTA4IDM1LjY4NDEgODcuMzcyMyAzOC4zMTRDODMuNDMzOCA0MC44MTIgNzkuNjQzMSA0Mi4zODk2IDc2IDQzLjA0NzRWNzIuNjMwNEM4MC41MjkyIDcxLjQ0NzMgODQuNjE1NCA2OS42NzI0IDg4LjI1ODUgNjcuMzA1N0M5MiA2NC44MDc2IDk1LjI0OTIgNjEuODQ5MSA5OC4wMDYyIDU4LjQzMDdDOTkuNDY1NSA1Ni41NTEzIDEwMC43NDUgNTQuNTk4NiAxMDEuODQ2IDUyLjU3MjNWMTYwSDM1QzE1LjY3IDE2MCAwIDE0NC4zMyAwIDEyNVYzNVoiIGZpbGw9IiNmZmZmZmYiLz48L3N2Zz4K)](https://studio1hq.com)
[![Built with Bright Data](https://img.shields.io/badge/Built_with_Bright_Data-141414?style=for-the-badge)](https://brightdata.com)

[Bright Data docs](https://docs.brightdata.com) &nbsp;·&nbsp; [Bright Data](https://brightdata.com) &nbsp;·&nbsp; [More examples](https://github.com/Studio1HQ) &nbsp;·&nbsp; [studio1hq.com](https://studio1hq.com)

</div>

<br />

## Overview

A set of three Python demos where a [Strands](https://strandsagents.com) agent decides on its own which Bright Data tools to call. The agent connects to the hosted Bright Data MCP server through `mcp-remote` and uses Claude (via the Anthropic API) as its model. Prompts are plain language; there are no hardcoded tool sequences.

The Bright Data product here is the Bright Data MCP server. The agent gets four tools: `search_engine`, `scrape_as_markdown`, `search_engine_batch` and `scrape_batch`.

## Features

- **Autonomous tool choice**: The agent picks search or scrape tools from the prompt.
- **Market analysis**: Demo 1 maps players, trends and opportunities with search and scraping.
- **Competitor analysis**: Demo 2 scrapes competitor sites for pricing, products and positioning.
- **Multi-step workflow**: Demo 3 chains market discovery and competitor analysis into one recommendation.
- **Shared base class**: `base_agent.py` holds the MCP connection and agent setup for all demos.
- **Batch tools**: Uses batch search and batch scrape for several queries or URLs at once.

## Tech stack

| Layer | Tool |
| --- | --- |
| Agent framework | [Strands Agents](https://strandsagents.com) (`strands-agents`) |
| Web data | [Bright Data MCP](https://brightdata.com) (hosted, via `mcp-remote`) |
| LLM | [Anthropic](https://www.anthropic.com) Claude |
| Language | Python 3.8+ |

## Getting started

### Prerequisites

- Python 3.8+
- Node.js (for `npx mcp-remote`)
- A [Bright Data](https://brightdata.com) account and API token
- An [Anthropic](https://console.anthropic.com) API key

### Installation

```bash
git clone https://github.com/Studio1HQ/brightdata_aws_strands.git
cd brightdata_aws_strands
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
```

### Environment variables

| Variable | Description |
| --- | --- |
| `BRIGHT_DATA_API_KEY` | Bright Data API token, from the Bright Data dashboard. `base_agent.py` reads this name. |
| `ANTHROPIC_API_KEY` | Anthropic API key. Required. |
| `ANTHROPIC_MODEL` | Claude model ID. Default `claude-3-opus-20240229`. |

Note: `.env.example` lists the Bright Data token as `BRIGHT_DATA_API_TOKEN`, but the code reads `BRIGHT_DATA_API_KEY`. Set `BRIGHT_DATA_API_KEY`.

### Run

```bash
python demo1_market_analysis.py
python demo2_competitor_analysis.py
python demo3_multi_step_workflow.py
```

## How it works

| File | Role |
| --- | --- |
| `base_agent.py` | Shared base class. Creates the Anthropic model and an MCP client that runs `npx mcp-remote https://mcp.brightdata.com/mcp?token=...`. |
| `demo1_market_analysis.py` | Market research agent: market size, landscape, opportunities. |
| `demo2_competitor_analysis.py` | Competitor agent: scrapes sites for pricing, product details and strategy. |
| `demo3_multi_step_workflow.py` | Coordinates discovery and competitor phases, then synthesizes recommendations. |

On start the agent connects to MCP, discovers the four Bright Data tools, then chooses and sequences them to answer the prompt.

Troubleshooting:

- **MCP connection**: Check `BRIGHT_DATA_API_KEY` and that `npx mcp-remote` runs.
- **Anthropic errors**: Check the key, credits and rate limits.
- **Import errors**: Confirm the install completed on Python 3.8+.

## Resources

- [Bright Data docs](https://docs.brightdata.com): MCP server, SERP and Web Unlocker docs.
- [Bright Data](https://brightdata.com): Account and API token.
- [Strands Agents](https://strandsagents.com): Agent framework documentation.

<br />

---

<div align="center">

<a href="https://studio1hq.com">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Studio1HQ/website/main/brand/studio1-logo-on-dark.svg" />
    <img src="https://raw.githubusercontent.com/Studio1HQ/website/main/brand/studio1-logo-on-light.svg" alt="Studio1" width="160" />
  </picture>
</a>

Built by **[Studio1](https://studio1hq.com)**, the technical content and DevRel partner for devtool teams. Made with [Bright Data](https://brightdata.com).<br />
Browse more open-source examples at [github.com/Studio1HQ](https://github.com/Studio1HQ).

[![Website](https://img.shields.io/badge/studio1hq.com-0b0807?style=for-the-badge&logo=googlechrome&logoColor=white)](https://studio1hq.com)
[![Book a call](https://img.shields.io/badge/Book_a_strategy_call-f97316?style=for-the-badge&logo=googlecalendar&logoColor=white)](https://cal.com/studio1/collab)
[![X](https://img.shields.io/badge/%40Studio1HQ-141414?style=for-the-badge&logo=x&logoColor=white)](https://x.com/Studio1HQ)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0a66c2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/company/studio1hq/)

<sub><a href="https://studio1hq.com">studio1hq.com</a> · Technical content, docs, video and DevRel for devtools</sub>

</div>
