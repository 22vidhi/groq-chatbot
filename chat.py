# groq_chatbot.py
from dotenv import load_dotenv
load_dotenv()

import requests
import os
api_key = os.getenv("GROQ_API_KEY")


def get_groq_response(user_input):
    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "llama3-8b-8192",  # Or llama3-70b-8192
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input}
        ],
        "temperature": 0.7
    }

    try:
        response = requests.post(url, headers=headers, json=payload)

        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        else:
            return f"❌ Error {response.status_code}: {response.text}"
    except Exception as e:
        return f"⚠️ Exception occurred: {str(e)}"
