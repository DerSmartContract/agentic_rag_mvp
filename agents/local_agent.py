import os
import logging
from pathlib import Path

class LocalAgent:
    def __init__(self, data_path: str = "data/local_docs/"):
        self.data_path = Path(data_path)
        if not self.data_path.exists():
            logging.warning(f"[LocalAgent] Lokaler Datenpfad nicht gefunden: {self.data_path}")
        else:
            logging.info(f"[LocalAgent] Initialisiert mit Pfad: {self.data_path}")

    def fetch(self, query: str) -> str:
        logging.info(f"[LocalAgent] Bearbeite lokale Anfrage: {query}")
        if not self.data_path.exists():
            return f"⚠️ Lokale Datenquelle fehlt: {self.data_path}"

        results = []
        for file in self.data_path.glob("*.txt"):
            try:
                content = file.read_text(encoding="utf-8")
                if query.lower() in content.lower():
                    results.append(f"{file.name}: {self._extract_snippet(content, query)}")
            except Exception as e:
                logging.error(f"[LocalAgent] Fehler beim Lesen von {file.name}: {e}")

        if results:
            return "\n".join(results)
        return f"📁 Keine lokalen Treffer zu '{query}' gefunden."

    def _extract_snippet(self, text: str, keyword: str, context_len: int = 40) -> str:
        idx = text.lower().find(keyword.lower())
        if idx == -1:
            return "Kein Ausschnitt verfügbar."
        start = max(0, idx - context_len)
        end = min(len(text), idx + len(keyword) + context_len)
        return text[start:end].replace("\n", " ").strip()