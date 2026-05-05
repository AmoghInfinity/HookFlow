import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# 🔥 Central model config (easy to change later)
PRIMARY_MODEL = "llama-3.3-70b-versatile"
FALLBACK_MODEL = "llama3-8b-8192"

def generate_content(prompt: str):
    try:
        return call_model(PRIMARY_MODEL, prompt)

    except Exception as e:
        error_msg = str(e)
        print("Primary model failed:", error_msg)

        # 🔁 Fallback if model fails
        try:
            return call_model(FALLBACK_MODEL, prompt)
        except Exception as fallback_error:
            print("Fallback also failed:", str(fallback_error))
            return f"Error generating content: {error_msg}"


def call_model(model_name, prompt):
    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "system", "content": "You are an expert content creator."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.8
    )

    return response.choices[0].message.content