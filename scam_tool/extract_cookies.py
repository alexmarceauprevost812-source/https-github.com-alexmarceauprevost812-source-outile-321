#!/usr/bin/env python3
"""
Outil d'extraction des cookies locaux
Fonctionne sur Linux avec Chrome ou Firefox
"""

import os
import sys
import sqlite3
import json
from datetime import datetime

def get_cookie_paths():
    """Retourne les chemins possibles pour les cookies"""
    return {
        "chrome": os.path.expanduser("~/.config/google-chrome/Default/Cookies"),
        "firefox": os.path.expanduser("~/.mozilla/firefox/*/cookies.sqlite"),
        "safari": os.path.expanduser("~/Library/Safari/cookies.sqlite")
    }

def extract_chrome_cookies(output_file):
    """Extrait les cookies de Chrome"""
    chrome_path = os.path.expanduser("~/.config/google-chrome/Default/Cookies")
    
    if not os.path.exists(chrome_path):
        print(f"[ERREUR] Fichier Chrome non trouvé : {chrome_path}")
        return False
    
    try:
        conn = sqlite3.connect(chrome_path)
        cursor = conn.cursor()
        cursor.execute("SELECT host_key, name, value, path, is_secure, is_httponly, domain, port FROM cookies")
        rows = cursor.fetchall()
        conn.close()
        
        with open(output_file, "w", encoding="utf-8") as f:
            f.write("# Fichier cookie.txt - extrait d'un appareil\n")
            f.write(f"Appareil: {os.getlogin()}\n")
            f.write(f"Navigateur: chrome\n")
            f.write(f"Date: {datetime.now()}\n")
            f.write(f"Source: {chrome_path}\n")
            f.write("\n")
            f.write("Host,Name,Value,Path,Secure,HttpOnly,Domain,Port\n")
            for row in rows:
                f.write(f"{row[0]},{row[1]},{row[2]},{row[3]},{row[4]},{row[5]},{row[6]},{row[7]}\n")
        
        print(f"[SUCCESS] Cookies extrait avec succès dans {output_file}")
        return True
        
    except Exception as e:
        print(f"[ERREUR] Impossible de lire les cookies Chrome : {e}")
        return False

def extract_firefox_cookies(output_file):
    """Extrait les cookies de Firefox"""
    firefox_paths = os.path.expanduser("~/.mozilla/firefox/")
    
    if not os.path.exists(firefox_paths):
        print(f"[ERREUR] Répertoire Firefox non trouvé : {firefox_paths}")
        return False
    
    # Recherche des profils
    try:
        profiles = [d for d in os.listdir(firefox_paths) if d.endswith('.default-release') or d.endswith('.default')]
        if not profiles:
            print("[ERREUR] Aucun profil Firefox trouvé")
            return False
            
        profile_path = os.path.join(firefox_paths, profiles[0])
        cookies_path = os.path.join(profile_path, "cookies.sqlite")
        
        if not os.path.exists(cookies_path):
            print(f"[ERREUR] Fichier cookies.sqlite non trouvé : {cookies_path}")
            return False
            
        conn = sqlite3.connect(cookies_path)
        cursor = conn.cursor()
        cursor.execute("SELECT host, name, value, path, isSecure, isHttpOnly, domain, port FROM moz_cookies")
        rows = cursor.fetchall()
        conn.close()
        
        with open(output_file, "w", encoding="utf-8") as f:
            f.write("# Fichier cookie.txt - extrait d'un appareil\n")
            f.write(f"Appareil: {os.getlogin()}\n")
            f.write(f"Navigateur: firefox\n")
            f.write(f"Date: {datetime.now()}\n")
            f.write(f"Source: {cookies_path}\n")
            f.write("\n")
            f.write("Host,Name,Value,Path,Secure,HttpOnly,Domain,Port\n")
            for row in rows:
                f.write(f"{row[0]},{row[1]},{row[2]},{row[3]},{row[4]},{row[5]},{row[6]},{row[7]}\n")
        
        print(f"[SUCCESS] Cookies extrait avec succès dans {output_file}")
        return True
        
    except Exception as e:
        print(f"[ERREUR] Impossible de lire les cookies Firefox : {e}")
        return False

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 extract_cookies.py <navigateur>")
        print("Navigateurs : chrome, firefox, safari")
        print("Exemple : python3 extract_cookies.py chrome")
        sys.exit(1)
    
    browser = sys.argv[1].lower()
    output_file = f"cookies_{browser}_{os.getlogin()}.txt"
    
    if browser == "chrome":
        extract_chrome_cookies(output_file)
    elif browser == "firefox":
        extract_firefox_cookies(output_file)
    elif browser == "safari":
        print("[INFO] Extraction Safari non implémentée dans cette version")
    else:
        print(f"[ERREUR] Navigateur '{browser}' non supporté")
        sys.exit(1)

if __name__ == "__main__":
    main()