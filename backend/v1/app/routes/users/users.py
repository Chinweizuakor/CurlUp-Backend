"""CurlUp Backend System Customer Routes."""

from fastapi import APIRouter, HTTPException, status

from backend.v1.app.models.users import UserCreate, UserLogin, UserPublic

router = APIRouter()


@router.post("/register", response_model=UserPublic, tags=["users"])
async def register(user: UserCreate) -> UserPublic:
    """Register a New User."""
    return UserPublic(**user.model_dump())


@router.post("/login", response_model=UserLogin, tags=["users"])
async def login(user: UserLogin) -> UserLogin:
    """
    Handles user login requests, supporting login via username or email.

    This endpoint accepts a UserLogin object in the request body.
    It returns the received user login details.

    Args:
        user (UserLogin): The UserLogin object containing username, email (optional),
                          and password from the request body.

    Returns:
        UserLogin: The received UserLogin object.
    """
    if user.username:
        print(f"Received login attempt for username: {user.username}")
    if user.email:
        print(f"Received login attempt for email: {user.email}")
    if user.username and user.email:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Login with either Username or Email. Not Both")
    if not user.username and not user.email:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Provide either the Username or Email to login.")
    return UserLogin(**user.model_dump(exclude_none=True))
