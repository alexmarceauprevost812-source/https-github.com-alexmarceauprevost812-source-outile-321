#!/usr/bin/env python3
"""
Analyseur réseau pour l'IA Locale
Analyse les flux réseau pour détecter les activités suspectes
"""

import os
import sys
import json
import time
import threading
from datetime import datetime
from typing import Dict, List, Optional
from collections import defaultdict, deque

# Ajout du dossier ai_local au chemin Python
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from config import AI_CONFIG
from utils import setup_logging, load_data, save_data

class NetworkAnalyzer:
    """Classe pour l'analyse réseau"""
    
    def __init__(self):
        """Initialisation de l'analyseur réseau"""
        self.logger = setup_logging()
        self.connection_history = deque(maxlen=1000)  # Historique des connexions
        self.packet_stats = defaultdict(int)
        self.suspicious_activities = deque(maxlen=100)  # Activités suspectes
        self.logger.info("Analyseur réseau initialisé")
    
    def analyze_packet(self, packet_data: Dict) -> Dict:
        """Analyse un paquet réseau"""
        try:
            # Analyse des données du paquet
            analysis = {
                "timestamp": datetime.now().isoformat(),
                "packet_id": packet_data.get("id", ""),
                "source_ip": packet_data.get("source_ip", ""),
                "destination_ip": packet_data.get("destination_ip", ""),
                "protocol": packet_data.get("protocol", ""),
                "size": packet_data.get("size", 0),
                "flags": packet_data.get("flags", {}),
                "analysis": {
                    "suspicious": False,
                    "risk_level": "low",
                    "patterns_found": []
                }
            }
            
            # Vérification des motifs suspectes
            suspicious_patterns = self._check_suspicious_patterns(packet_data)
            
            if suspicious_patterns:
                analysis["analysis"]["suspicious"] = True
                analysis["analysis"]["patterns_found"] = suspicious_patterns
                analysis["analysis"]["risk_level"] = "high"
                
                # Ajout à l'historique des activités suspectes
                self.suspicious_activities.append({
                    "timestamp": analysis["timestamp"],
                    "packet_id": analysis["packet_id"],
                    "risk_level": "high",
                    "patterns": suspicious_patterns
                })
            
            # Mise à jour des statistiques
            self._update_packet_stats(packet_data)
            
            self.logger.debug(f"Analyse de paquet terminée: {analysis['packet_id']}")
            return analysis
            
        except Exception as e:
            self.logger.error(f"Erreur lors de l'analyse du paquet: {e}")
            return {
                "timestamp": datetime.now().isoformat(),
                "error": str(e)
            }
    
    def _check_suspicious_patterns(self, packet_data: Dict) -> List[str]:
        """Vérifie les motifs suspectes dans les données du paquet"""
        suspicious_patterns = []
        
        # Vérification des ports suspects
        destination_port = packet_data.get("destination_port", 0)
        if destination_port in [21, 22, 23, 25, 53, 80, 110, 143, 443, 993, 995]:
            suspicious_patterns.append("port_suspicious")
        
        # Vérification des protocoles suspects
        protocol = packet_data.get("protocol", "").lower()
        if protocol in ["tcp", "udp"]:
            suspicious_patterns.append("protocol_analyzed")
        
        # Vérification des tailles de paquets suspectes
        size = packet_data.get("size", 0)
        if size > 10000:  # Paquets très grands
            suspicious_patterns.append("packet_size_large")
        
        # Vérification des adresses IP suspectes
        source_ip = packet_data.get("source_ip", "")
        destination_ip = packet_data.get("destination_ip", "")
        
        if self._is_suspicious_ip(source_ip):
            suspicious_patterns.append("source_ip_suspicious")
        
        if self._is_suspicious_ip(destination_ip):
            suspicious_patterns.append("destination_ip_suspicious")
        
        return suspicious_patterns
    
    def _is_suspicious_ip(self, ip: str) -> bool:
        """Vérifie si une adresse IP est suspecte"""
        # Liste des IPs suspectes (à remplacer par une base de données réelle)
        suspicious_ips = [
            "192.168.1.100",
            "10.0.0.100",
            "172.16.0.100"
        ]
        
        return ip in suspicious_ips
    
    def _update_packet_stats(self, packet_data: Dict):
        """Met à jour les statistiques de paquets"""
        try:
            protocol = packet_data.get("protocol", "").lower()
            size = packet_data.get("size", 0)
            
            # Mise à jour des statistiques par protocole
            self.packet_stats[f"protocol_{protocol}"] += 1
            self.packet_stats[f"size_{size}"] += 1
            
            # Ajout à l'historique
            self.connection_history.append({
                "timestamp": datetime.now().isoformat(),
                "protocol": protocol,
                "size": size,
                "source_ip": packet_data.get("source_ip", ""),
                "destination_ip": packet_data.get("destination_ip", "")
            })
            
        except Exception as e:
            self.logger.error(f"Erreur lors de la mise à jour des statistiques: {e}")
    
    def get_network_stats(self) -> Dict:
        """Retourne les statistiques réseau"""
        return {
            "total_packets": len(self.connection_history),
            "suspicious_activities": len(self.suspicious_activities),
            "packet_stats": dict(self.packet_stats),
            "timestamp": datetime.now().isoformat()
        }
    
    def get_recent_connections(self, limit: int = 10) -> List[Dict]:
        """Retourne les connexions récentes"""
        return list(self.connection_history)[-limit:]
    
    def get_suspicious_activities(self, limit: int = 10) -> List[Dict]:
        """Retourne les activités suspectes récentes"""
        return list(self.suspicious_activities)[-limit:]
    
    def start_monitoring(self, interval: int = 5):
        """Démarre la surveillance réseau"""
        def monitoring_loop():
            while True:
                try:
                    # Simulation d'analyse de paquets
                    # Dans une version réelle, cela serait connecté à un capteur réseau
                    time.sleep(interval)
                    
                    # Ici, on pourrait intégrer avec un outil comme Scapy
                    self.logger.debug("Surveillance réseau active...")
                    
                except Exception as e:
                    self.logger.error(f"Erreur dans la boucle de surveillance: {e}")
                    time.sleep(interval)
        
        # Démarrage dans un thread séparé
        monitor_thread = threading.Thread(target=monitoring_loop, daemon=True)
        monitor_thread.start()
        self.logger.info("Surveillance réseau démarrée")
        
        return monitor_thread
    
    def stop_monitoring(self):
        """Arrête la surveillance réseau"""
        self.logger.info("Surveillance réseau arrêtée")

