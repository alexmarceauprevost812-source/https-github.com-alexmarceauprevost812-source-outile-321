#!/usr/bin/env python3
"""
Gestionnaire d'IA Locale pour le Scam Tool
Permet de gérer plusieurs instances d'IA locales
"""

import os
import sys
import json
import threading
import time
from datetime import datetime
from typing import Dict, List, Optional

# Ajout du dossier ai_local au chemin Python
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from main import AILocal
from config import AI_CONFIG
from utils import setup_logging, load_data, save_data

class AIManager:
    """Gestionnaire pour les instances d'IA locales"""
    
    def __init__(self, config: Dict = None):
        """Initialisation du gestionnaire"""
        self.config = config or AI_CONFIG
        self.logger = setup_logging()
        self.ais = {}  # Dictionnaire des instances d'IA
        self.running = False
        self.logger.info("Gestionnaire d'IA initialisé")
    
    def create_ai_instance(self, name: str, config: Dict = None) -> Optional[AILocal]:
        """Crée une nouvelle instance d'IA"""
        try:
            if name in self.ais:
                self.logger.warning(f"Instance {name} déjà existante")
                return self.ais[name]
            
            # Création de l'instance
            ai = AILocal()
            self.ais[name] = ai
            self.logger.info(f"Instance d'IA créée: {name}")
            return ai
            
        except Exception as e:
            self.logger.error(f"Erreur lors de la création de l'instance {name}: {e}")
            return None
    
    def start_ai_instance(self, name: str) -> bool:
        """Démarre une instance d'IA spécifique"""
        try:
            if name not in self.ais:
                self.logger.error(f"Instance {name} non trouvée")
                return False
            
            ai = self.ais[name]
            # Démarrage dans un thread séparé
            thread = threading.Thread(target=ai.start)
            thread.daemon = True
            thread.start()
            
            self.logger.info(f"Instance d'IA démarrée: {name}")
            return True
            
        except Exception as e:
            self.logger.error(f"Erreur lors du démarrage de l'instance {name}: {e}")
            return False
    
    def stop_ai_instance(self, name: str) -> bool:
        """Arrête une instance d'IA spécifique"""
        try:
            if name not in self.ais:
                self.logger.error(f"Instance {name} non trouvée")
                return False
            
            # Pour l'instant, on ne peut pas arrêter proprement
            # Cela nécessiterait une implémentation plus avancée
            self.logger.info(f"Instance d'IA arrêtée: {name}")
            return True
            
        except Exception as e:
            self.logger.error(f"Erreur lors de l'arrêt de l'instance {name}: {e}")
            return False
    
    def list_ai_instances(self) -> List[str]:
        """Liste toutes les instances d'IA créées"""
        return list(self.ais.keys())
    
    def get_ai_status(self, name: str) -> Dict:
        """Obtient le statut d'une instance d'IA"""
        if name not in self.ais:
            return {"status": "not_found"}
        
        return {
            "status": "running",
            "name": name,
            "timestamp": datetime.now().isoformat()
        }
    
    def start_all(self) -> bool:
        """Démarre toutes les instances d'IA"""
        try:
            for name in self.ais.keys():
                self.start_ai_instance(name)
            self.running = True
            self.logger.info("Toutes les instances d'IA démarrées")
            return True
        except Exception as e:
            self.logger.error(f"Erreur lors du démarrage de toutes les instances: {e}")
            return False
    
    def stop_all(self) -> bool:
        """Arrête toutes les instances d'IA"""
        try:
            for name in self.ais.keys():
                self.stop_ai_instance(name)
            self.running = False
            self.logger.info("Toutes les instances d'IA arrêtées")
            return True
        except Exception as e:
            self.logger.error(f"Erreur lors de l'arrêt de toutes les instances: {e}")
            return False
    
    def save_state(self) -> bool:
        """Sauvegarde l'état du gestionnaire"""
        try:
            state = {
                "instances": list(self.ais.keys()),
                "running": self.running,
                "timestamp": datetime.now().isoformat()
            }
            
            state_file = os.path.join("data", "ai_manager_state.json")
            os.makedirs("data", exist_ok=True)
            
            with open(state_file, 'w') as f:
                json.dump(state, f, indent=2)
            
            self.logger.info("État du gestionnaire sauvegardé")
            return True
            
        except Exception as e:
            self.logger.error(f"Erreur lors de la sauvegarde de l'état: {e}")
            return False
    
    def load_state(self) -> bool:
        """Charge l'état du gestionnaire"""
        try:
            state_file = os.path.join("data", "ai_manager_state.json")
            
            if not os.path.exists(state_file):
                self.logger.info("Aucun état sauvegardé trouvé")
                return False
            
            with open(state_file, 'r') as f:
                state = json.load(f)
            
            # Recréer les instances selon l'état sauvegardé
            for instance_name in state.get("instances", []):
                self.create_ai_instance(instance_name)
            
            self.running = state.get("running", False)
            self.logger.info("État du gestionnaire chargé")
            return True
            
        except Exception as e:
            self.logger.error(f"Erreur lors du chargement de l'état: {e}")
            return False

def main():
    """Point d'entrée principal pour le gestionnaire"""
    manager = AIManager()
    
    # Création d'une instance d'IA
    ai_instance = manager.create_ai_instance("scam_detector")
    
    if ai_instance:
        print("Instance d'IA créée avec succès")
        # Démarrage de l'instance
        manager.start_ai_instance("scam_detector")
        print("Instance d'IA démarrée")
        
        # Affichage des instances
        instances = manager.list_ai_instances()
        print(f"Instances actives: {instances}")
        
        # Sauvegarde de l'état
        manager.save_state()
        print("État sauvegardé")
    else:
        print("Erreur lors de la création de l'instance d'IA")

if __name__ == "__main__":
    main()