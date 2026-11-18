"""
Initialisation du package IA Locale
"""

# Importation des classes principales
from .ai_manager import AIManager
from .ai_monitor import AIMonitor
from .scam_detector import ScamDetector
from .network_analyzer import NetworkAnalyzer
from .ai_integration import AIIntegration
from .config import config

# Définition des exports
__all__ = [
    'AIManager',
    'AIMonitor', 
    'ScamDetector',
    'NetworkAnalyzer',
    'AIIntegration',
    'config'
]

# Version du package
__version__ = '1.0.0'
__author__ = 'Scam Tool Team'
__email__ = 'contact@scamtool.com'

def initialize():
    """
    Initialise le système IA Locale
    
    Cette fonction configure le système avec les paramètres par défaut
    et prépare les composants pour l'exécution.
    """
    # Configuration initiale
    print("Initialisation du système IA Locale...")
    
    # Vérification des répertoires
    import os
    directories = [
        config.get('data_dir'),
        config.get('cache_dir'),
        config.get('models_dir'),
        config.get('logs_dir')
    ]
    
    for directory in directories:
        if directory:
            dir_path = os.path.abspath(directory)
            os.makedirs(dir_path, exist_ok=True)
    
    print("Système IA Locale initialisé avec succès")
    return True

# Point d'entrée principal
if __name__ == "__main__":
    initialize()