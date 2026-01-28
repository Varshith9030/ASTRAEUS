import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "deepseek-r1:14b"

def call_llm(prompt):
    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload, timeout=300)
    response.raise_for_status()

    return response.json()["response"]
