"""Pydantic schemas for conversation and message responses."""

from datetime import datetime

from pydantic import BaseModel


class ConversationSummary(BaseModel):
    """Lightweight conversation representation used in list responses."""

    id: str
    title: str
    created_at: datetime
    updated_at: datetime


class MessageResponse(BaseModel):
    """Representation of a single message within a conversation."""

    id: int
    role: str
    content: str
    created_at: datetime


class ConversationDetail(BaseModel):
    """Full conversation representation including all messages."""

    id: str
    title: str
    created_at: datetime
    updated_at: datetime
    messages: list[MessageResponse]
