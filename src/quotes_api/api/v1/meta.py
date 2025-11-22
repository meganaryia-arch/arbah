"""
Metadata and informational endpoints.
"""

from fastapi import APIRouter

from quotes_api.config import settings
from quotes_api.services.quote_service import QuoteService

router = APIRouter(prefix="/meta", tags=["metadata"])
quote_service = QuoteService()


@router.get("/info", summary="Application information")
async def get_app_info():
    """Return general information about the application."""
    return {
        "name": settings.app_name,
        "version": settings.app_version,
        "description": "A simple FastAPI application for serving inspirational quotes",
        "environment": settings.environment,
        "api_version": "v1",
        "docs_url": "/docs" if settings.enable_docs else None
    }


@router.get("/stats", summary="Quote statistics")
async def get_quote_stats():
    """Return statistics about the quote collection."""
    quotes = quote_service.get_all_quotes()
    categories = quote_service.get_categories()
    authors = quote_service.get_authors()

    category_counts = {}
    for category in categories:
        category_quotes = quote_service.get_quotes_by_category(category)
        category_counts[category] = len(category_quotes)

    author_counts = {}
    for author in authors:
        author_quotes = quote_service.get_quotes_by_author(author)
        author_counts[author] = len(author_quotes)

    return {
        "total_quotes": len(quotes),
        "total_categories": len(categories),
        "total_authors": len(authors),
        "categories": category_counts,
        "authors": author_counts,
        "language_distribution": {
            "fr": len(quotes)  # Currently all quotes are in French
        }
    }


@router.get("/categories", summary="List all categories")
async def get_categories():
    """Return all available quote categories."""
    categories = quote_service.get_categories()
    return {
        "categories": categories,
        "count": len(categories)
    }


@router.get("/authors", summary="List all authors")
async def get_authors():
    """Return all available quote authors."""
    authors = quote_service.get_authors()
    return {
        "authors": authors,
        "count": len(authors)
    }