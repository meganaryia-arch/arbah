# Arbah Quotes API 🌸

Une API FastAPI élégante pour servir des citations inspirantes en français.

![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)
![Framework](https://img.shields.io/badge/fastapi-0.104+-green.svg)
![License](https://img.shields.io/badge/license-MIT-purple.svg)
![Tests](https://img.shields.io/badge/tests-passing-brightgreen.svg)

## 📖 Description

Arbah Quotes API est une application Python moderne construite avec FastAPI qui fournit des points d'accès pour récupérer, rechercher et explorer des citations inspirantes. L'API est conçue avec une architecture propre, des tests complets et des outils de développement modernes.

### ✨ Caractéristiques

- **Architecture Propre**: Structure de projet organisée avec séparation des responsabilités
- **Tests Complets**: Tests unitaires et d'intégration avec pytest
- **Documentation Auto-générée**: Documentation interactive avec Swagger/OpenAPI
- **Qualité de Code**: Linting, formatage, et analyse statique configurés
- **Configuration Centralisée**: Gestion des paramètres avec Pydantic
- **Logging Structuré**: Logs formatés JSON avec structlog
- **Support Docker**: Conteneurisation facile pour le déploiement
- **CI/CD**: GitHub Actions pour l'intégration et le déploiement continus

## 🚀 Démarrage Rapide

### Prérequis

- Python 3.8+
- pip (gestionnaire de paquets Python)

### Installation

1. **Cloner le dépôt:**
   ```bash
   git clone https://github.com/votre-username/arbah.git
   cd arabah
   ```

2. **Créer un environnement virtuel:**
   ```bash
   python -m venv venv

   # Windows
   venv\Scripts\activate

   # Unix/macOS
   source venv/bin/activate
   ```

3. **Installer les dépendances:**
   ```bash
   make install-dev
   # ou
   pip install -r requirements.txt
   pip install -e .
   ```

4. **Configurer l'environnement:**
   ```bash
   cp .env.example .env
   # Éditez .env selon vos besoins
   ```

### Lancement

**Mode Développement:**
```bash
make dev
# ou
python -m uvicorn arbah.main:app --reload
```

**Mode Production:**
```bash
make run
# ou
python -m uvicorn arbah.main:app --host 0.0.0.0 --port 8000
```

L'API sera disponible sur `http://localhost:8000`

## 📚 Documentation API

### Endpoints Principaux

#### 🔮 Citation Aléatoire
```http
GET /api/v1/quotes/random
```

#### 📝 Toutes les Citations
```http
GET /api/v1/quotes/
```

#### 🔍 Recherche de Citations
```http
GET /api/v1/quotes/search/?q=<terme_recherche>
```

#### 📚 Citations par Catégorie
```http
GET /api/v1/quotes/category/<categorie>
```

#### ✍️ Citations par Auteur
```http
GET /api/v1/quotes/author/<auteur>
```

#### 🏥 Santé de l'API
```http
GET /api/v1/health/
GET /api/v1/health/detailed
```

### Documentation Interactive

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`
- **OpenAPI Schema**: `http://localhost:8000/openapi.json`

## 🧪 Tests

### Exécuter tous les tests
```bash
make test
# ou
pytest tests/
```

### Tests avec couverture
```bash
make test-cov
# ou
pytest tests/ --cov=arbah --cov-report=html
```

### Tests en continu
```bash
pytest-watch tests/
```

## 🔧 Développement

### Commandes Disponibles

```bash
# Installation
make install          # Install production dependencies
make install-dev      # Install development dependencies

# Code Quality
make lint            # Run linting checks
make format          # Format code with black and isort
make check           # Run all quality checks

# Development
make dev             # Run development server
make run             # Run production server

# Testing
make test            # Run tests
make test-cov        # Run tests with coverage

# Docker
make docker-build    # Build Docker image
make docker-run      # Run Docker container

# Cleanup
make clean           # Clean temporary files
```

### Structure du Projet

```
arbah/
├── src/
│   └── arbah/
│       ├── api/                 # Routes API
│       │   └── v1/             # Version 1 de l'API
│       ├── config/             # Configuration
│       ├── models/             # Modèles de données
│       ├── services/           # Logique métier
│       ├── utils/              # Utilitaires
│       └── main.py             # Point d'entrée
├── tests/
│   ├── integration/            # Tests d'intégration
│   └── unit/                   # Tests unitaires
├── backend/
│   └── main.py                 # Ancien point d'entrée (compatibilité)
├── requirements.txt            # Dépendances
├── pyproject.toml             # Configuration du projet
├── .env.example               # Variables d'environnement
├── .flake8                    # Configuration flake8
├── .pre-commit-config.yaml    # Hooks pre-commit
├── Dockerfile                 # Configuration Docker
├── Makefile                   # Commandes pratiques
└── README.md                  # Documentation
```

## 🐳 Docker

### Construction de l'image
```bash
make docker-build
# ou
docker build -t arabah-quotes-api .
```

### Exécution du conteneur
```bash
make docker-run
# ou
docker run -p 8000:8000 arabah-quotes-api
```

### Avec variables d'environnement
```bash
docker run -p 8000:8000 \
  -e DEBUG=true \
  -e LOG_LEVEL=INFO \
  arabah-quotes-api
```

## 🔧 Configuration

### Variables d'Environnement

```bash
# Application
APP_NAME=Arbah Quotes API
APP_VERSION=0.1.0
DEBUG=false
ENVIRONMENT=production

# Serveur
HOST=0.0.0.0
PORT=8000

# Logging
LOG_LEVEL=INFO
LOG_FORMAT=json

# API
API_V1_PREFIX=/api/v1
CORS_ORIGINS=["http://localhost:3000"]

# Features
ENABLE_METRICS=true
ENABLE_DOCS=true
ENABLE_HEALTH_CHECK=true
```

## 🚀 Déploiement

### Heroku
```bash
# Créer l'app
heroku create votre-app

# Déployer
git push heroku main
```

### Railway
```bash
# Connecter le dépôt
railway login
railway link

# Déployer
railway up
```

### Azure App Service
```bash
# Créer les ressources
az group create --name arabah-rg --location westeurope
az webapp create --resource-group arabah-rg --plan arabah-plan --name votre-app

# Déployer
git azure webapp deployment source config-local-git --resource-group arabah-rg --name votre-app
git push azure main
```

## 📊 Monitoring

### Health Checks
- **Basic**: `/api/v1/health/`
- **Detailed**: `/api/v1/health/detailed` (inclut les métriques système)

### Logging
Les logs sont structurés en JSON pour une meilleure intégration avec les systèmes de logging:

```json
{
  "timestamp": "2023-12-01T10:00:00Z",
  "level": "INFO",
  "message": "HTTP request",
  "method": "GET",
  "path": "/api/v1/quotes/random",
  "status_code": 200,
  "duration_ms": 15.2
}
```

## 🤝 Contribution

1. Fork le projet
2. Créer une branche feature (`git checkout -b feature/amazing-feature`)
3. Committer les changements (`git commit -m 'Add amazing feature'`)
4. Pusher vers la branche (`git push origin feature/amazing-feature`)
5. Ouvrir une Pull Request

### Code Quality
Le projet utilise des hooks pre-commit pour maintenir la qualité du code:

```bash
# Installer les hooks
pre-commit install

# Exécuter tous les hooks
pre-commit run --all-files
```

## 📝 Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

## 🙏 Remerciements

- Citations inspirantes de divers auteurs francophones
- FastAPI pour le framework web performant
- Pydantic pour la validation des données
- Pytest pour les tests
- Black, flake8, et mypy pour la qualité du code

## 📞 Contact

- **Projet**: https://github.com/votre-username/arbah
- **Issues**: https://github.com/votre-username/arbah/issues
- **Email**: votre-email@example.com

---

*Built with ❤️ using FastAPI*