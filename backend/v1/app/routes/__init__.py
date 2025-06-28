"""CurlUp Backend System Routes."""

from fastapi import APIRouter

from backend.v1.app.routes.client import router as client_router
from backend.v1.app.routes.system import router as system_router
from backend.v1.app.routes.vendor import router as vendor_router

router = APIRouter()

router.include_router(client_router)
router.include_router(system_router)
router.include_router(vendor_router)
