#!/bin/bash

# Script de déploiement pour PlanetHoster

echo "🚀 Déploiement de Quotes API sur PlanetHoster..."

# Variables
PROJECT_DIR="/home/your_username/your_domain"
BACKUP_DIR="/home/your_username/backups"

# Créer une sauvegarde
echo "📦 Création d'une sauvegarde..."
mkdir -p $BACKUP_DIR
cp -r $PROJECT_DIR $BACKUP_DIR/quotes-api-$(date +%Y%m%d-%H%M%S)

# Aller dans le répertoire du projet
cd $PROJECT_DIR

# Activer l'environnement virtuel
source venv/bin/activate

# Mettre à jour le code
echo "📥 Mise à jour du code..."
git pull origin main

# Mettre à jour les dépendances
echo "📦 Mise à jour des dépendances..."
pip install -r requirements-prod.txt

# Redémarrer Passenger
echo "🔄 Redémarrage de Passenger..."
touch passenger_wsgi.py

echo "✅ Déploiement terminé avec succès !"