"""CurlUp Backend System Database Operations Module."""

import os
from contextlib import asynccontextmanager

from fastapi import FastAPI
from sqlalchemy.exc import OperationalError
from sqlmodel import Session, SQLModel, create_engine

DATABASE_URL = os.getenv("DATABASE_URL")
if DATABASE_URL is None:
    raise ValueError("DATABASE_URL environment variable is not set.")

engine = create_engine(url=DATABASE_URL, echo=True)


def init_db():
    """Initialize the database by creating all tables."""
    try:
        SQLModel.metadata.create_all(engine)
    except OperationalError as e:
        raise Exception(f"Failed to connect to database: {e}") from e


def get_db():
    """
    Dependency to provide a database session.
    Used in operations involving the database e.g login/register
    """
    with Session(engine) as session:
        yield session


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Asynchronous context manager for FastAPI application lifespan events.

    This function initializes the database connection when the FastAPI application starts
    and performs any necessary cleanup when the application shuts down.

    Args:
        app (FastAPI): The FastAPI application instance.

    Yields:
        None: Control is yielded back to the FastAPI application after initialization.
    """
    init_db()
    yield
