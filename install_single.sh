#!/bin/bash

# ============================================================
# Scam Tool - Installation Unique
# Script d'installation complet en une seule commande
# ============================================================

echo "============================================================"
echo "Scam Tool - Installation Unique"
echo "============================================================"

# Vérification de la distribution Linux
if [ -f /etc/kali-version ]; then
    echo "✓ Kali Linux détecté"
    DISTRO="kali"
elif [ -f /etc/debian_version ]; then
    echo "✓ Distribution Debian/Ubuntu détectée"
    DISTRO="ubuntu"
elif [ -f /etc/redhat-release ]; then
    echo "✓ Distribution RedHat/CentOS détectée"
    DISTRO="centos"
else
    echo "⚠ Distribution non reconnue, continuer avec les outils par défaut"
    DISTRO="unknown"
fi

# Mise à jour des paquets
echo "Mise à jour des paquets..."
sudo apt update

# Installation des outils système nécessaires
echo "Installation des outils système..."
sudo apt install -y \
    python3 \
    python3-pip \
    git \
    curl \
    wget \
    nmap \
    arp-scan \
    dnsenum \
    john \
    hashcat \
    wifite \
    aircrack-ng \
    ettercap-text-only \
    sslstrip \
    mitmf \
    build-essential \
    python3-dev \
    libpcap-dev

# Installation des bibliothèques Python
echo "Installation des bibliothèques Python..."
pip3 install --upgrade pip
pip3 install -r requirements.txt

# Création des répertoires nécessaires
echo "Création des répertoires..."
mkdir -p scam_results data cache models logs

# Configuration du projet
echo "Configuration du projet..."
chmod +x scam_tool.py

# Vérification et installation des dépendances spécifiques au sous-module AI
echo "Installation des dépendances spécifiques à l'IA locale..."
if [ -f "scam_tool/ai_local/requirements.txt" ]; then
    pip3 install -r scam_tool/ai_local/requirements.txt
fi

# Vérification de l'installation
echo "Vérification de l'installation..."
if command -v python3 &> /dev/null; then
    echo "✓ Python3 est installé"
else
    echo "✗ Python3 n'est pas installé"
    exit 1
fi

if command -v pip3 &> /dev/null; then
    echo "✓ pip3 est installé"
else
    echo "✗ pip3 n'est pas installé"
    exit 1
fi

echo "============================================================"
echo "Installation terminée avec succès !"
echo "Pour utiliser l'outil :"
echo "  python3 scam_tool.py --help"
echo "============================================================"