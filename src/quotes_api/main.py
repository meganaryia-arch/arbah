"""
Main FastAPI application entry point.
"""

import time
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from quotes_api.api.v1 import router as v1_router
from quotes_api.config import settings
from quotes_api.utils import setup_logging
from quotes_api.utils.exceptions import QuotesAPIException
from quotes_api.utils.logger import get_logger, log_request_response

# Setup logging
setup_logging()
logger = get_logger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan manager."""
    logger.info("Starting Quotes API", version=settings.app_version)

    # Startup
    logger.info("Application started successfully")
    yield

    # Shutdown
    logger.info("Shutting down Quotes API")


# Create FastAPI application
app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="A simple FastAPI application for serving inspirational quotes",
    docs_url="/docs" if settings.enable_docs else None,
    redoc_url="/redoc" if settings.enable_docs else None,
    openapi_url="/openapi.json" if settings.enable_docs else None,
    lifespan=lifespan,
)

# Add CORS middleware
if settings.cors_origins:
    # Convert URL objects to strings and handle trailing slashes
    allowed_origins = [str(origin).rstrip('/') for origin in settings.cors_origins]
    # For development, also allow common local ports
    allowed_origins.extend([
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ])

    app.add_middleware(
        CORSMiddleware,
        allow_origins=allowed_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


# Request logging middleware
@app.middleware("http")
async def log_requests(request: Request, call_next):
    """Log HTTP requests and responses."""
    start_time = time.time()

    response = await call_next(request)

    process_time = time.time() - start_time
    log_request_response(
        logger=logger,
        method=request.method,
        path=request.url.path,
        status_code=response.status_code,
        duration=process_time,
        user_agent=request.headers.get("user-agent"),
        remote_addr=request.client.host if request.client else None,
    )

    # Add processing time header
    response.headers["X-Process-Time"] = str(process_time)

    return response


# Exception handlers
@app.exception_handler(QuotesAPIException)
async def quotes_api_exception_handler(request: Request, exc: QuotesAPIException):
    """Handle custom Quotes API exceptions."""
    logger.error("Application error", exc_info=exc, **exc.to_dict())
    return JSONResponse(
        status_code=400,
        content={
            "success": False,
            "error": exc.to_dict(),
            "message": exc.message
        }
    )


@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    """Handle unexpected exceptions."""
    logger.error("Unexpected error", exc_info=exc)
    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "error": "INTERNAL_SERVER_ERROR",
            "message": "An unexpected error occurred"
        }
    )


# Include API routes
app.include_router(v1_router, prefix=settings.api_v1_prefix)


# Root endpoint
@app.get("/", tags=["root"])
async def root():
    """Root endpoint with basic API information."""
    return {
        "message": "Welcome to Quotes API",
        "version": settings.app_version,
        "docs": "/docs" if settings.enable_docs else None,
        "health": f"{settings.api_v1_prefix}/health",
        "quotes": f"{settings.api_v1_prefix}/quotes"
    }


if __name__ == "__main__":
    import uvicorn

    logger.info(
        "Starting server",
        host=settings.host,
        port=settings.port,
        debug=settings.debug
    )

    uvicorn.run(
        "quotes_api.main:app",
        host=settings.host,
        port=settings.port,
        reload=settings.debug,
        log_level=settings.log_level.lower(),
    )