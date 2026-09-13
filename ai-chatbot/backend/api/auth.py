from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
)
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from models.user import User

from api.dependencies import get_current_user
from core.security import create_access_token
from db.database import get_db
from schemas.auth import (
    RegisterRequest,
    TokenResponse,
    UserResponse,
)
from services.auth_service import (
    authenticate_user,
    create_user,
    get_user_by_email,
)


router = APIRouter(
    prefix="/api/auth",
    tags=["Authentication"],
)


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)
def register(
    request: RegisterRequest,
    db: Session = Depends(get_db),
):
    existing_user = get_user_by_email(
        db,
        request.email,
    )

    if existing_user:
        raise HTTPException(
            status_code=409,
            detail="Email already registered",
        )

    user = create_user(
        db=db,
        email=request.email,
        name=request.name,
        password=request.password,
    )

    return UserResponse(
        id=user.id,
        name=user.name,
        email=user.email,
    )


@router.post(
    "/login",
    response_model=TokenResponse,
)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    user = authenticate_user(
        db=db,
        email=form_data.username,
        password=form_data.password,
    )

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password",
        )

    return TokenResponse(
        access_token=create_access_token(
            user.id
        ),
    )

@router.get(
"/me",
response_model=UserResponse,
)

def get_me(
    user: User = Depends(get_current_user),
):
    return UserResponse(
        id=user.id,
        name=user.name,
        email=user.email,
    )