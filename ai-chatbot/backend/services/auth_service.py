from sqlalchemy import select
from sqlalchemy.orm import Session

from models.user import User
from core.security import (
    hash_password,
    verify_password,
)


def get_user_by_email(
    db: Session,
    email: str,
):
    return db.scalar(
        select(User).where(
            User.email == email.lower()
        )
    )


def create_user(
    db: Session,
    email: str,
    name: str,
    password: str,
):
    user = User(
        email=email.lower(),
        name=name.strip(),
        hashed_password=hash_password(password),
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def authenticate_user(
    db: Session,
    email: str,
    password: str,
):
    user = get_user_by_email(
        db,
        email,
    )

    if not user:
        return None

    if not verify_password(
        password,
        user.hashed_password,
    ):
        return None

    return user