"""CurlUp Backend System Vendor Routes."""

from fastapi import APIRouter

from backend.v1.app.models.vendor import VendorCreate, VendorPublic

router = APIRouter()


@router.post("/register", response_model=VendorPublic, tags=["Vendor"])
async def register(new_user: VendorCreate) -> VendorPublic:
    return VendorPublic(**new_user.model_dump())
