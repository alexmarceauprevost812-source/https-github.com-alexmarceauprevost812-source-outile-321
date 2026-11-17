#!/usr/bin/env python3
"""
Example usage of the Scam Tool
"""

import subprocess
import sys
import os

def main():
    print("Scam Tool - Example Usage")
    print("=" * 40)
    
    # Show how to run the tool
    print("To use the scam tool:")
    print("1. Make sure you have Kali Linux tools installed")
    print("2. Run the tool with a network range:")
    print("   python scam_tool.py --network 192.168.1.0/24")
    print()
    
    print("To install required tools:")
    print("   python install_tools.py")
    print()
    
    print("To run tests:")
    print("   python -m pytest tests/")
    print()
    
    # Show current directory structure
    print("Current directory contents:")
    for root, dirs, files in os.walk('.'):
        level = root.replace('.', '').count(os.sep)
        indent = ' ' * 2 * level
        print(f"{indent}{os.path.basename(root)}/")
        subindent = ' ' * 2 * (level + 1)
        for file in files:
            print(f"{subindent}{file}")

if __name__ == "__main__":
    main()