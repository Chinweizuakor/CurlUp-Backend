from typing import List

from fastapi import APIRouter, Body

from backend.v1.app.api.models.user import UserCreate, UserPublic, UserInDB


router = APIRouter()


@router.post("/register", response_model=UserPublic, tags=["users"])
async def register(
        new_user: UserCreate = Body(..., embed=True)
):
    return UserPublic(**new_user.dict())


@router.post("/login", tags=["users"])
async def register(
        user
):
    print(user)
    return user







