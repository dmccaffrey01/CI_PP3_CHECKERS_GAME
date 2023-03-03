import unittest
from unittest.mock import patch
import main_menu as mm
import sys
import io
import gspread

class MockWorksheet():
    """
    Creates an mock instance of Worksheet class from gspread
    """
    mock_player1 = mm.Player("John", "john@gmail.com", 10, 4, 6)

    def __init__(self, value):
        self.value = value

    def col_values(self, value):
        return [self.mock_player1.email]

    def update_cell(self, row, cell, value):
        return True

    def append_row(self, row):
        return True

mock_worksheet = MockWorksheet(1)

class TestNumPlayers(unittest.TestCase):
    """ 
    Verification of the number of players
    input values and types
    """
    def test_validate_num_players(self):
        self.assertEqual(mm.validate_num_players("1"), 1)
        self.assertEqual(mm.validate_num_players("2"), 2)
        self.assertEqual(mm.validate_num_players("3"), False)

    # Test if statement in while loop
    @patch('builtins.input', lambda _: '1')
    @patch("main_menu.log_in_players")
    @patch("main_menu.validate_num_players")
    def test_get_num_players_1(self, mock_num1, mock_log_in):
        sys.stdout = io.StringIO()

        mock_num1.return_value = 1
        mock_log_in.return_value = True
        self.assertEqual(mm.get_num_players(), 1)

        mock_num1.return_value = 2
        mock_log_in.return_value = True
        self.assertEqual(mm.get_num_players(), 2)

        sys.stdout = sys.__stdout__
        
class TestPlayer(unittest.TestCase):
    """ 
    Verification of player class
    """
    def setUp(self):
        self.player1 = mm.Player("John", "john@gmail.com", 10, 4, 6)
        self.player2 = mm.Player("Pat", "pat@gmail.com", 0, 0, 0)

    def test_name(self):
        self.assertEqual(self.player1.name, "John")
        self.player1.name = "George"
        self.assertEqual(self.player1.name, "George")
    
    def test_email(self):
        self.assertEqual(self.player1.email, "john@gmail.com")
        self.player1.email = "george@gmail.com"
        self.assertEqual(self.player1.email, "george@gmail.com")

    def test_total_games(self):
        self.assertEqual(self.player1.total_games, 10)
        self.player1.total_games = 11
        self.assertEqual(self.player1.total_games, 11)

    def test_wins(self):
        self.assertEqual(self.player1.wins, 4)
        self.player1.wins = 5
        self.assertEqual(self.player1.wins, 5)

    def test_loses(self):
        self.assertEqual(self.player1.loses, 6)
        self.player1.loses = 7
        self.assertEqual(self.player1.loses, 7)
    
    @patch("main_menu.WORKSHEET", mock_worksheet)
    def test_update_database_value(self):
        self.assertEqual(self.player1.update_database_value("name", "john", self.player1.email), [1, 1])
        self.assertEqual(self.player1.update_database_value("email", "john", self.player1.email), [1, 2])
        self.assertEqual(self.player1.update_database_value("total_games", "john", self.player1.email), [1, 3])
        self.assertEqual(self.player1.update_database_value("wins", "john", self.player1.email), [1, 4])
        self.assertEqual(self.player1.update_database_value("loses", "john", self.player1.email), [1, 5])

    @patch("main_menu.WORKSHEET", mock_worksheet)
    def test_add_player_to_database(self):
        self.assertEqual(self.player1.add_player_to_database(self.player1.name, self.player1.email, self.player1.total_games, self.player1.wins, self.player1.loses), ["John", "john@gmail.com", 10, 4, 6])

    @patch("main_menu.WORKSHEET", mock_worksheet)
    def test_check_is_email_registered(self):
        self.assertEqual(mm.check_is_email_registered(self.player1.email), True)
        self.assertEqual(mm.check_is_email_registered("pat@gmail.com"), False)

    @patch("main_menu.WORKSHEET", mock_worksheet)
    def test_regisiter_or_login_player(self):
        self.assertEqual(self.player1.register_or_login_player(), [self.player1.name, self.player1.email])
        self.assertEqual(self.player2.register_or_login_player(), [self.player2.name, self.player2.email, self.player2.total_games, self.player2.wins, self.player2.loses])
        
if __name__ == "__main__":
    unittest.main()
