class Planner:
    def create_plan(self, query: str) -> list:
        if "AWS" in query:
            return ["local", "cloud", "web"]
        return ["local", "web"]