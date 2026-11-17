#!/usr/bin/env python3
"""
Menu interactif pour l'IA Locale
Permet de gérer les différentes fonctionnalités de l'IA Locale
"""

import os
import sys
import json
import time
import threading
from datetime import datetime
from typing import Dict, List, Optional

# Ajout du dossier ai_local au chemin Python
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from main import AILocal
from ai_manager import AIManager
from scam_detector import ScamDetector
from network_analyzer import NetworkAnalyzer
from ai_integration import AIIntegration
from ai_monitor import AIMonitor
from config import AI_CONFIG
from utils import setup_logging, load_data, save_data

class AILocalMenu:
    """Classe pour le menu interactif de l'IA Locale"""
    
    def __init__(self):
        """Initialisation du menu"""
        self.logger = setup_logging()
        self.ai_local = AILocal()
        self.ai_manager = AIManager()
        self.scam_detector = ScamDetector()
        self.network_analyzer = NetworkAnalyzer()
        self.ai_integration = AIIntegration()
        self.ai_monitor = AIMonitor()
        self.running = True
        self.logger.info("Menu de l'IA Locale initialisé")
    
    def display_menu(self):
        """Affiche le menu principal"""
        print("\n" + "="*50)
        print("           MENU DE L'IA LOCALE")
        print("="*50)
        print("1. Démarrer l'IA Locale")
        print("2. Arrêter l'IA Locale")
        print("3. Afficher l'état de l'IA")
        print("4. Gérer les instances AI")
        print("5. Analyse de fraude")
        print("6. Analyse réseau")
        print("7. Intégration des outils")
        print("8. Surveillance système")
        print("9. Exporter les données")
        print("10. Importer les données")
        print("11. Afficher la configuration")
        print("12. Quitter")
        print("="*50)
    
    def handle_choice(self, choice: str):
        """Gère le choix de l'utilisateur"""
        try:
            if choice == "1":
                self.start_ai_local()
            elif choice == "2":
                self.stop_ai_local()
            elif choice == "3":
                self.show_ai_status()
            elif choice == "4":
                self.manage_ai_instances()
            elif choice == "5":
                self.scam_detection_analysis()
            elif choice == "6":
                self.network_analysis()
            elif choice == "7":
                self.tool_integration()
            elif choice == "8":
                self.system_monitoring()
            elif choice == "9":
                self.export_data()
            elif choice == "10":
                self.import_data()
            elif choice == "11":
                self.show_config()
            elif choice == "12":
                self.quit_program()
            else:
                print("Choix invalide. Veuillez sélectionner un numéro entre 1 et 12.")
        except Exception as e:
            self.logger.error(f"Erreur lors du traitement du choix: {e}")
            print(f"Erreur: {e}")
    
    def start_ai_local(self):
        """Démarrage de l'IA Locale"""
        print("Démarrage de l'IA Locale...")
        try:
            # Démarrage de l'IA Locale dans un thread séparé
            ai_thread = threading.Thread(target=self.ai_local.start, daemon=True)
            ai_thread.start()
            print("L'IA Locale a été démarrée.")
        except Exception as e:
            print(f"Erreur lors du démarrage: {e}")
    
    def stop_ai_local(self):
        """Arrêt de l'IA Locale"""
        print("Arrêt de l'IA Locale...")
        try:
            self.ai_local.stop()
            print("L'IA Locale a été arrêtée.")
        except Exception as e:
            print(f"Erreur lors de l'arrêt: {e}")
    
    def show_ai_status(self):
        """Affichage de l'état de l'IA"""
        print("État de l'IA Locale:")
        try:
            status = self.ai_local.get_status()
            print(json.dumps(status, indent=2, ensure_ascii=False))
        except Exception as e:
            print(f"Erreur lors de la récupération de l'état: {e}")
    
    def manage_ai_instances(self):
        """Gestion des instances AI"""
        print("Gestion des instances AI:")
        try:
            instances = self.ai_manager.list_ai_instances()
            print("Instances actuelles:")
            for instance in instances:
                print(f"  - {instance}")
        except Exception as e:
            print(f"Erreur lors de la gestion des instances: {e}")
    
    def scam_detection_analysis(self):
        """Analyse de détection de fraude"""
        print("Analyse de détection de fraude:")
        try:
            # Chargement des domaines suspects
            self.scam_detector.load_known_scams()
            
            # Test de détection
            test_urls = [
                "http://scam-site.net",
                "https://legitimate-site.com"
            ]
            
            for url in test_urls:
                result = self.scam_detector.is_scam_url(url)
                print(f"URL: {url} - Est scam: {result}")
        except Exception as e:
            print(f"Erreur lors de l'analyse de fraude: {e}")
    
    def network_analysis(self):
        """Analyse réseau"""
        print("Analyse réseau:")
        try:
            # Exemple de données de paquet à analyser
            test_packets = [
                {"src": "192.168.1.100", "dst": "192.168.1.1", "protocol": "TCP"},
                {"src": "192.168.1.101", "dst": "192.168.1.2", "protocol": "UDP"}
            ]
            
            for packet in test_packets:
                result = self.network_analyzer.analyze_packet(packet)
                print(f"Paquet: {packet} - Analyse: {result}")
        except Exception as e:
            print(f"Erreur lors de l'analyse réseau: {e}")
    
    def tool_integration(self):
        """Intégration des outils"""
        print("Intégration des outils:")
        try:
            # Test de l'intégration
            integration_result = self.ai_integration.get_integration_status()
            print(f"Statut d'intégration: {integration_result}")
        except Exception as e:
            print(f"Erreur lors de l'intégration: {e}")
    
    def system_monitoring(self):
        """Surveillance système"""
        print("Surveillance système:")
        try:
            # Affichage des métriques
            metrics = self.ai_monitor.get_metrics()
            print("Métriques système:")
            print(json.dumps(metrics, indent=2, ensure_ascii=False))
        except Exception as e:
            print(f"Erreur lors de la surveillance: {e}")
    
    def export_data(self):
        """Exportation des données"""
        print("Exportation des données:")
        try:
            # Exemple d'exportation de données
            data = {
                "timestamp": datetime.now().isoformat(),
                "status": "exported",
                "data": "Données d'analyse"
            }
            
            # Sauvegarde dans un fichier
            filename = f"data_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            with open(filename, 'w') as f:
                json.dump(data, f, indent=2)
            
            print(f"Données exportées dans {filename}")
        except Exception as e:
            print(f"Erreur lors de l'exportation: {e}")
    
    def import_data(self):
        """Importation des données"""
        print("Importation des données:")
        try:
            # Exemple d'importation de données
            filename = "data_export.json"
            if os.path.exists(filename):
                with open(filename, 'r') as f:
                    data = json.load(f)
                print(f"Données importées depuis {filename}")
                print(json.dumps(data, indent=2, ensure_ascii=False))
            else:
                print("Fichier d'importation non trouvé.")
        except Exception as e:
            print(f"Erreur lors de l'importation: {e}")
    
    def show_config(self):
        """Affichage de la configuration"""
        print("Configuration de l'IA Locale:")
        try:
            config = self.ai_local.get_config()
            print(json.dumps(config, indent=2, ensure_ascii=False))
        except Exception as e:
            print(f"Erreur lors de l'affichage de la configuration: {e}")
    
    def quit_program(self):
        """Fermeture du programme"""
        print("Fermeture du programme...")
        self.running = False
        sys.exit(0)
    
    def run(self):
        """Exécution du menu"""
        print("Bienvenue dans le menu de l'IA Locale")
        while self.running:
            self.display_menu()
            try:
                choice = input("Veuillez choisir une option (1-12): ").strip()
                if choice:
                    self.handle_choice(choice)
                else:
                    print("Veuillez faire un choix valide.")
            except EOFError:
                print("\nFin de l'entrée. Fermeture du programme...")
                self.quit_program()
            except KeyboardInterrupt:
                print("\nInterruption par l'utilisateur. Fermeture du programme...")
                self.quit_program()

# Fonction principale
def main():
    """Fonction principale du menu"""
    try:
        menu = AILocalMenu()
        menu.run()
    except KeyboardInterrupt:
        print("\nProgramme interrompu par l'utilisateur")
        sys.exit(0)
    except Exception as e:
        print(f"Erreur critique: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()