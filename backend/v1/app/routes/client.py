"""CurlUp Backend System Client Routes."""

from fastapi import APIRouter, HTTPException, status

from backend.v1.app.models.client import ClientCreate, ClientLogin

router = APIRouter()


@router.post("/register", response_model=ClientCreate, tags=["Client"])
async def register(user: ClientCreate) -> ClientCreate:
    """Register a Client to the CurlUp Platform."""
    return ClientCreate(**user.model_dump())


@router.post("/login", response_model=ClientLogin, tags=["Client"])
async def login(user: ClientLogin) -> ClientLogin:
    """
    Handles user login requests, supporting login via username or email.

    This endpoint accepts a ClientLogin object in the request body.
    It returns the received user login details.

    Args:
        user (ClientLogin): The ClientLogin object containing username, email (optional),
                          and password from the request body.

    Returns:
        ClientLogin: The received ClientLogin object.
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
    return ClientLogin(**user.model_dump())
