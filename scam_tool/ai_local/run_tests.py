#!/usr/bin/env python3
"""
Script pour exécuter tous les tests de l'IA Locale
"""

import subprocess
import sys
import os

def run_tests():
    """Exécute tous les tests"""
    print("Exécution des tests pour l'IA Locale...")
    
    try:
        # Exécution des tests avec pytest
        result = subprocess.run([
            sys.executable, '-m', 'pytest', 
            'ai_local/test_ai.py', 
            '-v'
        ], capture_output=True, text=True)
        
        print("Sortie des tests:")
        print(result.stdout)
        
        if result.stderr:
            print("Erreurs:")
            print(result.stderr)
            
        if result.returncode == 0:
            print("✅ Tous les tests ont réussi!")
        else:
            print("❌ Certains tests ont échoué.")
            
        return result.returncode
        
    except Exception as e:
        print(f"Erreur lors de l'exécution des tests: {e}")
        return 1

def run_simple_tests():
    """Exécution simple des tests sans pytest"""
    print("Exécution des tests simples...")
    
    try:
        # Exécution directe du script de test
        result = subprocess.run([
            sys.executable, 'ai_local/test_ai.py'
        ], capture_output=True, text=True)
        
        print("Sortie des tests:")
        print(result.stdout)
        
        if result.stderr:
            print("Erreurs:")
            print(result.stderr)
            
        return result.returncode
        
    except Exception as e:
        print(f"Erreur lors de l'exécution des tests: {e}")
        return 1

if __name__ == "__main__":
    print("=== Script d'exécution des tests ===")
    
    # Vérification si pytest est disponible
    try:
        import pytest
        print("pytest disponible - exécution avec pytest")
        exit_code = run_tests()
    except ImportError:
        print("pytest non disponible - exécution simple")
        exit_code = run_simple_tests()
    
    sys.exit(exit_code)