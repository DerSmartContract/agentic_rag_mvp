import json
import os
from difflib import get_close_matches
import logging

MEMORY_FILE = "data/memory.json"

class Memory:
    def __init__(self):
        os.makedirs("data", exist_ok=True)
        if not os.path.exists(MEMORY_FILE):
            with open(MEMORY_FILE, "w", encoding="utf-8") as f:
                json.dump({}, f, indent=2)
        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            self.data = json.load(f)

    def store(self, query: str, context: str):
        self.data[query] = context
        with open(MEMORY_FILE, "w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=2, ensure_ascii=False)

    def retrieve(self, query: str, threshold: float = 0.7) -> str:
        match = get_close_matches(query, self.data.keys(), n=1, cutoff=threshold)
        return self.data[match[0]] if match else ""

    def inspect(self):
        logging.info(f"[Memory] Aktuelle gespeicherte Queries: {list(self.data.keys())}")
        return list(self.data.keys())

    def clear(self):
        self.data = {}
        with open(MEMORY_FILE, "w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=2, ensure_ascii=False)
        logging.info("[Memory] Speicher vollständig gelöscht.")

    def delete(self, query: str):
        if query in self.data:
            del self.data[query]
            with open(MEMORY_FILE, "w", encoding="utf-8") as f:
                json.dump(self.data, f, indent=2, ensure_ascii=False)
            logging.info(f"[Memory] Query gelöscht: '{query}'")
        else:
            logging.warning(f"[Memory] Kein Eintrag gefunden für Löschversuch: '{query}'")