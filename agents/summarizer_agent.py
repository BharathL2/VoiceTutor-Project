# Summarization agent using LLM
from langchain.llms import OpenAI

llm = OpenAI(temperature=0)

def summarize(text):
    prompt = f"Summarize the following text:\n\n{text}"
    return llm(prompt)
