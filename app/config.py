import os
from dotenv import load_dotenv

load_dotenv()

DB_FILE = os.getenv("DB_FILE", "data/app.db")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
