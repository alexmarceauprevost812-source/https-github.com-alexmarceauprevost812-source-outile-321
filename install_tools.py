#!/usr/bin/env python3
"""
Installer script for Scam Tool dependencies
"""

import subprocess
import sys

def install_kali_tools():
    """Install required Kali Linux tools"""
    tools = ['nmap', 'arp-scan', 'dnsenum']
    
    print("Installing required Kali Linux tools...")
    print("This may take a few minutes...")
    
    try:
        # Update package list
        print("Updating package list...")
        subprocess.run(['sudo', 'apt', 'update'], check=True)
        
        # Install tools
        for tool in tools:
            print(f"Installing {tool}...")
            subprocess.run(['sudo', 'apt', 'install', '-y', tool], check=True)
            print(f"{tool} installed successfully")
        
        print("All tools installed successfully!")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"Error installing tools: {e}")
        return False
    except KeyboardInterrupt:
        print("\nInstallation cancelled by user")
        return False

def main():
    print("Scam Tool - Kali Linux Edition")
    print("Installer Script")
    print("=" * 40)
    
    if sys.platform != "linux":
        print("This installer is designed for Linux systems (Kali Linux)")
        return
    
    try:
        choice = input("Do you want to install the required tools? (y/n): ")
        if choice.lower() in ['y', 'yes']:
            install_kali_tools()
        else:
            print("Installation cancelled")
    except KeyboardInterrupt:
        print("\nInstallation cancelled by user")

if __name__ == "__main__":
    main()