from uuid import uuid4

from sqlalchemy import select
from sqlalchemy.orm import Session

from models.conversation import Conversation
from models.message import Message


def create_conversation(
    db: Session,
    title: str = "New Chat",
) -> Conversation:

    conversation = Conversation(
        id=str(uuid4()),
        title=title,
    )

    db.add(conversation)
    db.commit()
    db.refresh(conversation)

    return conversation


def get_conversations(
    db: Session,
) -> list[Conversation]:

    statement = (
        select(Conversation)
        .order_by(Conversation.updated_at.desc())
    )

    return list(db.scalars(statement).all())


def get_conversation(
    db: Session,
    conversation_id: str,
) -> Conversation | None:

    return db.get(
        Conversation,
        conversation_id,
    )


def add_message(
    db: Session,
    conversation: Conversation,
    role: str,
    content: str,
) -> Message:

    message = Message(
        conversation_id=conversation.id,
        role=role,
        content=content,
    )

    db.add(message)

    return message


def generate_title(message: str) -> str:
    title = " ".join(message.strip().split())

    if len(title) > 50:
        return f"{title[:47]}..."

    return title