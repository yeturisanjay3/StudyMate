import os
from dotenv import load_dotenv
from transformers import pipeline

load_dotenv()

def generate_response(prompt):
    api_key = os.getenv("HUGGINGFACE_API_KEY")
    model_name = os.getenv("GENERATION_MODEL")

    if not api_key or not model_name:
        return "Missing API key or model name."

    try:
        generator = pipeline(
            "text-generation",
            model=model_name,
            use_auth_token=api_key
        )
        result = generator(prompt, max_new_tokens=200, do_sample=True, temperature=0.7)
        return result[0]['generated_text']
    except Exception as e:
        return f"Error generating response: {e}"
