# Scam Tool - Ubuntu Installation Guide

## Overview

The Scam Tool is a comprehensive network security assessment tool designed for educational purposes. This guide provides step-by-step instructions for installing and using the Scam Tool on Ubuntu systems.

## Prerequisites

Before installing the Scam Tool on Ubuntu, ensure you have the following:

- A computer running Ubuntu (18.04 or later)
- At least 4GB of RAM
- 10GB of available disk space
- Internet connectivity
- Root privileges or sudo access

## Installation Steps

### Step 1: Update Your System

First, update your package list to ensure you have the latest software versions:

```bash
sudo apt update
```

### Step 2: Install Required Dependencies

Install the necessary dependencies for the Scam Tool:

```bash
sudo apt install -y curl wget git python3 python3-pip
```

### Step 3: Download and Install the Scam Tool

Download the installation script and run it with sudo:

```bash
wget https://example.com/install_tools_ubuntu.sh
chmod +x install_tools_ubuntu.sh
sudo ./install_tools_ubuntu.sh
```

### Step 4: Verify Installation

After installation, verify that all tools are properly installed:

```bash
# Check if tools are available
nmap --version
arp-scan --version
dnsenum --version
mitmf --version
ettercap --version
aircrack-ng --version
john --version
hashcat --version

# Check Python packages
python3 --version
pip3 --version
```

### Step 5: Configure the Tool

The Scam Tool comes with a sample configuration file. Edit it to customize your scan parameters:

```bash
nano ~/.scam_tool/config/scan_config.yaml
```

Modify the configuration to match your network environment and security requirements.

## Usage Instructions

To run the Scam Tool:

```bash
python3 scam_tool.py
```

The tool will generate a scan report in the `scam_results/` directory.

## Important Notes

- This tool is designed for educational purposes only and should be used in accordance with local laws and regulations.
- The Scam Tool has limitations and may not provide complete attack simulation capabilities without proper network configuration.
- Full attack simulation requires integration with tools like mitmf, ettercap, and wifite.
- Always ensure you have proper authorization before conducting network security assessments.

## Sample Configuration

The sample configuration file includes default settings for network scanning and vulnerability assessment:

```yaml
# Sample configuration for Scam Tool
# This file can be customized for specific scan parameters

scan:
  target_network: "192.168.1.0/24"
  scan_type: "full"
  tools:
    - nmap
    - arp-scan
    - dnsenum

device_info:
  enabled: true
  ports:
    - 22
    - 80
    - 443
    - 3389

vulnerability:
  enabled: true
  recommendations:
    - "Enable SSH key authentication only"
    - "Implement HTTPS with proper security headers"
    - "Secure RDP access with network-level authentication"
    - "Implement stricter firewall rules"
    - "Ensure all systems are up to date with security patches"

attack_simulation:
  enabled: false
  # Note: Attack simulation requires proper network configuration and user interaction

general:
  version: "1.0"
  created: "2025-04-05"
  author: "Scam Tool - Ubuntu Edition"
  disclaimer: "This tool is for educational purposes only and should be used in accordance with local laws and regulations."
```

## Sample Log File

A sample log file is created during installation:

```text
# Scan Log - Sample
# Generated on: 2025-04-05
# Target Network: 192.168.1.0/24
# Scan Type: Full Network Discovery
# Status: Completed
# Devices Found: 3
# Vulnerabilities Identified: 5
# Recommendations Generated: 5

# Security Recommendations:
# 1. Enable SSH key authentication only, disable password authentication
# 2. Implement HTTPS with proper security headers
# 3. Secure RDP access with network-level authentication
# 4. Implement stricter firewall rules
# 5. Ensure all systems are up to date with security patches
```

## Troubleshooting

If you encounter issues during installation:

- Ensure you have sufficient disk space
- Verify your internet connection
- Check that you have sudo privileges
- Review the installation log for specific errors

## License

This tool is provided for educational purposes only. Use it in accordance with local laws and regulations.