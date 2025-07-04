"""CurlUp Backend System Vendor Models."""

import re
from enum import Enum
from typing import Self

from pydantic import BaseModel, EmailStr, Field, field_validator, model_validator
from pydantic_core.core_schema import ValidationInfo


class BusinessType(Enum):
    SINGLE_OWNER = "Single Owner"
    PARTNERSHIP = "Partnership"
    LLC = "Limited Liability Company"


class VendorBase(BaseModel):
    """All Common Characterists of CurlUp Vendors."""

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


class VendorCreate(VendorBase):
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


class VendorPublic(VendorBase):
    pass


# class BusinessCreate(ClientBase):
#     "attributes required to create a new resource - used at POST requests"
#     password: constr(min_length=7, max_length=100)
#     username: constr(min_length=3, max_length=20)
#
#     # @validator("username", pre=True)
#     def username_is_valid(cls, username: str) -> str:
#         return validate_username(username)


class VendorLogin(BaseModel):
    email: EmailStr
    password: str


