import openai

def generate_response(query: str, context: str) -> str:
    prompt = f"""
    Du bist ein Agentic RAG-System. Verwende den folgenden Kontext zur Beantwortung der Nutzerfrage.

    === Kontext ===
    {context}

    === Nutzerfrage ===
    {query}

    === Antwort ===
    """
    # Mocked OpenAI call
    return f"[MOCKED] Antwort auf: {query} basierend auf Kontext:\n{context}"