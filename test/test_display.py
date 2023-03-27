import unittest
from unittest.mock import patch
import os
import sys
import io
parent_path = os.path.abspath(os.path
                                .join(os.path.dirname(__file__), os.pardir))
sys.path.append(parent_path)
sys.path.insert(0, 'main_menu_folder/')
import display


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


if __name__ == "__main__":
    unittest.main()
