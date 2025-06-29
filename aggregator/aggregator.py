# aggregator/aggregator.py
from agents.local_agent import LocalAgent
from agents.web_agent import WebAgent
from agents.cloud_agent import CloudAgent
from planner.planner import Planner
from memory.memory import Memory
from utils.rag_model import generate_response
import asyncio

"""
AggregatorAgent orchestrates the interaction between local, web, and cloud agents,
utilizing a planner to create a query execution plan and a memory module to store context.
"""

class AggregatorAgent:
    def __init__(self):
        self.local_agent = LocalAgent()
        self.web_agent = WebAgent()
        self.cloud_agent = CloudAgent()
        self.memory = Memory()
        self.planner = Planner()

    async def handle_query(self, query: str) -> str:
        cached = self.memory.retrieve(query)
        if cached:
            return generate_response(query, cached)

        plan = self.planner.create_plan(query)
        tasks = []

        if "local" in plan:
            tasks.append(self.local_agent.fetch(query))
        if "web" in plan:
            tasks.append(self.web_agent.fetch(query))
        if "cloud" in plan:
            tasks.append(self.cloud_agent.fetch(query))

        results = await asyncio.gather(*tasks)
        context = "\n".join(results)

        self.memory.store(query, context)
        return generate_response(query, context)