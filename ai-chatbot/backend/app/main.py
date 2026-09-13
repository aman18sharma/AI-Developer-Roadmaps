"""FastAPI application factory: registers routers, middleware, and exception handlers."""

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from api.auth import router as auth_router
from api.chat import router as chat_router
from api.conversations import router as conversations_router
from core.exceptions import AppException
from core.logging_config import configure_logging
from db.database import Base, engine
import models  # noqa: F401 – registers all ORM models with SQLAlchemy metadata

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
    """Return service health status."""
    return {
        "status": "healthy",
    }


@app.exception_handler(AppException)
async def app_exception_handler(
    request: Request,  # pylint: disable=unused-argument
    exc: AppException,
):
    """Convert AppException instances to structured JSON error responses."""
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": {
                "code": exc.code,
                "message": exc.message,
            }
        },
    )
