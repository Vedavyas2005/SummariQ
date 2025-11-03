import google.generativeai as genai
from config import GEMINI_API_KEY

MODEL = "gemini-2.5-flash"
import streamlit as st

genai.configure(api_key=GEMINI_API_KEY)

def generate_summary(context: str, detail_level: str = "brief") -> str:
    """Generate a summary or detailed explanation using Gemini API."""
    prompt = f"Summarize this in an easily understandable way:\n{context}"
    if detail_level == "detailed":
        prompt = f"Explain in detail:\n{context}\nUse simple vocabulary."
    try:
        model = genai.GenerativeModel(MODEL)
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Gemini API error: {e}"
