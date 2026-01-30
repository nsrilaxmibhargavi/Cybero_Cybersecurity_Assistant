import openai
import os

# Set your API key as an environment variable
# Windows (PowerShell):
# setx OPENAI_API_KEY "your_key_here"

openai.api_key = os.getenv("Your key here")

SYSTEM_PROMPT = (
    "You are a helpful cybersecurity assistant. "
    "Explain concepts clearly and concisely for students."
)

def ai_reply(user_input, context=None):
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT}
    ]

    if context:
        messages.append({
            "role": "assistant",
            "content": f"Previous topic: {context}"
        })

    messages.append({
        "role": "user",
        "content": user_input
    })

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=messages,
        temperature=0.4
    )

    return response.choices[0].message.content.strip()

print("AI fallback called")

