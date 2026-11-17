"""
Configuration de l'IA Locale
"""

import os

# Configuration principale
AI_CONFIG = {
    # Paramètres de base
    'name': 'ScamTool AI Local',
    'version': '1.0.0',
    'author': 'ScamTool Team',
    
    # Paramètres de logging
    'log_level': 'INFO',
    'log_file': 'ai_local.log',
    
    # Paramètres d'analyse
    'cycle_interval': 30,  # En secondes
    'max_scans': 1000,
    
    # Paramètres de sécurité
    'enable_detection': True,
    'enable_analysis': True,
    
    # Chemins de fichiers
    'data_dir': 'data',
    'config_dir': 'config',
    
    # Paramètres réseau
    'scan_timeout': 10,
    'max_connections': 100,
    
    # Paramètres de sauvegarde
    'backup_interval': 3600,  # En secondes
    'max_backups': 5
}

# Création des répertoires si nécessaire
def setup_directories():
    """Crée les répertoires nécessaires"""
    directories = [
        AI_CONFIG['data_dir'],
        AI_CONFIG['config_dir']
    ]
    
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"Répertoire créé: {directory}")

# Appel automatique pour créer les répertoires
setup_directories()