"""
Intégration d'IA pour l'IA Locale
Permet d'intégrer les différents composants de l'IA
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
from ai_manager import AIManager
from ai_monitor import AIMonitor
from scam_detector import ScamDetector
from network_analyzer import NetworkAnalyzer

class AIIntegration:
    """Classe pour intégrer les différents composants de l'IA"""
    
    def __init__(self):
        """Initialisation de l'intégration d'IA"""
        self.logger = setup_logging()
        self.ai_manager = AIManager()
        self.monitor = AIMonitor()
        self.scam_detector = ScamDetector()
        self.network_analyzer = NetworkAnalyzer()
        self.is_running = False
        self.logger.info("Intégration d'IA initialisée")
    
    def start_integration(self):
        """Démarre l'intégration des composants"""
        if self.is_running:
            self.logger.warning("L'intégration est déjà en cours")
            return False
        
        # Ajout des composants au gestionnaire
        self.ai_manager.add_component("monitor", "ai_monitor", "AIMonitor")
        self.ai_manager.add_component("scam_detector", "scam_detector", "ScamDetector")
        self.ai_manager.add_component("network_analyzer", "network_analyzer", "NetworkAnalyzer")
        
        # Démarrage des composants
        self.ai_manager.start_all_components()
        
        # Démarrage du monitoring
        self.monitor.start_monitoring()
        
        # Démarrage du détecteur d'escroqueries
        self.scam_detector.start_monitoring()
        
        # Démarrage de l'analyseur réseau
        self.network_analyzer.start_analysis()
        
        self.is_running = True
        self.logger.info("Intégration d'IA démarrée")
        return True
    
    def stop_integration(self):
        """Arrête l'intégration des composants"""
        self.is_running = False
        
        # Arrêt des composants
        self.ai_manager.stop_all_components()
        
        # Arrêt du monitoring
        self.monitor.stop_monitoring()
        
        # Arrêt du détecteur d'escroqueries
        self.scam_detector.stop_monitoring()
        
        # Arrêt de l'analyseur réseau
        self.network_analyzer.stop_analysis()
        
        self.logger.info("Intégration d'IA arrêtée")
    
    def get_system_status(self) -> Dict:
        """Retourne l'état du système"""
        try:
            return {
                "status": "running" if self.is_running else "stopped",
                "components": self.ai_manager.get_all_components_status(),
                "timestamp": datetime.now().isoformat()
            }
        except Exception as e:
            self.logger.error(f"Erreur lors de la récupération de l'état du système: {e}")
            return {}
    
    def get_performance_metrics(self) -> Dict:
        """Retourne les métriques de performance"""
        try:
            metrics = {}
            
            # Récupération des métriques du monitor
            monitor_metrics = self.monitor.get_current_metrics()
            metrics["monitor"] = monitor_metrics
            
            # Récupération des métriques du détecteur d'escroqueries
            scam_metrics = {
                "suspicious_ips": self.scam_detector.get_suspicious_ips(),
                "suspicious_ports": self.scam_detector.get_suspicious_ports(),
                "packet_history_count": len(self.scam_detector.get_packet_history()),
                "alerts_count": len(self.scam_detector.get_alerts())
            }
            metrics["scam_detector"] = scam_metrics
            
            # Récupération des métriques de l'analyseur réseau
            network_stats = self.network_analyzer.get_network_stats()
            metrics["network_analyzer"] = network_stats
            
            return metrics
        except Exception as e:
            self.logger.error(f"Erreur lors de la récupération des métriques: {e}")
            return {}
    
    def get_alerts(self) -> List[Dict]:
        """Retourne les alertes système"""
        try:
            alerts = []
            
            # Récupération des alertes du détecteur d'escroqueries
            scam_alerts = self.scam_detector.get_alerts()
            for alert in scam_alerts:
                alert["source"] = "scam_detector"
                alerts.append(alert)
            
            # Récupération des alertes du monitor
            # (Cela pourrait impliquer une vérification de l'état de santé du système)
            monitor_alerts = self.monitor.get_system_status()
            if monitor_alerts.get("status") != "healthy":
                alerts.append({
                    "source": "monitor",
                    "type": "system_health",
                    "details": monitor_alerts,
                    "timestamp": datetime.now().isoformat()
                })
            
            return alerts
        except Exception as e:
            self.logger.error(f"Erreur lors de la récupération des alertes: {e}")
            return []
    
    def export_data(self, file_path: str = "data/integration_data.json") -> bool:
        """Exporte les données dans un fichier"""
        try:
            data = {
                "system_status": self.get_system_status(),
                "performance_metrics": self.get_performance_metrics(),
                "alerts": self.get_alerts(),
                "exported_at": datetime.now().isoformat()
            }
            
            # Création du dossier si nécessaire
            dir_name = os.path.dirname(file_path)
            if dir_name and not os.path.exists(dir_name):
                os.makedirs(dir_name)
            
            with open(file_path, 'w') as f:
                json.dump(data, f, indent=2)
            
            self.logger.info(f"Données exportées: {file_path}")
            return True
        except Exception as e:
            self.logger.error(f"Erreur lors de l'exportation des données: {e}")
            return False
    
    def health_check(self) -> Dict:
        """Vérifie l'état de santé du système"""
        try:
            health = {
                "status": "healthy",
                "checks": [],
                "timestamp": datetime.now().isoformat()
            }
            
            # Vérification de l'état du système
            system_status = self.get_system_status()
            if system_status.get("status") != "running":
                health["status"] = "unhealthy"
                health["checks"].append({
                    "component": "system",
                    "status": system_status.get("status"),
                    "message": "System not running"
                })
            
            # Vérification des composants
            components_status = self.ai_manager.get_all_components_status()
            for component_name, status in components_status.items():
                if status != "active" and status != "running":
                    health["status"] = "unhealthy"
                    health["checks"].append({
                        "component": component_name,
                        "status": status,
                        "message": f"Component {component_name} not active"
                    })
            
            return health
        except Exception as e:
            self.logger.error(f"Erreur lors de la vérification de l'état de santé: {e}")
            return {"status": "error", "message": str(e)}

# Exemple d'utilisation
if __name__ == "__main__":
    # Création d'une instance de l'intégration
    integration = AIIntegration()
    
    # Démarrage de l'intégration
    integration.start_integration()
    
    # Affichage de l'état du système
    print("État du système:", integration.get_system_status())
    
    # Affichage des métriques de performance
    print("Métriques de performance:", integration.get_performance_metrics())
    
    # Vérification de l'état de santé
    print("État de santé:", integration.health_check())
    
    # Exportation des données
    integration.export_data()
    
    # Arrêt de l'intégration
    integration.stop_integration()