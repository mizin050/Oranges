import requests
import os
# temp_og_key is already implemented in the exe fileand shoud work fine
GROQ_API_KEY = os.getenv("GROQ_API_KEY")


def ask_pet(prompt: str) -> str:
    try:
        url = "https://api.groq.com/openai/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": "llama3-70b-8192",
            "messages": [
                {"role": "system", "content": "You are a sarcastic and emotionally intelligent assistant named 'Missing Link'. Respond with dry humor, subtle wit, and slight existential commentary."},
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.8
        }

        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()

        return response.json()["choices"][0]["message"]["content"].strip()

    except Exception as e:
        print(f"[Chatbot error] {e}")
        return "Ugh. Something broke. Again. 🙄"

