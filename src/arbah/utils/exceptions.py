"""
Custom exceptions for Arbah Quotes API.
"""

from typing import Any, Dict, Optional


class ArbahException(Exception):
    """Base exception for all Arbah application errors."""

    def __init__(
        self,
        message: str,
        error_code: Optional[str] = None,
        details: Optional[Dict[str, Any]] = None
    ):
        """
        Initialize the exception.

        Args:
            message: Human-readable error message
            error_code: Machine-readable error code
            details: Additional error details
        """
        super().__init__(message)
        self.message = message
        self.error_code = error_code or self.__class__.__name__
        self.details = details or {}

    def to_dict(self) -> Dict[str, Any]:
        """Convert exception to dictionary representation."""
        return {
            "error": self.__class__.__name__,
            "error_code": self.error_code,
            "message": self.message,
            "details": self.details
        }


class QuoteNotFoundError(ArbahException):
    """Exception raised when a quote is not found."""

    def __init__(self, quote_id: Optional[int] = None, query: Optional[str] = None):
        """
        Initialize the exception.

        Args:
            quote_id: ID of the quote that wasn't found
            query: Search query that returned no results
        """
        if quote_id is not None:
            message = f"Quote with ID {quote_id} not found"
            details = {"quote_id": quote_id}
        elif query is not None:
            message = f"No quotes found matching query: {query}"
            details = {"query": query}
        else:
            message = "Quote not found"
            details = {}

        super().__init__(message, error_code="QUOTE_NOT_FOUND", details=details)


class ValidationError(ArbahException):
    """Exception raised for validation errors."""

    def __init__(self, message: str, field: Optional[str] = None, value: Any = None):
        """
        Initialize the exception.

        Args:
            message: Validation error message
            field: Name of the field that failed validation
            value: The invalid value
        """
        details = {}
        if field is not None:
            details["field"] = field
        if value is not None:
            details["value"] = str(value)

        super().__init__(message, error_code="VALIDATION_ERROR", details=details)


class ConfigurationError(ArbahException):
    """Exception raised for configuration errors."""

    def __init__(self, message: str, config_key: Optional[str] = None):
        """
        Initialize the exception.

        Args:
            message: Configuration error message
            config_key: The configuration key that caused the error
        """
        details = {}
        if config_key is not None:
            details["config_key"] = config_key

        super().__init__(message, error_code="CONFIGURATION_ERROR", details=details)


class ServiceUnavailableError(ArbahException):
    """Exception raised when external services are unavailable."""

    def __init__(self, service_name: str, details: Optional[Dict[str, Any]] = None):
        """
        Initialize the exception.

        Args:
            service_name: Name of the unavailable service
            details: Additional error details
        """
        message = f"Service {service_name} is currently unavailable"
        error_details = {"service_name": service_name}
        if details:
            error_details.update(details)

        super().__init__(message, error_code="SERVICE_UNAVAILABLE", details=error_details)


class RateLimitExceededError(ArbahException):
    """Exception raised when rate limits are exceeded."""

    def __init__(self, limit: int, window: int, reset_time: int):
        """
        Initialize the exception.

        Args:
            limit: Number of requests allowed
            window: Time window in seconds
            reset_time: Unix timestamp when the limit resets
        """
        message = f"Rate limit exceeded: {limit} requests per {window} seconds"
        details = {
            "limit": limit,
            "window": window,
            "reset_time": reset_time
        }

        super().__init__(message, error_code="RATE_LIMIT_EXCEEDED", details=details)