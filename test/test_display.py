import unittest
from unittest.mock import patch
import os
import sys
import io
# Get the parent path of the current script
parent_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
# Add the parent path to the system path
sys.path.append(parent_path)
from main_menu import display


class TestDisplay(unittest.TestCase):
    """
    Testing of the display functions 
    """
    def setUp(self):
        # Disable print output
        self.saved_stdout = sys.stdout
        sys.stdout = io.StringIO()

    def tearDown(self):
        # Enable print output
        sys.stdout = self.saved_stdout

    def test_cls(self):
        self.assertEqual(display.cls(), "clear")

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