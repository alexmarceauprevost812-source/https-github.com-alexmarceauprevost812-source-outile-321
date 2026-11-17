#!/bin/bash
#
# Scam Tool - Ubuntu Edition
# Installation Script for Required Tools
#
# This script installs all necessary tools for the Scam Tool to function properly
# It includes tools for network scanning, vulnerability assessment, and attack simulation
#
# This version is specifically designed for Ubuntu systems
#
# Usage: Make the script executable and run it with sudo
#
# chmod +x install_tools_ubuntu.sh
# sudo ./install_tools_ubuntu.sh
#
# Note: This script is designed for Ubuntu or similar Linux distributions
#
# Exit on any error
set -e

# Display script information
echo "=== Scam Tool - Ubuntu Edition ==="
echo "Installing required tools..."
echo "This will take a few minutes..."

# Update package list
echo "Updating package list..."
apt update

# Install core security tools
echo "Installing core security tools..."
apt install -y nmap arp-scan dnsenum sslstrip mitmf ettercap aircrack-ng john hashcat

# Install additional utilities
echo "Installing additional utilities..."
apt install -y curl wget git net-tools

# Install Python3 and pip for script execution
echo "Installing Python3 and pip..."
apt install -y python3 python3-pip

# Install additional Python packages
echo "Installing Python packages..."
python3 -m pip install --upgrade pip
python3 -m pip install requests

# Install firewall and network configuration tools
echo "Installing firewall and network configuration tools..."
apt install -y ufw iputils-ping

# Create a directory for tool configurations
echo "Creating tool configuration directory..."
mkdir -p ~/scam_tool/config

# Create a sample configuration file
echo "Creating sample configuration file..."
cat > ~/scam_tool/config/scan_config.yaml << 'EOF'
# Sample configuration for Scam Tool
# This file can be customized for specific scan parameters
# For production use, create a more comprehensive configuration

# Scan settings
scan:
  target_network: "192.168.1.0/24"
  scan_type: "full"
  tools:
    - nmap
    - arp-scan
    - dnsenum

# Device information settings
device_info:
  enabled: true
  ports:
    -  22
    -  80
    -  443
    -  3389

# Vulnerability assessment settings
vulnerability:
  enabled: true
  recommendations:
    - "Enable SSH key authentication only"
    - "Implement HTTPS with proper security headers"
    - "Secure RDP access with network-level authentication"
    - "Implement stricter firewall rules"
    - "Ensure all systems are up to date with security patches"

# Attack simulation settings
attack_simulation:
  enabled: false
  # Note: Attack simulation requires proper network configuration and user interaction
  # Full attack simulation would require integration with mitmf, ettercap, and wifite

# General settings
general:
  version: "1.0"
  created: "2025-04-05"
  author: "Scam Tool - Ubuntu Edition"
  disclaimer: "This tool is for educational purposes only and should be used in accordance with local laws and regulations."

EOF

# Create a sample log file
echo "Creating sample log file..."
cat > ~/scam_tool/logs/scan_log.txt << 'EOF'
# Scan Log - Sample
# Generated on: 2025-04-05
# Target Network: 192.168.1.0/24
# Scan Type: Full Network Discovery
# Status: Completed
# Devices Found: 3
# Vulnerabilities Identified: 5
# Recommendations Generated: 5
# Note: This is a sample log. For actual scans, log files would contain detailed scan results.

# Security Recommendations:
# 1. Enable SSH key authentication only, disable password authentication
# 2. Implement HTTPS with proper security headers
# 3. Secure RDP access with network-level authentication
# 4. Implement stricter firewall rules
# 5. Ensure all systems are up to date with security patches

# This log was generated using the Scam Tool - Ubuntu Edition
# For complete attack simulation, additional tools such as mitmf, ettercap, and wifite would be required.

EOF

# Display completion message
echo "=== Installation Complete ==="
echo ""
echo "Tools successfully installed!"
echo ""
echo "Configuration files created in:"
echo "  ~/scam_tool/config/scan_config.yaml"
echo "  ~/scam_tool/logs/scan_log.txt"
echo ""
echo "To use the Scam Tool, run:"
echo "  python3 scam_tool.py"
echo ""
echo "Note: The Scam Tool has limitations and may not provide complete attack simulation capabilities without proper network configuration and user interaction."
echo ""
echo "Always ensure you have proper authorization before conducting network security assessments."

# Provide instructions for running the tool
echo ""
echo "=== Instructions ==="
echo "1. Make sure you have root privileges"
echo "2. Run the tool with: python3 scam_tool.py"
echo "3. Configure your scan parameters in scan_config.yaml"
echo "4. Review the generated scan report in scam_results/scan_report.md"
echo "5. For complete attack simulation, ensure proper network configuration and user interaction"

# Exit successfully
exit 0
