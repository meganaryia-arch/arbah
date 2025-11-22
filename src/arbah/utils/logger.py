"""
Logging configuration and utilities.
"""

import logging
import sys
from typing import Any, Dict

import structlog
from structlog.stdlib import LoggerFactory

from arbah.config import settings


def setup_logging() -> None:
    """Configure structured logging for the application."""
    # Configure structlog
    structlog.configure(
        processors=[
            structlog.stdlib.filter_by_level,
            structlog.stdlib.add_logger_name,
            structlog.stdlib.add_log_level,
            structlog.stdlib.PositionalArgumentsFormatter(),
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.processors.StackInfoRenderer(),
            structlog.processors.format_exc_info,
            structlog.processors.UnicodeDecoder(),
            structlog.processors.JSONRenderer() if settings.log_format == "json"
            else structlog.dev.ConsoleRenderer(),
        ],
        context_class=dict,
        logger_factory=LoggerFactory(),
        wrapper_class=structlog.stdlib.BoundLogger,
        cache_logger_on_first_use=True,
    )

    # Configure standard library logging
    logging.basicConfig(
        format="%(message)s",
        stream=sys.stdout,
        level=getattr(logging, settings.log_level.upper()),
    )


def get_logger(name: str) -> structlog.stdlib.BoundLogger:
    """
    Get a configured logger instance.

    Args:
        name: Logger name (typically __name__)

    Returns:
        Configured bound logger
    """
    return structlog.get_logger(name)


class LoggerMixin:
    """Mixin class to add logging capabilities to other classes."""

    @property
    def logger(self) -> structlog.stdlib.BoundLogger:
        """Get logger for this class."""
        return get_logger(self.__class__.__module__ + "." + self.__class__.__name__)


def log_request_response(
    logger: structlog.stdlib.BoundLogger,
    method: str,
    path: str,
    status_code: int = None,
    duration: float = None,
    **kwargs: Any
) -> None:
    """
    Log HTTP request/response information.

    Args:
        logger: Logger instance
        method: HTTP method
        path: Request path
        status_code: Response status code (optional)
        duration: Request duration in seconds (optional)
        **kwargs: Additional log fields
    """
    log_data: Dict[str, Any] = {
        "method": method,
        "path": path,
        **kwargs
    }

    if status_code is not None:
        log_data["status_code"] = status_code

    if duration is not None:
        log_data["duration_ms"] = round(duration * 1000, 2)

    if status_code and status_code >= 400:
        logger.error("HTTP request error", **log_data)
    else:
        logger.info("HTTP request", **log_data)