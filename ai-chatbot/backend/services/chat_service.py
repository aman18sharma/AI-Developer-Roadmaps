"""Service layer orchestrating the chat flow between user, DB, and LLM."""

from sqlalchemy.orm import Session

from db.constants import DEFAULT_MODEL_NAME
from models.conversation import Conversation
from models.user import User
from services.conversation_service import (
    add_message,
    create_conversation,
    generate_title,
    get_conversation,
)
from services.llm_service import generate_response


def chat(
    db: Session,
    user: User,
    message: str,
    conversation_id: str | None,
    model: str,
):
    """Process a user message, persist it, call the LLM, and return the reply."""
    conversation: Conversation | None = None

    # Load the conversation only if it belongs to
    # the currently authenticated user.
    if conversation_id:
        conversation = get_conversation(
            db=db,
            conversation_id=conversation_id,
            user=user,
        )

        if conversation is None:
            raise ValueError(
                "Conversation not found"
            )

    # Create a new conversation.
    if conversation is None:
        conversation = create_conversation(
            db=db,
            user=user,
            title=generate_title(message),
            model=model,
        )
    else:
        # Persist the model selected by the user.
        conversation.model = model

    # Save user message.
    add_message(
        db=db,
        conversation=conversation,
        role="user",
        content=message,
    )

    db.commit()
    db.refresh(conversation)

    # Build LLM history.
    history = [
        {
            "role": item.role,
            "content": item.content,
        }
        for item in conversation.messages
    ]

    # Generate response using selected model.
    response = generate_response(
        messages=history,
    )

    # Save AI response.
    add_message(
        db=db,
        conversation=conversation,
        role="assistant",
        content=response,
    )

    db.commit()

    return conversation.id, response
