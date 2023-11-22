from openai import OpenAI

from settings import OPENAI_API_KEY, OPENAI_MODEL, OPENAI_TEMPERATURE

client = OpenAI(
    api_key=OPENAI_API_KEY,
)


def get_completion_from_messages(messages: dict) -> str:
    response = client.chat.completions.create(
        messages=messages,
        model=OPENAI_MODEL,
        temperature=OPENAI_TEMPERATURE,
    )

    return response.choices[0].message.content
