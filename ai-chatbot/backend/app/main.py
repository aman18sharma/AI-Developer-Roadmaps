from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.chat import router as chat_router
from api.conversations import (
    router as conversations_router,
)

from db.database import Base, engine

# Import models so SQLAlchemy knows about them
from models.conversation import Conversation
from models.message import Message


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="AI Chatbot API",
    version="1.0.0",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(chat_router)
app.include_router(conversations_router)


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
    }