"""
Backend entry point - redirects to the main application.

This file is maintained for backward compatibility but the main application
is now located in src/arbah/main.py
"""

import sys
import os

# Add src directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

# Import and run the main application
from arbah.main import app

# The app object is now imported from the main application
# This allows both development servers to work the same way
