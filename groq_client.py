import os
import requests
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")  # ✅ FIXED NAME

def generate_questions(prompt):
    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }

    response = requests.post(url, headers=headers, json=data)

    print("STATUS:", response.status_code)
    print("TEXT:", response.text)

    try:
        result = response.json()
    except:
        return "ERROR: Invalid JSON response"

    if "choices" in result:
        return result["choices"][0]["message"]["content"]
    else:
        return f"ERROR: {result}"
    