"""
Quote-related API endpoints.
"""

from typing import List, Optional

from fastapi import APIRouter, HTTPException, Query

from quotes_api.models.quote import Quote, QuoteResponse, QuoteListResponse
from quotes_api.services.quote_service import QuoteService

router = APIRouter(prefix="/quotes", tags=["quotes"])
quote_service = QuoteService()


@router.get("/random", response_model=QuoteResponse, summary="Get a random quote")
async def get_random_quote():
    """Return a random quote from the collection."""
    quote = quote_service.get_random_quote()
    return QuoteResponse(data=quote, message="Random quote retrieved successfully")


@router.get("/", response_model=QuoteListResponse, summary="Get all quotes")
async def get_all_quotes():
    """Return all available quotes."""
    quotes = quote_service.get_all_quotes()
    return QuoteListResponse(
        data=quotes,
        count=len(quotes),
        message="All quotes retrieved successfully"
    )


@router.get("/{quote_id}", response_model=QuoteResponse, summary="Get a quote by ID")
async def get_quote_by_id(quote_id: int):
    """Return a specific quote by its ID."""
    quote = quote_service.get_quote_by_id(quote_id)
    if not quote:
        raise HTTPException(status_code=404, detail="Quote not found")
    return QuoteResponse(data=quote, message="Quote retrieved successfully")


@router.get("/category/{category}", response_model=QuoteListResponse, summary="Get quotes by category")
async def get_quotes_by_category(category: str):
    """Return all quotes from a specific category."""
    quotes = quote_service.get_quotes_by_category(category)
    if not quotes:
        raise HTTPException(status_code=404, detail=f"No quotes found in category: {category}")
    return QuoteListResponse(
        data=quotes,
        count=len(quotes),
        message=f"Quotes from category '{category}' retrieved successfully"
    )


@router.get("/author/{author}", response_model=QuoteListResponse, summary="Get quotes by author")
async def get_quotes_by_author(author: str):
    """Return all quotes from a specific author."""
    quotes = quote_service.get_quotes_by_author(author)
    if not quotes:
        raise HTTPException(status_code=404, detail=f"No quotes found from author: {author}")
    return QuoteListResponse(
        data=quotes,
        count=len(quotes),
        message=f"Quotes from author '{author}' retrieved successfully"
    )


@router.get("/search/", response_model=QuoteListResponse, summary="Search quotes")
async def search_quotes(
    q: str = Query(..., min_length=1, description="Search query to find quotes"),
):
    """Search quotes by text, author, or category."""
    quotes = quote_service.search_quotes(q)
    if not quotes:
        raise HTTPException(status_code=404, detail=f"No quotes found matching: {q}")
    return QuoteListResponse(
        data=quotes,
        count=len(quotes),
        message=f"Quotes matching '{q}' retrieved successfully"
    )