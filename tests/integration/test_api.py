"""
Integration tests for the API endpoints.
"""

import pytest

from arbah.models.quote import Quote


class TestQuotesAPI:
    """Integration tests for quotes API endpoints."""

    def test_root_endpoint(self, client):
        """Test the root endpoint."""
        response = client.get("/")
        assert response.status_code == 200
        data = response.json()
        assert "message" in data
        assert "version" in data
        assert "docs" in data
        assert "health" in data
        assert "quotes" in data

    def test_get_random_quote(self, client):
        """Test getting a random quote."""
        response = client.get("/api/v1/quotes/random")
        assert response.status_code == 200
        data = response.json()
        assert data["success"] is True
        assert "data" in data
        assert "message" in data
        assert "text" in data["data"]
        assert data["data"]["language"] == "fr"

    def test_get_all_quotes(self, client):
        """Test getting all quotes."""
        response = client.get("/api/v1/quotes/")
        assert response.status_code == 200
        data = response.json()
        assert data["success"] is True
        assert "data" in data
        assert "count" in data
        assert isinstance(data["data"], list)
        assert data["count"] == len(data["data"])
        assert len(data["data"]) > 0

    def test_get_quote_by_id_valid(self, client):
        """Test getting a quote by valid ID."""
        response = client.get("/api/v1/quotes/1")
        assert response.status_code == 200
        data = response.json()
        assert data["success"] is True
        assert data["data"]["id"] == 1

    def test_get_quote_by_id_invalid(self, client):
        """Test getting a quote by invalid ID."""
        response = client.get("/api/v1/quotes/999")
        assert response.status_code == 404
        data = response.json()
        assert "detail" in data
        assert "not found" in data["detail"].lower()

    def test_get_quotes_by_category_valid(self, client):
        """Test getting quotes by valid category."""
        response = client.get("/api/v1/quotes/category/Amour")
        assert response.status_code == 200
        data = response.json()
        assert data["success"] is True
        assert isinstance(data["data"], list)
        assert len(data["data"]) > 0
        assert all(quote["category"] == "Amour" for quote in data["data"])

    def test_get_quotes_by_category_invalid(self, client):
        """Test getting quotes by invalid category."""
        response = client.get("/api/v1/quotes/category/NonExistentCategory")
        assert response.status_code == 404
        data = response.json()
        assert "detail" in data

    def test_get_quotes_by_author_valid(self, client):
        """Test getting quotes by valid author."""
        response = client.get("/api/v1/quotes/author/Victor Hugo")
        assert response.status_code == 200
        data = response.json()
        assert data["success"] is True
        assert isinstance(data["data"], list)
        assert len(data["data"]) > 0
        assert all(quote["author"] == "Victor Hugo" for quote in data["data"])

    def test_get_quotes_by_author_invalid(self, client):
        """Test getting quotes by invalid author."""
        response = client.get("/api/v1/quotes/author/NonExistentAuthor")
        assert response.status_code == 404
        data = response.json()
        assert "detail" in data

    def test_search_quotes_valid(self, client):
        """Test searching quotes with valid query."""
        response = client.get("/api/v1/quotes/search/?q=vie")
        assert response.status_code == 200
        data = response.json()
        assert data["success"] is True
        assert isinstance(data["data"], list)
        assert len(data["data"]) > 0

    def test_search_quotes_no_results(self, client):
        """Test searching quotes with no results."""
        response = client.get("/api/v1/quotes/search/?q=NonExistentSearchTerm")
        assert response.status_code == 404
        data = response.json()
        assert "detail" in data

    def test_search_quotes_missing_query(self, client):
        """Test searching quotes without query parameter."""
        response = client.get("/api/v1/quotes/search/")
        assert response.status_code == 422  # Validation error


class TestHealthAPI:
    """Integration tests for health check endpoints."""

    def test_health_check(self, client):
        """Test basic health check."""
        response = client.get("/api/v1/health/")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "healthy"
        assert "timestamp" in data
        assert "app_name" in data
        assert "version" in data

    def test_detailed_health_check(self, client):
        """Test detailed health check."""
        response = client.get("/api/v1/health/detailed")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "healthy"
        assert "system" in data
        assert "features" in data
        assert "platform" in data["system"]
        assert "memory" in data["system"]

    def test_ping(self, client):
        """Test ping endpoint."""
        response = client.get("/api/v1/health/ping")
        assert response.status_code == 200
        data = response.json()
        assert data["ping"] == "pong"


class TestMetaAPI:
    """Integration tests for metadata endpoints."""

    def test_get_app_info(self, client):
        """Test getting application info."""
        response = client.get("/api/v1/meta/info")
        assert response.status_code == 200
        data = response.json()
        assert "name" in data
        assert "version" in data
        assert "description" in data
        assert "environment" in data

    def test_get_quote_stats(self, client):
        """Test getting quote statistics."""
        response = client.get("/api/v1/meta/stats")
        assert response.status_code == 200
        data = response.json()
        assert "total_quotes" in data
        assert "total_categories" in data
        assert "total_authors" in data
        assert "categories" in data
        assert "authors" in data
        assert data["total_quotes"] > 0

    def test_get_categories(self, client):
        """Test getting all categories."""
        response = client.get("/api/v1/meta/categories")
        assert response.status_code == 200
        data = response.json()
        assert "categories" in data
        assert "count" in data
        assert isinstance(data["categories"], list)
        assert data["count"] == len(data["categories"])

    def test_get_authors(self, client):
        """Test getting all authors."""
        response = client.get("/api/v1/meta/authors")
        assert response.status_code == 200
        data = response.json()
        assert "authors" in data
        assert "count" in data
        assert isinstance(data["authors"], list)
        assert data["count"] == len(data["authors"])


class TestAsyncAPI:
    """Tests using async client."""

    @pytest.mark.asyncio
    async def test_async_get_random_quote(self, async_client):
        """Test getting a random quote using async client."""
        response = await async_client.get("/api/v1/quotes/random")
        assert response.status_code == 200
        data = response.json()
        assert data["success"] is True
        assert "data" in data
        assert "text" in data["data"]

    @pytest.mark.asyncio
    async def test_async_health_check(self, async_client):
        """Test health check using async client."""
        response = await async_client.get("/api/v1/health/")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "healthy"