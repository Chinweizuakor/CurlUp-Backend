"""CurlUp Backend System Client Routes."""

# from datetime import UTC, datetime
from fastapi import APIRouter, Depends, HTTPException, status
from jose import jwt
from jwt import ExpiredSignatureError, InvalidTokenError
from sqlmodel import Session, select

from backend.v1.app.auth.config import ALGORITHM, SECRET_KEY
from backend.v1.app.auth.passwords import hash_password
from backend.v1.app.auth.tokens import create_verification_token
from backend.v1.app.database.operations import get_db
from backend.v1.app.models.client import ClientCreate, ClientRegisterResponse, ClientVerifyResponse
from backend.v1.app.models.generate import generate_client_id, generate_uuid
from backend.v1.app.schema.client import Client

router = APIRouter()


@router.post("/register", response_model=ClientRegisterResponse)
async def register(client: ClientCreate,
                   db: Session = Depends(get_db)) -> ClientRegisterResponse: # noqa: B008
    """
    Registers a new client by creating an entry in the database.

    Checks for existing username or email to prevent duplicate registrations.
    
    Upon successful registration, a verification token is generated,
    and a verification email is sent to the client for verification.
    """
    statement = select(Client).where(
        (Client.username == client.username) | (Client.email == client.email)
    )
    existing_client = db.exec(statement).first()
    if existing_client:
        if existing_client.username == client.username:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Username already exists"
            )
        if existing_client.email == client.email:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already exists"
            )
    password_hash = hash_password(client.password)
    
    # Generate IDs for New User
    new_id = generate_uuid() 
    new_user_id = generate_client_id()

    # Create Client Record in Client Table
    new_client = Client(
        id=new_id,
        user_id=new_user_id,
        first_name=client.first_name,
        middle_name=client.middle_name,
        last_name=client.last_name,
        email=client.email,
        username=client.username.lower(),
        gender=client.gender,
        date_of_birth=client.date_of_birth,
        phone_number=client.phone_number,
        address_1=client.address_1,
        address_2=client.address_2,
        city=client.city,
        state=client.state,
        zip_code=client.zip_code,
        country=client.country,
        password_hash=password_hash,
        is_verified=False
    )

    # # Create Client Record in Users Table
    # new_user = Users(
    #     user_id=new_user_id,
    #     username=client.username.lower(),
    #     join_datetime=datetime.now(UTC),
    #     last_password_update=datetime.now(UTC)
    # )

    # Save to database
    db.add(new_client)   
    # db.add(new_user)

    db.commit()
    
    db.refresh(new_client)
    # db.refresh(new_user)

    # Generate verification token
    token = create_verification_token(client.email)

    # await send_verification_email(client.email, token)

    response = {
        "message": "Registration successful. Please check your email for verification.",
        "email": client.email,
        "token": token
    }
    return ClientRegisterResponse(**response)


@router.get("/verify/{token}", response_model=ClientVerifyResponse)
async def verify_email(token: str,
                db: Session = Depends(get_db)) -> ClientVerifyResponse: # noqa: B008
    """
    Verifies a client's email address using a JWT token sent to the email provided for
    verification.

    This endpoint is typically hit when a user clicks a verification link sent to their email.

    The token is decoded to extract the client's email, and the corresponding client record
    in the database is updated to set `is_verified` to `True`.

    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str | None = payload.get("sub")
        if email is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid token"
            )
    except ExpiredSignatureError as err:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=(
                "Token has expired. Please request a new verification email."
            )
        ) from err

    except InvalidTokenError as err:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid token"
        ) from err

    statement = select(Client).where(Client.email == email)
    client = db.exec(statement).first()

    if not client:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Client not found"
        )

    if client.is_verified:
        response = {"message": "Email already verified"}
        return ClientVerifyResponse(**response)

    # Mark client as verified
    client.is_verified = True
    db.add(client)
    db.commit()

    response = {"message": "Email verified successfully"}

    return ClientVerifyResponse(**response)
