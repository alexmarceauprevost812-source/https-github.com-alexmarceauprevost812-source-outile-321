#!/bin/bash

# Script d'installation complet pour le Scam Tool
# Ce script installe toutes les dépendances nécessaires

echo "Installation complète du Scam Tool..."

# Mise à jour des paquets
echo "Mise à jour des paquets..."
sudo apt update

# Installation des dépendances système
echo "Installation des dépendances système..."
sudo apt install -y python3 python3-pip git wget curl

# Installation des bibliothèques Python
echo "Installation des bibliothèques Python..."
pip3 install --upgrade pip
pip3 install requests numpy pandas

# Clonage du dépôt si nécessaire
echo "Clonage du dépôt..."
git clone https://github.com/username/scam-tool.git /tmp/scam-tool
cd /tmp/scam-tool

# Installation des dépendances du projet
echo "Installation des dépendances du projet..."
pip3 install -r requirements.txt

# Configuration du projet
echo "Configuration du projet..."
python3 setup.py install

echo "Installation complète terminée!"