# test_csstotailwind.py
"""
Tests for CssToTailwind module.
"""

import unittest
from csstotailwind import CssToTailwind

class TestCssToTailwind(unittest.TestCase):
    """Test cases for CssToTailwind class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CssToTailwind()
        self.assertIsInstance(instance, CssToTailwind)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CssToTailwind()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
