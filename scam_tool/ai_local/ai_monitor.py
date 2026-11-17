#!/usr/bin/env python3
"""
Moniteur d'IA Locale
Surveille l'état et les performances de l'IA Locale
"""

import os
import sys
import json
import time
import threading
from datetime import datetime
from typing import Dict, List, Optional
import logging

# Ajout du dossier ai_local au chemin Python
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from config import AI_CONFIG
from utils import setup_logging, load_data, save_data

class AIMonitor:
    """Classe pour le moniteur d'IA Locale"""
    
    def __init__(self):
        """Initialisation du moniteur"""
        self.logger = setup_logging()
        self.monitoring = False
        self.monitoring_thread = None
        self.metrics = {
            "cpu_usage": 0,
            "memory_usage": 0,
            "disk_usage": 0,
            "network_io": 0,
            "timestamp": datetime.now().isoformat()
        }
        self.logger.info("Moniteur d'IA initialisé")
    
    def start_monitoring(self, interval: int = 5):
        """Démarre la surveillance"""
        def monitoring_loop():
            self.monitoring = True
            self.logger.info(f"Surveillance démarrée avec intervalle {interval}s")
            
            while self.monitoring:
                try:
                    # Collecte des métriques système
                    self._collect_system_metrics()
                    
                    # Enregistrement des métriques
                    self._save_metrics()
                    
                    # Attendre l'intervalle
                    time.sleep(interval)
                    
                except Exception as e:
                    self.logger.error(f"Erreur dans la boucle de surveillance: {e}")
                    time.sleep(interval)
        
        # Démarrage dans un thread séparé
        self.monitoring_thread = threading.Thread(target=monitoring_loop, daemon=True)
        self.monitoring_thread.start()
        
        return self.monitoring_thread
    
    def stop_monitoring(self):
        """Arrête la surveillance"""
        self.monitoring = False
        if self.monitoring_thread:
            self.monitoring_thread.join()
        self.logger.info("Surveillance arrêtée")
    
    def _collect_system_metrics(self):
        """Collecte les métriques système"""
        try:
            # Pour l'instant, on simule les métriques
            # Dans une version réelle, on utiliserait psutil
            import random
            
            # Utilisation CPU (simulation)
            cpu_percent = random.randint(10, 70)
            
            # Utilisation mémoire (simulation)
            memory_percent = random.randint(20, 80)
            
            # Utilisation disque (simulation)
            disk_percent = random.randint(30, 70)
            
            # I/O réseau (simulation)
            network_io = random.randint(1000000, 10000000)
            
            # Mise à jour des métriques
            self.metrics = {
                "cpu_usage": cpu_percent,
                "memory_usage": memory_percent,
                "disk_usage": disk_percent,
                "network_io": network_io,
                "timestamp": datetime.now().isoformat()
            }
            
            # Logging des métriques
            self.logger.debug(f"Métriques collectées: CPU={cpu_percent}%, "
                            f"Memory={memory_percent}%, Disk={disk_percent}%")
            
        except Exception as e:
            self.logger.error(f"Erreur lors de la collecte des métriques: {e}")
    
    def _save_metrics(self):
        """Sauvegarde les métriques dans un fichier"""
        try:
            os.makedirs("data", exist_ok=True)
            metrics_file = "data/ai_metrics.json"
            
            with open(metrics_file, 'w') as f:
                json.dump(self.metrics, f, indent=2)
            
        except Exception as e:
            self.logger.error(f"Erreur lors de la sauvegarde des métriques: {e}")
    
    def get_metrics(self) -> Dict:
        """Retourne les métriques actuelles"""
        return self.metrics.copy()
    
    def get_system_status(self) -> Dict:
        """Retourne l'état du système"""
        try:
            # Pour l'instant, on simule les informations système
            import random
            
            return {
                "cpu_count": 4,  # Simulation
                "memory_total": 8192 * 1024 * 1024,  # 8GB en bytes
                "memory_available": random.randint(1000 * 1024 * 1024, 6000 * 1024 * 1024),  # 1-6GB
                "memory_percent": random.randint(20, 80),
                "disk_total": 500 * 1024 * 1024 * 1024,  # 500GB
                "disk_used": random.randint(100 * 1024 * 1024 * 1024, 400 * 1024 * 1024 * 1024),  # 100-400GB
                "disk_percent": random.randint(30, 70),
                "timestamp": datetime.now().isoformat()
            }
            
        except Exception as e:
            self.logger.error(f"Erreur lors de la récupération de l'état système: {e}")
            return {
                "error": str(e),
                "timestamp": datetime.now().isoformat()
            }
    
    def check_performance(self) -> Dict:
        """Vérifie les performances de l'IA"""
        try:
            metrics = self.get_metrics()
            system_status = self.get_system_status()
            
            # Vérification des seuils critiques
            warnings = []
            
            if metrics.get("cpu_usage", 0) > 80:
                warnings.append("CPU usage high")
            
            if metrics.get("memory_usage", 0) > 80:
                warnings.append("Memory usage high")
            
            if metrics.get("disk_usage", 0) > 80:
                warnings.append("Disk usage high")
            
            return {
                "performance": {
                    "cpu_usage": metrics.get("cpu_usage", 0),
                    "memory_usage": metrics.get("memory_usage", 0),
                    "disk_usage": metrics.get("disk_usage", 0),
                    "network_io": metrics.get("network_io", 0)
                },
                "system_status": system_status,
                "warnings": warnings,
                "timestamp": datetime.now().isoformat()
            }
            
        except Exception as e:
            self.logger.error(f"Erreur lors de la vérification des performances: {e}")
            return {
                "error": str(e),
                "timestamp": datetime.now().isoformat()
            }
    
    def generate_report(self) -> Dict:
        """Génère un rapport de surveillance"""
        try:
            performance = self.check_performance()
            
            return {
                "report": {
                    "timestamp": datetime.now().isoformat(),
                    "performance": performance,
                    "uptime": "running"  # À implémenter avec un compteur
                }
            }
            
        except Exception as e:
            self.logger.error(f"Erreur lors de la génération du rapport: {e}")
            return {
                "error": str(e),
                "timestamp": datetime.now().isoformat()
            }

def main():
    """Point d'entrée principal pour le moniteur"""
    monitor = AIMonitor()
    
    # Démarrage de la surveillance
    monitor.start_monitoring(interval=3)
    print("Surveillance démarrée...")
    
    # Attendre quelques secondes
    time.sleep(10)
    
    # Obtenir les métriques
    metrics = monitor.get_metrics()
    print(f"Métriques actuelles: {metrics}")
    
    # Obtenir l'état système
    system_status = monitor.get_system_status()
    print(f"État système: {system_status}")
    
    # Vérifier les performances
    performance = monitor.check_performance()
    print(f"Performances: {performance}")
    
    # Générer un rapport
    report = monitor.generate_report()
    print(f"Rapport: {report}")
    
    # Arrêter la surveillance
    monitor.stop_monitoring()
    print("Surveillance arrêtée")

if __name__ == "__main__":
    main()