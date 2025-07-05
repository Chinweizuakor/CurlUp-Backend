"""CurlUp Token Module."""

from datetime import UTC, datetime, timedelta

from jose import jwt as jose_jwt

from backend.v1.app.auth.config import (
    ALGORITHM,
    SECRET_KEY,
    VERIFICATION_TOKEN_EXPIRE_MINUTES,
)


def create_verification_token(email: str) -> str:
    """Generate a JWT token for email verification."""
    expire = datetime.now(UTC) + timedelta(minutes=VERIFICATION_TOKEN_EXPIRE_MINUTES)
    to_encode = {"sub": email, "exp": expire}
    return jose_jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
