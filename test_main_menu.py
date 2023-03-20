import unittest
from unittest.mock import patch
import main_menu as mm
import checkers
import run
import sys
import io
import gspread
import colorama
from colorama import Fore, Back, Style

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

def mock_function_1_arg_true(arg):
    """
    Mocks a function with one argument to return True
    """
    return True

def mock_function_0_arg_true():
    """ 
    Mocks a functino with zero arguments to return True
    """

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

def mock_scg(player1, player2, num):
    """
    Mocks the start checkers game function to return True 
    """
    return True

class TestMainMenu(unittest.TestCase):
    """ 
    Testing of the main menu and the selection of options
    """
    def test_validate_main_menu_selection(self):
        # Disable print output
        sys.stdout = io.StringIO()
        
        self.assertEqual(mm.validate_main_menu_selection("1"), 1)
        self.assertEqual(mm.validate_main_menu_selection("one"), 1)
        self.assertEqual(mm.validate_main_menu_selection("2"), 2)
        self.assertEqual(mm.validate_main_menu_selection("two"), 2)
        self.assertEqual(mm.validate_main_menu_selection("3"), 3)
        self.assertEqual(mm.validate_main_menu_selection("three"), 3)
        self.assertEqual(mm.validate_main_menu_selection("4"), 4)
        self.assertEqual(mm.validate_main_menu_selection("-1"), False)
        self.assertEqual(mm.validate_main_menu_selection("5"), False)
        

    @patch("main_menu.get_num_players", mock_function_0_arg_true)
    @patch("main_menu.display_game_rules", mock_function_0_arg_true)
    @patch("main_menu.go_to_leaderboard", mock_function_0_arg_true)
    @patch("main_menu.exit_game", mock_function_0_arg_true)
    def test_main_menu_selection(self):
        self.assertEqual(mm.main_menu_selection(1), 1)
        self.assertEqual(mm.main_menu_selection(2), 2)
        self.assertEqual(mm.main_menu_selection(3), 3)
        self.assertEqual(mm.main_menu_selection(4), 4)

    @patch("main_menu.main_menu_selection", mock_function_1_arg_true)
    @patch("builtins.input", lambda _: "1")
    def test_main_menu_screen_1(self):
        self.assertEqual(mm.main_menu_screen(), 1)

    @patch("main_menu.main_menu_selection", mock_function_1_arg_true)
    @patch("builtins.input", lambda _: "2")
    def test_main_menu_screen_2(self):
        self.assertEqual(mm.main_menu_screen(), 2)

    @patch("main_menu.main_menu_selection", mock_function_1_arg_true)
    @patch("builtins.input", lambda _: "3")
    def test_main_menu_screen_3(self):
        self.assertEqual(mm.main_menu_screen(), 3)

class TestNumPlayers(unittest.TestCase):
    """
    Testing of the number of players
    input values and types
    """
    @patch("main_menu.return_to_main_menu", mock_function_0_arg_true)
    def test_validate_num_players(self):
        self.assertEqual(mm.validate_num_players("1"), 1)
        self.assertEqual(mm.validate_num_players("2"), 2)
        self.assertEqual(mm.validate_num_players("3"), 3)
        self.assertEqual(mm.validate_num_players("r"), 4)
        self.assertEqual(mm.validate_num_players("4"), False)


    # Test if statement in while loop
    @patch("builtins.input", lambda _: "1")
    @patch("main_menu.log_in_players", mock_function_1_arg_true)
    def test_get_num_players_1(self):
        self.assertEqual(mm.get_num_players(), 1)


    @patch("builtins.input", lambda _: "2")
    @patch("main_menu.log_in_players", mock_function_1_arg_true)
    def test_get_num_players_2(self):
        self.assertEqual(mm.get_num_players(), 2)

    @patch("builtins.input", lambda _: "3")
    @patch("main_menu.start_cpu_game", mock_function_1_arg_true)
    def test_get_num_players_3(self):
        self.assertEqual(mm.get_num_players(), 3)

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
        self.assertEqual(self.player1.display_player_stats(), f"{Fore.CYAN + 'Name: ' + Fore.WHITE + 'John' + Fore.CYAN + '   Email: ' + Fore.WHITE + 'john@gmail.com' + Fore.CYAN + '   Total Games: ' + Fore.WHITE + '10' + Fore.CYAN + '   Wins: ' + Fore.WHITE + '4' + Fore.CYAN + '   Loses: ' + Fore.WHITE + '6'}")
    
