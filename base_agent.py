#!/usr/bin/env python3
"""
Base Agent for Strands + Bright Data MCP Integration
Common functionality shared across demos
"""

import asyncio
import os
import logging
from typing import Dict, Any, List
from dotenv import load_dotenv

# Strands imports
from strands import Agent
from strands.models.anthropic import AnthropicModel
from strands.tools.mcp.mcp_client import MCPClient

# MCP client imports
from mcp.client.stdio import stdio_client, StdioServerParameters

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class BaseCompetitiveIntelligenceAgent:
    """Base agent class with shared MCP setup functionality"""

    def __init__(self):
        # Initialize Anthropic model
        api_key = os.getenv("ANTHROPIC_API_KEY")
        if not api_key:
            raise ValueError("ANTHROPIC_API_KEY must be set")

        self.model = AnthropicModel(
            model_id=os.getenv("ANTHROPIC_MODEL", "claude-3-opus-20240229"),
            max_tokens=4096,
            params={
                "temperature": 0.3
            }
        )

        # Set the API key as environment variable for Anthropic
        os.environ["ANTHROPIC_API_KEY"] = api_key

        # MCP client for Bright Data (will be initialized in connect_mcp_tools)
        self.mcp_client = None
        self.agent = None

        logger.info("✅ Strands agent initialized with Anthropic Claude")

    def _get_system_prompt(self) -> str:
        """Override this in subclasses for specific demo behavior"""
        return """You are an expert competitive intelligence analyst with access to powerful web data tools through MCP.

## Available MCP Tools
You have access to these Bright Data MCP tools:
- search_engine: Scrape search results from Google, Bing or Yandex. Returns SERP results in JSON or Markdown
- scrape_as_markdown: Scrape a single webpage URL with advanced options for content extraction
- search_engine_batch: Run multiple search queries simultaneously
- scrape_batch: Scrape multiple webpages URLs with advanced options for content extraction

## Autonomous Workflow Guidelines
When asked to analyze a market or competitor, you should autonomously:

1. **Discovery Phase**
   - Use search_engine to identify key players in the market
   - Search for industry trends and recent news
   - Find competitor websites and online presence

2. **Deep Analysis Phase**
   - Use scrape_as_markdown on each major competitor's site
   - Extract product catalogs, pricing strategies, and unique features
   - Use search_engine_batch for efficiency when needed

3. **Synthesis Phase**
   - Combine all gathered data into actionable insights
   - Identify market gaps and opportunities
   - Generate specific strategic recommendations

## Important Behaviors
- Always use multiple tools to cross-verify information
- Be proactive in gathering comprehensive data
- Don't wait to be told which tools to use - decide based on the goal
- Provide quantitative insights with specific numbers
- Focus on actionable business strategies

Remember: You have autonomy to use any combination of tools to accomplish the analysis."""

    async def connect_mcp_tools(self):
        """Connect to Bright Data MCP via Claude Desktop"""

        logger.info("Connecting to Bright Data MCP via Claude Desktop...")

        # Create MCP client for Bright Data hosted remote MCP
        # This matches your Claude Desktop config for Bright Data MCP
        bright_data_token = os.getenv("BRIGHT_DATA_API_KEY")
        if not bright_data_token:
            raise ValueError("BRIGHT_DATA_API_KEY must be set in .env")

        server_params = StdioServerParameters(
            command="npx",
            args=["mcp-remote", f"https://mcp.brightdata.com/mcp?token={bright_data_token}"],
            env={}
        )

        # Create MCP client following Strands docs pattern
        self.mcp_client = MCPClient(lambda: stdio_client(server_params))

        # Use context manager for all MCP operations
        with self.mcp_client:
            # Get tools from MCP server
            tools = self.mcp_client.list_tools_sync()
            logger.info(f"📦 Discovered {len(tools)} MCP tools:")

            for tool in tools:
                # Use tool_name attribute for MCPAgentTool
                tool_name = tool.tool_name
                # Get description from tool_spec if available
                tool_desc = getattr(tool.mcp_tool, 'description', 'No description available')
                logger.info(f"  - {tool_name}: {tool_desc}")

            # Create agent with MCP tools following docs pattern
            self.agent = Agent(
                model=self.model,
                tools=tools,
                system_prompt=self._get_system_prompt()
            )

            logger.info("✅ Agent created with MCP tools")
            return tools

    async def run_analysis(self, prompt: str):
        """Run analysis within MCP context"""
        # Agent will autonomously decide to use tools based on system prompt
        # Ensure agent runs within MCP context manager
        with self.mcp_client:
            result = await self.agent.invoke_async(prompt)

        return result

    def extract_result_content(self, result):
        """Extract content from AgentResult for display"""
        return getattr(result, 'content', str(result))