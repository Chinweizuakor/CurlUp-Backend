"""CurlUp Backend System Customer Routes."""

from fastapi import APIRouter

from backend.v1.app.models.users import (
    UserCreate,
    UserPublic,
)

router = APIRouter()


@router.post("/register", response_model=UserPublic, tags=["users"])
async def register(user: UserCreate) -> UserPublic:
    """Register a New User on the CurlUp Website."""
    return UserPublic(**user.dict())
