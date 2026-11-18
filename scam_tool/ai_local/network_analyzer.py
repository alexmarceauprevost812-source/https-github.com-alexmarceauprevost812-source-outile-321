"""
Analyseur de réseau pour l'IA Locale
Permet d'analyser le trafic réseau
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
import dpkt

# Ajout du dossier ai_local au chemin Python
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from utils import setup_logging, load_data, save_data

class NetworkAnalyzer:
    """Classe pour analyser le trafic réseau"""
    
    def __init__(self):
        """Initialisation de l'analyseur de réseau"""
        self.logger = setup_logging()
        self.packets = []
        self.analyzed_packets = []
        self.is_analyzing = False
        self.logger.info("Analyseur de réseau initialisé")
    
    def start_analysis(self):
        """Démarre l'analyse du trafic réseau"""
        if self.is_analyzing:
            self.logger.warning("L'analyse est déjà en cours")
            return False
        
        self.is_analyzing = True
        self.logger.info("Analyse du trafic réseau démarrée")
        return True
    
    def stop_analysis(self):
        """Arrête l'analyse du trafic réseau"""
        self.is_analyzing = False
        self.logger.info("Analyse du trafic réseau arrêtée")
    
    def capture_packet(self, packet_data: bytes, interface: str = "eth0") -> Dict:
        """Capture et analyse un paquet réseau"""
        try:
            # Vérification de la taille du paquet
            if len(packet_data) < 14:  # En-tête Ethernet minimum
                self.logger.warning("Paquet trop court")
                return {"status": "error", "message": "Packet too short"}
            
            # Décomposition du paquet
            eth = dpkt.ethernet.Ethernet(packet_data)
            
            # Analyse de l'en-tête Ethernet
            packet_info = {
                "timestamp": datetime.now().isoformat(),
                "interface": interface,
                "ethernet": {
                    "src_mac": ':'.join('%02x' % ord(b) for b in eth.src),
                    "dst_mac": ':'.join('%02x' % ord(b) for b in eth.dst),
                    "ethertype": eth.type
                }
            }
            
            # Analyse des protocoles supérieurs
            if isinstance(eth.data, dpkt.ip.IP):
                ip = eth.data
                packet_info["ip"] = {
                    "version": ip.v,
                    "header_length": ip.hl,
                    "tos": ip.tos,
                    "length": ip.len,
                    "id": ip.id,
                    "flags": ip.flags,
                    "fragment_offset": ip.off,
                    "ttl": ip.ttl,
                    "protocol": ip.p,
                    "checksum": ip.sum,
                    "src_ip": socket.inet_ntoa(ip.src),
                    "dst_ip": socket.inet_ntoa(ip.dst)
                }
                
                # Analyse des protocoles transport
                if isinstance(ip.data, dpkt.tcp.TCP):
                    tcp = ip.data
                    packet_info["tcp"] = {
                        "src_port": tcp.sport,
                        "dst_port": tcp.dport,
                        "seq": tcp.seq,
                        "ack": tcp.ack,
                        "header_length": tcp.off,
                        "flags": tcp.flags,
                        "window": tcp.win,
                        "checksum": tcp.sum,
                        "urgent_ptr": tcp.urp
                    }
                elif isinstance(ip.data, dpkt.udp.UDP):
                    udp = ip.data
                    packet_info["udp"] = {
                        "src_port": udp.sport,
                        "dst_port": udp.dport,
                        "length": udp.ulen,
                        "checksum": udp.sum
                    }
            
            # Ajout à l'historique
            self.packets.append(packet_info)
            
            # Analyse supplémentaire
            analysis = self._analyze_packet(packet_info)
            self.analyzed_packets.append({
                "original_packet": packet_info,
                "analysis": analysis,
                "timestamp": datetime.now().isoformat()
            })
            
            return {
                "status": "success",
                "packet_info": packet_info,
                "analysis": analysis
            }
        except Exception as e:
            self.logger.error(f"Erreur lors de la capture du paquet: {e}")
            return {"status": "error", "message": str(e)}
    
    def _analyze_packet(self, packet_info: Dict) -> Dict:
        """Effectue une analyse détaillée du paquet"""
        try:
            analysis = {
                "timestamp": packet_info["timestamp"],
                "is_malformed": False,
                "is_large": False,
                "is_suspicious": False,
                "suspicious_indicators": []
            }
            
            # Vérification de la validité du paquet
            if "ip" in packet_info:
                ip_info = packet_info["ip"]
                
                # Vérification de la taille du paquet
                if ip_info["length"] > 1500:
                    analysis["is_large"] = True
                    analysis["suspicious_indicators"].append("Packet size exceeds MTU")
                
                # Vérification de l'adresse IP source
                src_ip = ip_info["src_ip"]
                if self._is_suspicious_ip(src_ip):
                    analysis["is_suspicious"] = True
                    analysis["suspicious_indicators"].append("Suspicious source IP")
                
                # Vérification de l'adresse IP destination
                dst_ip = ip_info["dst_ip"]
                if self._is_suspicious_ip(dst_ip):
                    analysis["is_suspicious"] = True
                    analysis["suspicious_indicators"].append("Suspicious destination IP")
            
            # Vérification des protocoles
            if "tcp" in packet_info:
                tcp_info = packet_info["tcp"]
                if tcp_info["flags"] & 0x02:  # SYN flag
                    analysis["suspicious_indicators"].append("SYN packet detected")
            
            return analysis
        except Exception as e:
            self.logger.error(f"Erreur lors de l'analyse du paquet: {e}")
            return {"status": "error", "message": str(e)}
    
    def _is_suspicious_ip(self, ip_address: str) -> bool:
        """Vérifie si une adresse IP est suspecte"""
        # Cette méthode peut être améliorée avec une base de données de IPs suspectes
        suspicious_ips = ["192.168.1.100", "10.0.0.1"]
        return ip_address in suspicious_ips
    
    def get_packets(self) -> List[Dict]:
        """Retourne la liste des paquets capturés"""
        return self.packets
    
    def get_analyzed_packets(self) -> List[Dict]:
        """Retourne la liste des paquets analysés"""
        return self.analyzed_packets
    
    def get_network_stats(self) -> Dict:
        """Retourne les statistiques réseau"""
        try:
            stats = {
                "total_packets": len(self.packets),
                "total_analyzed": len(self.analyzed_packets),
                "timestamp": datetime.now().isoformat()
            }
            
            # Analyse des protocoles
            protocol_count = {}
            for packet in self.packets:
                if "ip" in packet:
                    protocol = packet["ip"]["protocol"]
                    protocol_count[protocol] = protocol_count.get(protocol, 0) + 1
            
            stats["protocol_distribution"] = protocol_count
            
            return stats
        except Exception as e:
            self.logger.error(f"Erreur lors de la génération des statistiques: {e}")
            return {}
    
    def clear_data(self):
        """Efface toutes les données"""
        self.packets.clear()
        self.analyzed_packets.clear()
        self.logger.info("Données effacées")
    
    def export_data(self, file_path: str = "data/network_data.json") -> bool:
        """Exporte les données dans un fichier"""
        try:
            data = {
                "packets": self.packets,
                "analyzed_packets": self.analyzed_packets,
                "network_stats": self.get_network_stats(),
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
                
                self.packets = data.get("packets", [])
                self.analyzed_packets = data.get("analyzed_packets", [])
                
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
    # Création d'une instance de l'analyseur
    analyzer = NetworkAnalyzer()
    
    # Démarrage de l'analyse
    analyzer.start_analysis()
    
    # Capture d'un paquet (exemple simplifié)
    # Dans un vrai scénario, vous obtiendriez les paquets à partir d'une interface réseau
    
    # Création d'un paquet d'exemple
    example_packet = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00' + b'\x00' * 100
    
    # Capture et analyse du paquet
    result = analyzer.capture_packet(example_packet)
    print("Résultat de la capture:", result)
    
    # Affichage des statistiques
    stats = analyzer.get_network_stats()
    print("Statistiques réseau:", stats)
    
    # Exportation des données
    analyzer.export_data()