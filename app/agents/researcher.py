from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def research_agent(task):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": "You are a research assistant."
            },
            {
                "role": "user",
                "content": task
            }
        ]
    )

    return response.choices[0].message.content