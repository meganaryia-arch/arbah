"""
Application settings and configuration.
"""

import os
from typing import List, Optional

from pydantic import AnyHttpUrl, BaseSettings, validator


class Settings(BaseSettings):
    """Application settings."""

    # Application
    app_name: str = "Arbah Quotes API"
    app_version: str = "0.1.0"
    debug: bool = False
    environment: str = "development"

    # Server
    host: str = "0.0.0.0"
    port: int = 8000

    # Logging
    log_level: str = "INFO"
    log_format: str = "json"

    # API
    api_v1_prefix: str = "/api/v1"
    cors_origins: List[AnyHttpUrl] = []

    # Feature flags
    enable_metrics: bool = True
    enable_docs: bool = True
    enable_health_check: bool = True

    @validator("cors_origins", pre=True)
    def assemble_cors_origins(cls, v: str | List[str]) -> List[str]:
        """Parse CORS origins from string or list."""
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    class Config:
        """Pydantic config."""
        env_file = ".env"
        case_sensitive = False


# Create global settings instance
settings = Settings()