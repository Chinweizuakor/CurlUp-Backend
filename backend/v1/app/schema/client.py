"""CurlUp Backend Client Tables Schemas."""

from datetime import date

from sqlmodel import Column, Field, SQLModel
from sqlmodel import Enum as SQLModelEnum

from backend.v1.app.models.client import Gender


class Client(SQLModel, table=True):
    id: str = Field(unique=True, nullable=False, primary_key=True)
    user_id: str = Field(unique=True, nullable=False)
    first_name: str = Field(max_length=25, nullable=False)
    middle_name: str | None = Field(default=None, max_length=25)
    last_name: str = Field(max_length=25, nullable=False)
    email: str = Field(nullable=False, unique=True)
    username: str = Field(max_length=25, nullable=False, unique=True)
    gender: Gender = Field(
        sa_column=Column(SQLModelEnum(Gender), nullable=False)
    )
    date_of_birth: date = Field(nullable=False)
    phone_number: str = Field(max_length=20, nullable=False)
    address_1: str = Field(max_length=50, nullable=False)
    address_2: str | None = Field(default=None, max_length=50)
    city: str | None = Field(default=None)
    state: str | None = Field(default=None)
    zip_code: str | None = Field(default=None, max_length=5)
    country: str | None = Field(default="USA")
    password_hash: str = Field(nullable=False)
    is_verified: bool = Field(default=False)
