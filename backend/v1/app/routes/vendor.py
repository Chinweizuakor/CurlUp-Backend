"""CurlUp Backend System Vendor Routes."""

from fastapi import APIRouter

from backend.v1.app.models.client import StylistCreate, StylistPublic

router = APIRouter()


@router.post("/register", response_model=StylistPublic, tags=["Vendor"])
async def register(new_user: StylistCreate) -> StylistPublic:
    return StylistPublic(**new_user.model_dump())
