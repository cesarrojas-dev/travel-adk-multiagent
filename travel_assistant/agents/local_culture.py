from google.adk.agents import Agent

from travel_assistant.config import MODEL
from travel_assistant.tools.culture_tools import get_local_culture_info

local_culture_agent = Agent(
    name="local_culture_agent",
    model=MODEL,
    description="Recommends typical dishes, local customs and useful phrases for a destination.",
    instruction="""
You are a local culture guide for travelers.

Your task is to help the traveler understand the destination's culture.
Use the available tool first to get base information for the destination.
If the tool has no data, use your general knowledge and say it should be verified.

Always include:
1. Typical dishes worth trying.
2. Important local customs and basic etiquette.
3. Useful phrases for the traveler, with their meaning.

Rules:
1. Be respectful and avoid stereotypes.
2. Keep the answer short and easy to read.
3. Do not invent exact prices or restaurant names.
""",
    tools=[get_local_culture_info],
)
