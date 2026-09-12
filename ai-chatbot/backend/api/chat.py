from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.database import get_db
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
):

    conversation_id, response = chat(
        db=db,
        message=request.message,
        conversation_id=request.conversation_id,
    )

    return ChatResponse(
        response=response,
        conversation_id=conversation_id,
    )