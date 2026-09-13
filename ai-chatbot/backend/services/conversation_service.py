from uuid import uuid4

from sqlalchemy import select
from sqlalchemy.orm import Session

from models.conversation import Conversation
from models.message import Message
from models.user import User
from db.constants import DEFAULT_MODEL_NAME


def create_conversation(
    db: Session,
    user: User,
    title: str,
    model: str = DEFAULT_MODEL_NAME
) -> Conversation:

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
    user
) -> Conversation | None:

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

    title = " ".join(
        message.strip().split()
    )

    if len(title) > 50:
        return f"{title[:47]}..."

    return title