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
    Testing of the number of players
    input values and types
    """
    def test_validate_num_players(self):
        self.assertEqual(mm.validate_num_players("1"), 1)
        self.assertEqual(mm.validate_num_players("2"), 2)
        self.assertEqual(mm.validate_num_players("3"), False)

    # Test if statement in while loop
    @patch("builtins.input", lambda _: "1")
    @patch("main_menu.log_in_players")
    def test_get_num_players_1(self, mock_log_in):
        sys.stdout = io.StringIO()
        
        mock_log_in.return_value = True
        self.assertEqual(mm.get_num_players(), 1)

    @patch("builtins.input", lambda _: "2")
    @patch("main_menu.log_in_players")
    def test_get_num_players_2(self, mock_log_in):
        mock_log_in.return_value = True
        self.assertEqual(mm.get_num_players(), 2)
        
class TestPlayer(unittest.TestCase):
    """ 
    Testing of player class
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

class TestLogInPlayers(unittest.TestCase):
    """
    Testing of loging in players feature
    """
    @patch("main_menu.return_to_num_players")
    def test_validate_registered_input(self, mock_rtnp):
        mock_rtnp.return_value = True
        
        self.assertEqual(mm.validate_registered_input("1"), 1)
        self.assertEqual(mm.validate_registered_input("y"), 1)
        self.assertEqual(mm.validate_registered_input("yes"), 1)
        self.assertEqual(mm.validate_registered_input("2"), 2)
        self.assertEqual(mm.validate_registered_input("n"), 2)
        self.assertEqual(mm.validate_registered_input("no"), 2)
        self.assertEqual(mm.validate_registered_input("r"), 3)
        self.assertEqual(mm.validate_registered_input("4"), False)
        self.assertEqual(mm.validate_registered_input("-1"), False)

    @patch("builtins.input", lambda _: "1")
    def test_ask_registered_1(self):
        self.assertEqual(mm.ask_registered("1"), True)
    
    @patch("builtins.input", lambda _: "2")
    def test_ask_registered_2(self):
        self.assertEqual(mm.ask_registered("1"), False)

    def test_validate_user_name(self):
        self.assertEqual(mm.validate_user_name("John"), True)

    @patch("builtins.input", lambda _: "John")
    def test_ask_player_name(self):
        self.assertEqual(mm.ask_player_name("1"), "John")


    sys.stdout = sys.__stdout__

        

if __name__ == "__main__":
    unittest.main()
