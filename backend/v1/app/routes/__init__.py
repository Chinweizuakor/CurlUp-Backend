from fastapi import APIRouter

from backend.v1.app.routes.users import router as user_router
from backend.v1.app.routes.system import router as system_router


router = APIRouter()


router.include_router(system_router)
router.include_router(user_router)
