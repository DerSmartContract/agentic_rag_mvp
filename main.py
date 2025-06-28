from aggregator.aggregator import AggregatorAgent

if __name__ == "__main__":
    user_query = "Wie richte ich ein GitHub Actions Deployment auf AWS ein?"

    agent = AggregatorAgent()
    response = agent.handle_query(user_query)

    print("✅ Final Response:\n", response)