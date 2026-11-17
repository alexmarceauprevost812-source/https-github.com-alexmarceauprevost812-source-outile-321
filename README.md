# Scam Tool - Kali Linux Edition

This tool is designed to perform various scam operations including:
- Finding device addresses
- Conducting attacks on new devices
- Using Kali Linux tools for network reconnaissance and exploitation

## Features
- Address discovery
- Device scanning
- Network attack simulation
- Integration with Kali Linux tools
- Auto-attack mode for all discovered devices
- Password cracking with John the Ripper and Hashcat
- Wi-Fi network attacks with Wifite

## Installation

### Prerequisites
This tool requires Kali Linux tools to be installed. Run the following commands to install all dependencies:

```bash
# Update package list
sudo apt update

# Install required tools
sudo apt install nmap arp-scan dnsenum john hashcat wifite aircrack-ng ettercap
```

### Install Script
Alternatively, you can use our automated installer:

```bash
# Make the installer executable
chmod +x install_tools.py

# Run the installer
python install_tools.py
```

## Usage

### Basic Usage
```bash
# Show help
python scam_tool.py --help
```

### Network Scanning
```bash
# Scan a network for devices
python scam_tool.py --network 192.168.1.0/24
```

### Auto-Attack Mode
```bash
# Automatically scan and attack all devices in a network
python scam_tool.py --auto-attack 192.168.1.0/24
```

### Wi-Fi Attacks
```bash
# Attack a Wi-Fi network
python scam_tool.py --attack-wifi "NetworkSSID" --interface wlan0
```

### Password Cracking
```bash
# Crack password hashes with John the Ripper
python scam_tool.py --hash-file hashes.txt --cracker john

# Crack password hashes with Hashcat
python scam_tool.py --hash-file hashes.txt --cracker hashcat --wordlist /usr/share/wordlists/rockyou.txt
```

## Requirements
- Python 3.x
- Kali Linux tools (nmap, arp-scan, john, hashcat, wifite, etc.)
- Network interface for wireless attacks (if applicable)

## Results Storage
Scan results are automatically saved in the `scam_results` directory.

## License
This tool is for educational purposes only.

## Author
Scam Tool - Kali Linux Edition