#!/usr/bin/env python3
"""
Demo 2: Competitive Intelligence
Shows deep competitor analysis with website scraping
"""

import asyncio
import logging
from base_agent import BaseCompetitiveIntelligenceAgent

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class CompetitorAnalysisAgent(BaseCompetitiveIntelligenceAgent):
    """Agent specialized for competitor intelligence"""

    def _get_system_prompt(self) -> str:
        """Agent behavior focused on competitor analysis"""
        return """You are an expert competitive intelligence analyst with access to powerful web data tools through MCP.

## Your Mission
Conduct deep competitive analysis to understand competitor strategies, strengths, and vulnerabilities.

## Available MCP Tools
You have access to these Bright Data MCP tools:
- search_engine: Scrape search results from Google, Bing or Yandex. Returns SERP results in JSON or Markdown
- scrape_as_markdown: Scrape a single webpage URL with advanced options for content extraction
- search_engine_batch: Run multiple search queries simultaneously
- scrape_batch: Scrape multiple webpages URLs with advanced options for content extraction

## Autonomous Competitive Intelligence Workflow

When asked to analyze a competitor, you should autonomously:

1. **Competitor Discovery**
   - Use search_engine to find the competitor's main website and online presence
   - Search for recent news, press releases, and market mentions
   - Identify key product pages and pricing information

2. **Deep Website Analysis**
   - Use scrape_as_markdown to extract detailed content from competitor websites
   - Analyze product catalogs, pricing strategies, and value propositions
   - Extract company information, team details, and strategic messaging

3. **Competitive Positioning**
   - Use search_engine to understand how they position against other competitors
   - Research customer reviews and market perception
   - Identify their unique selling points and market strategy

4. **Strategic Intelligence**
   - Synthesize findings into actionable competitive insights
   - Identify competitor strengths and potential vulnerabilities
   - Recommend strategic responses and market opportunities

## Key Behaviors
- Be thorough in data gathering - use multiple tools for comprehensive analysis
- Focus on extracting specific details about products, pricing, and strategy
- Look for competitive advantages and weaknesses
- Provide actionable intelligence for strategic decision-making

Remember: You have full autonomy to decide which tools to use for thorough competitive analysis."""


async def main():
    """Demo competitor analysis with autonomous tool usage"""

    print("🚀 Demo 2: Autonomous Competitor Analysis with Strands + Bright Data MCP")
    print("=" * 75)

    try:
        # Initialize agent
        agent = CompetitorAnalysisAgent()

        # Connect to MCP tools
        tools = await agent.connect_mcp_tools()

        print(f"\n✅ Connected to MCP with {len(tools)} tools available")
        print("\n🎯 Competitive Intelligence Demo")
        print("-" * 40)
        print("Giving agent the goal: 'Deep analysis of Tesla's strategy'")
        print("Agent will decide how to gather competitive intelligence...\n")

        # Let agent autonomously analyze competitor
        prompt = """
        Perform a comprehensive competitive intelligence analysis of Tesla (tesla.com).

        I need deep insights on:
        - Their current product lineup and pricing strategy
        - Market positioning and key value propositions
        - Recent strategic announcements or developments
        - Competitive advantages and potential vulnerabilities
        - How they differentiate from other automotive companies

        Use whatever tools you need to get comprehensive competitive intelligence.
        """

        result = await agent.run_analysis(prompt)

        print("\nAgent's Competitive Analysis:")
        print("=" * 50)
        result_content = agent.extract_result_content(result)
        print(result_content[:2000] + "..." if len(str(result_content)) > 2000 else result_content)

        print("\n✅ Competitive analysis completed successfully!")
        print("\nKey Features Demonstrated:")
        print("- Autonomous competitive intelligence gathering")
        print("- Deep website content extraction")
        print("- Strategic analysis and vulnerability assessment")
        print("- Actionable competitive insights")

    except Exception as e:
        logger.error(f"Demo failed: {e}")
        print(f"\n❌ Error: {e}")
        print("\nEnsure:")
        print("1. ANTHROPIC_API_KEY is set in .env")
        print("2. BRIGHT_DATA_API_KEY is set in .env")
        print("3. Bright Data MCP is configured in Claude Desktop")


if __name__ == "__main__":
    asyncio.run(main())