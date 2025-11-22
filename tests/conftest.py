"""
Pytest configuration and shared fixtures.
"""

import pytest
import asyncio
from typing import AsyncGenerator, Generator

from fastapi.testclient import TestClient
from httpx import AsyncClient

from arbah.main import app


@pytest.fixture(scope="session")
def event_loop() -> Generator:
    """Create an instance of the default event loop for the test session."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture
def client() -> TestClient:
    """Create a test client for the FastAPI application."""
    return TestClient(app)


@pytest.fixture
async def async_client() -> AsyncGenerator[AsyncClient, None]:
    """Create an async test client for the FastAPI application."""
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac


@pytest.fixture
def sample_quotes_data():
    """Sample quotes data for testing."""
    return [
        {
            "id": 1,
            "text": "La vie est une fleur dont l'amour est le miel.",
            "author": "Victor Hugo",
            "category": "Amour",
            "language": "fr"
        },
        {
            "id": 2,
            "text": "Le succès n'est pas la clé du bonheur.",
            "author": "Albert Schweitzer",
            "category": "Succès",
            "language": "fr"
        }
    ]


@pytest.fixture
def mock_settings():
    """Mock settings for testing."""
    import os
    from unittest.mock import patch

    test_settings = {
        "app_name": "Arbah Quotes API (Test)",
        "app_version": "0.1.0-test",
        "debug": True,
        "environment": "testing",
        "log_level": "DEBUG",
        "enable_docs": True,
        "enable_health_check": True,
        "enable_metrics": False,
    }

    with patch.dict(os.environ, {**test_settings, **os.environ}):
        yield test_settings