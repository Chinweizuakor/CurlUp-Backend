from datetime import datetime

from pydantic import BaseModel, Field


class HealthCheckBase(BaseModel):
    service: str = Field(..., description="The name of the service being checked")
    status: str = Field(..., description="The health status of the service (e.g. OK, FAIL)")
    timestamp: datetime = Field(..., description="Timestamp of the health check")
    response_time_ms: int | None = Field(
        None, description="Time taken to get response in milliseconds"
    )
    uptime_seconds: int | None = Field(None, description="Service uptime in seconds")
    version: str | None = Field(None, description="Version of the service/component")
    error_message: str | None = Field(None, description="Error message if applicable")


class HealthCheckResponse(HealthCheckBase):
    url_pattern: str | None = Field(None, description="Error message if applicable")
