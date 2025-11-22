"""
Arbah Quotes API

A simple FastAPI application for serving inspirational quotes.
"""

__version__ = "0.1.0"
__author__ = "Your Name"
__email__ = "your.email@example.com"

from arbah.config import settings
from arbah.main import app

__all__ = ["app", "settings", "__version__"]