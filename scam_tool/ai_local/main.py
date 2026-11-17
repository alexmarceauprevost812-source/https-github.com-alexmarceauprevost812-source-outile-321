"""
Fichier principal de l'IA Locale
Gère le démarrage et l'arrêt de l'IA Locale
"""

import os
import sys
import threading
import time
from datetime import datetime
from typing import Dict, List, Optional

# Ajout du dossier ai_local au chemin Python
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from utils import setup_logging, load_data, save_data
from config import AI_CONFIG

class AILocal:
    """Classe principale de l'IA Locale"""
    
    def __init__(self):
        """Initialisation de l'IA Locale"""
        self.logger = setup_logging()
        self.is_running = False
        self.config = AI_CONFIG
        self.logger.info("IA Locale initialisée avec succès")
    
    def start(self):
        """Démarrage de l'IA Locale"""
        if self.is_running:
            self.logger.warning("L'IA Locale est déjà en cours d'exécution")
            return
        
        self.is_running = True
        self.logger.info("Démarrage de l'IA Locale")
        
        # Initialisation des composants
        self._initialize_components()
        
        # Boucle principale
        try:
            while self.is_running:
                # Logique principale de l'IA
                self._main_loop()
                time.sleep(1)  # Pause de 1 seconde entre les itérations
        except KeyboardInterrupt:
            self.logger.info("Interruption par l'utilisateur")
            self.stop()
        except Exception as e:
            self.logger.error(f"Erreur critique dans le démarrage de l'IA: {e}")
            self.stop()
    
    def stop(self):
        """Arrêt de l'IA Locale"""
        self.is_running = False
        self.logger.info("Arrêt de l'IA Locale")
    
    def _initialize_components(self):
        """Initialisation des composants de l'IA"""
        self.logger.debug("Initialisation des composants")
        
        # Création des répertoires nécessaires
        directories = [
            "data",
            "cache",
            "logs",
            "models"
        ]
        
        for directory in directories:
            if not os.path.exists(directory):
                os.makedirs(directory)
                self.logger.debug(f"Répertoire créé: {directory}")
        
        # Chargement des données de configuration
        self.logger.debug("Configuration chargée")
    
    def _main_loop(self):
        """Boucle principale de l'IA"""
        # Logique principale de l'IA
        # Pour l'instant, on fait juste un peu de logging
        pass
    
    def get_status(self) -> Dict:
        """Retourne l'état courant de l'IA"""
        return {
            "status": "running" if self.is_running else "stopped",
            "start_time": datetime.now().isoformat(),
            "config": self.config
        }
    
    def get_config(self) -> Dict:
        """Retourne la configuration de l'IA"""
        return self.config
    
    def update_config(self, new_config: Dict) -> bool:
        """Met à jour la configuration de l'IA"""
        try:
            self.config.update(new_config)
            self.logger.info("Configuration mise à jour")
            return True
        except Exception as e:
            self.logger.error(f"Erreur lors de la mise à jour de la configuration: {e}")
            return False

# Fonction principale
def main():
    """Fonction principale de l'IA Locale"""
    ai = AILocal()
    
    try:
        ai.start()
    except KeyboardInterrupt:
        print("Interruption par l'utilisateur")
        ai.stop()

if __name__ == "__main__":
    main()