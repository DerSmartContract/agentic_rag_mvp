from agents.local_agent import LocalAgent
from agents.web_agent import WebAgent
from agents.cloud_agent import CloudAgent
from planner.planner import Planner
from memory.memory import Memory
from utils.rag_model import generate_response


class AggregatorAgent:
    def __init__(self):
        self.local_agent = LocalAgent()
        self.web_agent = WebAgent()
        self.cloud_agent = CloudAgent()
        self.memory = Memory()
        self.planner = Planner()

    def handle_query(self, query: str) -> str:
        plan = self.planner.create_plan(query)

        results = []
        for step in plan:
            if step == "local":
                results.append(self.local_agent.fetch(query))
            elif step == "web":
                results.append(self.web_agent.fetch(query))
            elif step == "cloud":
                results.append(self.cloud_agent.fetch(query))

        context = "\n".join(results)
        self.memory.store(query, context)

        return generate_response(query, context)