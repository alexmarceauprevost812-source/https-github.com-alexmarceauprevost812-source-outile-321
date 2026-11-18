"""
Gestionnaire d'IA pour l'IA Locale
Permet de gérer les différents composants de l'IA
"""

import os
import sys
import json
import threading
import time
from datetime import datetime
from typing import Dict, List, Optional
import importlib

# Ajout du dossier ai_local au chemin Python
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from utils import setup_logging, load_data, save_data
from ai_monitor import AIMonitor
from ai_integration import AIIntegration

class AIManager:
    """Classe pour gérer les composants de l'IA"""
    
    def __init__(self):
        """Initialisation du gestionnaire d'IA"""
        self.logger = setup_logging()
        self.components = {}
        self.status = "initialized"
        self.logger.info("Gestionnaire d'IA initialisé")
    
    def add_component(self, component_name: str, component_module: str, component_class: str) -> bool:
        """Ajoute un composant à la gestion"""
        try:
            # Vérification si le composant existe déjà
            if component_name in self.components:
                self.logger.warning(f"Composant déjà ajouté: {component_name}")
                return False
            
            # Chargement du module
            module = importlib.import_module(component_module)
            component_class_obj = getattr(module, component_class)
            
            # Création de l'instance du composant
            component_instance = component_class_obj()
            
            # Enregistrement du composant
            self.components[component_name] = {
                "module": component_module,
                "class": component_class,
                "instance": component_instance,
                "status": "active",
                "added_at": datetime.now().isoformat()
            }
            
            self.logger.info(f"Composant ajouté avec succès: {component_name}")
            return True
        except Exception as e:
            self.logger.error(f"Erreur lors de l'ajout du composant {component_name}: {e}")
            return False
    
    def remove_component(self, component_name: str) -> bool:
        """Supprime un composant de la gestion"""
        try:
            if component_name not in self.components:
                self.logger.warning(f"Composant non trouvé: {component_name}")
                return False
            
            # Suppression du composant
            del self.components[component_name]
            
            self.logger.info(f"Composant supprimé: {component_name}")
            return True
        except Exception as e:
            self.logger.error(f"Erreur lors de la suppression du composant {component_name}: {e}")
            return False
    
    def get_component_status(self, component_name: str) -> str:
        """Retourne le statut d'un composant"""
        component = self.components.get(component_name)
        if component:
            return component["status"]
        return "unknown"
    
    def get_all_components_status(self) -> Dict:
        """Retourne le statut de tous les composants"""
        status = {}
        for component_name in self.components.keys():
            status[component_name] = self.get_component_status(component_name)
        return status
    
    def get_component_instance(self, component_name: str) -> Optional[object]:
        """Retourne l'instance d'un composant"""
        component = self.components.get(component_name)
        if component:
            return component["instance"]
        return None
    
    def get_component_module(self, component_name: str) -> Optional[str]:
        """Retourne le module d'un composant"""
        component = self.components.get(component_name)
        if component:
            return component["module"]
        return None
    
    def get_component_class(self, component_name: str) -> Optional[str]:
        """Retourne la classe d'un composant"""
        component = self.components.get(component_name)
        if component:
            return component["class"]
        return None
    
    def list_components(self) -> List[str]:
        """Retourne la liste des composants"""
        return list(self.components.keys())
    
    def get_components_info(self) -> List[Dict]:
        """Retourne les informations de tous les composants"""
        info_list = []
        for component_name in self.components.keys():
            component = self.components[component_name]
            info_list.append({
                "name": component_name,
                "module": component["module"],
                "class": component["class"],
                "status": component["status"],
                "added_at": component["added_at"]
            })
        return info_list
    
    def start_component(self, component_name: str) -> bool:
        """Démarre un composant"""
        try:
            component = self.components.get(component_name)
            if not component:
                self.logger.warning(f"Composant non trouvé: {component_name}")
                return False
            
            # Vérification si le composant a une méthode start
            if hasattr(component["instance"], "start"):
                component["instance"].start()
                component["status"] = "running"
                self.logger.info(f"Composant démarré: {component_name}")
                return True
            else:
                self.logger.warning(f"Composant sans méthode start: {component_name}")
                return False
        except Exception as e:
            self.logger.error(f"Erreur lors du démarrage du composant {component_name}: {e}")
            return False
    
    def stop_component(self, component_name: str) -> bool:
        """Arrête un composant"""
        try:
            component = self.components.get(component_name)
            if not component:
                self.logger.warning(f"Composant non trouvé: {component_name}")
                return False
            
            # Vérification si le composant a une méthode stop
            if hasattr(component["instance"], "stop"):
                component["instance"].stop()
                component["status"] = "stopped"
                self.logger.info(f"Composant arrêté: {component_name}")
                return True
            else:
                self.logger.warning(f"Composant sans méthode stop: {component_name}")
                return False
        except Exception as e:
            self.logger.error(f"Erreur lors de l'arrêt du composant {component_name}: {e}")
            return False
    
    def start_all_components(self) -> bool:
        """Démarre tous les composants"""
        try:
            success_count = 0
            for component_name in self.components.keys():
                if self.start_component(component_name):
                    success_count += 1
            
            self.logger.info(f"Tous les composants démarrés ({success_count}/{len(self.components)})")
            return True
        except Exception as e:
            self.logger.error(f"Erreur lors du démarrage des composants: {e}")
            return False
    
    def stop_all_components(self) -> bool:
        """Arrête tous les composants"""
        try:
            success_count = 0
            for component_name in self.components.keys():
                if self.stop_component(component_name):
                    success_count += 1
            
            self.logger.info(f"Tous les composants arrêtés ({success_count}/{len(self.components)})")
            return True
        except Exception as e:
            self.logger.error(f"Erreur lors de l'arrêt des composants: {e}")
            return False
    
    def get_component_metrics(self, component_name: str) -> Dict:
        """Retourne les métriques d'un composant"""
        try:
            component = self.components.get(component_name)
            if not component:
                return {}
            
            # Vérification si le composant a une méthode get_metrics
            if hasattr(component["instance"], "get_metrics"):
                return component["instance"].get_metrics()
            else:
                self.logger.warning(f"Composant sans méthode get_metrics: {component_name}")
                return {}
        except Exception as e:
            self.logger.error(f"Erreur lors de la récupération des métriques du composant {component_name}: {e}")
            return {}
    
    def get_system_status(self) -> Dict:
        """Retourne l'état du système"""
        try:
            return {
                "status": self.status,
                "components": self.get_all_components_status(),
                "timestamp": datetime.now().isoformat()
            }
        except Exception as e:
            self.logger.error(f"Erreur lors de la récupération de l'état du système: {e}")
            return {}
    
    def health_check(self) -> Dict:
        """Vérifie l'état de santé du système"""
        try:
            health = {
                "status": "healthy",
                "checks": [],
                "timestamp": datetime.now().isoformat()
            }
            
            # Vérification de chaque composant
            for component_name, component in self.components.items():
                status = component["status"]
                if status != "active" and status != "running":
                    health["status"] = "unhealthy"
                    health["checks"].append({
                        "component": component_name,
                        "status": status,
                        "message": f"Composant {component_name} non actif"
                    })
            
            return health
        except Exception as e:
            self.logger.error(f"Erreur lors de la vérification de l'état de santé: {e}")
            return {"status": "error", "message": str(e)}
    
    def export_components(self, file_path: str = "data/components.json") -> bool:
        """Exporte les composants dans un fichier"""
        try:
            data = {
                "components": self.components,
                "exported_at": datetime.now().isoformat()
            }
            
            # Création du dossier si nécessaire
            dir_name = os.path.dirname(file_path)
            if dir_name and not os.path.exists(dir_name):
                os.makedirs(dir_name)
            
            with open(file_path, 'w') as f:
                json.dump(data, f, indent=2)
            
            self.logger.info(f"Composants exportés: {file_path}")
            return True
        except Exception as e:
            self.logger.error(f"Erreur lors de l'exportation des composants: {e}")
            return False
    
    def import_components(self, file_path: str) -> bool:
        """Importe les composants depuis un fichier"""
        try:
            if os.path.exists(file_path):
                with open(file_path, 'r') as f:
                    data = json.load(f)
                
                self.components = data.get("components", {})
                
                self.logger.info(f"Composants importés: {file_path}")
                return True
            else:
                self.logger.warning(f"Fichier non trouvé: {file_path}")
                return False
        except Exception as e:
            self.logger.error(f"Erreur lors de l'importation des composants: {e}")
            return False
    
    def clear_components(self):
        """Efface tous les composants"""
        self.components.clear()
        self.logger.info("Tous les composants ont été effacés")

# Exemple d'utilisation
if __name__ == "__main__":
    # Création d'une instance du gestionnaire
    manager = AIManager()
    
    # Ajout de composants
    print("Ajout des composants...")
    manager.add_component("monitor", "ai_monitor", "AIMonitor")
    manager.add_component("integration", "ai_integration", "AIIntegration")
    
    # Liste des composants
    print("Composants actuels:", manager.list_components())
    
    # Démarrage des composants
    print("Démarrage des composants...")
    manager.start_all_components()
    
    # Vérification de l'état du système
    print("État du système:", manager.get_system_status())
    
    # Vérification de l'état de santé
    print("État de santé:", manager.health_check())