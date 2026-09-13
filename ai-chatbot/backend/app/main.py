from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from core.exceptions import AppException

from api.chat import router as chat_router
from api.conversations import (
    router as conversations_router,
)
from api.auth import router as auth_router

from db.database import Base, engine
from core.logging_config import configure_logging

# Import models so SQLAlchemy knows about them
from models.conversation import Conversation
from models.message import Message

from db.database import Base

import models

Base.metadata.create_all(bind=engine)
configure_logging()

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
app.include_router(auth_router)


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
    }

@app.exception_handler(AppException)
async def app_exception_handler(
    request: Request,
    exc: AppException,
):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": {
                "code": exc.code,
                "message": exc.message,
            }
        },
    )