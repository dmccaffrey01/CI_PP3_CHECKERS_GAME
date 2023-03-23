import unittest
from unittest.mock import patch
import os
import sys
import io
import colorama
from colorama import Fore, Back, Style
# Get the parent path of the current script
parent_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
# Add the parent path to the system path
sys.path.append(parent_path)
sys.path.insert(0, 'checkers_folder/')
import feature_testing as ft

class TestFeatureTesting(unittest.TestCase):
    """
    Testing of the leaderboard sort ranks 
    """
    def setUp(self):
        # Disable print output
        self.saved_stdout = sys.stdout
        sys.stdout = io.StringIO()

    def tearDown(self):
        # Enable print output
        sys.stdout = self.saved_stdout

    def test_go_to_feature_testing(self):
        