class TestLogInPlayers(unittest.TestCase):
    """
    Testing of loging in players feature
    """
    def setUp(self):
        self.player1 = mm.Player("John", "john@gmail.com", 10, 4, 6)
        self.player2 = mm.Player("Pat", "pat@gmail.com", 0, 0, 0)

    @patch("main_menu.return_to_main_menu", mock_function_0_arg_true)
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

    @patch("main_menu.validate_email", mock_function_1_arg_true)
    def test_validate_user_email(self):
        self.assertEqual(mm.validate_user_email(self.player1.email), True)

    @patch("main_menu.validate_email", mock_function_1_arg_true)
    @patch("builtins.input", lambda _: "john@gmail.com")
    def test_ask_player_email(self):
        self.assertEqual(mm.ask_player_email(self.player1.name), self.player1.email)
   
    @patch("main_menu.return_to_main_menu", mock_function_0_arg_true)
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

    @patch("main_menu.ask_registered", mock_ar)
    @patch("main_menu.ask_player_name", mock_apn)
    @patch("main_menu.validate_email_registered", mock_ver)
    @patch("main_menu.ask_player_email", mock_ape)
    @patch("main_menu.get_worksheet_value", mock_gwv)
    @patch("main_menu.start_checkers_game", mock_scg)
    @patch("main_menu.ask_cpu_difficulty", mock_function_0_arg_true)
    @patch("main_menu.WORKSHEET", mock_worksheet)
    def test_log_in_players(self):
        self.assertEqual(mm.log_in_players(1), 1)
        self.assertEqual(mm.log_in_players(2), 2)

class TestCheckersGame(unittest.TestCase):
    """
    Testing of the start checkers game 
    """

    @patch("main_menu.return_to_main_menu", mock_function_0_arg_true)
    def test_validate_cpu_difficulty_input(self):
        self.assertEqual(mm.validate_cpu_difficulty_input("1"), 1)
        self.assertEqual(mm.validate_cpu_difficulty_input("2"), 2)
        self.assertEqual(mm.validate_cpu_difficulty_input("3"), 3)
        self.assertEqual(mm.validate_cpu_difficulty_input("r"), 4)
        self.assertEqual(mm.validate_cpu_difficulty_input("5"), False)

    @patch("main_menu.return_to_main_menu", mock_function_0_arg_true)
    @patch("builtins.input", lambda _: "1")
    def test_ask_cpu_difficulty1(self):
        self.assertEqual(mm.ask_cpu_difficulty(), 1)

    @patch("main_menu.return_to_main_menu", mock_function_0_arg_true)
    @patch("builtins.input", lambda _: "2")
    def test_ask_cpu_difficulty2(self):
        self.assertEqual(mm.ask_cpu_difficulty(), 2)

    @patch("main_menu.return_to_main_menu", mock_function_0_arg_true)
    @patch("builtins.input", lambda _: "3")
    def test_ask_cpu_difficulty3(self):
        self.assertEqual(mm.ask_cpu_difficulty(), 3)

    @patch("builtins.input", lambda _: "1")
    @patch("main_menu.start_checkers_game", mock_scg)
    def test_start_cpu_game(self):
        self.assertEqual(mm.start_cpu_game(0), [1, 1])

    @patch("checkers.start_game", mock_scg)
    def test_start_checkers_game(self):
        self.assertEqual(mm.start_checkers_game(1, 1, 0), True)

class TestLeaderboardSortRanks(unittest.TestCase):
    """
    Testing of the leaderboard sort ranks 
    """

    def test_validate_sort_ranks_input(self):
        self.assertEqual(mm.validate_sort_ranks_input("1"), 3)
        self.assertEqual(mm.validate_sort_ranks_input("2"), 2)
        self.assertEqual(mm.validate_sort_ranks_input("3"), 4)
        self.assertEqual(mm.validate_sort_ranks_input("r"), "return")
        self.assertEqual(mm.validate_sort_ranks_input("5"), False)

    @patch("builtins.input", lambda _: "1")
    def test_ask_user_to_sort_ranks1(self):
        self.assertEqual(mm.ask_user_to_sort_ranks(), 3)

    @patch("builtins.input", lambda _: "2")
    def test_ask_user_to_sort_ranks2(self):
        self.assertEqual(mm.ask_user_to_sort_ranks(), 2)

    @patch("builtins.input", lambda _: "3")
    def test_ask_user_to_sort_ranks3(self):
        self.assertEqual(mm.ask_user_to_sort_ranks(), 4)

    @patch("builtins.input", lambda _: "r")
    def test_ask_user_to_sort_ranks4(self):
        self.assertEqual(mm.ask_user_to_sort_ranks(), "return")

    
