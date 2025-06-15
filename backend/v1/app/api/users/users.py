from typing import List

from fastapi import APIRouter, Body

from backend.v1.app.api.models.user import UserCreate, UserPublic, UserInDB


router = APIRouter()


@router.post("/register", response_model=UserPublic, tags=["users"])
async def register(
        new_user: UserCreate = Body(..., embed=True)
):
    return UserPublic(**new_user.dict())


@router.post("/login", response_model=UserInDB, tags=["users"])
async def register(
        user: UserInDB = Body(..., embed=True)
):
    print(user.dict())
    return UserInDB(**new_user.dict())







