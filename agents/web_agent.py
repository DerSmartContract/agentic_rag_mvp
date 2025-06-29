import logging
from duckduckgo_search import DDGS

class WebAgent:
    def __init__(self, max_results: int = 3):
        self.max_results = max_results
        logging.info(f"[WebAgent] Initialisiert mit max_results={self.max_results}")

    def fetch(self, query: str) -> str:
        logging.info(f"[WebAgent] Web-Suche gestartet für: '{query}'")
        try:
            with DDGS() as ddgs:
                results = ddgs.text(query, max_results=self.max_results)
                if not results:
                    return "🌐 Keine Web-Ergebnisse gefunden."

                snippets = [
                    f"• {res['body'][:250].strip()} [...]" 
                    for res in results if 'body' in res
                ]
                return "🌐 Web Info:\n" + "\n".join(snippets)
        except Exception as e:
            logging.error(f"[WebAgent] Fehler bei Websuche: {e}")
            return f"❌ Fehler bei der Websuche: {str(e)}"