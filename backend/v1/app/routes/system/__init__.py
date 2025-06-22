from fastapi import APIRouter

from backend.v1.app.routes.system.health_check import router as health_router
from backend.v1.app.routes.system.home import router as home_router

router = APIRouter()

router.include_router(home_router, tags=["Home"])
router.include_router(health_router, tags=["Health Check"])
