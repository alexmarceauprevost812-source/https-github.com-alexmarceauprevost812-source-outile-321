# Kit d'outils Kali Linux pour les attaques de phishing et ingénierie sociale

## 🛠️ Liste complète des outils et leurs commandes d'installation

### 1. **Gophish**  
Outil de phishing open-source pour créer et exécuter des campagnes de phishing.  
```bash
sudo apt update && sudo apt install gophish
```

### 2. **Phishery**  
Serveur HTTP simple pour attaquer les utilisateurs via des pages web falsifiées.  
```bash
sudo apt install phishery
```

### 3. **Social-Engineer Toolkit (SET)**  
Outil puissant pour la collecte de credentials via des sites clonés ou des attaques de phishing.  
```bash
sudo apt install social-engineer-toolkit
```

### 4. **Redsnarf**  
Outil pour récupérer les hashes et credentials des machines Windows via des techniques opérationnelles sécurisées.  
```bash
sudo apt install redsnarf
```

### 5. **MOSINT**  
Outil d'OSINT pour la reconnaissance d'adresses email et d'informations cibles.  
```bash
sudo apt install mosint
```

### 6. **HostHunter**  
Outil pour découvrir et extraire des noms d'hôtes à partir d'adresses IP.  
```bash
sudo apt install hosthunter
```

### 7. **Netdiscover**  
Outil de découverte réseau pour identifier les hôtes actifs sur un réseau local.  
```bash
sudo apt install netdiscover
```

### 8. **Nmap**  
Scanner réseau pour détecter les hôtes vivants, les ports et les services.  
```bash
sudo apt install nmap
```

### 9. **Sn0int**  
Outil d'information gathering automatisé pour explorer la surface d'attaque.  
```bash
sudo apt install sn0int
```

### 10. **Maltego**  
Plateforme de gathering d'informations graphiques pour visualiser les relations entre entités.  
```bash
sudo apt install maltego
```

---

## 📝 Notes supplémentaires
- Utilisez `sudo` pour les commandes de mise à jour/installation.  
- Consultez la documentation de chaque outil pour des configurations avancées.  
- Ces outils sont conçus pour des attaques de type ingénierie sociale, phishing et reconnaissance réseau.  
- Pour une utilisation éthique, veillez à obtenir les autorisations nécessaires avant d'attaquer des systèmes cibles.

---

## 🧪 Exemple d'utilisation de SET (Social-Engineer Toolkit)
```bash
sudo setoolkit
```
Sélectionnez :
- Social-Engineering Attacks
- Website Attack Vectors
- Credential Harvester Attack Method
- Site Cloner
- Entrez l'URL du site cible (ex: https://www.google.com)
- Démarrez le serveur de phishing

---

## 📦 Installation complète du kit
Pour installer tous les outils en une seule commande :
```bash
sudo apt update && sudo apt install gophish phishery social-engineer-toolkit redsnarf mosint hosthunter netdiscover nmap sn0int maltego
```

---

## 🔄 Mise à jour des outils
Pour mettre à jour tous les outils :
```bash
sudo apt update && sudo apt upgrade
```
