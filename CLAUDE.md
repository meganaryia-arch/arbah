# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a professional Python-based project called "Quotes API" - a FastAPI application for serving inspirational quotes. The project follows Python senior-level best practices with clean architecture, comprehensive testing, and modern development tooling.

## Architecture

### 🏗️ **Professional Structure**
```
src/quotes_api/              # Main application package
├── api/v1/                 # API routes (v1)
│   ├── quotes.py          # Quote endpoints
│   ├── health.py          # Health check endpoints
│   └── meta.py            # Metadata endpoints
├── config/                # Configuration management
│   └── settings.py        # Application settings
├── models/                # Data models
│   └── quote.py           # Quote data structures
├── services/              # Business logic
│   └── quote_service.py   # Quote service logic
├── utils/                 # Utilities
│   ├── logger.py          # Logging configuration
│   └── exceptions.py      # Custom exceptions
└── main.py                # FastAPI application entry point

backend/                   # Legacy entry point (backward compatibility)
tests/                     # Test suite
├── unit/                  # Unit tests
└── integration/           # Integration tests
```

### 🎯 **Key Architectural Principles**
- **Separation of Concerns**: Each module has a single responsibility
- **Layered Architecture**: API → Services → Models (clean separation)
- **Dependency Injection**: Configuration is injected, not global
- **Type Safety**: Full type annotations throughout
- **Error Handling**: Custom exception hierarchy

## Development Setup

### 🚀 **Quick Start**
```bash
# 1. Install development dependencies
make install-dev

# 2. Run development server
make dev

# 3. Run tests
make test

# 4. Check code quality
make check
```

### 📋 **Detailed Setup**
1. **Set up Python environment:**
   ```bash
   python -m venv venv
   # Windows: venv\Scripts\activate
   # Unix: source venv/bin/activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   pip install -e .
   ```

3. **Configure environment:**
   ```bash
   cp .env.example .env
   # Edit .env as needed
   ```

## Common Commands

### 🛠️ **Development Commands**
```bash
make install-dev      # Install dev dependencies + setup pre-commit
make install          # Install production dependencies only
make dev             # Run development server with reload
make run             # Run production server
make test            # Run tests
make test-cov        # Run tests with coverage report
make lint            # Run linting (flake8, mypy, bandit)
make format          # Format code (black, isort)
make check           # Run all quality checks (lint + test)
make clean           # Clean temporary files
make pre-commit      # Run pre-commit hooks on all files
```

### 🧪 **Testing Commands**
```bash
pytest tests/                           # Run all tests
pytest tests/unit/                       # Unit tests only
pytest tests/integration/               # Integration tests only
pytest tests/ --cov=quotes_api          # With coverage
pytest-watch tests/                     # Watch mode
```

### 📊 **Code Quality**
```bash
black src/ tests/                       # Format code
isort src/ tests/                       # Sort imports
flake8 src/ tests/                      # Lint code
mypy src/                               # Type checking
bandit -r src/                          # Security check
```

## Key Development Practices

### ✅ **Code Quality Standards**
- **Black** for code formatting (88 character line length)
- **isort** for import sorting
- **flake8** for linting
- **mypy** for static type checking
- **Pre-commit hooks** for automated quality checks

### 🧪 **Testing Philosophy**
- **Unit tests**: Test individual components in isolation
- **Integration tests**: Test API endpoints end-to-end
- **Coverage**: Maintain high test coverage
- **Fixtures**: Reusable test data and configurations

### 🏗️ **Architecture Patterns**
- **Service Layer**: Business logic separated from API layer
- **Configuration Management**: Centralized settings with Pydantic
- **Error Handling**: Structured exception hierarchy
- **Logging**: Structured JSON logging with context

## Important Notes for Claude

### ⚠️ **Critical Guidelines**
1. **Never modify test files to make broken code pass** - Fix the implementation instead
2. **Always maintain backward compatibility** - Don't break existing APIs
3. **Follow the established patterns** - Don't introduce architectural inconsistencies
4. **Add tests for new features** - Every new feature needs comprehensive tests
5. **Update documentation** - Keep README and docstrings current

### 🎯 **When Adding Features**
1. **Add models** in `src/quotes_api/models/`
2. **Implement business logic** in `src/quotes_api/services/`
3. **Create API endpoints** in `src/quotes_api/api/v1/`
4. **Add comprehensive tests** in `tests/`
5. **Update configuration** if needed in `src/quotes_api/config/`
6. **Run quality checks** before committing

### 📁 **File Organization Rules**
- **Models**: Pure data structures, no business logic
- **Services**: Business logic, no HTTP dependencies
- **API Routes**: HTTP handling only, delegate to services
- **Utils**: Reusable utilities, logging, exceptions
- **Config**: Configuration and settings only

## Environment Variables

### 🔧 **Key Configuration**
```bash
# Application
APP_NAME=Quotes API
DEBUG=false
ENVIRONMENT=development

# Server
HOST=0.0.0.0
PORT=8000

# Logging
LOG_LEVEL=INFO
LOG_FORMAT=json

# Features
ENABLE_DOCS=true
ENABLE_HEALTH_CHECK=true
```

## API Documentation

- **Swagger UI**: `http://localhost:8000/docs` (when enabled)
- **ReDoc**: `http://localhost:8000/redoc` (when enabled)
- **OpenAPI Schema**: `http://localhost:8000/openapi.json`

This project represents a production-ready Python application following industry best practices.