"""Pydantic schemas for chat request and response payloads."""

from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    """Request body for sending a chat message."""

    message: str = Field(min_length=1)

    conversation_id: str | None = None

    model: str = "gpt-4o-mini"


class ChatResponse(BaseModel):
    """Response body containing the AI reply and conversation context."""

    response: str
    conversation_id: str
    model: str
