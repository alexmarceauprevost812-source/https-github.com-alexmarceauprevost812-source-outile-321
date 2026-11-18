"""
IA Locale Scam Tool
Outil d'IA pour la détection de scams
"""

# Version de l'application
__version__ = "1.0.0"
__author__ = "Scam Tool Team"
__email__ = "contact@scamtool.com"
__license__ = "MIT"
__description__ = "Outil d'IA pour la détection de scams"

# Importation des modules principaux
from .config import config, load_config, save_config
from .utils import setup_logging, load_data, save_data
from .ai_monitor import AIMonitor
from .ai_manager import AIManager
from .ai_integration import AIIntegration
from .ai_monitor import AIMonitor
from .ai_manager import AIManager

# Initialisation du logger
logger = setup_logging()

# Définition des classes principales
__all__ = [
    'config',
    'load_config',
    'save_config',
    'setup_logging',
    'load_data',
    'save_data',
    'AIMonitor',
    'AIManager',
    'AIIntegration',
    'AIMonitor',
    'AIManager'
]

# Fonction d'initialisation
def initialize():
    """
    Initialise le système d'IA Locale
    """
    logger.info("Initialisation du système d'IA Locale")
    
    # Création des répertoires nécessaires
    directories = [
        config.get('data_dir', './data'),
        config.get('cache_dir', './cache'),
        config.get('models_dir', './models'),
        config.get('logs_dir', './logs')
    ]
    
    for directory in directories:
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
            logger.info(f"Répertoire créé: {directory}")
    
    logger.info("Initialisation terminée")

# Initialisation automatique
try:
    import os
    initialize()
except Exception as e:
    print(f"Erreur lors de l'initialisation: {e}")