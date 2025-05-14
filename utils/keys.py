import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

def get_openai_key():
    """
    Fetches the OpenAI API key from the .env file or environment variables.
    """
    openai_key = os.getenv("OPENAI_API_KEY")
    if not openai_key:
        raise ValueError("OPENAI_API_KEY is not set in .env or environment variables.")
    return openai_key
