"""Service layer for user authentication and account management."""

from sqlalchemy import select
from sqlalchemy.orm import Session

from core.security import hash_password, verify_password
from models.user import User


def get_user_by_email(
    db: Session,
    email: str,
):
    """Return the user with the given email address, or None if not found."""
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
    """Create, persist, and return a new user account."""
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
    """Verify credentials and return the user, or None if invalid."""
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
