"""
Détecteur de escroqueries pour l'IA Locale
Permet de détecter les escroqueries dans le trafic réseau
"""

import os
import sys
import json
import threading
import time
from datetime import datetime
from typing import Dict, List, Optional
import socket
import struct

# Ajout du dossier ai_local au chemin Python
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from utils import setup_logging, load_data, save_data

class ScamDetector:
    """Classe pour détecter les escroqueries"""
    
    def __init__(self):
        """Initialisation du détecteur d'escroqueries"""
        self.logger = setup_logging()
        self.suspicious_ips = set()
        self.suspicious_ports = set()
        self.packet_history = []
        self.alerts = []
        self.is_monitoring = False
        self.logger.info("Détecteur d'escroqueries initialisé")
    
    def start_monitoring(self):
        """Démarre la surveillance du trafic"""
        if self.is_monitoring:
            self.logger.warning("La surveillance est déjà en cours")
            return False
        
        self.is_monitoring = True
        self.logger.info("Surveillance du trafic démarrée")
        return True
    
    def stop_monitoring(self):
        """Arrête la surveillance du trafic"""
        self.is_monitoring = False
        self.logger.info("Surveillance du trafic arrêtée")
    
    def add_suspicious_ip(self, ip_address: str):
        """Ajoute une adresse IP suspecte"""
        try:
            # Validation de l'adresse IP
            socket.inet_aton(ip_address)
            self.suspicious_ips.add(ip_address)
            self.logger.info(f"Adresse IP suspecte ajoutée: {ip_address}")
        except socket.error:
            self.logger.warning(f"Adresse IP invalide: {ip_address}")
    
    def remove_suspicious_ip(self, ip_address: str):
        """Supprime une adresse IP suspecte"""
        if ip_address in self.suspicious_ips:
            self.suspicious_ips.remove(ip_address)
            self.logger.info(f"Adresse IP suspecte supprimée: {ip_address}")
    
    def add_suspicious_port(self, port: int):
        """Ajoute un port suspect"""
        if 0 <= port <= 65535:
            self.suspicious_ports.add(port)
            self.logger.info(f"Port suspect ajouté: {port}")
        else:
            self.logger.warning(f"Port invalide: {port}")
    
    def remove_suspicious_port(self, port: int):
        """Supprime un port suspect"""
        if port in self.suspicious_ports:
            self.suspicious_ports.remove(port)
            self.logger.info(f"Port suspect supprimé: {port}")
    
    def analyze_packet(self, packet_data: Dict) -> Dict:
        """Analyse un paquet réseau pour détecter les escroqueries"""
        try:
            # Vérification des données du paquet
            if not self._validate_packet_data(packet_data):
                self.logger.warning("Données de paquet invalides")
                return {"status": "error", "message": "Invalid packet data"}
            
            # Analyse du paquet
            analysis = self._perform_scam_analysis(packet_data)
            
            # Ajout à l'historique
            self.packet_history.append({
                "timestamp": datetime.now().isoformat(),
                "packet": packet_data,
                "analysis": analysis
            })
            
            # Vérification des alertes
            self._check_alerts(analysis)
            
            return analysis
        except Exception as e:
            self.logger.error(f"Erreur lors de l'analyse du paquet: {e}")
            return {"status": "error", "message": str(e)}
    
    def _validate_packet_data(self, packet_data: Dict) -> bool:
        """Valide les données d'un paquet"""
        required_fields = ["source_ip", "destination_ip", "protocol", "timestamp"]
        for field in required_fields:
            if field not in packet_data:
                return False
        return True
    
    def _perform_scam_analysis(self, packet_data: Dict) -> Dict:
        """Effectue l'analyse détaillée pour détecter les escroqueries"""
        try:
            analysis = {
                "timestamp": packet_data["timestamp"],
                "source_ip": packet_data["source_ip"],
                "destination_ip": packet_data["destination_ip"],
                "protocol": packet_data["protocol"],
                "is_scam": False,
                "reasons": [],
                "confidence": 0.0
            }
            
            # Vérification des adresses IP suspectes
            if packet_data["source_ip"] in self.suspicious_ips:
                analysis["is_scam"] = True
                analysis["reasons"].append("Adresse IP source suspecte")
            
            if packet_data["destination_ip"] in self.suspicious_ips:
                analysis["is_scam"] = True
                analysis["reasons"].append("Adresse IP destination suspecte")
            
            # Vérification des ports suspectes
            if "source_port" in packet_data and packet_data["source_port"] in self.suspicious_ports:
                analysis["is_scam"] = True
                analysis["reasons"].append("Port source suspect")
            
            if "destination_port" in packet_data and packet_data["destination_port"] in self.suspicious_ports:
                analysis["is_scam"] = True
                analysis["reasons"].append("Port destination suspect")
            
            # Vérification de la taille du paquet
            if "packet_size" in packet_data:
                if packet_data["packet_size"] > 1500:  # Taille maximale Ethernet
                    analysis["is_scam"] = True
                    analysis["reasons"].append("Taille de paquet excessive")
            
            # Calcul du niveau de confiance (simplifié)
            if analysis["reasons"]:
                analysis["confidence"] = min(len(analysis["reasons"]) * 0.33, 1.0)
            
            return analysis
        except Exception as e:
            self.logger.error(f"Erreur lors de l'analyse des escroqueries: {e}")
            return {"status": "error", "message": str(e)}
    
    def _check_alerts(self, analysis: Dict):
        """Vérifie si des alertes doivent être générées"""
        if analysis["is_scam"]:
            alert = {
                "timestamp": datetime.now().isoformat(),
                "type": "scam_detected",
                "details": analysis,
                "confidence": analysis["confidence"]
            }
            self.alerts.append(alert)
            self.logger.warning(f"Escroquerie détectée: {analysis}")
    
    def get_suspicious_ips(self) -> List[str]:
        """Retourne la liste des adresses IP suspectes"""
        return list(self.suspicious_ips)
    
    def get_suspicious_ports(self) -> List[int]:
        """Retourne la liste des ports suspectes"""
        return list(self.suspicious_ports)
    
    def get_packet_history(self) -> List[Dict]:
        """Retourne l'historique des paquets"""
        return self.packet_history
    
    def get_alerts(self) -> List[Dict]:
        """Retourne les alertes générées"""
        return self.alerts
    
    def clear_history(self):
        """Efface l'historique"""
        self.packet_history.clear()
        self.alerts.clear()
        self.logger.info("Historique effacé")
    
    def export_data(self, file_path: str = "data/scam_data.json") -> bool:
        """Exporte les données dans un fichier"""
        try:
            data = {
                "suspicious_ips": list(self.suspicious_ips),
                "suspicious_ports": list(self.suspicious_ports),
                "packet_history": self.packet_history,
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
                
                self.suspicious_ips = set(data.get("suspicious_ips", []))
                self.suspicious_ports = set(data.get("suspicious_ports", []))
                self.packet_history = data.get("packet_history", [])
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
    # Création d'une instance du détecteur
    detector = ScamDetector()
    
    # Ajout d'adresses IP suspectes
    detector.add_suspicious_ip("192.168.1.100")
    detector.add_suspicious_ip("10.0.0.1")
    
    # Ajout de ports suspectes
    detector.add_suspicious_port(23)
    detector.add_suspicious_port(25)
    
    # Démarrage de la surveillance
    detector.start_monitoring()
    
    # Analyse de paquets
    packet1 = {
        "source_ip": "192.168.1.100",
        "destination_ip": "8.8.8.8",
        "protocol": "TCP",
        "source_port": 23,
        "destination_port": 80,
        "packet_size": 1000,
        "timestamp": datetime.now().isoformat()
    }
    
    packet2 = {
        "source_ip": "10.0.0.1",
        "destination_ip": "1.1.1.1",
        "protocol": "UDP",
        "source_port": 53,
        "destination_port": 53,
        "packet_size": 500,
        "timestamp": datetime.now().isoformat()
    }
    
    # Analyse des paquets
    result1 = detector.analyze_packet(packet1)
    result2 = detector.analyze_packet(packet2)
    
    print("Résultat 1:", result1)
    print("Résultat 2:", result2)
    
    # Affichage des alertes
    print("Alertes:", detector.get_alerts())
    
    # Exportation des données
    detector.export_data()