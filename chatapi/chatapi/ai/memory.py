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
    return get_completion_from_messages(messages)


def clear_messages():
    global messages
    messages = []
