"""
Configuration file for Scam Tool
"""

# Default settings
DEFAULT_NETWORK_RANGE = "192.168.1.0/24"
DEFAULT_TIMEOUT = 30
DEFAULT_OUTPUT_DIR = "./scam_results"

# Tool configurations
TOOLS = {
    'nmap': {
        'command': 'nmap',
        'options': ['-sn', '-T4']
    },
    'arp-scan': {
        'command': 'arp-scan',
        'options': ['--quiet']
    }
}

# Logging configuration
LOG_LEVEL = "INFO"
LOG_FILE = "scam_tool.log"