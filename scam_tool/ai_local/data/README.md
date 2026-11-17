# Répertoire de données

Ce dossier contient les fichiers de données utilisés par l'IA Locale.

## Fichiers

- `ai_data.json` - Données de l'IA locale
- `ai_manager_state.json` - État du gestionnaire d'IA
- `scam_domains.json` - Liste des domaines suspects
- `scam_ips.json` - Liste des IPs suspects
- `scam_urls.json` - Liste des URLs suspects

## Format des fichiers

### ai_data.json
```json
{
  "timestamp": "2023-01-01T00:00:00",
  "data": {}
}
```

### scam_domains.json, scam_ips.json, scam_urls.json
```json
[
  "example.com",
  "scam-site.net"
]
```

## Structure

```
data/
├── ai_data.json
├── ai_manager_state.json
├── scam_domains.json
├── scam_ips.json
└── scam_urls.json
```

## Utilisation

Les fichiers sont gérés automatiquement par les classes d'IA. Ne modifiez pas manuellement ces fichiers sauf si nécessaire.