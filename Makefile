.PHONY: help install install-dev test lint format clean run dev check

# Default target
help:
	@echo "Available commands:"
	@echo "  install      Install production dependencies"
	@echo "  install-dev  Install development dependencies"
	@echo "  test         Run tests"
	@echo "  test-cov     Run tests with coverage"
	@echo "  lint         Run linting checks"
	@echo "  format       Format code with black and isort"
	@echo "  check        Run all quality checks (lint + test)"
	@echo "  clean        Clean temporary files"
	@echo "  run          Run production server"
	@echo "  dev          Run development server with reload"
	@echo "  pre-commit   Install pre-commit hooks"

# Installation
install:
	pip install -r requirements.txt

install-dev:
	pip install -r requirements.txt
	pip install -e .
	pre-commit install

# Testing
test:
	pytest tests/ -v

test-cov:
	pytest tests/ --cov=quotes_api --cov-report=html --cov-report=term-missing -v

test-watch:
	pytest-watch tests/

# Code quality
lint:
	flake8 src/ tests/
	mypy src/
	bandit -r src/

format:
	black src/ tests/
	isort src/ tests/

check: lint test

# Development
dev:
	python -m uvicorn quotes_api.main:app --reload --host 0.0.0.0 --port 8000

run:
	python -m uvicorn quotes_api.main:app --host 0.0.0.0 --port 8000

# Cleanup
clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	rm -rf build/
	rm -rf dist/
	rm -rf .coverage
	rm -rf htmlcov/
	rm -rf .pytest_cache/
	rm -rf .mypy_cache/
	rm -rf bandit-report.json


# Pre-commit
pre-commit:
	pre-commit run --all-files

# Development helpers
setup-dev: install-dev
	@echo "Development environment setup complete!"

# Production deployment
build:
	python -m build

publish:
	python -m twine upload dist/*