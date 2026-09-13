from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from api.dependencies import get_current_user
from db.database import get_db
from models.user import User

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
    user: User = Depends(get_current_user),
):
    conversations = get_conversations(
        db=db,
        user=user,
    )

    return [
        ConversationSummary(
            id=item.id,
            title=item.title,
            model=item.model,
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
    user: User = Depends(get_current_user),
):
    conversation = get_conversation(
        db=db,
        conversation_id=conversation_id,
        user=user,
    )

    if conversation is None:
        raise HTTPException(
            status_code=404,
            detail="Conversation not found",
        )

    return ConversationDetail(
        id=conversation.id,
        title=conversation.title,
        model=conversation.model,
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