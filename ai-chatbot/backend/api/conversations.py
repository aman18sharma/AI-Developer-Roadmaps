from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db.database import get_db
from schemas.conversation import (
    ConversationDetail,
    ConversationSummary,
    MessageResponse,
)
from services.conversation_service import (
    get_conversation,
    get_conversations,
)


router = APIRouter(
    prefix="/api/conversations",
    tags=["Conversations"],
)


@router.get(
    "",
    response_model=list[ConversationSummary],
)
def list_conversations(
    db: Session = Depends(get_db),
):

    conversations = get_conversations(db)

    return [
        ConversationSummary(
            id=item.id,
            title=item.title,
            created_at=item.created_at,
            updated_at=item.updated_at,
        )
        for item in conversations
    ]


@router.get(
    "/{conversation_id}",
    response_model=ConversationDetail,
)
def get_conversation_details(
    conversation_id: str,
    db: Session = Depends(get_db),
):

    conversation = get_conversation(
        db,
        conversation_id,
    )

    if conversation is None:
        raise HTTPException(
            status_code=404,
            detail="Conversation not found",
        )

    return ConversationDetail(
        id=conversation.id,
        title=conversation.title,
        created_at=conversation.created_at,
        updated_at=conversation.updated_at,
        messages=[
            MessageResponse(
                id=message.id,
                role=message.role,
                content=message.content,
                created_at=message.created_at,
            )
            for message in conversation.messages
        ],
    )