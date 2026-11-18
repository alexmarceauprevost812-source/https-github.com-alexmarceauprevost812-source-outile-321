"""
Fonctions utilitaires pour l'IA Locale
Contient des fonctions utilitaires pour l'IA
"""

import os
import sys
import json
import logging
import time
from datetime import datetime
from typing import Dict, List, Optional, Any
import hashlib

# Ajout du dossier ai_local au chemin Python
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def setup_logging(log_level: str = "INFO", log_file: str = "logs/ai_local.log"):
    """
    Configure le système de journalisation
    
    Args:
        log_level (str): Niveau de journalisation (DEBUG, INFO, WARNING, ERROR)
        log_file (str): Fichier de log
    
    Returns:
        logging.Logger: Logger configuré
    """
    # Création du dossier de logs si nécessaire
    log_dir = os.path.dirname(log_file)
    if log_dir and not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    # Configuration du logger
    logger = logging.getLogger("ai_local")
    logger.setLevel(getattr(logging, log_level.upper()))
    
    # Création du formateur
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    # Création du gestionnaire de fichier
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(getattr(logging, log_level.upper()))
    file_handler.setFormatter(formatter)
    
    # Création du gestionnaire de console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(getattr(logging, log_level.upper()))
    console_handler.setFormatter(formatter)
    
    # Ajout des gestionnaires au logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger

def load_data(file_path: str) -> Dict:
    """
    Charge des données depuis un fichier JSON
    
    Args:
        file_path (str): Chemin du fichier
    
    Returns:
        Dict: Données chargées
    """
    try:
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                data = json.load(f)
            return data
        else:
            return {}
    except Exception as e:
        print(f"Erreur lors du chargement des données: {e}")
        return {}

def save_data(data: Dict, file_path: str) -> bool:
    """
    Sauvegarde des données dans un fichier JSON
    
    Args:
        data (Dict): Données à sauvegarder
        file_path (str): Chemin du fichier
    
    Returns:
        bool: True si la sauvegarde a réussi
    """
    try:
        # Création du dossier si nécessaire
        dir_name = os.path.dirname(file_path)
        if dir_name and not os.path.exists(dir_name):
            os.makedirs(dir_name)
        
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=2)
        return True
    except Exception as e:
        print(f"Erreur lors de la sauvegarde des données: {e}")
        return False

def get_file_hash(file_path: str) -> str:
    """
    Calcule le hash d'un fichier
    
    Args:
        file_path (str): Chemin du fichier
    
    Returns:
        str: Hash du fichier
    """
    try:
        with open(file_path, 'rb') as f:
            file_hash = hashlib.md5()
            while chunk := f.read(8192):
                file_hash.update(chunk)
        return file_hash.hexdigest()
    except Exception as e:
        print(f"Erreur lors du calcul du hash: {e}")
        return ""

def create_backup(file_path: str, backup_dir: str = "backups") -> str:
    """
    Crée une sauvegarde d'un fichier
    
    Args:
        file_path (str): Chemin du fichier à sauvegarder
        backup_dir (str): Répertoire de sauvegarde
    
    Returns:
        str: Chemin de la sauvegarde créée
    """
    try:
        # Création du dossier de sauvegarde si nécessaire
        if not os.path.exists(backup_dir):
            os.makedirs(backup_dir)
        
        # Génération du nom de fichier de sauvegarde
        filename = os.path.basename(file_path)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_filename = f"{filename}.backup_{timestamp}"
        backup_path = os.path.join(backup_dir, backup_filename)
        
        # Copie du fichier
        with open(file_path, 'r') as src:
            with open(backup_path, 'w') as dst:
                dst.write(src.read())
        
        return backup_path
    except Exception as e:
        print(f"Erreur lors de la création de la sauvegarde: {e}")
        return ""

def validate_data_structure(data: Dict, required_fields: List[str]) -> bool:
    """
    Valide la structure d'un dictionnaire de données
    
    Args:
        data (Dict): Données à valider
        required_fields (List[str]): Champs requis
    
    Returns:
        bool: True si la structure est valide
    """
    try:
        for field in required_fields:
            if field not in data:
                return False
        return True
    except Exception:
        return False

