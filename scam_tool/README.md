# Outils de gestion des cookies

## Description

Cet ensemble d'outils permet d'extraire et de gérer les cookies locaux sur un système Linux.

## Fonctionnalités

### 1. Extraction des cookies locaux
- Extraction des cookies de Chrome
- Extraction des cookies de Firefox
- Format de sortie CSV

### 2. Capturer les cookies via proxy
- Configuration de mitmproxy
- Capture en temps réel des requêtes HTTP

### 3. Analyse des sessions
- Analyse des sessions actives
- Détection des cookies sensibles

## Utilisation

### Extraction des cookies locaux

```bash
# Extraire les cookies de Chrome
python3 extract_cookies.py chrome

# Extraire les cookies de Firefox
python3 extract_cookies.py firefox
```

### Menu interactif

```bash
# Lancer le menu
python3 cookie_menu.py
```

## Structure des fichiers

- `extract_cookies.py` - Extraction des cookies locaux
- `cookie_menu.py` - Interface interactive
- `README.md` - Documentation

## Prérequis

- Python 3
- sqlite3
- Chrome ou Firefox installés

## Limitations

- Extraction locale uniquement
- Nécessite un navigateur avec profil actif
- Fonctionne sur Linux uniquement

## Licence

MIT