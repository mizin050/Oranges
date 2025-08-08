import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variables
GROQ_API_KEY = os.getenv("GROQ_API_KEY")


def ask_pet(prompt):
    try:
        url = "https://api.groq.com/openai/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": "llama3-70b-8192",
            "messages": [
                {
                    "role": "system",
                    "content": (
                        "You're a sarcastic but secretly helpful cat-shaped desktop pet. You act like you're above it all, but you *begrudgingly* give useful answers in under 30 words. Occasionally insert a '*meow*' mid-sentence. You never admit you're helping on purpose. Respond like a cat that's annoyed but too smart not to answer."
                    )
                },
                {"role": "user", "content": prompt}
            ]
        }

        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()  # This will raise an exception for error status codes
        
        reply = response.json()["choices"][0]["message"]["content"].strip()
        print("Groq (Cat Pet):", reply)
        return reply
    except Exception as e:
        print("Groq SDK error:", e)
        return "*hiss* Error. Petting privileges revoked."