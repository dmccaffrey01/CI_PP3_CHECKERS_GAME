import unittest
from unittest.mock import patch
import leaderboard
from test import test_main_menu as tmm
import sys
import io
import colorama
from colorama import Fore, Back, Style

#Initialize colorama
colorama.init(autoreset=True)

# Disable print output
sys.stdout = io.StringIO()

class TestLeaderboardSortRanks(unittest.TestCase):
    """
    Testing of the leaderboard sort ranks 
    """
    def test_validate_sort_ranks_input(self):
        self.assertEqual(leaderboard.validate_sort_ranks_input("1"), 3)
        self.assertEqual(leaderboard.validate_sort_ranks_input("2"), 2)
        self.assertEqual(leaderboard.validate_sort_ranks_input("3"), 4)
        self.assertEqual(leaderboard.validate_sort_ranks_input("r"), "return")
        self.assertEqual(leaderboard.validate_sort_ranks_input("5"), False)

    @patch("builtins.input", lambda _: "1")
    def test_ask_user_to_sort_ranks1(self):
        self.assertEqual(leaderboard.ask_user_to_sort_ranks(), 3)

    @patch("builtins.input", lambda _: "2")
    def test_ask_user_to_sort_ranks2(self):
        self.assertEqual(leaderboard.ask_user_to_sort_ranks(), 2)

    @patch("builtins.input", lambda _: "3")
    def test_ask_user_to_sort_ranks3(self):
        self.assertEqual(leaderboard.ask_user_to_sort_ranks(), 4)

    @patch("builtins.input", lambda _: "r")
    def test_ask_user_to_sort_ranks4(self):
        self.assertEqual(leaderboard.ask_user_to_sort_ranks(), "return")

    
