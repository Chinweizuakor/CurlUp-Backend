"""CurlUp Backend System Stylist Routes."""

from fastapi import APIRouter

from backend.v1.app.models.users import StylistCreate, StylistPublic

router = APIRouter()


@router.post("/register", response_model=StylistPublic, tags=["stylists"])
async def register(new_user: StylistCreate) -> StylistPublic:
    return StylistPublic(**new_user.dict())
