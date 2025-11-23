"""
Passenger WSGI interface for PlanetHoster deployment.
"""

import os
import sys

# Add the src directory to Python path
project_root = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.join(project_root, 'src')
sys.path.insert(0, src_path)

# Set environment variables
os.environ.setdefault('PYTHONPATH', src_path)

from quotes_api.main import app

# Passenger expects an object named 'application'
application = app