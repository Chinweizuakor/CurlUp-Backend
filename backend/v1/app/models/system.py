from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class HealthCheckBase(BaseModel):
    service: str = Field(..., description="The name of the service being checked")
    status: str = Field(..., description="The health status of the service (e.g. OK, FAIL)")
    timestamp: datetime = Field(..., description="Timestamp of the health check")
    response_time_ms: Optional[int] = Field(None, description="Time taken to get response in milliseconds")
    uptime_seconds: Optional[int] = Field(None, description="Service uptime in seconds")
    version: Optional[str] = Field(None, description="Version of the service/component")
    error_message: Optional[str] = Field(None, description="Error message if applicable")


class HealthCheckResponse(HealthCheckBase):
    url_pattern: Optional[str] = Field(None, description="Error message if applicable")




