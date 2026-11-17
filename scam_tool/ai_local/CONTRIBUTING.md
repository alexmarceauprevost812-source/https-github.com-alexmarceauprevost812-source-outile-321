# Contribuer à l'IA Locale

Bienvenue dans le projet d'IA Locale ! Ce document vous guide dans la contribution au développement de l'IA locale.

## Structure du projet

```
ai_local/
├── main.py              # Point d'entrée principal
├── config.py            # Configuration de l'IA
├── utils.py             # Fonctions utilitaires
├── menu.py              # Interface de menu interactif
├── test_ai.py           # Tests unitaires
├── run_tests.py         # Script d'exécution des tests
├── requirements.txt     # Dépendances
├── README.md            # Documentation principale
└── CONTRIBUTING.md      # Ce fichier
```

## Comment contribuer

### 1. Fork du dépôt

1. Fork le dépôt sur GitHub
2. Clone le dépôt local

### 2. Installation

```bash
# Installer les dépendances
pip install -r requirements.txt
```

### 3. Développement

- Créez une branche pour votre fonctionnalité
- Développez votre code
- Ajoutez des tests pour votre code
- Documentez vos modifications

### 4. Tests

Assurez-vous que tous les tests passent :

```bash
python3 ai_local/run_tests.py
```

### 5. Pull Request

1. Poussez vos modifications
2. Créez une Pull Request
3. Décrivez vos modifications

## Bonnes pratiques

### Code

- Suivez le style de codage Python (PEP 8)
- Utilisez des docstrings pour tous les modules et fonctions
- Écrivez des tests unitaires pour chaque nouvelle fonctionnalité
- Divisez les fonctions en sous-fonctions si nécessaire

### Documentation

- Documentez chaque fonction avec des docstrings
- Mettez à jour le README.md si nécessaire
- Ajoutez des commentaires explicatifs dans le code

### Tests

- Écrivez des tests unitaires pour chaque fonctionnalité
- Utilisez des mocks pour les tests d'intégration
- Vérifiez que tous les tests passent avant de soumettre

## Structure des fichiers

### main.py

Le point d'entrée principal de l'IA locale. Contient la classe principale `AILocal` avec les fonctionnalités principales.

### config.py

Configuration de l'IA avec des paramètres par défaut et validation.

### utils.py

Fonctions utilitaires pour le logging, la gestion des données, etc.

### menu.py

Interface de menu interactif pour l'IA locale.

## Tests

Les tests sont situés dans `test_ai.py` et peuvent être exécutés avec `run_tests.py`.

## Contribution aux fonctionnalités

### Ajout de nouvelles fonctionnalités

1. Identifiez l'endroit approprié dans le code
2. Ajoutez votre fonctionnalité
3. Créez des tests pour celle-ci
4. Documentez votre fonctionnalité

### Correction de bugs

1. Identifiez le problème
2. Créez un test qui reproduit le bug
3. Corrigez le problème
4. Vérifiez que le test passe

## Questions ?

Pour toute question concernant le développement, contactez l'équipe de développement.