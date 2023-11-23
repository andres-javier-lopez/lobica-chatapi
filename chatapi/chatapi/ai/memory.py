from .client import get_completion_from_messages


messages = []


def add_context(content: str):
    messages.append({
        'role': 'system',
        'content': content
    })


def get_response(prompt: str) -> str:
    messages.append({
        'role': 'user',
        'content': prompt
    })
    response = get_completion_from_messages(messages)
    messages.append({
        'role': 'assistant',
        'content': response,
    })
    return response


def get_messages() -> list[dict[str, str]]:
    return messages


def clear_messages():
    global messages
    messages = []
