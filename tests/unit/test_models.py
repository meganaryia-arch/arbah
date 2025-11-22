"""
Unit tests for data models.
"""

import pytest
from datetime import datetime
from pydantic import ValidationError

from arbah.models.quote import Quote, QuoteResponse, QuoteListResponse


class TestQuoteModel:
    """Test cases for Quote model."""

    def test_quote_creation_minimal(self):
        """Test creating a quote with minimal required fields."""
        quote = Quote(text="Test quote text")
        assert quote.text == "Test quote text"
        assert quote.id is None
        assert quote.author is None
        assert quote.category is None
        assert quote.language == "fr"

    def test_quote_creation_full(self):
        """Test creating a quote with all fields."""
        now = datetime.now()
        quote = Quote(
            id=1,
            text="Test quote text",
            author="Test Author",
            category="Test Category",
            language="en",
            created_at=now,
            updated_at=now
        )
        assert quote.id == 1
        assert quote.text == "Test quote text"
        assert quote.author == "Test Author"
        assert quote.category == "Test Category"
        assert quote.language == "en"
        assert quote.created_at == now
        assert quote.updated_at == now

    def test_quote_validation_text_required(self):
        """Test that text field is required."""
        with pytest.raises(ValidationError):
            Quote()

    def test_quote_validation_text_length(self):
        """Test text field length validation."""
        # Empty text should fail
        with pytest.raises(ValidationError):
            Quote(text="")

        # Text that's too long should fail
        with pytest.raises(ValidationError):
            Quote(text="a" * 1001)

    def test_quote_validation_author_length(self):
        """Test author field length validation."""
        # Author that's too long should fail
        with pytest.raises(ValidationError):
            Quote(text="Valid text", author="a" * 101)

    def test_quote_validation_category_length(self):
        """Test category field length validation."""
        # Category that's too long should fail
        with pytest.raises(ValidationError):
            Quote(text="Valid text", category="a" * 51)

    def test_quote_validation_language_length(self):
        """Test language field length validation."""
        # Language that's too long should fail
        with pytest.raises(ValidationError):
            Quote(text="Valid text", language="a" * 6)


class TestQuoteResponseModel:
    """Test cases for QuoteResponse model."""

    def test_quote_response_creation(self):
        """Test creating a quote response."""
        quote = Quote(text="Test quote", author="Test Author")
        response = QuoteResponse(data=quote)
        assert response.success is True
        assert response.data == quote
        assert response.message == "Quote retrieved successfully"

    def test_quote_response_custom_message(self):
        """Test creating a quote response with custom message."""
        quote = Quote(text="Test quote")
        response = QuoteResponse(data=quote, message="Custom message")
        assert response.message == "Custom message"

    def test_quote_response_serialization(self):
        """Test quote response serialization."""
        quote = Quote(id=1, text="Test quote", author="Test Author")
        response = QuoteResponse(data=quote)
        data = response.dict()
        assert data["success"] is True
        assert data["data"]["text"] == "Test quote"
        assert data["data"]["author"] == "Test Author"
        assert data["message"] == "Quote retrieved successfully"


class TestQuoteListResponseModel:
    """Test cases for QuoteListResponse model."""

    def test_quote_list_response_creation(self):
        """Test creating a quote list response."""
        quotes = [
            Quote(text="Quote 1", author="Author 1"),
            Quote(text="Quote 2", author="Author 2")
        ]
        response = QuoteListResponse(data=quotes, count=2)
        assert response.success is True
        assert response.data == quotes
        assert response.count == 2
        assert response.message == "Quotes retrieved successfully"

    def test_quote_list_response_count_mismatch(self):
        """Test that count can be different from actual list length."""
        quotes = [Quote(text="Quote 1")]
        response = QuoteListResponse(data=quotes, count=5)
        assert response.count == 5  # Should accept whatever count is provided

    def test_quote_list_response_empty(self):
        """Test creating a quote list response with empty list."""
        response = QuoteListResponse(data=[], count=0)
        assert response.data == []
        assert response.count == 0
        assert response.success is True

    def test_quote_list_response_serialization(self):
        """Test quote list response serialization."""
        quotes = [
            Quote(id=1, text="Quote 1", author="Author 1"),
            Quote(id=2, text="Quote 2", author="Author 2")
        ]
        response = QuoteListResponse(data=quotes, count=2)
        data = response.dict()
        assert data["success"] is True
        assert len(data["data"]) == 2
        assert data["count"] == 2
        assert data["message"] == "Quotes retrieved successfully"