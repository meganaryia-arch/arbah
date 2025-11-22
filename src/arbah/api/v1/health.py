"""
Health check and monitoring endpoints.
"""

import time
from typing import Dict, Any

from fastapi import APIRouter

from arbah.config import settings

router = APIRouter(prefix="/health", tags=["health"])


@router.get("/", summary="Health check")
async def health_check() -> Dict[str, Any]:
    """
    Basic health check endpoint.

    Returns the application status and basic information.
    """
    return {
        "status": "healthy",
        "timestamp": int(time.time()),
        "app_name": settings.app_name,
        "version": settings.app_version,
        "environment": settings.environment,
        "uptime": "healthy"
    }


@router.get("/detailed", summary="Detailed health check")
async def detailed_health_check() -> Dict[str, Any]:
    """
    Detailed health check with system information.

    Returns comprehensive health information including system resources.
    """
    import sys
    import platform
    from psutil import virtual_memory, cpu_percent

    return {
        "status": "healthy",
        "timestamp": int(time.time()),
        "app_name": settings.app_name,
        "version": settings.app_version,
        "environment": settings.environment,
        "system": {
            "platform": platform.platform(),
            "python_version": sys.version,
            "cpu_percent": cpu_percent(interval=1),
            "memory": {
                "total": virtual_memory().total,
                "available": virtual_memory().available,
                "percent": virtual_memory().percent
            }
        },
        "features": {
            "metrics_enabled": settings.enable_metrics,
            "docs_enabled": settings.enable_docs,
            "health_check_enabled": settings.enable_health_check
        }
    }


@router.get("/ping", summary="Ping endpoint")
async def ping() -> Dict[str, str]:
    """
    Simple ping endpoint for basic connectivity testing.
    """
    return {"ping": "pong"}