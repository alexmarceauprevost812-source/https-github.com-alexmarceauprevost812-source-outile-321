#!/usr/bin/env bash

# ============================================================
# Scam Tool - Kali Linux Edition
# Installation Script
# ============================================================

echo "============================================================"
echo "Scam Tool - Kali Linux Edition"
echo "Installation Script"
echo "============================================================"

# Check if running on Kali Linux
if [ -f /etc/kali-version ]; then
    echo "✓ Kali Linux detected"
else
    echo "⚠ Warning: This script is designed for Kali Linux"
    read -p "Continue anyway? (y/n): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "Installation cancelled"
        exit 1
    fi
fi

# Update package list
echo "Updating package list..."
sudo apt update

# Install required tools
echo "Installing required tools..."
sudo apt install -y \
    nmap \
    arp-scan \
    dnsenum \
    john \
    hashcat \
    wifite \
    aircrack-ng \
    ettercap-text-only \
    sslstrip \
    mitmf

# Install Python dependencies
echo "Installing Python dependencies..."
pip3 install --upgrade pip
pip3 install -r requirements.txt

# Create results directory
echo "Creating results directory..."
mkdir -p scam_results

# Make the main script executable
echo "Making main script executable..."
chmod +x scam_tool.py

echo "============================================================"
echo "Installation completed successfully!"
echo "To use the tool:"
echo "  python3 scam_tool.py --help"
echo "============================================================"