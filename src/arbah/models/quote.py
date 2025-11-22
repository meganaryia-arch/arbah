"""
Quote data models.
"""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class Quote(BaseModel):
    """Quote model."""

    id: Optional[int] = Field(None, description="Quote ID")
    text: str = Field(..., description="Quote text", min_length=1, max_length=1000)
    author: Optional[str] = Field(None, description="Quote author", max_length=100)
    category: Optional[str] = Field(None, description="Quote category", max_length=50)
    language: str = Field("fr", description="Quote language", max_length=5)
    created_at: Optional[datetime] = Field(None, description="Creation timestamp")
    updated_at: Optional[datetime] = Field(None, description="Update timestamp")

    class Config:
        """Pydantic config."""
        json_encoders = {
            datetime: lambda v: v.isoformat() if v else None
        }


class QuoteResponse(BaseModel):
    """API response model for quotes."""

    success: bool = Field(True, description="Success status")
    data: Quote = Field(..., description="Quote data")
    message: str = Field("Quote retrieved successfully", description="Response message")


class QuoteListResponse(BaseModel):
    """API response model for multiple quotes."""

    success: bool = Field(True, description="Success status")
    data: list[Quote] = Field(..., description="List of quotes")
    count: int = Field(..., description="Number of quotes")
    message: str = Field("Quotes retrieved successfully", description="Response message")