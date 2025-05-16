import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# https://platform.openai.com/docs/quickstart?api-mode=responses&lang=python
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Write a limerick about the Python programming language. Add an inspirational quote from Alan Turing."
        },
    ],
)

output = response.choices[0].message.content
print(output)
