"""
Fonctions utilitaires pour l'IA Locale
"""

import os
import json
import logging
import sys
from datetime import datetime
from typing import Dict, List, Optional

# Configuration du logging
def setup_logging():
    """Configure le système de logging"""
    # Création du dossier de logs s'il n'existe pas
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    # Configuration du logger
    logger = logging.getLogger('ai_local')
    logger.setLevel(logging.DEBUG)
    
    # Création du handler de fichier
    log_file = os.path.join(log_dir, 'ai_local.log')
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)
    
    # Création du formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    file_handler.setFormatter(formatter)
    
    # Ajout du handler au logger
    logger.addHandler(file_handler)
    
    # Ajout du handler de console
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    # Message de confirmation
    logger.info("Système de logging configuré avec succès")
    
    return logger

# Gestion des données
def load_data(filename: str) -> Dict:
    """Charge les données depuis un fichier JSON"""
    try:
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                data = json.load(f)
            return data
        else:
            return {}
    except Exception as e:
        logging.getLogger('ai_local').error(f"Erreur lors du chargement des données: {e}")
        return {}

def save_data(filename: str, data: Dict) -> bool:
    """Sauvegarde les données dans un fichier JSON"""
    try:
        # Création du dossier si nécessaire
        dir_name = os.path.dirname(filename)
        if dir_name and not os.path.exists(dir_name):
            os.makedirs(dir_name)
        
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
        return True
    except Exception as e:
        logging.getLogger('ai_local').error(f"Erreur lors de la sauvegarde des données: {e}")
        return False

# Gestion des fichiers
def create_directories(paths: List[str]) -> bool:
    """Crée les répertoires spécifiés"""
    try:
        for path in paths:
            if not os.path.exists(path):
                os.makedirs(path)
        return True
    except Exception as e:
        logging.getLogger('ai_local').error(f"Erreur lors de la création des répertoires: {e}")
        return False

# Gestion des permissions
def check_permissions(filepath: str) -> bool:
    """Vérifie les permissions d'accès à un fichier"""
    try:
        return os.access(filepath, os.R_OK | os.W_OK)
    except Exception as e:
        logging.getLogger('ai_local').error(f"Erreur lors de la vérification des permissions: {e}")
        return False

# Gestion des erreurs
def handle_error(error: Exception, context: str = "") -> None:
    """Gère les erreurs de manière centralisée"""
    logger = logging.getLogger('ai_local')
    error_msg = f"Erreur dans {context}: {str(error)}"
    logger.error(error_msg)
    raise error

# Gestion des dates
def get_timestamp() -> str:
    """Retourne un timestamp formaté"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Validation des données
def validate_data(data: Dict, required_fields: List[str]) -> bool:
    """Valide que les champs requis sont présents dans les données"""
    for field in required_fields:
        if field not in data:
            return False
    return True

# Nettoyage des données
def clean_data(data: Dict) -> Dict:
    """Nettoie les données en supprimant les champs vides"""
    cleaned = {}
    for key, value in data.items():
        if value is not None and value != "":
            cleaned[key] = value
    return cleaned

# Conversion de données
def convert_to_json(data: Dict) -> str:
    """Convertit un dictionnaire en chaîne JSON"""
    try:
        return json.dumps(data, indent=2)
    except Exception as e:
        logging.getLogger('ai_local').error(f"Erreur lors de la conversion en JSON: {e}")
        return ""

# Gestion des configurations
def load_config(config_file: str = "config.json") -> Dict:
    """Charge la configuration depuis un fichier"""
    try:
        if os.path.exists(config_file):
            with open(config_file, 'r') as f:
                config = json.load(f)
            return config
        else:
            # Retourne une configuration par défaut
            return {
                "log_level": "INFO",
                "debug": False,
                "data_dir": "./data",
                "cache_dir": "./cache"
            }
    except Exception as e:
        logging.getLogger('ai_local').error(f"Erreur lors du chargement de la configuration: {e}")
        return {}

# Sauvegarde des configurations
def save_config(config: Dict, config_file: str = "config.json") -> bool:
    """Sauvegarde la configuration dans un fichier"""
    try:
        # Création du dossier si nécessaire
        dir_name = os.path.dirname(config_file)
        if dir_name and not os.path.exists(dir_name):
            os.makedirs(dir_name)
        
        with open(config_file, 'w') as f:
            json.dump(config, f, indent=2)
        return True
    except Exception as e:
        logging.getLogger('ai_local').error(f"Erreur lors de la sauvegarde de la configuration: {e}")
        return False

# Gestion des logs
def log_message(message: str, level: str = "INFO") -> None:
    """Enregistre un message dans les logs"""
    logger = logging.getLogger('ai_local')
    if level.upper() == "DEBUG":
        logger.debug(message)
    elif level.upper() == "INFO":
        logger.info(message)
    elif level.upper() == "WARNING":
        logger.warning(message)
    elif level.upper() == "ERROR":
        logger.error(message)
    elif level.upper() == "CRITICAL":
        logger.critical(message)