"""
Configuration de l'IA Locale
Contient les paramètres de configuration de l'IA
"""

import os
import json
import sys
from datetime import datetime
from typing import Dict, List, Optional

# Ajout du dossier ai_local au chemin Python
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from utils import setup_logging

# Configuration par défaut
AI_CONFIG = {
    "version": "1.0.0",
    "name": "IA Locale Scam Tool",
    "description": "Outil d'IA pour la détection de scams",
    "author": "Scam Tool Team",
    "license": "MIT",
    "debug": False,
    "log_level": "INFO",
    "data_dir": "./data",
    "cache_dir": "./cache",
    "models_dir": "./models",
    "logs_dir": "./logs",
    "max_workers": 4,
    "timeout": 30,
    "retry_attempts": 3,
    "enable_monitoring": True,
    "monitoring_interval": 5,
    "enable_alerts": True,
    "alert_thresholds": {
        "cpu_usage": 80,
        "memory_usage": 80,
        "disk_usage": 80
    },
    "network": {
        "capture_interface": "eth0",
        "max_packet_size": 1500,
        "monitoring_enabled": True
    },
    "scam_detection": {
        "enable_suspicious_ips": True,
        "enable_suspicious_ports": True,
        "enable_packet_size_analysis": True,
        "suspicious_ports": [23, 25, 110, 143, 993, 995],
        "max_packet_size": 1500
    }
}

# Initialisation du logger
logger = setup_logging()

def load_config(config_file: str = "config.json") -> Dict:
    """Charge la configuration depuis un fichier"""
    try:
        if os.path.exists(config_file):
            with open(config_file, 'r') as f:
                config = json.load(f)
            
            # Fusionner avec la configuration par défaut
            merged_config = AI_CONFIG.copy()
            merged_config.update(config)
            
            logger.info(f"Configuration chargée depuis {config_file}")
            return merged_config
        else:
            logger.warning(f"Fichier de configuration non trouvé: {config_file}")
            logger.info("Utilisation de la configuration par défaut")
            return AI_CONFIG
    except Exception as e:
        logger.error(f"Erreur lors du chargement de la configuration: {e}")
        return AI_CONFIG

def save_config(config: Dict, config_file: str = "config.json") -> bool:
    """Sauvegarde la configuration dans un fichier"""
    try:
        # Création du dossier si nécessaire
        dir_name = os.path.dirname(config_file)
        if dir_name and not os.path.exists(dir_name):
            os.makedirs(dir_name)
        
        with open(config_file, 'w') as f:
            json.dump(config, f, indent=2)
        
        logger.info(f"Configuration sauvegardée dans {config_file}")
        return True
    except Exception as e:
        logger.error(f"Erreur lors de la sauvegarde de la configuration: {e}")
        return False

def get_config_value(key: str, default_value=None) -> any:
    """Récupère une valeur spécifique de la configuration"""
    try:
        keys = key.split('.')
        config = AI_CONFIG
        
        for k in keys:
            config = config[k]
        
        return config
    except (KeyError, TypeError):
        return default_value

def set_config_value(key: str, value: any) -> bool:
    """Définit une valeur spécifique dans la configuration"""
    try:
        keys = key.split('.')
        config = AI_CONFIG
        
        for k in keys[:-1]:
            if k not in config:
                config[k] = {}
            config = config[k]
        
        config[keys[-1]] = value
        return True
    except Exception as e:
        logger.error(f"Erreur lors de la définition de la valeur de configuration: {e}")
        return False

def get_config_as_dict() -> Dict:
    """Retourne la configuration sous forme de dictionnaire"""
    return AI_CONFIG.copy()

def get_config_version() -> str:
    """Retourne la version de la configuration"""
    return AI_CONFIG.get("version", "unknown")

def get_config_description() -> str:
    """Retourne la description de la configuration"""
    return AI_CONFIG.get("description", "No description")

def get_config_author() -> str:
    """Retourne l'auteur de la configuration"""
    return AI_CONFIG.get("author", "Unknown")

def get_config_license() -> str:
    """Retourne la licence de la configuration"""
    return AI_CONFIG.get("license", "Unknown")

def get_config_timestamp() -> str:
    """Retourne l'horodatage de la configuration"""
    return datetime.now().isoformat()

# Export des configurations
config = AI_CONFIG
load_config = load_config
save_config = save_config
get_config_value = get_config_value
set_config_value = set_config_value
get_config_as_dict = get_config_as_dict
get_config_version = get_config_version
get_config_description = get_config_description
get_config_author = get_config_author
get_config_license = get_config_license
get_config_timestamp = get_config_timestamp

# Exemple d'utilisation
if __name__ == "__main__":
    print("Configuration de l'IA Locale")
    print(f"Version: {get_config_version()}")
    print(f"Description: {get_config_description()}")
    print(f"Auteur: {get_config_author()}")
    print(f"Licence: {get_config_license()}")