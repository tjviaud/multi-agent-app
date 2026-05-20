from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def planner_agent(task):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": "You are a planning agent."
            },
            {
                "role": "user",
                "content": task
            }
        ]
    )

    return response.choices[0].message.content