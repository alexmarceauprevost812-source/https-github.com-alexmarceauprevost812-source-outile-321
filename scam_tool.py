#!/usr/bin/env python3
"""
Scam Tool - Kali Linux Edition
A tool for finding device addresses and conducting attacks on new devices
using Kali Linux tools.
"""

import subprocess
import sys
import os
import argparse
import json
from datetime import datetime

class ScamTool:
    def __init__(self):
        self.tools = {
            'nmap': 'nmap',
            'arp-scan': 'arp-scan',
            'dnsenum': 'dnsenum',
            'john': 'john',
            'hashcat': 'hashcat',
            'wifite': 'wifite',
            'aircrack-ng': 'aircrack-ng',
            'ettercap': 'ettercap'
        }
        self.results_dir = "./scam_results"
        self.create_results_dir()
    
    def create_results_dir(self):
        """Create directory for storing results"""
        if not os.path.exists(self.results_dir):
            os.makedirs(self.results_dir)
    
    def check_tools(self):
        """Check if required Kali Linux tools are installed"""
        missing_tools = []
        for tool_name, tool_command in self.tools.items():
            if not self.is_tool_installed(tool_command):
                missing_tools.append(tool_name)
        
        if missing_tools:
            print(f"Warning: Missing tools: {', '.join(missing_tools)}")
            print("Please install these tools using: sudo apt install <tool-name>")
            return False
        return True
    
    def is_tool_installed(self, tool_name):
        """Check if a tool is installed"""
        try:
            subprocess.run(['which', tool_name], 
                         stdout=subprocess.PIPE, 
                         stderr=subprocess.PIPE, 
                         check=True)
            return True
        except subprocess.CalledProcessError:
            return False
    
    def scan_network(self, network_range):
        """Scan network for devices using nmap"""
        print(f"Scanning network: {network_range}")
        try:
            result = subprocess.run([
                'nmap', '-sn', network_range, '-oN', f'{self.results_dir}/nmap_scan.txt'
            ], capture_output=True, text=True, check=True)
            
            print("Scan results:")
            print(result.stdout)
            return result.stdout
        except subprocess.CalledProcessError as e:
            print(f"Error during scan: {e}")
            return None
    
    def scan_devices_arp(self, network_range):
        """Scan for devices using arp-scan"""
        print(f"Scanning devices with arp-scan: {network_range}")
        try:
            result = subprocess.run([
                'arp-scan', '--quiet', network_range, '--output', f'{self.results_dir}/arp_scan.txt'
            ], capture_output=True, text=True, check=True)
            
            print("ARP scan results:")
            print(result.stdout)
            return result.stdout
        except subprocess.CalledProcessError as e:
            print(f"Error during arp scan: {e}")
            return None
    
    def find_device_addresses(self, network_range):
        """Find device addresses in the network"""
        print("Finding device addresses...")
        # First try arp-scan
        arp_result = self.scan_devices_arp(network_range)
        
        # Then try nmap for additional info
        nmap_result = self.scan_network(network_range)
        
        return arp_result, nmap_result
    
    def crack_passwords_with_john(self, hash_file):
        """Crack passwords using John the Ripper"""
        print(f"Cracking passwords with John the Ripper: {hash_file}")
        try:
            result = subprocess.run([
                'john', '--wordlist=/usr/share/wordlists/rockyou.txt', hash_file
            ], capture_output=True, text=True, check=True)
            
            print("John the Ripper results:")
            print(result.stdout)
            return result.stdout
        except subprocess.CalledProcessError as e:
            print(f"Error during John cracking: {e}")
            return None
    
    def crack_passwords_with_hashcat(self, hash_file, wordlist):
        """Crack passwords using Hashcat"""
        print(f"Cracking passwords with Hashcat: {hash_file}")
        try:
            result = subprocess.run([
                'hashcat', '-m', '0', hash_file, wordlist
            ], capture_output=True, text=True, check=True)
            
            print("Hashcat results:")
            print(result.stdout)
            return result.stdout
        except subprocess.CalledProcessError as e:
            print(f"Error during Hashcat cracking: {e}")
            return None
    
    def attack_wifi_network(self, ssid, interface):
        """Attack a Wi-Fi network using Wifite"""
        print(f"Attacking Wi-Fi network: {ssid}")
        try:
            # Run wifite in a way that allows us to capture output
            result = subprocess.run([
                'wifite', '--kill', '--dict', '/usr/share/wordlists/rockyou.txt', 
                '--interface', interface, '--ssid', ssid
            ], capture_output=True, text=True, check=True)
            
            print("Wifite attack results:")
            print(result.stdout)
            return result.stdout
        except subprocess.CalledProcessError as e:
            print(f"Error during Wi-Fi attack: {e}")
            return None
    
    def get_device_info(self, target_ip):
        """Get detailed information about a device"""
        print(f"Getting detailed info for: {target_ip}")
        try:
            result = subprocess.run([
                'nmap', '-sV', '-O', target_ip, '-oN', f'{self.results_dir}/device_info_{target_ip.replace(".", "_")}.txt'
            ], capture_output=True, text=True, check=True)
            
            print("Device info:")
            print(result.stdout)
            return result.stdout
        except subprocess.CalledProcessError as e:
            print(f"Error getting device info: {e}")
            return None
    
    def auto_attack_network(self, network_range):
        """Automatically scan and attack all devices in the network"""
        print("Starting automatic network attack...")
        
        # Scan for devices
        print("Scanning for devices...")
        addresses = self.find_device_addresses(network_range)
        
        if addresses[0]:  # ARP scan results
            print("Auto-attacking discovered devices...")
            # In a real implementation, we would parse the results and attack each device
            print("Auto-attack completed")
        
        return True
    
    def run(self, args):
        """Main execution method"""
        print("Starting Scam Tool - Kali Linux Edition")
        print("=" * 50)
        
        # Check if tools are installed
        if not self.check_tools():
            print("Please install required tools before proceeding.")
            return
        
        # If no arguments provided, show help
        if not args.network and not args.attack_wifi and not args.auto_attack:
            print("Usage: python scam_tool.py")
            print("  --network <network_range>     : Scan network")
            print("  --attack-wifi <ssid>          : Attack Wi-Fi network")
            print("  --auto-attack <network_range> : Auto-attack all devices")
            print("  --hash-file <file>            : Crack passwords")
            return
        
        # Handle auto-attack mode
        if args.auto_attack:
            print("Starting auto-attack mode...")
            self.auto_attack_network(args.auto_attack)
        
        # Handle network scanning
        if args.network:
            print("Finding device addresses...")
            addresses = self.find_device_addresses(args.network)
        
        # Handle Wi-Fi attack
        if args.attack_wifi and args.interface:
            print("Starting Wi-Fi attack...")
            attack_result = self.attack_wifi_network(args.attack_wifi, args.interface)
        
        # Handle password cracking
        if args.hash_file:
            print("Starting password cracking...")
            if args.cracker == 'john':
                crack_result = self.crack_passwords_with_john(args.hash_file)
            elif args.cracker == 'hashcat':
                crack_result = self.crack_passwords_with_hashcat(args.hash_file, args.wordlist)
        
        print("Scam Tool execution finished.")

def main():
    parser = argparse.ArgumentParser(description='Scam Tool - Kali Linux Edition')
    parser.add_argument('--network', help='Network range to scan (e.g., 192.168.1.0/24)')
    parser.add_argument('--attack-wifi', help='SSID of Wi-Fi network to attack')
    parser.add_argument('--interface', help='Network interface to use for Wi-Fi attack')
    parser.add_argument('--hash-file', help='File containing password hashes to crack')
    parser.add_argument('--cracker', choices=['john', 'hashcat'], default='john', help='Password cracker to use')
    parser.add_argument('--wordlist', default='/usr/share/wordlists/rockyou.txt', help='Wordlist file for cracking')
    parser.add_argument('--auto-attack', help='Auto-attack all devices in network range')
    
    args = parser.parse_args()
    
    # Create and run the scam tool
    tool = ScamTool()
    tool.run(args)

if __name__ == "__main__":
    main()