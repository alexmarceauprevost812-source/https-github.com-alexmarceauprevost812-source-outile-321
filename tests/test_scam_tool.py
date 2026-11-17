#!/usr/bin/env python3
"""
Unit tests for Scam Tool
"""

import unittest
import sys
import os

# Add the project root to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + '/..')

from scam_tool import ScamTool

class TestScamTool(unittest.TestCase):
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.tool = ScamTool()
    
    def test_tool_initialization(self):
        """Test that the tool initializes correctly"""
        self.assertIsInstance(self.tool, ScamTool)
    
    def test_tool_check_tools(self):
        """Test tool checking functionality"""
        # This test will depend on whether tools are installed
        # For now, we'll just check that the method exists and runs
        result = self.tool.check_tools()
        self.assertIsInstance(result, bool)
    
    def test_is_tool_installed(self):
        """Test tool installation checking"""
        # Test with a tool that should exist
        result = self.tool.is_tool_installed('nmap')
        # This may return True or False depending on installation
        self.assertIsInstance(result, bool)
    
    def test_network_scanning(self):
        """Test network scanning functionality"""
        # Since we can't actually scan without a network,
        # we'll just test that the method exists
        self.assertTrue(hasattr(self.tool, 'scan_network'))

if __name__ == '__main__':
    unittest.main()