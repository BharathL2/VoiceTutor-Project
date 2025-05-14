# Explanation agent using LLM
from langchain_community.llms import OpenAI


from utils.helpers import get_openai_key

llm = OpenAI(api_key=get_openai_key())

def explain(text):
    prompt = f"Explain this in simple terms:\n\n{text}"
    return llm(prompt)
