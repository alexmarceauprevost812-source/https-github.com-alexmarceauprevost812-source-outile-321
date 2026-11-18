"""
Moniteur d'IA pour l'IA Locale
Permet de surveiller les performances de l'IA
"""

import os
import sys
import json
import threading
import time
from datetime import datetime
from typing import Dict, List, Optional
import psutil
import platform

# Ajout du dossier ai_local au chemin Python
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from utils import setup_logging, load_data, save_data

class AIMonitor:
    """Classe pour surveiller les performances de l'IA"""
    
    def __init__(self):
        """Initialisation du moniteur d'IA"""
        self.logger = setup_logging()
        self.is_monitoring = False
        self.monitoring_interval = 5  # en secondes
        self.metrics_history = []
        self.alerts = []
        self.logger.info("Moniteur d'IA initialisé")
    
    def start_monitoring(self):
        """Démarre la surveillance"""
        if self.is_monitoring:
            self.logger.warning("La surveillance est déjà en cours")
            return False
        
        self.is_monitoring = True
        self.logger.info("Surveillance démarrée")
        
        # Démarrage du thread de surveillance
        monitor_thread = threading.Thread(target=self._monitor_loop)
        monitor_thread.daemon = True
        monitor_thread.start()
        
        return True
    
    def stop_monitoring(self):
        """Arrête la surveillance"""
        self.is_monitoring = False
        self.logger.info("Surveillance arrêtée")
    
    def _monitor_loop(self):
        """Boucle principale de surveillance"""
        while self.is_monitoring:
            try:
                # Collecte des métriques
                metrics = self._collect_metrics()
                
                # Enregistrement des métriques
                self.metrics_history.append({
                    "timestamp": datetime.now().isoformat(),
                    "metrics": metrics
                })
                
                # Vérification des alertes
                self._check_alerts(metrics)
                
                # Attente avant la prochaine collecte
                time.sleep(self.monitoring_interval)
            except Exception as e:
                self.logger.error(f"Erreur dans la boucle de surveillance: {e}")
                time.sleep(self.monitoring_interval)
    
    def _collect_metrics(self) -> Dict:
        """Collecte les métriques système"""
        try:
            # Métriques CPU
            cpu_percent = psutil.cpu_percent(interval=1)
            cpu_count = psutil.cpu_count()
            
            # Métriques Mémoire
            memory = psutil.virtual_memory()
            memory_percent = memory.percent
            
            # Métriques Disque
            disk = psutil.disk_usage('/')
            disk_percent = (disk.used / disk.total) * 100
            
            # Métriques Réseau
            net_io = psutil.net_io_counters()
            bytes_sent = net_io.bytes_sent
            bytes_recv = net_io.bytes_recv
            
            # Métriques Processus
            processes = []
            for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
                try:
                    processes.append(proc.info)
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    pass
            
            # Retour des métriques
            return {
                "timestamp": datetime.now().isoformat(),
                "system": {
                    "platform": platform.system(),
                    "platform_version": platform.version(),
                    "processor": platform.processor()
                },
                "cpu": {
                    "percent": cpu_percent,
                    "count": cpu_count
                },
                "memory": {
                    "percent": memory_percent,
                    "total": memory.total,
                    "available": memory.available,
                    "used": memory.used
                },
                "disk": {
                    "percent": disk_percent,
                    "total": disk.total,
                    "used": disk.used,
                    "free": disk.free
                },
                "network": {
                    "bytes_sent": bytes_sent,
                    "bytes_recv": bytes_recv
                },
                "processes": {
                    "count": len(processes),
                    "top_processes": sorted(processes, key=lambda x: x['cpu_percent'], reverse=True)[:5]
                }
            }
        except Exception as e:
            self.logger.error(f"Erreur lors de la collecte des métriques: {e}")
            return {}
    
    def _check_alerts(self, metrics: Dict):
        """Vérifie si des alertes doivent être générées"""
        try:
            # Vérification des seuils critiques
            cpu_percent = metrics.get("cpu", {}).get("percent", 0)
            memory_percent = metrics.get("memory", {}).get("percent", 0)
            disk_percent = metrics.get("disk", {}).get("percent", 0)
            
            # Vérification des seuils
            if cpu_percent > 80:
                alert = {
                    "timestamp": datetime.now().isoformat(),
                    "type": "cpu_usage",
                    "value": cpu_percent,
                    "threshold": 80,
                    "message": f"Usage CPU élevé: {cpu_percent}%"
                }
                self.alerts.append(alert)
                self.logger.warning(f"Alerte CPU: {cpu_percent}%")
            
            if memory_percent > 80:
                alert = {
                    "timestamp": datetime.now().isoformat(),
                    "type": "memory_usage",
                    "value": memory_percent,
                    "threshold": 80,
                    "message": f"Usage mémoire élevé: {memory_percent}%"
                }
                self.alerts.append(alert)
                self.logger.warning(f"Alerte mémoire: {memory_percent}%")
            
            if disk_percent > 80:
                alert = {
                    "timestamp": datetime.now().isoformat(),
                    "type": "disk_usage",
                    "value": disk_percent,
                    "threshold": 80,
                    "message": f"Utilisation disque élevée: {disk_percent}%"
                }
                self.alerts.append(alert)
                self.logger.warning(f"Alerte disque: {disk_percent}%")
        except Exception as e:
            self.logger.error(f"Erreur lors de la vérification des alertes: {e}")
    
    def get_current_metrics(self) -> Dict:
        """Retourne les métriques actuelles"""
        try:
            if self.metrics_history:
                return self.metrics_history[-1]["metrics"]
            return {}
        except Exception as e:
            self.logger.error(f"Erreur lors de la récupération des métriques actuelles: {e}")
            return {}
    
    def get_metrics_history(self) -> List[Dict]:
        """Retourne l'historique des métriques"""
        return self.metrics_history
    
    def get_alerts(self) -> List[Dict]:
        """Retourne les alertes générées"""
        return self.alerts
    
    def get_system_status(self) -> Dict:
        """Retourne l'état du système"""
        try:
            # Vérification de l'état de santé global
            health = {
                "status": "healthy",
                "timestamp": datetime.now().isoformat()
            }
            
            # Vérification des alertes récentes
            recent_alerts = [alert for alert in self.alerts if 
                            datetime.fromisoformat(alert["timestamp"]).timestamp() > 
                            (datetime.now().timestamp() - 300)]  # Dernières 5 minutes
            
            if recent_alerts:
                health["status"] = "unhealthy"
                health["recent_alerts"] = len(recent_alerts)
            
            return health
        except Exception as e:
            self.logger.error(f"Erreur lors de la récupération de l'état du système: {e}")
            return {}
    
    def clear_history(self):
        """Efface l'historique"""
        self.metrics_history.clear()
        self.alerts.clear()
        self.logger.info("Historique effacé")
    
    def export_data(self, file_path: str = "data/monitor_data.json") -> bool:
        """Exporte les données dans un fichier"""
        try:
            data = {
                "metrics_history": self.metrics_history,
                "alerts": self.alerts,
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
    
    def import_data(self, file_path: str) -> bool:
        """Importe les données depuis un fichier"""
        try:
            if os.path.exists(file_path):
                with open(file_path, 'r') as f:
                    data = json.load(f)
                
                self.metrics_history = data.get("metrics_history", [])
                self.alerts = data.get("alerts", [])
                
                self.logger.info(f"Données importées: {file_path}")
                return True
            else:
                self.logger.warning(f"Fichier non trouvé: {file_path}")
                return False
        except Exception as e:
            self.logger.error(f"Erreur lors de l'importation des données: {e}")
            return False

# Exemple d'utilisation
if __name__ == "__main__":
    # Création d'une instance du moniteur
    monitor = AIMonitor()
    
    # Démarrage de la surveillance
    monitor.start_monitoring()
    
    # Attente pour collecter des données
    time.sleep(10)
    
    # Affichage des métriques actuelles
    current_metrics = monitor.get_current_metrics()
    print("Métriques actuelles:", current_metrics)
    
    # Affichage des alertes
    alerts = monitor.get_alerts()
    print("Alertes:", alerts)
    
    # Exportation des données
    monitor.export_data()
    
    # Arrêt de la surveillance
    monitor.stop_monitoring()