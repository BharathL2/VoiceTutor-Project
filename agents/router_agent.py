# agents/router_agent.py

from agents.explainer_agent import explain
from agents.quiz_agent import quiz
from agents.code_agent import generate_code

def route(query: str) -> str:
    query_lower = query.lower()

    if "explain" in query_lower or "what is" in query_lower:
        return explain(query)
    elif "quiz" in query_lower or "test" in query_lower:
        return quiz(query)
    elif "code" in query_lower or "implement" in query_lower:
        return generate_code(query)
    else:
        return "I'm not sure how to help with that. Could you please clarify your request?"
