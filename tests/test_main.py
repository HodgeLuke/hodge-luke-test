#!/usr/bin/env python3
"""
Test file for main.py
"""

import unittest
import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from main import greet

class TestGreet(unittest.TestCase):
    """Test cases for greet function"""
    
    def test_greet_world(self):
        """Test greeting with 'World'"""
        result = greet("World")
        self.assertEqual(result, "Hello, World!")
    
    def test_greet_custom_name(self):
        """Test greeting with custom name"""
        result = greet("Hodge Luke")
        self.assertEqual(result, "Hello, Hodge Luke!")

if __name__ == '__main__':
    unittest.main()
