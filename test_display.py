import unittest
from unittest.mock import patch
import display
import sys
import io

class TestDisplay(unittest.TestCase):
    """
    Testing of the display functions 
    """
    def test_cls(self):
        self.assertEqual(display.cls(), "clear")

        # Disable print output
        sys.stdout = io.StringIO()

    def test_new_line(self):
        self.assertEqual(display.new_line(), "new line")

    def test_welcome(self):
        self.assertEqual(display.welcome(), "welcome")
    
    def test_typewriter(self):
        self.assertEqual(display.typewriter("test"), "typewriter") 


# Enable print output
sys.stdout = sys.__stdout__ 


    


if __name__ == "__main__":
    unittest.main()