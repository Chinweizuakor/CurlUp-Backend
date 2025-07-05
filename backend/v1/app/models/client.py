"""CurlUp Backend System Client Models."""

import re
from datetime import date
from enum import Enum
from typing import Self

from pydantic import BaseModel, EmailStr, Field, field_validator, model_validator
from pydantic_core.core_schema import ValidationInfo


class Gender(Enum):
    MALE = "Male"
    FEMALE = "Female"


class ClientBase(BaseModel):
    """
    Model to Validate the common characteristics of clients who
    use the CurlUp website for services.    
    """
    first_name: str = Field(
        ..., 
        min_length=1,
        max_length=25,
        description="The client's first or given name. This field is required."
    )
    middle_name: str | None = Field(
        None,
        min_length=1,
        max_length=25,
        description="The client's middle name. This field is optional."
    )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=25,
        description="The client's last name. This field is required."
    )
    email: EmailStr = Field(
        ...,
        description="The client's primary email address. It must be a valid email format."
    )
    username: str = Field(
        ...,
        min_length=1,
        max_length=25,
        description="A unique username for the client to log in. This field is required."
    )
    gender: Gender = Field(
        ...,
        description="The client's gender, selected from a predefined list of options."
    )
    date_of_birth: date = Field(
        ...,
        description="The client's date of birth in YYYY-MM-DD format. This field is required."
    )
    phone_number: str = Field(
        ...,
        min_length=7,
        max_length=20,
        description=(
            "The client's mobile phone number, including country code if applicable. "
            "Must be between 7 and 20 characters long."
        )
    )
    address_1: str = Field(
        ...,
        min_length=1,
        max_length=50,
        description=(
            "The first line of the client's street address. "
            "This field is required for a complete address."
        )
    )
    address_2: str | None = Field(
        None,
        min_length=1,
        max_length=50,
        description=(
            "The second line of the client's street address, such as an apartment or suite number. "
            "This field is optional."
        )
    )
    city: str | None = Field(
        None,
        description=(
            "The city of the client's address. "
            "This field is optional for a complete address."
        )
    )
    state: str | None = Field(
        None,
        description=(
            "The state, province, or region of the client's address. "
            "This field is optional for a complete address."
        )
    )
    country: str | None = Field(
        None,
        description=(
            "The country of the client's address. "
            "This field is optional for a complete address."
        )
    )
    zip_code: str | None = Field(
        None,
        max_length=5,
        description=(
            "The client's postal or ZIP code. Must be a maximum of 5 characters long. "
            "This field is optional for a complete address."
        )
    )

    @field_validator("phone_number")
    @classmethod
    def validate_mobile_format(cls, v: str, info: ValidationInfo) -> str:
        """
        This function uses regular expression framework in validating
        the format of the mobile number using a regular expression.
        """
        pattern = r'^\+?[\d\s\-\(\)]+$'
        if not re.match(pattern, v):
            raise ValueError(
                'Invalid phone number format. Must contain only digits, spaces, dashes, or '
                'parentheses, and can start with a "+".'
            )
        return v
    
    @field_validator("username")
    @classmethod
    def lowercase_username(cls, v: str) -> str:
        return v.lower()


class ClientCreate(ClientBase):
    """Attributes required to create a Client Account."""
    password: str = Field(min_length=8, max_length=25)
    confirm_password: str = Field(min_length=8, max_length=25)

    @field_validator("password")
    @classmethod
    def validate_password(cls, v: str, info: ValidationInfo) -> str:
        """
        This function uses regular expression framework in verifying the password.
        
        The password must satisfy the following conditions:
        - at least one uppercase.
        - at least one lowercase
        - at least one digit
        - at least one special character
        """
        pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*()_+\-=\[\]{};:'\",.<>?]).{8,25}$"
        if not re.match(pattern, v):
            raise ValueError(
                "Password must contain at least one uppercase letter, one lowercase letter, "
                "one number, and one special character (!@#$%^&*()_+-=[]{};:'\",.<>?)"
            )
        return v

    @model_validator(mode="after")
    def check_passwords_match(self) -> Self:
        if self.password != self.confirm_password:
            raise ValueError("Passwords do not match")
        return self


class ClientRegisterResponse(BaseModel):
    """
    Schema for client registration responses.
    Contains a message, email and token.
    """
    message: str
    email: EmailStr
    token: str


class ClientVerifyResponse(BaseModel):
    message: str


class ClientStatus(ClientBase):
    is_active: bool = True
    is_superuser: bool = False


class ClientLogin(BaseModel):
    """
    Pydantic model for user login credentials.
    - username: An optional string representing the user's username.
    - email: An optional email string representing the user's email address.
              At least one of username or email should be provided.
    - password: A string representing the user's password.
    """
    username: str | None = None 
    email: EmailStr | None = None
    password: str

    @model_validator(mode="before")
    @classmethod
    def ensure_exactly_one_identifier(cls, data: dict) -> dict:
        username = data.get("username")
        email = data.get("email")
        if (username is not None and email is not None):
            raise ValueError("Exactly one of username or email must be provided")
        if (username is None and email is None):
            raise ValueError("Please provide a username or an email")
        return data

