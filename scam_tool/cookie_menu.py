#!/usr/bin/env python3
"""
Menu interactif pour les outils de gestion des cookies
Options :
1. Extraire les cookies locaux
2. Capturer les cookies via proxy
3. Analyser les sessions
4. Documentation
"""

import os
import sys
import subprocess

def show_menu():
    print("\n=== MENU OUTILS COOKIES ===")
    print("1. Extraire les cookies locaux")
    print("2. Capturer les cookies via proxy")
    print("3. Analyser les sessions")
    print("4. Documentation")
    print("5. Quitter")
    print("============================")

def option_1():
    print("\n[INFO] Extraction des cookies locaux...")
    try:
        result = subprocess.run([sys.executable, "extract_cookies.py", "chrome"], 
                              capture_output=True, text=True)
        print(result.stdout)
        if result.stderr:
            print("ERREUR:", result.stderr)
    except Exception as e:
        print(f"[ERREUR] Impossible d'exécuter l'option 1 : {e}")

def option_2():
    print("\n[INFO] Configuration du proxy mitmproxy...")
    print("Installation de mitmproxy...")
    try:
        subprocess.run(["pip", "install", "mitmproxy"], check=True)
        print("mitmproxy installé avec succès")
        print("Utilisez : mitmdump -s proxy_script.py")
    except Exception as e:
        print(f"[ERREUR] Installation échouée : {e}")

def option_3():
    print("\n[INFO] Analyse des sessions...")
    print("Outil d'analyse des sessions en cours de développement...")
    print("Fonctionnalité disponible dans une version future.")

def option_4():
    print("\n[INFO] Documentation...")
    print("Pour plus d'informations, consultez le README.md")
    try:
        with open("README.md", "r") as f:
            print(f.read())
    except Exception as e:
        print(f"[ERREUR] Impossible d'afficher la documentation : {e}")

def main():
    while True:
        show_menu()
        choice = input("\nChoisissez une option (1-5) : ").strip()
        
        if choice == "1":
            option_1()
        elif choice == "2":
            option_2()
        elif choice == "3":
            option_3()
        elif choice == "4":
            option_4()
        elif choice == "5":
            print("Au revoir !")
            break
        else:
            print("[ERREUR] Option invalide. Veuillez choisir entre 1 et 5.")

if __name__ == "__main__":
    main()