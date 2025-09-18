# Strands + Bright Data MCP Demo Suite

This demo suite showcases autonomous AI agents using Strands framework with Bright Data MCP tools for competitive intelligence and market analysis.

## Overview

The demo demonstrates how Strands agents can autonomously decide which web data tools to use based on natural language prompts, showcasing true agentic behavior with real Bright Data MCP integration.

## Prerequisites

1. **Environment Setup**:
   - Python 3.8+
   - Virtual environment with required packages
   - `.env` file with API keys

2. **Required API Keys**:
   ```bash
   ANTHROPIC_API_KEY=your_anthropic_key_here
   BRIGHT_DATA_API_KEY=your_bright_data_token_here
   ANTHROPIC_MODEL=claude-3-opus-20240229
   ```

3. **Claude Desktop MCP Configuration** (if using hosted MCP):
   - Bright Data MCP configured in Claude Desktop
   - Uses `mcp-remote` for hosted MCP connection

## Installation

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install requirements
pip install -r requirements.txt

# Set up environment
cp .env.example .env
# Edit .env with your API keys
```

## Demo Suite

### Demo 1: Market Analysis (`demo1_market_analysis.py`)

**Purpose**: Demonstrates autonomous market research and analysis

**What it shows**:
- Agent autonomously selects tools for market discovery
- Uses search_engine for market research
- Scrapes competitor websites for detailed analysis
- Provides comprehensive market intelligence

**Usage**:
```bash
python demo1_market_analysis.py
```

**Key Features**:
- Market size and growth analysis
- Competitive landscape mapping
- Strategic opportunity identification
- Quantitative market insights

### Demo 2: Competitive Intelligence (`demo2_competitor_analysis.py`)

**Purpose**: Shows deep competitor analysis with website scraping

**What it shows**:
- Agent autonomously gathers competitor intelligence
- Uses scrape_as_markdown for detailed website analysis
- Extracts pricing, product details, and strategy
- Identifies competitive advantages and vulnerabilities

**Usage**:
```bash
python demo2_competitor_analysis.py
```

**Key Features**:
- Deep competitor website analysis
- Product and pricing strategy extraction
- Competitive positioning assessment
- Strategic vulnerability identification

### Demo 3: Multi-Step Workflow (`demo3_multi_step_workflow.py`)

**Purpose**: Demonstrates coordinated multi-phase analysis

**What it shows**:
- Agent orchestrates complex multi-step workflows
- Coordinates market discovery and competitor analysis
- Synthesizes insights across multiple analysis phases
- Provides executive-level strategic recommendations

**Usage**:
```bash
python demo3_multi_step_workflow.py
```

**Key Features**:
- Multi-phase workflow coordination
- Strategic synthesis of complex intelligence
- Executive-level recommendations
- Comprehensive competitive landscape analysis

## Available MCP Tools

The demos use these Bright Data MCP tools:

1. **search_engine**: Scrape search results from Google, Bing, or Yandex
2. **scrape_as_markdown**: Scrape single webpage with advanced content extraction
3. **search_engine_batch**: Run multiple search queries simultaneously
4. **scrape_batch**: Scrape multiple webpages with batch processing

## Architecture

- **base_agent.py**: Shared base class with MCP connection logic
- **demo1_market_analysis.py**: Market research focused agent
- **demo2_competitor_analysis.py**: Competitive intelligence focused agent
- **demo3_multi_step_workflow.py**: Multi-phase workflow coordination

## Key Technical Features

✅ **Autonomous Tool Selection**: Agents decide which tools to use based on prompts
✅ **Real Web Data**: Uses actual Bright Data MCP for web scraping
✅ **Agentic Behavior**: No hardcoded tool sequences - true AI decision making
✅ **Production Ready**: Real API integration with error handling
✅ **Modular Design**: Separate demos for different use cases

## Troubleshooting

**MCP Connection Issues**:
- Ensure Bright Data MCP is configured in Claude Desktop
- Check that BRIGHT_DATA_API_KEY is set correctly
- Verify `mcp-remote` is available via npx

**Anthropic API Issues**:
- Ensure ANTHROPIC_API_KEY is valid and has sufficient credits
- Check API key permissions and rate limits

**Import Issues**:
- Ensure all required packages are installed
- Check Python version compatibility (3.8+)

## Example Output

When running successfully, you'll see:
- MCP connection establishment
- Tool discovery (4 Bright Data tools)
- Agent autonomous tool selection
- Real-time web data extraction
- Comprehensive analysis results

The agent will autonomously decide to use multiple tools in sequence, demonstrating true agentic workflow behavior.