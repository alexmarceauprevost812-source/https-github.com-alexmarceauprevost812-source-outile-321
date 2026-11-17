#!/usr/bin/env python3
"""
Détection de scams pour l'IA Locale
Implémente des algorithmes de détection de fraude
"""

import os
import sys
import json
import hashlib
import time
from datetime import datetime
from typing import Dict, List, Tuple, Optional
from collections import defaultdict

# Ajout du dossier ai_local au chemin Python
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from config import AI_CONFIG
from utils import setup_logging, load_data, save_data

class ScamDetector:
    """Classe pour la détection de scams"""
    
    def __init__(self):
        """Initialisation du détecteur de scams"""
        self.logger = setup_logging()
        self.known_scams = set()
        self.scam_patterns = []
        self.scam_domains = set()
        self.scam_ips = set()
        self.scam_urls = set()
        self.logger.info("Détecteur de scams initialisé")
    
    def load_known_scams(self) -> bool:
        """Charge les scams connus depuis des fichiers"""
        try:
            # Charger les scams depuis des fichiers
            scam_files = [
                "data/scam_domains.json",
                "data/scam_ips.json",
                "data/scam_urls.json"
            ]
            
            for scam_file in scam_files:
                if os.path.exists(scam_file):
                    with open(scam_file, 'r') as f:
                        data = json.load(f)
                        if isinstance(data, list):
                            self.known_scams.update(data)
            
            self.logger.info(f"Chargé {len(self.known_scams)} scams connus")
            return True
            
        except Exception as e:
            self.logger.error(f"Erreur lors du chargement des scams: {e}")
            return False
    
    def add_scam_pattern(self, pattern: str) -> bool:
        """Ajoute un nouveau motif de scam"""
        try:
            if pattern not in self.scam_patterns:
                self.scam_patterns.append(pattern)
                self.logger.info(f"Motif de scam ajouté: {pattern}")
                return True
            return False
            
        except Exception as e:
            self.logger.error(f"Erreur lors de l'ajout du motif: {e}")
            return False
    
    def check_domain(self, domain: str) -> bool:
        """Vérifie si un domaine est un scam"""
        try:
            # Vérification rapide avec les domaines connus
            if domain in self.scam_domains:
                return True
            
            # Vérification avec les motifs
            for pattern in self.scam_patterns:
                if pattern in domain:
                    return True
            
            return False
            
        except Exception as e:
            self.logger.error(f"Erreur lors de la vérification du domaine: {e}")
            return False
    
    def check_ip(self, ip: str) -> bool:
        """Vérifie si une IP est un scam"""
        try:
            if ip in self.scam_ips:
                return True
            return False
            
        except Exception as e:
            self.logger.error(f"Erreur lors de la vérification de l'IP: {e}")
            return False
    
    def check_url(self, url: str) -> bool:
        """Vérifie si une URL est un scam"""
        try:
            # Vérification rapide avec les URLs connues
            if url in self.scam_urls:
                return True
            
            # Vérification avec les motifs
            for pattern in self.scam_patterns:
                if pattern in url:
                    return True
            
            return False
            
        except Exception as e:
            self.logger.error(f"Erreur lors de la vérification de l'URL: {e}")
            return False
    
    def analyze_network_data(self, data: Dict) -> Dict:
        """Analyse les données réseau pour détecter les scams"""
        try:
            results = {
                "timestamp": datetime.now().isoformat(),
                "analysis": {
                    "domain_checks": 0,
                    "ip_checks": 0,
                    "url_checks": 0,
                    "threats_found": 0
                }
            }
            
            # Analyse des domaines
            domains = data.get("domains", [])
            for domain in domains:
                if self.check_domain(domain):
                    results["analysis"]["threats_found"] += 1
                results["analysis"]["domain_checks"] += 1
            
            # Analyse des IPs
            ips = data.get("ips", [])
            for ip in ips:
                if self.check_ip(ip):
                    results["analysis"]["threats_found"] += 1
                results["analysis"]["ip_checks"] += 1
            
            # Analyse des URLs
            urls = data.get("urls", [])
            for url in urls:
                if self.check_url(url):
                    results["analysis"]["threats_found"] += 1
                results["analysis"]["url_checks"] += 1
            
            self.logger.info(f"Analyse réseau terminée: {results['analysis']}")
            return results
            
        except Exception as e:
            self.logger.error(f"Erreur lors de l'analyse réseau: {e}")
            return {
                "timestamp": datetime.now().isoformat(),
                "error": str(e)
            }
    
    def generate_hash(self, data: str) -> str:
        """Génère un hash pour les données"""
        return hashlib.md5(data.encode()).hexdigest()
    
    def add_scam_data(self, data: Dict) -> bool:
        """Ajoute des données de scam à la base"""
        try:
            # Sauvegarder dans les fichiers appropriés
            os.makedirs("data", exist_ok=True)
            
            # Domaines
            domains_file = "data/scam_domains.json"
            domains = set()
            if os.path.exists(domains_file):
                with open(domains_file, 'r') as f:
                    domains = set(json.load(f))
            
            domains.update(data.get("domains", []))
            with open(domains_file, 'w') as f:
                json.dump(list(domains), f, indent=2)
            
            # IPs
            ips_file = "data/scam_ips.json"
            ips = set()
            if os.path.exists(ips_file):
                with open(ips_file, 'r') as f:
                    ips = set(json.load(f))
            
            ips.update(data.get("ips", []))
            with open(ips_file, 'w') as f:
                json.dump(list(ips), f, indent=2)
            
            # URLs
            urls_file = "data/scam_urls.json"
            urls = set()
            if os.path.exists(urls_file):
                with open(urls_file, 'r') as f:
                    urls = set(json.load(f))
            
            urls.update(data.get("urls", []))
            with open(urls_file, 'w') as f:
                json.dump(list(urls), f, indent=2)
            
            self.logger.info(f"Données de scam ajoutées: {len(data.get('domains', []))} domaines, "
                           f"{len(data.get('ips', []))} IPs, {len(data.get('urls', []))} URLs")
            return True
            
        except Exception as e:
            self.logger.error(f"Erreur lors de l'ajout des données de scam: {e}")
            return False
    
    def get_statistics(self) -> Dict:
        """Retourne les statistiques du détecteur"""
        return {
            "scam_patterns": len(self.scam_patterns),
            "scam_domains": len(self.scam_domains),
            "scam_ips": len(self.scam_ips),
            "scam_urls": len(self.scam_urls),
            "known_scams": len(self.known_scams),
            "timestamp": datetime.now().isoformat()
        }

def main():
    """Point d'entrée principal pour le détecteur"""
    detector = ScamDetector()
    
    # Charger les scams connus
    detector.load_known_scams()
    
    # Exemple de données à analyser
    test_data = {
        "domains": ["example.com", "scam-site.net"],
        "ips": ["192.168.1.1", "10.0.0.1"],
        "urls": ["http://example.com", "http://scam-site.net"]
    }
    
    # Analyse des données
    results = detector.analyze_network_data(test_data)
    print(f"Résultats de l'analyse: {results}")
    
    # Statistiques
    stats = detector.get_statistics()
    print(f"Statistiques: {stats}")

if __name__ == "__main__":
    main()