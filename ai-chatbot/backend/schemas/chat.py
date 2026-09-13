from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    message: str = Field(min_length=1)

    conversation_id: str | None = None

    model: str = "gpt-4o-mini"


class ChatResponse(BaseModel):
    response: str
    conversation_id: str
    model: str