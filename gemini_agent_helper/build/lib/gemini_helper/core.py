# gemini_helper/core.py

import os
from dotenv import load_dotenv
from agents import AsyncOpenAI, OpenAIChatCompletionsModel

def get_gemini_model():
    load_dotenv()
    gemini_api_key = os.getenv("GEMINI_API_KEY")
    if not gemini_api_key:
        raise ValueError("GEMINI_API_KEY not found in .env file")
    
    provider = AsyncOpenAI(
        api_key = gemini_api_key,
        base_url = "https://generativelanguage.googleapis.com/v1beta/openai"
    )

    model = OpenAIChatCompletionsModel(
        model = "gemini-2.0-flash",
        openai_client = provider
    )
    return model
