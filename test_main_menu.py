import unittest
from unittest.mock import patch
import main_menu as mm
from contextlib import contextmanager
import sys
import io

class TestNumPlayers(unittest.TestCase):
    """ 
    Verification of the number of players
    input values and types
    """
    @patch('builtins.input', lambda _: '1')
    @patch("main_menu.log_in_players")
    @patch("main_menu.validate_num_players")
    def test_get_num_players_1(self, mock_num1, mock_log_in):
        sys.stdout = io.StringIO()

        mock_num1.return_value = 1
        mock_log_in.return_value = True
        self.assertEqual(mm.get_num_players(), 1)


    @patch('builtins.input', lambda _: '2')
    @patch("main_menu.log_in_players")
    @patch("main_menu.validate_num_players")
    def test_get_num_players_2(self, mock_num1, mock_log_in):
        mock_num1.return_value = 2
        mock_log_in.return_value = True
        self.assertEqual(mm.get_num_players(), 2)

        sys.stdout = sys.__stdout__
        

        
if __name__ == "__main__":
    unittest.main()
