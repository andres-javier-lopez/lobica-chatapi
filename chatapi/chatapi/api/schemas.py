from pydantic import BaseModel


class Message(BaseModel):
    role: str
    content: str


class MessagePayload(BaseModel):
    content: str


class MessagesResult(BaseModel):
    messages: list[Message]
