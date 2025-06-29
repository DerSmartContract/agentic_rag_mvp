# main.py
import asyncio
from aggregator.aggregator import AggregatorAgent

async def main():
    user_query = "Wie richte ich ein GitHub Actions Deployment auf AWS ein?"
    agent = AggregatorAgent()
    response = await agent.handle_query(user_query)
    print("✅ Final Response:\n", response)

if __name__ == "__main__":
    asyncio.run(main())