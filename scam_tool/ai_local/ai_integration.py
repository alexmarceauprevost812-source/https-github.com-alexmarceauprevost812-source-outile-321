#!/usr/bin/env python3
"""
Intégration de l'IA Locale avec les outils du projet
Fonctionnalités d'intégration avec les outils existants
"""

import os
import sys
import json
import time
from datetime import datetime
from typing import Dict, List, Optional

# Ajout du dossier ai_local au chemin Python
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from main import AILocal
from ai_manager import AIManager
from scam_detector import ScamDetector
from network_analyzer import NetworkAnalyzer
from config import AI_CONFIG
from utils import setup_logging, load_data, save_data

class AIIntegration:
    """Classe pour l'intégration de l'IA Locale"""
    
    def __init__(self):
        """Initialisation de l'intégration"""
        self.logger = setup_logging()
        self.ai_manager = AIManager()
        self.scam_detector = ScamDetector()
        self.network_analyzer = NetworkAnalyzer()
        self.logger.info("Intégration de l'IA Locale initialisée")
    
    def integrate_with_tools(self) -> bool:
        """Intègre l'IA avec les outils existants"""
        try:
            # Création des instances d'IA
            ai_instances = [
                ("scam_detector", self.scam_detector),
                ("network_analyzer", self.network_analyzer)
            ]
            
            for name, instance in ai_instances:
                self.ai_manager.create_ai_instance(name)
            
            self.logger.info("Intégration avec les outils terminée")
            return True
            
        except Exception as e:
            self.logger.error(f"Erreur lors de l'intégration: {e}")
            return False
    
    def run_integration_cycle(self) -> Dict:
        """Exécute un cycle d'intégration"""
        try:
            results = {
                "timestamp": datetime.now().isoformat(),
                "integration_status": "running",
                "components": {
                    "scam_detector": "active",
                    "network_analyzer": "active"
                }
            }
            
            # Mise à jour des composants
            self.scam_detector.load_known_scams()
            
            self.logger.info("Cycle d'intégration exécuté")
            return results
            
        except Exception as e:
            self.logger.error(f"Erreur lors du cycle d'intégration: {e}")
            return {
                "timestamp": datetime.now().isoformat(),
                "error": str(e)
            }
    
    def get_integration_status(self) -> Dict:
        """Retourne l'état de l'intégration"""
        try:
            return {
                "timestamp": datetime.now().isoformat(),
                "status": "operational",
                "components": {
                    "ai_manager": "active",
                    "scam_detector": "active",
                    "network_analyzer": "active"
                },
                "total_instances": len(self.ai_manager.list_ai_instances())
            }
            
        except Exception as e:
            self.logger.error(f"Erreur lors de la récupération de l'état: {e}")
            return {
                "timestamp": datetime.now().isoformat(),
                "error": str(e)
            }
    
    def export_integration_data(self, output_file: str) -> bool:
        """Exporte les données d'intégration"""
        try:
            # Récupération des données
            integration_data = self.get_integration_status()
            
            # Sauvegarde dans un fichier
            with open(output_file, 'w') as f:
                json.dump(integration_data, f, indent=2)
            
            self.logger.info(f"Données d'intégration exportées vers {output_file}")
            return True
            
        except Exception as e:
            self.logger.error(f"Erreur lors de l'exportation: {e}")
            return False
    
    def import_integration_data(self, input_file: str) -> bool:
        """Importe les données d'intégration"""
        try:
            # Lecture depuis un fichier
            with open(input_file, 'r') as f:
                integration_data = json.load(f)
            
            # Validation des données
            if "status" in integration_data:
                self.logger.info(f"Données d'intégration importées depuis {input_file}")
                return True
            
            self.logger.error("Données d'intégration invalides")
            return False
            
        except Exception as e:
            self.logger.error(f"Erreur lors de l'importation: {e}")
            return False

def main():
    """Point d'entrée principal pour l'intégration"""
    integration = AIIntegration()
    
    # Intégration avec les outils
    success = integration.integrate_with_tools()
    print(f"Intégration réussie: {success}")
    
    # Exécution d'un cycle
    cycle_results = integration.run_integration_cycle()
    print(f"Résultats du cycle: {cycle_results}")
    
    # Statut de l'intégration
    status = integration.get_integration_status()
    print(f"Statut de l'intégration: {status}")

if __name__ == "__main__":
    main()