def main():
    """Point d'entrée principal pour l'analyseur"""
    analyzer = NetworkAnalyzer()
    
    # Exemple de données de paquet à analyser
    test_packets = [
        {
            "id": "pkt_001",
            "source_ip": "192.168.1.10",
            "destination_ip": "192.168.1.1",
            "protocol": "TCP",
            "destination_port": 80,
            "size": 1500,
            "flags": {"SYN": True, "ACK": False}
        },
        {
            "id": "pkt_002",
            "source_ip": "10.0.0.5",
            "destination_ip": "172.16.0.1",
            "protocol": "UDP",
            "destination_port": 53,
            "size": 2000,
            "flags": {"URG": False, "PSH": False}
        }
    ]
    
    # Analyse des paquets
    for packet in test_packets:
        result = analyzer.analyze_packet(packet)
        print(f"Résultat d'analyse: {result}")
    
    # Statistiques
    stats = analyzer.get_network_stats()
    print(f"Statistiques réseau: {stats}")
    
    # Connexions récentes
    recent = analyzer.get_recent_connections(5)
    print(f"Connexions récentes: {recent}")
    
    # Activités suspectes
    suspicious = analyzer.get_suspicious_activities(5)
    print(f"Activités suspectes: {suspicious}")

if __name__ == "__main__":
    main()