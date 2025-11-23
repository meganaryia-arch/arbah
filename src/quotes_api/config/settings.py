"""
Application settings and configuration.
"""

from typing import List

from pydantic_settings import BaseSettings


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
    cors_origins_raw: str = ""

    # Feature flags
    enable_metrics: bool = True
    enable_docs: bool = True
    enable_health_check: bool = True

    @property
    def cors_origins(self) -> List[str]:
        """Parse CORS origins from raw string."""
        v = self.cors_origins_raw.strip()
        if not v:
            return []

        # Handle JSON array format
        if v.startswith("["):
            try:
                import json
                return json.loads(v)
            except json.JSONDecodeError:
                pass

        # Handle comma-separated format
        return [origin.strip() for origin in v.split(",") if origin.strip()]

    def get_cors_origins(self) -> List[str]:
        """Get CORS origins with environment-specific additions."""
        origins = list(self.cors_origins)

        # Add development-specific origins if in debug mode
        if self.debug:
            dev_origins = [
                "http://localhost:5173",
                "http://127.0.0.1:5173",
                "http://localhost:3000",
                "http://127.0.0.1:3000"
            ]
            for origin in dev_origins:
                if origin not in origins:
                    origins.append(origin)

        return origins

    model_config = {
        "env_file": ".env",
        "case_sensitive": False
    }


# Create global settings instance
settings = Settings()