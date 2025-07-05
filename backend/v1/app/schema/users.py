"""CurlUp Backend System Users Tables Schema."""

from datetime import datetime

from sqlmodel import Field, SQLModel


class Users(SQLModel, table=True):
    user_id: str = Field(nullable=False, primary_key=True)
    username: str = Field(max_length=25, nullable=False, unique=True)
    join_datetime : datetime = Field(nullable=False)
    last_password_update: datetime = Field(nullable=False)