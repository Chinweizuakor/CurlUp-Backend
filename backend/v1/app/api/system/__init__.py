from fastapi import APIRouter

from backend.v1.app.api.system.health_check import router as health_router


router = APIRouter()

router.include_router(health_router, tags=["Health Check"])