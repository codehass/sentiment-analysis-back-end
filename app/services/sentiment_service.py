import os
import requests
from dotenv import load_dotenv

load_dotenv()


def get_sentiment_analysis(input_text):
    API_URL = "https://router.huggingface.co/hf-inference/models/nlptown/bert-base-multilingual-uncased-sentiment"

    # Fix the header part, call os.getenv correctly
    headers = {
        "Authorization": f"Bearer {os.getenv('HF_TOKEN')}",
    }

    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()

    output = query(
        {
            "inputs": input_text,
        }
    )

    return output
