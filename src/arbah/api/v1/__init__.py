"""
API v1 routes.
"""

from .quotes import router as quotes_router
from .health import router as health_router
from .meta import router as meta_router

# Create main v1 router
from fastapi import APIRouter

router = APIRouter(prefix="/v1", tags=["v1"])

# Include sub-routers
router.include_router(quotes_router, tags=["quotes"])
router.include_router(health_router, tags=["health"])
router.include_router(meta_router, tags=["meta"])

__all__ = ["router", "quotes_router", "health_router", "meta_router"]