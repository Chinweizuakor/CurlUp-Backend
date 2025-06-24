"""CurlUp Backend System User Models."""

import re
from datetime import date
from enum import Enum
from typing import Self

from pydantic import BaseModel, EmailStr, Field, field_validator, model_validator
from pydantic_core.core_schema import ValidationInfo


class BusinessType(Enum):
    SINGLE_OWNER = "Single Owner"
    PARTNERSHIP = "Partnership"
    LLC = "Limited Liability Company"


class Gender(Enum):
    MALE = "Male"
    FEMALE = "Female"


class Timezone(Enum):
    UTC = "UTC"
    GMT = "GMT"
    EAT = "EAT"
    CAT = "CAT"
    WAT = "WAT"
    EET = "EET"
    CET = "CET"
    AEST = "AEST"
    EST = "EST"
    PST = "PST"
    CST = "CST"
    MST = "MST"


class UserBase(BaseModel):
    """
    All common characteristics of our users
    """

    first_name: str = Field(..., min_length=1)
    middle_name: str | None = Field(None, min_length=1)
    last_name: str = Field(..., min_length=1)
    email: EmailStr
    username: str = Field(..., min_length=1)
    gender: Gender
    dateofbirth: date
    timezone: Timezone | None = None
    mobile: str


class UserCreate(UserBase):
    """
    Attributes required to create a new resource - used at POST requests
    """

    password: str = Field(min_length=8, max_length=25)
    confirm_password: str = Field(min_length=8, max_length=25)

    @field_validator("password")
    @classmethod
    def validate_password(cls, v: str, info: ValidationInfo) -> str:
        # Regex: At least one uppercase, one lowercase, one digit, one special character
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


class UserStatus(UserBase):
    is_active: bool = True
    is_superuser: bool = False


class StylistBase(BaseModel):
    """All Common Characterists of Our Stylists."""

    business_name: str = Field(min_length=8, max_length=25)
    business_type: BusinessType
    business_email: EmailStr
    business_address_1: str
    business_address_2: str | None = None
    business_city: str
    business_state: str
    business_country: str
    business_zip: str | None
    mobile: str
    business_registration_number: str


class StylistCreate(StylistBase):
    """
    Attributes required to create a new resource - used at POST requests
    """

    password: str = Field(min_length=8, max_length=25)
    confirm_password: str = Field(min_length=8, max_length=25)

    @field_validator("password")
    @classmethod
    def validate_password(cls, v: str, info: ValidationInfo) -> str:
        import re

        # Regex: At least one uppercase, one lowercase, one digit, one special character
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


class UserPublic(UserBase):
    pass


class StylistPublic(StylistBase):
    pass


# class BusinessCreate(UserBase):
#     "attributes required to create a new resource - used at POST requests"
#     password: constr(min_length=7, max_length=100)
#     username: constr(min_length=3, max_length=20)
#
#     # @validator("username", pre=True)
#     def username_is_valid(cls, username: str) -> str:
#         return validate_username(username)


class StylistLogin(BaseModel):
    email: EmailStr
    password: str


class UserLogin(BaseModel):
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
        if (username is not None and email is not None) or (username is None and email is None):
            raise ValueError("Exactly one of username or email must be provided")
        return data
