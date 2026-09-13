"""Service layer for conversation and message persistence."""

from uuid import uuid4

from sqlalchemy import select
from sqlalchemy.orm import Session

from db.constants import DEFAULT_MODEL_NAME
from models.conversation import Conversation
from models.message import Message
from models.user import User


def create_conversation(
    db: Session,
    user: User,
    title: str,
    model: str = DEFAULT_MODEL_NAME,
) -> Conversation:
    """Create and persist a new conversation for the given user."""
    conversation = Conversation(
        id=str(uuid4()),
        user_id=user.id,
        title=title,
        model=model,
    )

    db.add(conversation)
    db.commit()
    db.refresh(conversation)

    return conversation


def get_conversations(
    db: Session,
    user: User,
) -> list[Conversation]:
    """Return all conversations for a user, ordered by most recently updated."""
    statement = (
        select(Conversation)
        .where(
            Conversation.user_id == user.id
        )
        .order_by(
            Conversation.updated_at.desc()
        )
    )

    return list(
        db.scalars(statement).all()
    )


def get_conversation(
    db: Session,
    conversation_id: str,
    user: User,
) -> Conversation | None:
    """Return a single conversation by ID if it belongs to the user, else None."""
    statement = (
        select(Conversation)
        .where(
            Conversation.id == conversation_id,
            Conversation.user_id == user.id,
        )
    )

    return db.scalar(statement)


def add_message(
    db: Session,
    conversation: Conversation,
    role: str,
    content: str,
) -> Message:
    """Append a message to a conversation and stage it for commit."""
    message = Message(
        conversation_id=conversation.id,
        role=role,
        content=content,
    )

    db.add(message)

    return message


def generate_title(
    message: str,
) -> str:
    """Derive a short conversation title from the first user message."""
    title = " ".join(
        message.strip().split()
    )

    if len(title) > 50:
        return f"{title[:47]}..."

    return title