def format_timestamp(timestamp: str) -> str:
    """
    Formate un horodatage
    
    Args:
        timestamp (str): Horodatage à formater
    
    Returns:
        str: Horodatage formaté
    """
    try:
        dt = datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
        return dt.strftime("%Y-%m-%d %H:%M:%S")
    except Exception:
        return timestamp

def get_current_timestamp() -> str:
    """
    Retourne l'horodatage actuel
    
    Returns:
        str: Horodatage actuel au format ISO
    """
    return datetime.now().isoformat()

def get_system_info() -> Dict:
    """
    Retourne les informations système
    
    Returns:
        Dict: Informations système
    """
    import platform
    return {
        "platform": platform.system(),
        "platform_version": platform.version(),
        "platform_release": platform.release(),
        "processor": platform.processor(),
        "machine": platform.machine(),
        "python_version": platform.python_version(),
        "timestamp": get_current_timestamp()
    }

def sanitize_string(input_string: str) -> str:
    """
    Nettoie une chaîne de caractères
    
    Args:
        input_string (str): Chaîne à nettoyer
    
    Returns:
        str: Chaîne nettoyée
    """
    if not isinstance(input_string, str):
        return ""
    # Supprime les caractères non imprimables
    return ''.join(char for char in input_string if char.isprintable())

def get_file_size(file_path: str) -> int:
    """
    Retourne la taille d'un fichier
    
    Args:
        file_path (str): Chemin du fichier
    
    Returns:
        int: Taille du fichier en octets
    """
    try:
        return os.path.getsize(file_path)
    except Exception:
        return 0

def is_valid_file_path(file_path: str) -> bool:
    """
    Vérifie si un chemin de fichier est valide
    
    Args:
        file_path (str): Chemin à vérifier
    
    Returns:
        bool: True si le chemin est valide
    """
    try:
        return os.path.isabs(file_path) and os.path.exists(os.path.dirname(file_path))
    except Exception:
        return False

def create_directory_if_not_exists(directory_path: str) -> bool:
    """
    Crée un répertoire s'il n'existe pas
    
    Args:
        directory_path (str): Chemin du répertoire
    
    Returns:
        bool: True si le répertoire existe ou a été créé
    """
    try:
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)
        return True
    except Exception as e:
        print(f"Erreur lors de la création du répertoire: {e}")
        return False

def get_elapsed_time(start_time: float) -> float:
    """
    Calcule le temps écoulé depuis un moment donné
    
    Args:
        start_time (float): Temps de départ
    
    Returns:
        float: Temps écoulé en secondes
    """
    return time.time() - start_time

def safe_dict_get(dictionary: Dict, key: str, default=None) -> Any:
    """
    Récupère une valeur d'un dictionnaire de manière sécurisée
    
    Args:
        dictionary (Dict): Dictionnaire à consulter
        key (str): Clé à rechercher
        default: Valeur par défaut
    
    Returns:
        Any: Valeur trouvée ou valeur par défaut
    """
    try:
        return dictionary.get(key, default)
    except Exception:
        return default

def safe_list_get(lst: List, index: int, default=None) -> Any:
    """
    Récupère un élément d'une liste de manière sécurisée
    
    Args:
        lst (List): Liste à consulter
        index (int): Index à rechercher
        default: Valeur par défaut
    
    Returns:
        Any: Élément trouvé ou valeur par défaut
    """
    try:
        return lst[index] if 0 <= index < len(lst) else default
    except Exception:
        return default

# Exemple d'utilisation
if __name__ == "__main__":
    # Configuration du logger
    logger = setup_logging()
    
    # Test des fonctions utilitaires
    logger.info("Fonctions utilitaires de l'IA Locale")
    
    # Test de sauvegarde de données
    test_data = {"message": "Hello, World!", "timestamp": get_current_timestamp()}
    save_data(test_data, "test_data.json")
    
    # Test de chargement de données
    loaded_data = load_data("test_data.json")
    logger.info(f"Données chargées: {loaded_data}")
    
    # Nettoyage
    os.remove("test_data.json")
    os.remove("logs/ai_local.log")