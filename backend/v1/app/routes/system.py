"""CurlUp Backend System System Routes."""

from fastapi import APIRouter

from backend.v1.app.models.system import HealthCheckResponse

router = APIRouter()

response = {
    "service": "Database",
    "status": "OK",
    "timestamp": "2025-06-14T12:34:56Z",
    "response_time_ms": 123,
    "uptime_seconds": 987654,
    "version": "12.5",
    "error_message": None,
}


@router.get("/", tags=["System"])
async def home():
    """CurlUp Home Endpoint"""
    return {"message": "Welcome to the CurlUp API"}


@router.get("/health-check/database", response_model=HealthCheckResponse,
            tags=["System"])
async def health_check():
    return HealthCheckResponse(**response)


@router.get("/health-check/database/kunle/{version}", tags=["System"])
async def health_check_1(state1: str, state2: str, database_name: str, version: str):
    return {"name": "Kunle"}


@router.get("/health-check/database/{database_name}/{version}", tags=["System"])
async def health_check_2(state1: str, state2: str, database_name: str, version: str):
    return {
        "system": "My Web App",
        "timestamp": "2025-06-14T16:40:10.654321",
        "database": {
            "name": f"{database_name}",
            "status": f"{state1} {state2}",
            "response_time_ms": 120,
            "uptime_seconds": 123456,
            "version": "PostgreSQL 15.2",
            "error_message": None,
        },
        "cache": {
            "name": "Redis Cache",
            "status": "OK",
            "response_time_ms": 15,
            "uptime_seconds": None,
            "version": f"{version}",
            "error_message": None,
        },
        "storage": None,
    }
