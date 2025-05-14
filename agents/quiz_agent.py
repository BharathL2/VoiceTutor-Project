# Quiz generation agent using LLM
from langchain.llms import OpenAI
from utils.helpers import get_openai_key

llm = OpenAI(api_key=get_openai_key())

def generate_quiz(text):
    prompt = f"""Generate 3 multiple-choice questions based on the following content:
    
    {text}

    Format:
    Q1. Question?
    a) ...
    b) ...
    c) ...
    d) ...
    Answer: ...
    """
    return llm(prompt)
# agents/quiz_agent.py

def quiz(query: str) -> str:
    return "Here's a quiz for you! What is the most common optimization algorithm in machine learning?"
