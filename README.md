# IA Locale Scam Tool

Outil d'IA pour la détection de scams basé sur une approche locale.

## Description

IA Locale Scam Tool est un outil d'intelligence artificielle conçu pour détecter les escroqueries dans le trafic réseau. Il utilise une approche locale pour éviter les transmissions de données vers des serveurs externes, garantissant ainsi la confidentialité des données.

## Fonctionnalités

- Détection d'escroqueries dans le trafic réseau
- Analyse de trafic réseau en temps réel
- Surveillance des performances système
- Intégration d'IA distribuée
- Exportation et importation de données
- Gestion de configuration

## Structure du Projet

```
scam_tool/
├── ai_local/
│   ├── __init__.py
│   ├── config.py
│   ├── utils.py
│   ├── ai_manager.py
│   ├── ai_monitor.py
│   ├── scam_detector.py
│   ├── network_analyzer.py
│   ├── ai_integration.py
├── data/
├── cache/
├── models/
├── logs/
├── config.json
└── requirements.txt
```

## Installation

### Prérequis

- Python 3.7+
- pip
- Accès root (pour l'analyse réseau)

### Étapes d'installation

1. **Cloner le dépôt :**
   ```bash
   git clone <url-du-depot>
   cd scam_tool
   ```

2. **Exécuter le script d'installation unique :**
   ```bash
   chmod +x install_single.sh
   ./install_single.sh
   ```

### Script d'installation unique

Le projet inclut un script d'installation unique qui effectue toutes les étapes nécessaires en une seule commande :

```bash
chmod +x install_single.sh
./install_single.sh
```

Ce script :
- Détecte automatiquement la distribution Linux
- Installe tous les outils système requis
- Installe les bibliothèques Python nécessaires
- Crée les répertoires nécessaires
- Configure le projet pour une utilisation immédiate

## Configuration

La configuration est gérée via le fichier `config.json`. Vous pouvez modifier les paramètres dans ce fichier ou utiliser les fonctions de gestion de configuration dans le code.

### Paramètres de configuration

- `data_dir`: Répertoire pour les données
- `cache_dir`: Répertoire pour le cache
- `models_dir`: Répertoire pour les modèles
- `logs_dir`: Répertoire pour les logs
- `monitoring_interval`: Intervalle de surveillance (en secondes)
- `log_level`: Niveau de journalisation
- `features`: Fonctionnalités activées

## Utilisation

### Démarrage

Pour démarrer l'outil :

```python
from ai_local import initialize

# Initialiser le système
initialize()

# Démarrer l'intégration
from ai_local.ai_integration import AIIntegration
integration = AIIntegration()
integration.start_integration()
```

### Exemple d'utilisation

```python
# Création d'un détecteur d'escroqueries
from ai_local.scam_detector import ScamDetector

detector = ScamDetector()

# Ajout d'adresses IP suspectes
detector.add_suspicious_ip("192.168.1.100")
detector.add_suspicious_ip("10.0.0.1")

# Ajout de ports suspectes
detector.add_suspicious_port(23)
detector.add_suspicious_port(25)

# Démarrage de la surveillance
detector.start_monitoring()

# Analyse de paquets
packet = {
    "source_ip": "192.168.1.100",
    "destination_ip": "8.8.8.8",
    "protocol": "TCP",
    "source_port": 23,
    "destination_port": 80,
    "packet_size": 1000,
    "timestamp": "2023-01-01T00:00:00Z"
}

result = detector.analyze_packet(packet)
print(result)
```

## Composants

### AIManager

Gestionnaire principal pour les composants de l'IA.

### AIMonitor

Surveille les performances système.

### ScamDetector

Détecte les escroqueries dans le trafic réseau.

### NetworkAnalyzer

Analyse le trafic réseau.

### AIIntegration

Intègre tous les composants de l'IA.

## Données

Les données sont stockées dans les répertoires suivants :

- `data/`: Données utilisateur
- `cache/`: Fichiers de cache
- `models/`: Modèles d'IA
- `logs/`: Fichiers de journalisation

## Exportation et Importation

Les données peuvent être exportées et importées via les méthodes :

- `export_data()`
- `import_data()`

## Sécurité

L'outil utilise une approche locale pour éviter les transmissions de données vers des serveurs externes. Les données sensibles sont conservées localement.

## Licence

Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus d'informations.

## Auteur

Scam Tool Team

## Remarques

- Ce projet est encore en développement
- Veuillez consulter les fichiers de log pour les informations de débogage
- Les fonctionnalités peuvent être étendues selon les besoins