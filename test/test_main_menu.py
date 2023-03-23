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
sys.path.insert(0, 'main_menu_folder/')
import main_menu as mm
import game_rules
sys.path.remove('main_menu_folder/')
sys.path.insert(0, 'checkers_folder/')
import checkers
import feature_testing

#Initialize colorama
colorama.init(autoreset=True)

class MockWorksheet():
    """
    Creates an mock instance of Worksheet class from gspread
    """
    def col_values(self, value):
        cols = [["empty col"], ["John"], ["john@gmail.com"], ["10"], ["4"], ["6"]]
        return cols[value]

    def update_cell(self, row, cell, value):
        return True

    def append_row(self, row):
        return True

    def get_all_values(self):
        return [["Name", "Email", "Games", "Wins", "Loses"], ["John", "john@gmail.com", "10", "4", "6"], ["Pat", "pat@gmail.com", "12", "8", "4"]]

mock_worksheet = MockWorksheet()

def mock_function(*args, **kwargs):
    """ 
    Mocks a function to return True
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
    if (name == "John"):
        return "john@gmail.com"
    else:
        return "pat@gmail.com"

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

def mock_ar(num):
    """ 
    Mocks the ask registered to return registered
    """
    if num == "1":
        return True
    else:
        return False

def mock_apn(num):
    """ 
    Mocks the ask player name to return name
    """
    if num == "1":
        return "John"
    else:
        return "Pat"

def mock_gwv(email, value):
    """ 
    Mocks the get worksheet value to return value
    """
    if value == "total_games":
        if email == "john@gmail.com":
            return 10
        else:
            return 0
    elif value == "wins":
        if email == "john@gmail.com":
            return 4
        else:
            return 0
    elif value == "loses":
        if email == "john@gmail.com":
            return 6
        else:
            return 0

class TestMainMenu(unittest.TestCase):
    """ 
    Testing of the main menu and the selection of options
    """
    def setUp(self):
        # Disable print output
        self.saved_stdout = sys.stdout
        sys.stdout = io.StringIO()

    def tearDown(self):
        # Enable print output
        sys.stdout = self.saved_stdout

    def test_validate_main_menu_selection(self):
        self.assertEqual(mm.validate_main_menu_selection("1"), 1)
        self.assertEqual(mm.validate_main_menu_selection("one"), 1)
        self.assertEqual(mm.validate_main_menu_selection("2"), 2)
        self.assertEqual(mm.validate_main_menu_selection("two"), 2)
        self.assertEqual(mm.validate_main_menu_selection("3"), 3)
        self.assertEqual(mm.validate_main_menu_selection("three"), 3)
        self.assertEqual(mm.validate_main_menu_selection("4"), 4)
        self.assertEqual(mm.validate_main_menu_selection("5"), 5)
        self.assertEqual(mm.validate_main_menu_selection("-1"), False)
        self.assertEqual(mm.validate_main_menu_selection("6"), False)
        

    @patch("main_menu.get_num_players", mock_function)
    @patch("game_rules.display_game_rules", mock_function)
    @patch("leaderboard.go_to_leaderboard", mock_function)
    @patch("feature_testing.go_to_feature_testing", mock_function)
    @patch("main_menu.exit_game", mock_function)
    def test_main_menu_selection(self):
        self.assertEqual(mm.main_menu_selection(1), 1)
        self.assertEqual(mm.main_menu_selection(2), 2)
        self.assertEqual(mm.main_menu_selection(3), 3)
        self.assertEqual(mm.main_menu_selection(4), 4)
        self.assertEqual(mm.main_menu_selection(5), 5)

    @patch("main_menu.main_menu_selection", mock_function)
    @patch("builtins.input", side_effect=["wrong", "1"])
    def test_main_menu_screen_1(self, mock_input):
        self.assertEqual(mm.main_menu_screen(), 1)

    @patch("main_menu.main_menu_selection", mock_function)
    @patch("builtins.input", lambda _: "2")
    def test_main_menu_screen_2(self):
        self.assertEqual(mm.main_menu_screen(), 2)

    @patch("main_menu.main_menu_selection", mock_function)
    @patch("builtins.input", lambda _: "3")
    def test_main_menu_screen_3(self):
        self.assertEqual(mm.main_menu_screen(), 3)

    @patch("main_menu.main_menu_selection", mock_function)
    @patch("builtins.input", lambda _: "4")
    def test_main_menu_screen_3(self):
        self.assertEqual(mm.main_menu_screen(), 4)

    @patch("main_menu.main_menu_selection", mock_function)
    @patch("builtins.input", lambda _: "5")
    def test_main_menu_screen_3(self):
        self.assertEqual(mm.main_menu_screen(), 5)

class TestNumPlayers(unittest.TestCase):
    """
    Testing of the number of players
    input values and types
    """
    def setUp(self):
        # Disable print output
        self.saved_stdout = sys.stdout
        sys.stdout = io.StringIO()

    def tearDown(self):
        # Enable print output
        sys.stdout = self.saved_stdout

    @patch("main_menu.raise_return_to_main_menu", mock_function)
    def test_validate_num_players(self):
        self.assertEqual(mm.validate_num_players("1"), 1)
        self.assertEqual(mm.validate_num_players("2"), 2)
        self.assertEqual(mm.validate_num_players("3"), 3)
        self.assertEqual(mm.validate_num_players("r"), 4)
        self.assertEqual(mm.validate_num_players("4"), False)

    @patch("builtins.input", side_effect=["wrong", "1"])
    @patch("main_menu.log_in_players", mock_function)
    def test_get_num_players_1(self, mock_input):
        self.assertEqual(mm.get_num_players(), 1)

    @patch("builtins.input", lambda _: "r")
    @patch("main_menu.main_menu_screen", mock_function)
    def test_get_num_players_return(self):
        self.assertEqual(mm.get_num_players(), "return_to_main_menu")

    @patch("builtins.input", lambda _: "2")
    @patch("main_menu.log_in_players", mock_function)
    def test_get_num_players_2(self):
        self.assertEqual(mm.get_num_players(), 2)

    @patch("builtins.input", lambda _: "3")
    @patch("main_menu.start_cpu_game", mock_function)
    def test_get_num_players_3(self):
        self.assertEqual(mm.get_num_players(), 3)

class TestPlayer(unittest.TestCase):
    """
    Testing of player class
    """
    def setUp(self):
        # Disable print output
        self.saved_stdout = sys.stdout
        sys.stdout = io.StringIO()

        self.player1 = mm.Player("John", "john@gmail.com", 10, 4, 6)
        self.player2 = mm.Player("Pat", "pat@gmail.com", 0, 0, 0)

    def tearDown(self):
        # Enable print output
        sys.stdout = self.saved_stdout

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
        self.assertEqual(self.player1.display_player_stats(), f"{Fore.CYAN + 'Name: ' + Fore.WHITE + 'John' + Fore.CYAN + '   Email: ' + Fore.WHITE + 'john@gmail.com' + Fore.CYAN + '   Total Games: ' + Fore.WHITE + '10' + Fore.CYAN + '   Wins: ' + Fore.WHITE + '4' + Fore.CYAN + '   Loses: ' + Fore.WHITE + '6'}")
    
class TestLogInPlayers(unittest.TestCase):
    """
    Testing of loging in players feature
    """
    def setUp(self):
        # Disable print output
        self.saved_stdout = sys.stdout
        sys.stdout = io.StringIO()

        self.player1 = mm.Player("John", "john@gmail.com", 10, 4, 6)
        self.player2 = mm.Player("Pat", "pat@gmail.com", 0, 0, 0)

    def tearDown(self):
        # Enable print output
        sys.stdout = self.saved_stdout

    @patch("main_menu.raise_return_to_main_menu", mock_function)
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

    @patch("builtins.input", side_effect=["wrong", "1"])
    def test_ask_registered_1(self, mock_input):
        self.assertEqual(mm.ask_registered("1"), True)
   
    @patch("builtins.input", lambda _: "2")
    def test_ask_registered_2(self):
        self.assertEqual(mm.ask_registered("1"), False)

    def test_validate_user_name(self):
        self.assertEqual(mm.validate_user_name(self.player1.name), True)
        self.assertEqual(mm.validate_user_name("1234"), False)

    @patch("builtins.input", side_effect=["1234567890123", "12A", "John"])
    def test_ask_player_name(self, mock_input):
        self.assertEqual(mm.ask_player_name("1"), self.player1.name)

    @patch("builtins.input", lambda _: "r")
    def test_ask_player_name_return(self):
        with self.assertRaises(Exception):
            mm.ask_player_name(1)

    def test_validate_user_email(self):
        self.assertEqual(mm.validate_user_email(self.player1.email), True)
        self.assertEqual(mm.validate_user_email("wrong"), False)

    @patch("builtins.input", lambda _: "john@gmail.com")
    def test_ask_player_email(self):
        self.assertEqual(mm.ask_player_email(self.player1.name), self.player1.email)

    @patch("builtins.input", lambda _: "r")
    def test_ask_player_email_return(self):
         with self.assertRaises(Exception):
            mm.ask_player_email("r")
   
    @patch("main_menu.raise_return_to_main_menu", mock_function)
    def test_validate_incorrect_email_input(self):
        self.assertEqual(mm.validate_incorrect_email_input("1"), 1)
        self.assertEqual(mm.validate_incorrect_email_input("2"), 2)
        self.assertEqual(mm.validate_incorrect_email_input("r"), 3)
        self.assertEqual(mm.validate_incorrect_email_input("3"), False)

    @patch("builtins.input", side_effect=["wrong", "1"])
    @patch("main_menu.validate_email_registered", mock_ver)
    @patch("main_menu.ask_player_email", mock_ape)
    def test_ask_incorrect_email_question1_1(self, mock_input):
        self.assertEqual(mm.ask_incorrect_email_question1(self.player1.name, True), self.player1.email)
       
    @patch("builtins.input", lambda _: "2")
    @patch("main_menu.validate_email_registered", mock_ver)
    @patch("main_menu.ask_player_email", mock_ape)
    def test_ask_incorrect_email_question1_2(self):
        self.assertEqual(mm.ask_incorrect_email_question1(self.player1.name, True), self.player1.email)

    @patch("builtins.input", side_effect=["wrong", "1"])
    @patch("main_menu.validate_email_registered", mock_ver)
    @patch("main_menu.ask_player_email", mock_ape)
    def test_ask_incorrect_email_question2_1(self, mock_input):
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

    @patch("main_menu.ask_registered", mock_ar)
    @patch("main_menu.ask_player_name", mock_apn)
    @patch("main_menu.validate_email_registered", mock_ver)
    @patch("main_menu.ask_player_email", mock_ape)
    @patch("main_menu.get_worksheet_value", mock_gwv)
    @patch("main_menu.start_checkers_game", mock_function)
    @patch("main_menu.ask_cpu_difficulty", mock_function)
    @patch("main_menu.WORKSHEET", mock_worksheet)
    def test_log_in_players(self):
        self.assertEqual(mm.log_in_players(1), 1)
        self.assertEqual(mm.log_in_players(2), 2)

    @patch("builtins.input", lambda _: "r")
    @patch("main_menu.main_menu_screen", mock_function)
    def test_log_in_players_return(self):
        self.assertEqual(mm.log_in_players(1), "return_to_main_menu")
        

class TestCheckersGame(unittest.TestCase):
    """
    Testing of the start checkers game 
    """
    def setUp(self):
        # Disable print output
        self.saved_stdout = sys.stdout
        sys.stdout = io.StringIO()

        # Disable display.typewriter
        patcher1 = patch('display.typewriter', return_value=None)
        patcher1.start()
        self.addCleanup(patcher1.stop)

    def tearDown(self):
        # Enable print output
        sys.stdout = self.saved_stdout

    @patch("main_menu.raise_return_to_main_menu", mock_function)
    def test_validate_cpu_difficulty_input(self):
        self.assertEqual(mm.validate_cpu_difficulty_input("1"), 1)
        self.assertEqual(mm.validate_cpu_difficulty_input("2"), 2)
        self.assertEqual(mm.validate_cpu_difficulty_input("3"), 3)
        self.assertEqual(mm.validate_cpu_difficulty_input("r"), 4)
        self.assertEqual(mm.validate_cpu_difficulty_input("5"), False)

    @patch("main_menu.raise_return_to_main_menu", mock_function)
    @patch("builtins.input", side_effect=["wrong", "1"])
    def test_ask_cpu_difficulty1(self, mock_input):
        self.assertEqual(mm.ask_cpu_difficulty(), 1)

    @patch("main_menu.raise_return_to_main_menu", mock_function)
    @patch("builtins.input", lambda _: "2")
    def test_ask_cpu_difficulty2(self):
        self.assertEqual(mm.ask_cpu_difficulty(), 2)

    @patch("main_menu.raise_return_to_main_menu", mock_function)
    @patch("builtins.input", lambda _: "3")
    def test_ask_cpu_difficulty3(self):
        self.assertEqual(mm.ask_cpu_difficulty(), 3)

    @patch("builtins.input", lambda _: "1")
    @patch("main_menu.start_checkers_game", mock_function)
    def test_start_cpu_game(self):
        self.assertEqual(mm.start_cpu_game(0), [1, 1])

    @patch("checkers.start_game", mock_function)
    def test_start_checkers_game(self):
        self.assertEqual(mm.start_checkers_game(1, 1, 0, "full", False), True)

    @patch("sys.exit", mock_function)
    def test_exit_game(self):
        self.assertEqual(mm.exit_game(), "exit_game")

    def test_exit_game_exception(self):
        self.assertEqual(mm.exit_game(), "exit_game")


if __name__ == "__main__":
    unittest.main()