class TestLeaderboardDisplay(unittest.TestCase):
    """
    Testing of the leaderboard display functions 
    """

    def test_top_bottom_of_leaderboard(self):
        self.assertEqual(mm.top_bottom_of_leaderboard(), f"{' ' * 19 + Fore.YELLOW + '=' * 87}\n")

    def test_empty_leaderboard_line(self):
        self.assertEqual(mm.empty_leaderboard_line(), f"{' ' * 19 + Fore.YELLOW + '|' + Fore.YELLOW + '|' + ' ' * 15 + Fore.YELLOW + '|' + ' ' * 15 + Fore.YELLOW + '|' + ' ' * 17 + Fore.YELLOW + '|' + ' ' * 15 + Fore.YELLOW + '|' + ' ' * 17 + Fore.YELLOW + '|' + Fore.YELLOW + '|'}\n")

    def test_leaderboard_headings(self):
        self.assertEqual(mm.leaderboard_headings(), f"{' ' * 19 + Fore.YELLOW + '|' + Fore.YELLOW + '|' + ' ' * 4 + Fore.CYAN + 'R A N K' + ' ' * 4 + Fore.YELLOW + '|' + ' ' * 4 + Fore.CYAN + 'N A M E' + ' ' * 4 + Fore.YELLOW + '|' + ' ' * 4 + Fore.CYAN + 'G A M E S' + ' ' * 4 + Fore.YELLOW + '|' + ' ' * 4 + Fore.CYAN + 'W I N S' + ' ' * 4 + Fore.YELLOW + '|' + ' ' * 4 + Fore.CYAN + 'L O S E S' + ' ' * 4 + Fore.YELLOW + '|' + Fore.YELLOW + '|'}\n")

    def test_display_leaderboard_heading(self):
        self.assertEqual(mm.display_leaderboard_heading(), f"{mm.top_bottom_of_leaderboard() + mm.empty_leaderboard_line() + mm.leaderboard_headings() + mm.empty_leaderboard_line() + mm.top_bottom_of_leaderboard()}")

    @patch("main_menu.WORKSHEET", mock_worksheet)
    def test_get_leaderboard_data(self):
        self.assertEqual(mm.get_leaderboard_data(), [["John", "john@gmail.com", "10", "4", "6"], ["Pat", "pat@gmail.com", "12", "8", "4"]])

    @patch("main_menu.WORKSHEET", mock_worksheet)
    def test_sort_leaderboard_data(self):
        self.assertEqual(mm.sort_leaderboard_data(mm.get_leaderboard_data(), 2), [["Pat", "pat@gmail.com", "12", "8", "4"], ["John", "john@gmail.com", "10", "4", "6"]])
        self.assertEqual(mm.sort_leaderboard_data(mm.get_leaderboard_data(), 3), [["Pat", "pat@gmail.com", "12", "8", "4"], ["John", "john@gmail.com", "10", "4", "6"]])
        self.assertEqual(mm.sort_leaderboard_data(mm.get_leaderboard_data(), 4), [["Pat", "pat@gmail.com", "12", "8", "4"], ["John", "john@gmail.com", "10", "4", "6"]])

    def test_format_leaderboard_rank_and_wins_and_name(self):
        self.assertEqual(mm.format_leaderboard_rank_and_wins_and_name("1", "rank"), f"{Fore.WHITE + ' ' * 7 + '1' + ' ' * 7}")
        self.assertEqual(mm.format_leaderboard_rank_and_wins_and_name("12", "rank"), f"{Fore.WHITE + ' ' * 6 + '1' + ' ' + '2' + ' ' * 6}")
        self.assertEqual(mm.format_leaderboard_rank_and_wins_and_name("123", "rank"), f"{Fore.WHITE + ' ' * 5 + '1' + ' ' + '2' + ' ' + '3' + ' ' * 5}")
        self.assertEqual(mm.format_leaderboard_rank_and_wins_and_name("1234", "rank"), f"{Fore.WHITE + ' ' * 4 + '1' + ' ' + '2' + ' ' + '3' + ' ' + '4' + ' ' * 4}")
        self.assertEqual(mm.format_leaderboard_rank_and_wins_and_name("12345", "rank"), f"{Fore.WHITE + ' ' * 3 + '9 9 9 9 +' + ' ' * 3}")
        self.assertEqual(mm.format_leaderboard_rank_and_wins_and_name("12345", "name"), f"{Fore.WHITE + ' ' * 3 + '1' + ' ' + '2' + ' ' + '3' + ' ' + '4' + ' ' + '5' + ' ' * 3}")
        self.assertEqual(mm.format_leaderboard_rank_and_wins_and_name("123456", "name"), f"{Fore.WHITE + ' ' * 2 + '1' + ' ' + '2' + ' ' + '3' + ' ' + '4' + ' ' + '5' + ' ' + '6' + ' ' * 2}")
        self.assertEqual(mm.format_leaderboard_rank_and_wins_and_name("1234567", "name"), f"{Fore.WHITE + ' ' * 3 + '12345' + '... ' + ' ' * 3}")


# Enable print output
sys.stdout = sys.__stdout__



if __name__ == "__main__":
    unittest.main()
