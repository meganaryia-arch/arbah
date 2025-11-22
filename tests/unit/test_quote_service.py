"""
Unit tests for the QuoteService.
"""

import pytest

from arbah.services.quote_service import QuoteService
from arbah.models.quote import Quote


class TestQuoteService:
    """Test cases for QuoteService."""

    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.quote_service = QuoteService()

    def test_get_random_quote(self):
        """Test getting a random quote."""
        quote = self.quote_service.get_random_quote()
        assert isinstance(quote, Quote)
        assert quote.text is not None
        assert len(quote.text) > 0
        assert quote.language == "fr"

    def test_get_quote_by_id_valid(self):
        """Test getting a quote by valid ID."""
        quote = self.quote_service.get_quote_by_id(1)
        assert quote is not None
        assert quote.id == 1
        assert quote.text is not None

    def test_get_quote_by_id_invalid(self):
        """Test getting a quote by invalid ID."""
        quote = self.quote_service.get_quote_by_id(999)
        assert quote is None

    def test_get_all_quotes(self):
        """Test getting all quotes."""
        quotes = self.quote_service.get_all_quotes()
        assert isinstance(quotes, list)
        assert len(quotes) == 10  # Based on our sample data
        assert all(isinstance(quote, Quote) for quote in quotes)

    def test_get_quotes_by_category_valid(self):
        """Test getting quotes by valid category."""
        quotes = self.quote_service.get_quotes_by_category("Amour")
        assert isinstance(quotes, list)
        assert len(quotes) > 0
        assert all(quote.category == "Amour" for quote in quotes)

    def test_get_quotes_by_category_invalid(self):
        """Test getting quotes by invalid category."""
        quotes = self.quote_service.get_quotes_by_category("NonExistentCategory")
        assert isinstance(quotes, list)
        assert len(quotes) == 0

    def test_get_quotes_by_author_valid(self):
        """Test getting quotes by valid author."""
        quotes = self.quote_service.get_quotes_by_author("Victor Hugo")
        assert isinstance(quotes, list)
        assert len(quotes) > 0
        assert all(quote.author == "Victor Hugo" for quote in quotes)

    def test_get_quotes_by_author_invalid(self):
        """Test getting quotes by invalid author."""
        quotes = self.quote_service.get_quotes_by_author("NonExistentAuthor")
        assert isinstance(quotes, list)
        assert len(quotes) == 0

    def test_search_quotes_by_text(self):
        """Test searching quotes by text content."""
        quotes = self.quote_service.search_quotes("vie")
        assert isinstance(quotes, list)
        assert len(quotes) > 0
        assert all("vie" in quote.text.lower() for quote in quotes)

    def test_search_quotes_by_author(self):
        """Test searching quotes by author name."""
        quotes = self.quote_service.search_quotes("Hugo")
        assert isinstance(quotes, list)
        assert len(quotes) > 0
        assert all(quote.author and "hugo" in quote.author.lower() for quote in quotes)

    def test_search_quotes_no_results(self):
        """Test searching quotes with no results."""
        quotes = self.quote_service.search_quotes("NonExistentSearchTerm")
        assert isinstance(quotes, list)
        assert len(quotes) == 0

    def test_get_categories(self):
        """Test getting all unique categories."""
        categories = self.quote_service.get_categories()
        assert isinstance(categories, list)
        assert len(categories) > 0
        assert all(isinstance(category, str) for category in categories)

    def test_get_authors(self):
        """Test getting all unique authors."""
        authors = self.quote_service.get_authors()
        assert isinstance(authors, list)
        assert len(authors) > 0
        assert all(isinstance(author, str) for author in authors)

    def test_quote_structure(self):
        """Test that quotes have the expected structure."""
        quote = self.quote_service.get_random_quote()
        assert hasattr(quote, 'id')
        assert hasattr(quote, 'text')
        assert hasattr(quote, 'author')
        assert hasattr(quote, 'category')
        assert hasattr(quote, 'language')
        assert isinstance(quote.text, str)
        assert len(quote.text) > 0
        assert quote.language == "fr"