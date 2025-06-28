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
    All common characteristics of our users
    """

    first_name: str = Field(..., min_length=1)
    middle_name: str | None = Field(None, min_length=1)
    last_name: str = Field(..., min_length=1)
    email: EmailStr
    username: str = Field(..., min_length=1)
    gender: Gender
    date_of_birth: date
    mobile: str


class ClientCreate(ClientBase):
    """
    Attributes required to create a new resource - used at POST requests
    """

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
