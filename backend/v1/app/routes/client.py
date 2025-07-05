"""CurlUp Backend System Client Routes."""

# from datetime import UTC, datetime

from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select

from backend.v1.app.auth.passwords import hash_password
from backend.v1.app.auth.tokens import create_verification_token
from backend.v1.app.database.operations import get_db
from backend.v1.app.models.client import ClientCreate, ClientRegisterResponse
from backend.v1.app.models.config import generate_client_id, generate_uuid
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
