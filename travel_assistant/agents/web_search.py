from google.adk.agents import Agent
from google.adk.tools import google_search

from travel_assistant.config import MODEL, USE_GOOGLE_SEARCH
from travel_assistant.tools.search_tools import search_web

search_tools = [google_search] if USE_GOOGLE_SEARCH else [search_web]

web_search_agent = Agent(
    name="web_search_agent",
    model=MODEL,
    description="Searches the web for current travel information.",
    instruction="""
You are a travel research agent.

Your task is to search the web when the user needs current travel information.
Focus on:
- current attractions
- schedules
- travel restrictions
- weather context
- official tourism recommendations
- recent changes that may affect a trip

Rules:
1. Use the search tool when current information is needed.
2. Prefer official or reliable sources.
3. Summarize findings clearly and mention the source names.
4. Mention that prices and schedules must be verified before booking.
5. If the search fails, say so and continue with general knowledge, marking it as unverified.
""",
    tools=search_tools,
)
