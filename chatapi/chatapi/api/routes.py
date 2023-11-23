import chatapi.ai as ai

from .app import app
from .schemas import MessagePayload, MessagesResult


@app.get("/messages")
async def get_messsages() -> MessagesResult:
    messages = ai.get_messages()

    return MessagesResult(messages=messages)


@app.post("/messages")
async def send_message(message: MessagePayload) -> MessagesResult:
    ai.get_response(message.content)
    messages = ai.get_messages()
    return MessagesResult(messages=messages)
