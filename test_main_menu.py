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

    def col_values(self, value):
        cols = [["empty col"], [self.mock_player1.name], [self.mock_player1.email], [self.mock_player1.total_games], [self.mock_player1.wins], [self.mock_player1.loses]]
        return cols[value]

    def update_cell(self, row, cell, value):
        return True

    def append_row(self, row):
        return True

mock_worksheet = MockWorksheet()

def mock_validate_email(email):
    """ 
    Mocks the validate email to return true
    """
    return True

def mock_rtnp():
    """ 
    Mocks the return to num players to return true
    """
    return True

def mock_ver(func, registered, name):
    """ 
    Mocks the validate email registered to return email
    """
    return func

def mock_ape(name):
    """ 
    Mocks the ask player email to return email
    """
    return "john@gmail.com"

def mock_aiep1(name, registered):
    """ 
    Mocks the ask incorrect email question to return email
    """
    return "john@gmail.com"

def mock_aiep2(name, registered, email):
    """ 
    Mocks the ask incorrect email question to return email
    """
    return email

def mock_cier1(email):
    """ 
    Mocks the check is email registered to return True
    """
    return True

def mock_cier2(email):
    """ 
    Mocks the check is email registered to return True
    """
    return False

def mock_iei(name, registered, email):
    """ 
    Mocks the incorrect email input to return email
    """
    return email

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
        self.assertEqual(self.player1.add_player_to_database(), ["John", "john@gmail.com", 10, 4, 6])

    @patch("main_menu.WORKSHEET", mock_worksheet)
    def test_check_is_email_registered(self):
        self.assertEqual(mm.check_is_email_registered(self.player1.email), True)
        self.assertEqual(mm.check_is_email_registered("pat@gmail.com"), False)

    @patch("main_menu.WORKSHEET", mock_worksheet)
    def test_regisiter_or_login_player(self):
        self.assertEqual(self.player1.register_or_login_player(), [self.player1.name, self.player1.email])
        self.assertEqual(self.player2.register_or_login_player(), [self.player2.name, self.player2.email, self.player2.total_games, self.player2.wins, self.player2.loses])

    def test_display_player_stats(self):
        self.assertEqual(self.player1.display_player_stats(), "Name: John Email: john@gmail.com Total Games: 10 Wins: 4 Loses: 6")


class TestLogInPlayers(unittest.TestCase):
    """
    Testing of loging in players feature
    """
    def setUp(self):
        self.player1 = mm.Player("John", "john@gmail.com", 10, 4, 6)
        self.player2 = mm.Player("Pat", "pat@gmail.com", 0, 0, 0)

    @patch("main_menu.return_to_num_players", mock_rtnp)
    def test_validate_registered_input(self):
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
        self.assertEqual(mm.validate_user_name(self.player1.name), True)

    @patch("builtins.input", lambda _: "John")
    def test_ask_player_name(self):
        self.assertEqual(mm.ask_player_name("1"), self.player1.name)

    @patch("main_menu.validate_email", mock_validate_email)
    def test_validate_user_email(self):
        self.assertEqual(mm.validate_user_email(self.player1.email), True)

    @patch("main_menu.validate_email", mock_validate_email)
    @patch("builtins.input", lambda _: "john@gmail.com")
    def test_ask_player_email(self):
        self.assertEqual(mm.ask_player_email(self.player1.name), self.player1.email)
    
    @patch("main_menu.return_to_num_players", mock_rtnp)
    def test_validate_incorrect_email_input(self):
        self.assertEqual(mm.validate_incorrect_email_input("1"), 1)
        self.assertEqual(mm.validate_incorrect_email_input("2"), 2)
        self.assertEqual(mm.validate_incorrect_email_input("r"), 3)
        self.assertEqual(mm.validate_incorrect_email_input("3"), False)

    @patch("builtins.input", lambda _: "1")
    @patch("main_menu.validate_email_registered", mock_ver)
    @patch("main_menu.ask_player_email", mock_ape)
    def test_ask_incorrect_email_question1_1(self):
        self.assertEqual(mm.ask_incorrect_email_question1(self.player1.name, True), self.player1.email)
        
    @patch("builtins.input", lambda _: "2")
    @patch("main_menu.validate_email_registered", mock_ver)
    @patch("main_menu.ask_player_email", mock_ape)
    def test_ask_incorrect_email_question1_2(self):
        self.assertEqual(mm.ask_incorrect_email_question1(self.player1.name, True), self.player1.email)

    @patch("builtins.input", lambda _: "1")
    @patch("main_menu.validate_email_registered", mock_ver)
    @patch("main_menu.ask_player_email", mock_ape)
    def test_ask_incorrect_email_question2_1(self):
        self.assertEqual(mm.ask_incorrect_email_question2(self.player1.name, True, self.player1.email), self.player1.email)

    @patch("builtins.input", lambda _: "2")
    @patch("main_menu.validate_email_registered", mock_ver)
    @patch("main_menu.ask_player_email", mock_ape)
    def test_ask_incorrect_email_question2_2(self):
        self.assertEqual(mm.ask_incorrect_email_question2(self.player1.name, True, self.player1.email), self.player1.email)

    @patch("main_menu.ask_incorrect_email_question1", mock_aiep1)
    @patch("main_menu.ask_incorrect_email_question2", mock_aiep2)
    def test_incorrect_email_input(self):
        self.assertEqual(mm.incorrect_email_input(self.player1.name, True, self.player1.email), self.player1.email)
        self.assertEqual(mm.incorrect_email_input(self.player1.name, False, self.player1.email), self.player1.email)

    @patch("main_menu.check_is_email_registered", mock_cier1)
    @patch("main_menu.incorrect_email_input", mock_iei)
    def test_validate_email_registered_1(self):
        self.assertEqual(mm.validate_email_registered(self.player1.email, True, self.player1.name), self.player1.email)
        self.assertEqual(mm.validate_email_registered(self.player1.email, False, self.player1.name), self.player1.email)

    @patch("main_menu.check_is_email_registered", mock_cier2)
    @patch("main_menu.incorrect_email_input", mock_iei)
    def test_validate_email_registered_2(self):
        self.assertEqual(mm.validate_email_registered(self.player1.email, True, self.player1.name), self.player1.email)
        self.assertEqual(mm.validate_email_registered(self.player1.email, False, self.player1.name), self.player1.email)

    @patch("main_menu.WORKSHEET", mock_worksheet)
    def test_get_worksheet_value(self):
        self.assertEqual(mm.get_worksheet_value(self.player1.email, "total_games"), 10)
        self.assertEqual(mm.get_worksheet_value(self.player1.email, "wins"), 4)
        self.assertEqual(mm.get_worksheet_value(self.player1.email, "loses"), 6)
        self.assertEqual(mm.get_worksheet_value("pat@gmail.com", "total_games"), 0)
        self.assertEqual(mm.get_worksheet_value(self.player1.email, "id"), 0)

        
    sys.stdout = sys.__stdout__    

if __name__ == "__main__":
    unittest.main()
