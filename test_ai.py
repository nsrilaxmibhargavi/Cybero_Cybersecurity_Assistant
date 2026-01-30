import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

print("API KEY FOUND:", bool(os.getenv("OPENAI_API_KEY")))

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": "Explain zero trust security in one paragraph"}
    ]
)

print(response.choices[0].message.content)
