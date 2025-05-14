# agents/code_agent.py

from langchain_community.llms import OpenAI  # updated import as per deprecation warning
from utils.keys import get_openai_key

def generate_code(prompt: str) -> str:
    """
    Generates code based on a given prompt using OpenAI's language model.
    """
    llm = OpenAI(api_key=get_openai_key())
    response = llm(prompt)
    return response.strip()
