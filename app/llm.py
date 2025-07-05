import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")
model = "mistralai/mistral-7b-instruct"  # You can also try: openai/gpt-3.5-turbo

def generate_synopsis(title, genre, style, tone, length, language):
    prompt = f"""
You are a professional screenwriter assistant.

Generate a {style} movie synopsis in {language} using the following structure:

Title: {title}

Synopsis:
(Write a creative, {tone}-toned, {length}-length synopsis for a {genre} movie.)

Make sure the synopsis includes emotional tone, plot hook, and mentions the main conflict.
"""

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://openrouter.ai",  # Required header
    }

    payload = {
        "model": model,
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=payload
        )
        result = response.json()
        return result['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Error generating synopsis: {e}"
