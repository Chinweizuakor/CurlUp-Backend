"""CurlUp Backend System Customer Routes."""

from fastapi import APIRouter

from backend.v1.app.models.users import UserCreate, UserLoginEmail, UserLoginUsername, UserPublic

router = APIRouter()


@router.post("/register", response_model=UserPublic, tags=["users"])
async def register(new_user: UserCreate) -> UserPublic:
    """Register a New User on the CurlUp Website."""
    return UserPublic(**new_user.dict())


@router.post("/username/login", tags=["users"])
async def login_email(user: UserLoginEmail) -> UserLoginEmail:
    """User Login via Email into Account on the CurlUp Website"""
    return UserLoginEmail(**user.dict())


@router.post("/email/login", tags=["users"])
async def login_username(user: UserLoginUsername) -> UserLoginUsername:
    """User Login via Username into Account on the CurlUp Website"""
    return UserLoginUsername(**user.dict())
