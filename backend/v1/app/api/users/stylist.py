from typing import List

from fastapi import APIRouter, Body

from backend.v1.app.api.models.user import StylistCreate, StylistPublic


router = APIRouter()


@router.post("/register", response_model=StylistPublic, tags=["stylists"])
async def register(
    new_user: StylistCreate = Body(..., embed=True)
):
    print(new_user)
    return StylistPublic(**new_user.dict())






