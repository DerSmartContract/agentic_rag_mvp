import logging
import re

class Planner:
    def __init__(self):
        self.rules = {
            "aws": ["local", "cloud", "web"],
            "deployment": ["local", "cloud"],
            "github": ["local", "web"],
            "websuche": ["web"],
            "lokal": ["local"],
        }
        logging.info(f"[Planner] Initialisiert mit {len(self.rules)} Regel(n)")

    def create_plan(self, query: str) -> list:
        plan = set()

        lowered_query = query.lower()
        for keyword, agents in self.rules.items():
            if re.search(rf"\b{re.escape(keyword)}\b", lowered_query):
                plan.update(agents)

        if not plan:
            plan = {"local", "web"}

        logging.info(f"[Planner] Plan erstellt für '{query}': {sorted(plan)}")
        return sorted(plan)