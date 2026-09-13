"""Chat API route for sending messages."""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.dependencies import get_current_user
from db.database import get_db
from models.user import User
from schemas.chat import ChatRequest, ChatResponse
from services.chat_service import chat


router = APIRouter(
    prefix="/api/chat",
    tags=["Chat"],
)


@router.post(
    "",
    response_model=ChatResponse,
)
def send_message(
    request: ChatRequest,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    """Send a message and receive an AI response."""
    conversation_id, response = chat(
        db=db,
        user=user,
        message=request.message,
        conversation_id=request.conversation_id,
        model=request.model,
    )

    return ChatResponse(
        response=response,
        conversation_id=conversation_id,
        model=request.model,
    )
