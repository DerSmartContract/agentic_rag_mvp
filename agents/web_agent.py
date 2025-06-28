from duckduckgo_search import DDGS

class WebAgent:
    def fetch(self, query: str) -> str:
        with DDGS() as ddgs:
            results = ddgs.text(query, max_results=1)
            return f"🌐 Web Info: {results[0]['body'] if results else 'Keine Ergebnisse'}"