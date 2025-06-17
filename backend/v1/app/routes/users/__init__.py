from fastapi import APIRouter

from backend.v1.app.routes.users.users import router as user_router
from backend.v1.app.routes.users.stylist import router as stylist_router


router = APIRouter()

router.include_router(user_router, prefix="/users")
router.include_router(stylist_router, prefix="/stylist")
