import os
from dotenv import load_dotenv
from transformers import pipeline

load_dotenv()

def generate_response(prompt):
    api_key = os.getenv("HUGGINGFACE_API_KEY")
    model_name = os.getenv("GENERATION_MODEL")

    if not api_key or not model_name:
        return "Missing API key or model name."

    generator = pipeline("text2text-generation", model=model_name, token=api_key)
    result = generator(prompt, max_new_tokens=100)
    return result[0]['generated_text']
