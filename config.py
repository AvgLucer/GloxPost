import os
from dotenv import load_dotenv
from openrouter import OpenRouter

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME")

if not API_KEY:
    raise ValueError("OPENROUTER_API_KEY is missing from .env")

if not MODEL_NAME:
    raise ValueError("MODEL_NAME is missing from .env")

client = OpenRouter(
    api_key=API_KEY
)