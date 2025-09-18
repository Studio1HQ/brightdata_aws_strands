#!/usr/bin/env python3
"""
Demo 1: Basic Market Analysis
Shows autonomous tool selection for market research
"""

import asyncio
import logging
from base_agent import BaseCompetitiveIntelligenceAgent

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class MarketAnalysisAgent(BaseCompetitiveIntelligenceAgent):
    """Agent specialized for market analysis"""

    def _get_system_prompt(self) -> str:
        """Agent behavior focused on market analysis"""
        return """You are an expert market research analyst with access to powerful web data tools through MCP.

## Your Mission
Conduct comprehensive market analysis to identify players, trends, and opportunities.

## Available MCP Tools
You have access to these Bright Data MCP tools:
- search_engine: Scrape search results from Google, Bing or Yandex. Returns SERP results in JSON or Markdown
- scrape_as_markdown: Scrape a single webpage URL with advanced options for content extraction
- search_engine_batch: Run multiple search queries simultaneously
- scrape_batch: Scrape multiple webpages URLs with advanced options for content extraction

## Autonomous Market Analysis Workflow

When asked to analyze a market, you should autonomously:

1. **Market Discovery**
   - Use search_engine to find the top players in the market
   - Search for market size, growth rates, and recent trends
   - Identify key industry reports and news

2. **Competitive Landscape**
   - Use search_engine_batch to research multiple competitors simultaneously
   - Use scrape_as_markdown to extract detailed information from competitor websites
   - Analyze product offerings, pricing strategies, and positioning

3. **Market Intelligence**
   - Synthesize findings into a comprehensive market overview
   - Identify market gaps and growth opportunities
   - Provide specific strategic recommendations

## Key Behaviors
- Be proactive in tool selection - decide which tools to use based on the analysis goal
- Use multiple tools to gather comprehensive data
- Focus on quantitative insights and specific market data
- Provide actionable business intelligence

Remember: You have full autonomy to use any combination of tools to deliver thorough market analysis."""


async def main():
    """Demo market analysis with autonomous tool usage"""

    print("🚀 Demo 1: Autonomous Market Analysis with Strands + Bright Data MCP")
    print("=" * 70)

    try:
        # Initialize agent
        agent = MarketAnalysisAgent()

        # Connect to MCP tools
        tools = await agent.connect_mcp_tools()

        print(f"\n✅ Connected to MCP with {len(tools)} tools available")
        print("\n📊 Market Analysis Demo")
        print("-" * 40)
        print("Giving agent the goal: 'Analyze the smart home devices market'")
        print("Watch as it autonomously decides which tools to use...\n")

        # Let agent autonomously analyze market
        prompt = """
        Conduct a comprehensive market analysis of the smart home devices market.

        I need to understand:
        - Who are the major players and their market share?
        - What are the key product categories and growth trends?
        - What are the pricing strategies across different segments?
        - Where are the biggest opportunities for new entrants?

        Be thorough and use all available tools to gather comprehensive market intelligence.
        """

        result = await agent.run_analysis(prompt)

        print("\nAgent's Market Analysis:")
        print("=" * 50)
        result_content = agent.extract_result_content(result)
        print(result_content[:2000] + "..." if len(str(result_content)) > 2000 else result_content)

        print("\n✅ Market analysis completed successfully!")
        print("\nKey Features Demonstrated:")
        print("- Autonomous tool selection based on analysis goals")
        print("- Real web data extraction through Bright Data MCP")
        print("- Comprehensive market intelligence gathering")
        print("- Strategic insights and recommendations")

    except Exception as e:
        logger.error(f"Demo failed: {e}")
        print(f"\n❌ Error: {e}")
        print("\nEnsure:")
        print("1. ANTHROPIC_API_KEY is set in .env")
        print("2. BRIGHT_DATA_API_KEY is set in .env")
        print("3. Bright Data MCP is configured in Claude Desktop")


if __name__ == "__main__":
    asyncio.run(main())