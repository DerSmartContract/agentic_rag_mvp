# Agentic RAG MVP
Ein modulares Retrieval-Augmented-Generation-System mit Hybrid-LLM-Integration und persistentem Speicher.

---

## Projektübersicht

Dieses Projekt implementiert ein minimales, erweiterbares agentenbasiertes RAG-System (Retrieval-Augmented Generation), das externe Informationsquellen mit leistungsstarken Sprachmodellen kombiniert, um kontextbezogene Antworten zu generieren.

### Hauptfunktionen

- **Modulare Agentenarchitektur**: Separate Agenten für lokale Daten, Websuche und Cloud-Quellen
- **Persistenter Speicher**: JSON-basierter Langzeitspeicher für Kontexte
- **Hybridbetrieb für Sprachmodelle**: Umschaltbar zwischen OpenAI (z. B. GPT-4o) und lokalen Modellen (über LM Studio)
- **Asynchrone Verarbeitung**: Aufgaben werden parallel über `asyncio` ausgeführt
- **Konfigurierbares Verhalten über .env-Datei**: Einfacher Wechsel zwischen Modellen

---

## Projektstruktur

```bash
agentic_rag_mvp/
├── main.py                                # Asynchroner Einstiegspunkt
├── .env                                   # Konfigurationsdatei: MODE und API-Key
├── data/memory.json                       # Persistente Kontextsicherung
├── requirements.txt                       # Abhängigkeiten
├── aggregator/aggregator.py               # Zentrale Koordination & Planung
├── agents/                                # Subagenten (lokal, web, cloud)
├── planner/planner.py                     # Planungsmodul zur Aufgabensteuerung
├── memory/memory.py                       # Speicher-Engine mit Ähnlichkeitsabgleich
└── utils/rag_model.py                     # Schnittstelle zu OpenAI oder LM Studio
```

---

## Installation

```bash
git clone https://github.com/<dein-benutzername>/agentic-rag-mvp.git
cd agentic-rag-mvp
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## Konfiguration

Erstelle eine `.env`-Datei im Projektverzeichnis:

```dotenv
MODE=LOCAL                  # oder OPENAI
OPENAI_API_KEY=sk-...       # nur erforderlich bei MODE=OPENAI
```

---

## Anwendung starten

```bash
python main.py
```

---

## Kontextspeicherung (Memory)

Das System speichert alle Anfragen und zugehörigen Kontexte automatisch in `data/memory.json` und ruft bei ähnlichen Anfragen passende Kontexte wieder ab. So wird Redundanz vermieden und die Effizienz gesteigert.

---

## Integration mit LM Studio

1. LM Studio starten
2. Ein Modell laden (z. B. Mistral 7B)
3. API-Zugriff aktivieren („Enable API“)
4. In `.env` den Modus auf `MODE=LOCAL` setzen
5. Anwendung starten

---

## 🔭 Weiterentwicklung & Roadmap

Wir entwickeln das System iterativ weiter in Richtung einer agentenbasierten Plattform mit Selbstüberwachung, Planungslogik und adaptivem Langzeitgedächtnis.

| Modul / Funktion                     | Status         | Beschreibung |
|--------------------------------------|----------------|--------------|
| 🧠 Vektorbasierter Speicher (ChromaDB) | In Planung     | Semantische Ähnlichkeit statt reinem Textvergleich |
| 🧩 ReAct-Agentenplanung                | Konzeptphase   | Reasoning + Acting in verketteten Agentenabläufen |
| 💻 Web-Oberfläche (Next.js / Streamlit)| In Entwicklung | Nutzeroberfläche für Queries, Logs, Memory        |
| 🐳 Docker / CI/CD Deployment          | Bereit         | Containerisierung & GitHub Actions                |
| 🔐 Authentifizierungsmodul (JWT)      | Geplant        | Sichere API-Nutzung & Mehrbenutzerbetrieb         |
| 🧪 Unit-Tests & Coverage              | In Entwicklung | Testabdeckung für Aggregator, Memory & Agents     |
| 📊 Metrik-Logging & Tracing           | Implementiert  | Logging aller Agentenentscheidungen und Antworten |
---
