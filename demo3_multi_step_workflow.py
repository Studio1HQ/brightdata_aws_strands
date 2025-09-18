#!/usr/bin/env python3
"""
Demo 3: Multi-Step Autonomous Workflow
Shows coordinated analysis across multiple competitors and market segments
"""

import asyncio
import logging
from typing import List
from base_agent import BaseCompetitiveIntelligenceAgent

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class WorkflowAgent(BaseCompetitiveIntelligenceAgent):
    """Agent specialized for multi-step competitive workflows"""

    def _get_system_prompt(self) -> str:
        """Agent behavior focused on coordinated multi-step analysis"""
        return """You are an expert strategic analyst with access to powerful web data tools through MCP.

## Your Mission
Orchestrate comprehensive multi-step competitive intelligence workflows to provide strategic market insights.

## Available MCP Tools
You have access to these Bright Data MCP tools:
- search_engine: Scrape search results from Google, Bing or Yandex. Returns SERP results in JSON or Markdown
- scrape_as_markdown: Scrape a single webpage URL with advanced options for content extraction
- search_engine_batch: Run multiple search queries simultaneously
- scrape_batch: Scrape multiple webpages URLs with advanced options for content extraction

## Autonomous Multi-Step Workflow

When given a complex analysis task, you should autonomously coordinate multiple phases:

1. **Market Discovery Phase**
   - Use search_engine to identify market landscape and key players
   - Research market size, trends, and growth opportunities
   - Map the competitive ecosystem

2. **Competitive Deep Dive Phase**
   - Use scrape_as_markdown to analyze each major competitor's website
   - Extract product details, pricing, and strategic positioning
   - Use search_engine_batch for efficient multi-competitor research

3. **Strategic Synthesis Phase**
   - Combine insights from market and competitor analysis
   - Identify market gaps and competitive opportunities
   - Generate specific strategic recommendations

## Advanced Behaviors
- Coordinate tool usage across multiple analysis phases
- Build comprehensive intelligence by layering insights
- Adapt tool selection based on information gathered in previous phases
- Provide executive-level strategic recommendations

Remember: You can autonomously decide how to sequence and coordinate tool usage for maximum insight generation."""

    async def run_multi_step_analysis(self, market: str, competitors: List[str]):
        """Execute multi-step competitive intelligence workflow"""

        logger.info(f"🔄 Starting multi-step workflow for {market} market")

        results = {}

        # Step 1: Market Landscape Analysis
        print(f"\n📊 Phase 1: Market Discovery - {market}")
        print("-" * 50)

        market_prompt = f"""
        Phase 1: Conduct comprehensive market discovery for the {market} market.

        Research and analyze:
        - Market size, growth rate, and key trends
        - Major players and their market positions
        - Emerging technologies and innovations
        - Customer segments and use cases

        Use search tools efficiently to gather comprehensive market intelligence.
        """

        market_result = await self.run_analysis(market_prompt)
        results['market_analysis'] = market_result

        print("✅ Market discovery completed")

        # Step 2: Multi-Competitor Analysis
        print(f"\n🎯 Phase 2: Competitive Deep Dive")
        print("-" * 50)

        competitor_prompt = f"""
        Phase 2: Perform deep competitive analysis of these key players: {', '.join(competitors)}

        For each competitor, analyze:
        - Product portfolio and pricing strategy
        - Market positioning and value propositions
        - Recent strategic moves and announcements
        - Competitive strengths and potential vulnerabilities

        Use both search and website scraping tools to gather detailed intelligence on each competitor.
        Be efficient by using batch tools when appropriate.
        """

        competitor_result = await self.run_analysis(competitor_prompt)
        results['competitor_analysis'] = competitor_result

        print("✅ Competitive analysis completed")

        # Step 3: Strategic Synthesis
        print(f"\n🧠 Phase 3: Strategic Synthesis")
        print("-" * 50)

        synthesis_prompt = f"""
        Phase 3: Synthesize all gathered intelligence into strategic recommendations.

        Based on the market analysis and competitive intelligence gathered, provide:
        - Overall market assessment and key trends
        - Competitive positioning map and market dynamics
        - Identification of market gaps and opportunities
        - Strategic recommendations for market entry or competitive response
        - Specific tactical actions and next steps

        Focus on actionable insights that can drive strategic decision-making.
        """

        synthesis_result = await self.run_analysis(synthesis_prompt)
        results['strategic_synthesis'] = synthesis_result

        print("✅ Strategic synthesis completed")

        return results


async def main():
    """Demo multi-step workflow with autonomous coordination"""

    print("🚀 Demo 3: Multi-Step Autonomous Workflow with Strands + Bright Data MCP")
    print("=" * 80)

    try:
        # Initialize agent
        agent = WorkflowAgent()

        # Connect to MCP tools
        tools = await agent.connect_mcp_tools()

        print(f"\n✅ Connected to MCP with {len(tools)} tools available")
        print("\n🔄 Multi-Step Competitive Intelligence Workflow")
        print("-" * 60)
        print("Executing coordinated analysis of electric vehicle market")
        print("Agent will autonomously orchestrate multiple analysis phases...\n")

        # Run multi-step workflow
        market = "electric vehicle"
        competitors = ["tesla.com", "rivian.com", "lucidmotors.com"]

        workflow_results = await agent.run_multi_step_analysis(market, competitors)

        print(f"\n📋 Workflow Summary")
        print("=" * 50)
        print(f"✅ Market Analysis: Completed")
        print(f"✅ Competitor Analysis: Completed for {len(competitors)} competitors")
        print(f"✅ Strategic Synthesis: Completed")

        print(f"\n📈 Final Strategic Recommendations:")
        print("-" * 50)
        synthesis_content = agent.extract_result_content(workflow_results['strategic_synthesis'])
        print(synthesis_content[:1500] + "..." if len(str(synthesis_content)) > 1500 else synthesis_content)

        print("\n✅ Multi-step workflow completed successfully!")
        print("\nKey Features Demonstrated:")
        print("- Coordinated multi-phase analysis")
        print("- Autonomous tool orchestration across workflow steps")
        print("- Strategic synthesis of complex market intelligence")
        print("- Executive-level strategic recommendations")

    except Exception as e:
        logger.error(f"Demo failed: {e}")
        print(f"\n❌ Error: {e}")
        print("\nEnsure:")
        print("1. ANTHROPIC_API_KEY is set in .env")
        print("2. BRIGHT_DATA_API_KEY is set in .env")
        print("3. Bright Data MCP is configured in Claude Desktop")


if __name__ == "__main__":
    asyncio.run(main())