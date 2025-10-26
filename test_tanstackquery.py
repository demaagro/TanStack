# test_tanstackquery.py
"""
Tests for TanStackQuery module.
"""

import unittest
from tanstackquery import TanStackQuery

class TestTanStackQuery(unittest.TestCase):
    """Test cases for TanStackQuery class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = TanStackQuery()
        self.assertIsInstance(instance, TanStackQuery)
        
    def test_run_method(self):
        """Test the run method."""
        instance = TanStackQuery()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
