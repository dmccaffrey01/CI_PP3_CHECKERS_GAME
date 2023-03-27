import unittest
from unittest.mock import patch
import sys
import io
import os
import colorama
from colorama import Fore, Back, Style
parent_path = os.path.abspath(os.path
                                .join(os.path.dirname(__file__), os.pardir))
sys.path.append(parent_path)
sys.path.insert(0, 'main_menu_folder/')
import game_rules as gr

# Initialize colorama
colorama.init(autoreset=True)


def mock_function(*args, **kwargs):
    """
    Mocks a function to return True
    """
    return True


def mock_ggrl():
    """
    Mocks the get game rules lines function to return mock lorem ipsum text
    """
    mock_lines = ["Lorem ipsum dolor sit amet, consectetur " +
                  "adipiscing elit, sed do", "nl",
                  "eiusmod tempor incididunt ut labore et " +
                  "dolore magna aliqua. Ut", "nl",
                  "enim ad minim veniam, quis nostrud exercitation ullamco"]
    return mock_lines


class TestGameRules(unittest.TestCase):
    """
    Testing of the game rules functions
    """
    def setUp(self):
        # Disable print output
        self.saved_stdout = sys.stdout
        sys.stdout = io.StringIO()

        # Disable time.sleep
        patcher1 = patch('time.sleep', return_value=None)
        patcher1.start()
        self.addCleanup(patcher1.stop)

    def tearDown(self):
        # Enable print output
        sys.stdout = self.saved_stdout

    def test_game_rules_start_of_line(self):
        self.assertEqual(
            gr.game_rules_start_of_line(),
            f"{' ' * 6 + Fore.YELLOW + '|' + ' ' * 4}")

    def test_game_rules_empty_line(self):
        self.assertEqual(
            gr.game_rules_empty_line(),
            f"{' ' * 6 + Fore.YELLOW + '|' + ' ' * 104 + Fore.YELLOW + '|'}\n")

    def test_game_rules_top_and_bottom_line(self):
        self.assertEqual(
            gr.game_rules_top_and_bottom_line(),
            f"{' ' * 6 + Fore.YELLOW + '=' * 106}\n")

    def test_format_game_rule_line(self):
        self.assertEqual(
            gr.format_game_rule_line(
                'Lorem ipsum dolor sit amet, consectetur ' +
                'adipiscing elit, sed do'),
            f"{gr.game_rules_start_of_line()}" +
            f"{Fore.WHITE + 'Lorem ipsum dolor sit amet, '}" +
            f"{'consectetur adipiscing elit, sed do' + ' ' * 37}" +
            f"{Fore.YELLOW + '|'}\n")
        self.assertEqual(
            gr.format_game_rule_line("nl"), gr.game_rules_empty_line())

    def test_get_game_rules_lines(self):
        self.assertEqual(
            gr.get_game_rules_lines(),
            ["Checkers is a classic board game that is played on an 8x8 " +
             "board with 64 squares of alternating",
             "colors, red and yellow in this game. The game is played " +
             "between two players, who each have",
             "12 pieces in their respective colors, either white or black, " +
             "arranged on opposite sides of the",
             "board.",
             "nl",
             "The objective of the game is to capture all of the opponent's " +
             "pieces or to block them so they",
             "cannot make any more moves.",
             "nl",
             'The rules of checkers are as follows:',
             'nl',
             'Players take turns moving one piece diagonally forward on the ' +
             'dark squares.',
             'nl',
             'Normal pieces can only move forward, but if they reach the ' +
             'last row on the opposite side of the',
             'board, they can be promoted to a king, which can move ' +
             'diagonally in any direction.',
             'nl',
             "Captures are made by jumping over an opponent's piece that is " +
             "adjacent and landing on an",
             'empty square. Multiple jumps are allowed in one turn.',
             'nl',
             'If there is a choice between multiple captures, the player ' +
             'can choose which one to make.',
             'nl',
             "The game ends when one player captures all of the opponent's " +
             "pieces or blocks them so they cannot",
             'make any more moves.',
             'nl',
             'If a player is unable to make a move or has no legal moves ' +
             'left, they lose the game.',
             'nl',
             'These are the basic rules of checkers, but there are ' +
             'variations in rules depending on the',
             'location and culture where it is played.'])

    @patch("game_rules.get_game_rules_lines", mock_ggrl)
    def test_format_game_rules_lines(self):
        self.assertEqual(
            gr.format_game_rules_lines(),
            f"{gr.format_game_rule_line(mock_ggrl()[0])}" +
            f"{gr.format_game_rule_line(mock_ggrl()[1])}" +
            f"{gr.format_game_rule_line(mock_ggrl()[2])}" +
            f"{gr.format_game_rule_line(mock_ggrl()[3])}" +
            f"{gr.format_game_rule_line(mock_ggrl()[4])}")

    def test_game_rules_heading(self):
        self.assertEqual(
            gr.game_rules_heading(),
            f"{' ' * 46 + Fore.CYAN + 'G A M E   R U L E S'}\n")

    def test_validate_exit_game_rules_input(self):
        self.assertEqual(gr.validate_exit_game_rules_input("1"), "return")
        self.assertEqual(gr.validate_exit_game_rules_input("r"), "return")
        self.assertEqual(gr.validate_exit_game_rules_input("2"), False)

    @patch("builtins.input", side_effect=["wrong", "1"])
    def test_ask_user_to_exit_game_rules(self, mock_input):
        self.assertEqual(gr.ask_user_to_exit_game_rules(), "return")

    @patch("builtins.input", lambda _: "1")
    @patch("main_menu.main_menu_screen", mock_function)
    def test_display_game_rules(self):
        self.assertEqual(gr.display_game_rules(), "return_to_main_menu")


if __name__ == "__main__":
    unittest.main()
