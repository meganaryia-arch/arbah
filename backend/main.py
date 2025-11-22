"""
Backend entry point - redirects to the main application.

This file is maintained for backward compatibility but the main application
is now located in src/quotes_api/main.py
"""

import sys
import os
import importlib.util

# Load the main application directly from file
current_dir = os.path.dirname(os.path.abspath(__file__))
main_file = os.path.join(current_dir, '..', 'src', 'quotes_api', 'main.py')

# Load the module dynamically
spec = importlib.util.spec_from_file_location("quotes_api_main", main_file)
module = importlib.util.module_from_spec(spec)
sys.modules["quotes_api_main"] = module
spec.loader.exec_module(module)

# Get the app object
app = module.app

# Export the app object for external use
__all__ = ["app"]
