# main.py
import asyncio
import logging
from dotenv import load_dotenv
from aggregator.aggregator import AggregatorAgent

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()]
)

async def main():
    print("\n🤖 Willkommen beim Agentic RAG MVP")
    user_query = input("🔎 Gib deine Frage ein: ").strip()
    if not user_query:
        print("⚠️  Keine Eingabe erkannt. Vorgang abgebrochen.")
        return

    agent = AggregatorAgent()
    response = await agent.handle_query(user_query)
    print("\n✅ Final Response:\n", response)

if __name__ == "__main__":
    asyncio.run(main())