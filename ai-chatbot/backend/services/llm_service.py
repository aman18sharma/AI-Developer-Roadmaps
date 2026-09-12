from openai import OpenAI

from app.config import settings


client = OpenAI(api_key=settings.xkiro_openai_api_key, base_url=settings.xkiro_base_url)


SYSTEM_PROMPT = """
You are a helpful AI assistant.

Rules:
1. Give accurate and useful answers.
2. If you don't know something, say so.
3. Do not invent facts.
4. Keep answers clear and structured.
"""


def generate_response(messages: list[dict]) -> str:

    response = client.chat.completions.create(
        model=settings.xkiro_model_name,
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },
            *messages,
        ],
        temperature=0.3,
    )

    return response.choices[0].message.content