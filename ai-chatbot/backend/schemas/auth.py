"""Pydantic schemas for authentication requests and responses."""

from pydantic import BaseModel, EmailStr, Field


class RegisterRequest(BaseModel):
    """Request body for user registration."""

    name: str = Field(
        min_length=2,
        max_length=100,
    )

    email: EmailStr

    password: str = Field(
        min_length=8,
        max_length=128,
    )


class UserResponse(BaseModel):
    """Response body containing public user information."""

    id: int
    name: str
    email: EmailStr


class TokenResponse(BaseModel):
    """Response body containing the issued access token."""

    access_token: str
    token_type: str = "bearer"
