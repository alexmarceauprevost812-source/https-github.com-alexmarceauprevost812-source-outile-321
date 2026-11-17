# IA Locale - Outils de Programmation

Ce dossier contient tous les outils nécessaires pour programmer une IA locale dans le projet Scam Tool.

## Structure du projet

- `ai_local/` - Dossier principal de l'IA locale
  - `main.py` - Point d'entrée principal
  - `config.py` - Configuration de l'IA
  - `utils.py` - Fonctions utilitaires
  - `requirements.txt` - Dépendances Python
  - `menu.py` - Interface de menu interactif
  - `__init__.py` - Initialisation du package
  - `test_ai.py` - Tests unitaires
  - `run_tests.py` - Script d'exécution des tests
  - `CONTRIBUTING.md` - Guide de contribution
  - `README.md` - Documentation principale

## Fonctionnalités

- Détection de fraude réseau
- Analyse de données
- Gestion des sessions
- Interface utilisateur
- Gestion des logs
- Sauvegarde des données

## Installation

1. Installer les dépendances : `pip install -r requirements.txt`
2. Configurer les paramètres dans `config.py`
3. Exécuter : `python3 main.py` ou `python3 menu.py`

## Utilisation

### Démarrage direct
```bash
python3 ai_local/main.py
```

### Interface interactive
```bash
python3 ai_local/menu.py
```

## Configuration

Le fichier `config.py` permet de personnaliser :
- Les intervalles d'analyse
- Les niveaux de log
- Les paramètres de sécurité
- Les chemins de fichiers

## Structure des fichiers

### main.py
Point d'entrée principal de l'IA locale avec les fonctionnalités principales.

### config.py
Configuration de l'IA avec des paramètres par défaut et validation.

### utils.py
Fonctions utilitaires pour le logging, la gestion des données, etc.

### menu.py
Interface de menu interactif pour l'IA locale.

## Dépendances

Les dépendances sont listées dans `requirements.txt`. Pour l'installation :
```bash
pip install -r requirements.txt
```

## Sécurité

L'IA locale inclut :
- Validation des configurations
- Gestion des logs sécurisée
- Sauvegarde automatique des données
- Gestion des erreurs robuste

## Développement

Pour développer l'IA locale :
1. Modifiez `main.py` pour ajouter de nouvelles fonctionnalités
2. Mettez à jour `config.py` pour ajuster les paramètres
3. Utilisez `utils.py` pour les fonctions utilitaires
4. Testez avec `menu.py` pour l'interface interactive