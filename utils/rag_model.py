# utils/rag_model.py
import os
from dotenv import load_dotenv
import logging

# Laden der Umgebungsvariablen
load_dotenv()
MODE = os.getenv("MODE", "OPENAI")

# === OPENAI-MODE ===
if MODE == "OPENAI":
    import openai
    openai.api_key = os.getenv("OPENAI_API_KEY")

    def generate_response(query: str, context: str) -> str:
        try:
            messages = [
                {"role": "system", "content": "Du bist ein smarter Assistent mit Zugriff auf externes Wissen."},
                {"role": "user", "content": f"Frage: {query}\n\nKontext:\n{context}"}
            ]
            response = openai.ChatCompletion.create(
                model="gpt-4o",  # alternativ: "gpt-3.5-turbo"
                messages=messages,
                temperature=0.3,
                max_tokens=800
            )
            answer = response.choices[0].message.content.strip()
            logging.info("[RAG OPENAI] Antwort erfolgreich generiert.")
            return answer
        except Exception as e:
            logging.error(f"[RAG OPENAI] Fehler bei API-Aufruf: {e}")
            return f"❌ Fehler bei OpenAI API: {e}"

# === LOCAL-MODE (LM Studio) ===
elif MODE == "LOCAL":
    import requests

    def generate_response(query: str, context: str) -> str:
        try:
            endpoint = "http://localhost:1234/v1/chat/completions"
            data = {
                "model": "local-model",
                "messages": [
                    {
                        "role": "system",
                        "content": (
                            "Du bist ein intelligenter Agentic RAG-Assistent. Nutze den Kontext zur präzisen Beantwortung."
                        )
                    },
                    {
                        "role": "user",
                        "content": f"Frage: {query}\n\nKontext:\n{context}"
                    }
                ],
                "temperature": 0.4
            }
            response = requests.post(endpoint, json=data, timeout=15)
            response.raise_for_status()
            result = response.json()
            answer = result["choices"][0]["message"]["content"].strip()
            logging.info("[RAG LOCAL] Antwort erfolgreich generiert.")
            return answer
        except Exception as e:
            logging.error(f"[RAG LOCAL] Fehler bei LM Studio API: {e}")
            return f"❌ Fehler bei LM Studio API: {e}"

# === FAILSAFE ===
else:
    def generate_response(query: str, context: str) -> str:
        return f"❌ Ungültiger MODE '{MODE}'. Bitte setze MODE=OPENAI oder MODE=LOCAL in deiner .env-Datei."