class TestLeaderboardDisplay(unittest.TestCase):
    """
    Testing of the leaderboard display functions 
    """

    def test_top_bottom_of_leaderboard(self):
        self.assertEqual(leaderboard.top_bottom_of_leaderboard(), f"{' ' * 19 + Fore.YELLOW + '=' * 87}\n")

    def test_empty_leaderboard_line(self):
        self.assertEqual(leaderboard.empty_leaderboard_line(), f"{' ' * 19 + Fore.YELLOW + '|' + Fore.YELLOW + '|' + ' ' * 15 + Fore.YELLOW + '|' + ' ' * 15 + Fore.YELLOW + '|' + ' ' * 17 + Fore.YELLOW + '|' + ' ' * 15 + Fore.YELLOW + '|' + ' ' * 17 + Fore.YELLOW + '|' + Fore.YELLOW + '|'}\n")

    def test_leaderboard_headings(self):
        self.assertEqual(leaderboard.leaderboard_headings(), f"{' ' * 19 + Fore.YELLOW + '|' + Fore.YELLOW + '|' + ' ' * 4 + Fore.CYAN + 'R A N K' + ' ' * 4 + Fore.YELLOW + '|' + ' ' * 4 + Fore.CYAN + 'N A M E' + ' ' * 4 + Fore.YELLOW + '|' + ' ' * 4 + Fore.CYAN + 'G A M E S' + ' ' * 4 + Fore.YELLOW + '|' + ' ' * 4 + Fore.CYAN + 'W I N S' + ' ' * 4 + Fore.YELLOW + '|' + ' ' * 4 + Fore.CYAN + 'L O S E S' + ' ' * 4 + Fore.YELLOW + '|' + Fore.YELLOW + '|'}\n")

    def test_display_leaderboard_heading(self):
        self.assertEqual(leaderboard.display_leaderboard_heading(), f"{leaderboard.top_bottom_of_leaderboard() + leaderboard.empty_leaderboard_line() + leaderboard.leaderboard_headings() + leaderboard.empty_leaderboard_line() + leaderboard.top_bottom_of_leaderboard()}")

    @patch("leaderboard.WORKSHEET", tmm.mock_worksheet)
    def test_get_leaderboard_data(self):
        self.assertEqual(leaderboard.get_leaderboard_data(), [["John", "john@gmail.com", "10", "4", "6"], ["Pat", "pat@gmail.com", "12", "8", "4"]])

    @patch("leaderboard.WORKSHEET", tmm.mock_worksheet)
    def test_sort_leaderboard_data(self):
        self.assertEqual(leaderboard.sort_leaderboard_data(leaderboard.get_leaderboard_data(), 2), [["Pat", "pat@gmail.com", "12", "8", "4"], ["John", "john@gmail.com", "10", "4", "6"]])
        self.assertEqual(leaderboard.sort_leaderboard_data(leaderboard.get_leaderboard_data(), 3), [["Pat", "pat@gmail.com", "12", "8", "4"], ["John", "john@gmail.com", "10", "4", "6"]])
        self.assertEqual(leaderboard.sort_leaderboard_data(leaderboard.get_leaderboard_data(), 4), [["Pat", "pat@gmail.com", "12", "8", "4"], ["John", "john@gmail.com", "10", "4", "6"]])

    def test_format_leaderboard_rank_and_wins_and_name(self):
        self.assertEqual(leaderboard.format_leaderboard_rank_and_wins_and_name("1", "rank"), f"{Fore.WHITE + ' ' * 7 + '1' + ' ' * 7}")
        self.assertEqual(leaderboard.format_leaderboard_rank_and_wins_and_name("12", "rank"), f"{Fore.WHITE + ' ' * 6 + '1' + ' ' + '2' + ' ' * 6}")
        self.assertEqual(leaderboard.format_leaderboard_rank_and_wins_and_name("123", "rank"), f"{Fore.WHITE + ' ' * 5 + '1' + ' ' + '2' + ' ' + '3' + ' ' * 5}")
        self.assertEqual(leaderboard.format_leaderboard_rank_and_wins_and_name("1234", "rank"), f"{Fore.WHITE + ' ' * 4 + '1' + ' ' + '2' + ' ' + '3' + ' ' + '4' + ' ' * 4}")
        self.assertEqual(leaderboard.format_leaderboard_rank_and_wins_and_name("12345", "rank"), f"{Fore.WHITE + ' ' * 3 + '9 9 9 9 +' + ' ' * 3}")
        self.assertEqual(leaderboard.format_leaderboard_rank_and_wins_and_name("12345", "name"), f"{Fore.WHITE + ' ' * 3 + '1' + ' ' + '2' + ' ' + '3' + ' ' + '4' + ' ' + '5' + ' ' * 3}")
        self.assertEqual(leaderboard.format_leaderboard_rank_and_wins_and_name("123456", "name"), f"{Fore.WHITE + ' ' * 2 + '1' + ' ' + '2' + ' ' + '3' + ' ' + '4' + ' ' + '5' + ' ' + '6' + ' ' * 2}")
        self.assertEqual(leaderboard.format_leaderboard_rank_and_wins_and_name("1234567", "name"), f"{Fore.WHITE + ' ' * 3 + '12345' + '... ' + ' ' * 3}")

    def test_format_leaderboard_games_and_loses(self):
        self.assertEqual(leaderboard.format_leaderboard_games_and_loses("1"), f"{Fore.WHITE + ' ' * 8 + '1' + ' ' * 8}")
        self.assertEqual(leaderboard.format_leaderboard_games_and_loses("12"), f"{Fore.WHITE + ' ' * 7 + '1' + ' ' + '2' + ' ' * 7}")
        self.assertEqual(leaderboard.format_leaderboard_games_and_loses("123"), f"{Fore.WHITE + ' ' * 6 + '1' + ' ' + '2' + ' ' + '3' + ' ' * 6}")
        self.assertEqual(leaderboard.format_leaderboard_games_and_loses("1234"), f"{Fore.WHITE + ' ' * 5 + '1' + ' ' + '2' + ' ' + '3' + ' ' + '4' + ' ' * 5}")
        self.assertEqual(leaderboard.format_leaderboard_games_and_loses("12345"), f"{Fore.WHITE + ' ' * 4 + '1 0 0 0 +' + ' ' * 4}")

    def test_leaderboard_data_line(self):
        self.assertEqual(leaderboard.leaderboard_data_line(["John", "john@gmail.com", "10", "4", "6"], "2"), f"{' ' * 19 + Fore.YELLOW + '|' + Fore.YELLOW + '|' + leaderboard.format_leaderboard_rank_and_wins_and_name('2', 'rank') + Fore.YELLOW + '|' + leaderboard.format_leaderboard_rank_and_wins_and_name('John', 'name') + Fore.YELLOW + '|' + leaderboard.format_leaderboard_games_and_loses('10') + Fore.YELLOW + '|' + leaderboard.format_leaderboard_rank_and_wins_and_name('4', 'wins') + Fore.YELLOW + '|' + leaderboard.format_leaderboard_games_and_loses('6') + Fore.YELLOW + '|' + Fore.YELLOW + '|'}\n")

    @patch("leaderboard.WORKSHEET", tmm.mock_worksheet)
    def test_display_leaderboard_ranks(self):
        self.assertEqual(leaderboard.display_leaderboard_ranks(2), [[1, "Pat", "pat@gmail.com", "12", "8", "4"], [2, "John", "john@gmail.com", "10", "4", "6"]])
        self.assertEqual(leaderboard.display_leaderboard_ranks(3), [[1, "Pat", "pat@gmail.com", "12", "8", "4"], [2, "John", "john@gmail.com", "10", "4", "6"]])
        self.assertEqual(leaderboard.display_leaderboard_ranks(4), [[1, "Pat", "pat@gmail.com", "12", "8", "4"], [2, "John", "john@gmail.com", "10", "4", "6"]])

    @patch("builtins.input", lambda _: "4")
    @patch("main_menu.return_to_main_menu", tmm.mock_function_0_arg_true)
    def test_go_to_leaderboard(self):
        self.assertEqual(leaderboard.go_to_leaderboard(), False)


# Enable print output
sys.stdout = sys.__stdout__

if __name__ == "__main__":
    unittest.main()
 