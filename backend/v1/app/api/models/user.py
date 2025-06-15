from typing import Optional

from pydantic import BaseModel
from pydantic import constr


class UserBase(BaseModel):
    """
    All common characteristics of our users
    """
    first_name: str
    last_name: str
    email: str
    phone_number: Optional[str]
    is_active: bool = True
    is_superuser: bool = False



class UserCreate(UserBase):
    "attributes required to create a new resource - used at POST requests"
    password: constr(min_length=7, max_length=100)
    username: constr(min_length=3, max_length=20)


class StylistCreate(UserBase):
    "attributes required to create a new resource - used at POST requests"
    password: constr(min_length=7, max_length=100)
    username: constr(min_length=3, max_length=20)
    certificate: str


class UserPublic(UserBase):
    pass

class StylistPublic(UserBase):
    pass

# class BusinessCreate(UserBase):
#     "attributes required to create a new resource - used at POST requests"
#     password: constr(min_length=7, max_length=100)
#     username: constr(min_length=3, max_length=20)
#
#     # @validator("username", pre=True)
#     def username_is_valid(cls, username: str) -> str:
#         return validate_username(username)