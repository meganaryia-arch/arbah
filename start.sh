#!/bin/bash

# Set environment variables
export PYTHONPATH="/home/your_username/your_domain/src:$PYTHONPATH"

# Navigate to project directory
cd /home/your_username/your_domain

# Activate virtual environment
source venv/bin/activate

# Start the application
uvicorn quotes_api.main:app --host 0.0.0.0 --port $PORT --workers 3