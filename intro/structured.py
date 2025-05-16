"""
Structired Output
Ensure responses adhere to a JSON schema.
"""

import os
from openai import OpenAI
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

# https://platform.openai.com/docs/quickstart?api-mode=responses&lang=python
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# -----------------------------------------------------------
# Step 1: Define the response format in a Pydantic model
# -----------------------------------------------------------

class CalendarEvent(BaseModel):
    name: str
    date: str
    participants: list[str]


# -----------------------------------------------------------
# Step 2: Use the model to parse the response
# -----------------------------------------------------------
    
        
response = client.beta.chat.completions.parse(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "Extract the event information"},
        {
            "role": "user",
            "content": "Steve and Deidre are going to an academic talk about Shakespeare in Oxford this friday."
        },
    ],
    response_format=CalendarEvent,
)

output = response.choices[0].message.content
print(output)
