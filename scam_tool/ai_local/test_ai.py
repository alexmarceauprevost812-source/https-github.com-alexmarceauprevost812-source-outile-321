#!/usr/bin/env python3
"""
Tests pour l'IA Locale
"""

import unittest
import os
import sys
from unittest.mock import patch

# Ajout du dossier ai_local au chemin Python
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from ai_local.main import AILocal
from ai_local.config import AI_CONFIG
from ai_local.utils import setup_logging, load_data, save_data

class TestAILocal(unittest.TestCase):
    """Tests pour l'IA Locale"""
    
    def setUp(self):
        """Configuration avant chaque test"""
        self.ai = AILocal()
    
    def test_config_loaded(self):
        """Test que la configuration est chargée"""
        self.assertIsNotNone(AI_CONFIG)
        self.assertIn('name', AI_CONFIG)
        self.assertIn('version', AI_CONFIG)
    
    def test_logging_setup(self):
        """Test de la configuration du logging"""
        logger = setup_logging()
        self.assertIsNotNone(logger)
    
    def test_data_functions(self):
        """Test des fonctions de gestion des données"""
        # Test de sauvegarde et de chargement
        test_data = {'test': 'data'}
        save_data(test_data)
        
        loaded_data = load_data()
        self.assertEqual(loaded_data, test_data)
        
        # Nettoyage
        os.remove(os.path.join('data', 'ai_data.json'))
    
    def test_ai_initialization(self):
        """Test de l'initialisation de l'IA"""
        self.assertIsNotNone(self.ai.config)
        self.assertIsNotNone(self.ai.logger)

class TestAILocalFunctions(unittest.TestCase):
    """Tests pour les fonctions spécifiques de l'IA"""
    
    def test_analyze_network_data(self):
        """Test de l'analyse réseau"""
        ai = AILocal()
        result = ai.analyze_network_data()
        self.assertIsNotNone(result)
        self.assertIn('status', result)
    
    def test_detect_scams(self):
        """Test de la détection de scams"""
        ai = AILocal()
        result = ai.detect_scams()
        self.assertIsNotNone(result)
        self.assertIn('status', result)

if __name__ == '__main__':
    # Exécution des tests
    unittest.main(verbosity=2)