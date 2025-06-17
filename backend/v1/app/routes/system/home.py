"""CurlUp Home Endpoint"""

from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def home():
    """Home Endpoint."""
    return {"message": "Welcome to the CurlUp API"}
