from sqlalchemy.orm import Session

from models.conversation import Conversation

from services.conversation_service import (
    add_message,
    create_conversation,
    generate_title,
    get_conversation,
)

from services.llm_service import generate_response


def chat(
    db: Session,
    message: str,
    conversation_id: str | None,
):

    conversation: Conversation | None = None

    if conversation_id:
        conversation = get_conversation(
            db,
            conversation_id,
        )

    # Create new conversation if necessary
    if conversation is None:
        conversation = create_conversation(
            db,
            title=generate_title(message),
        )

    # Save user message
    add_message(
        db,
        conversation,
        "user",
        message,
    )

    db.commit()

    # Get previous messages
    history = [
        {
            "role": item.role,
            "content": item.content,
        }
        for item in conversation.messages
    ]

    # Generate AI response
    response = generate_response(history)

    # Save AI response
    add_message(
        db,
        conversation,
        "assistant",
        response,
    )

    db.commit()

    return conversation.id, response