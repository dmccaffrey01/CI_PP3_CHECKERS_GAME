import unittest
from unittest.mock import patch
import os
import sys
import io
import colorama
from colorama import Fore, Back, Style
parent_path = os.path.abspath(os.path
                                .join(os.path.dirname(__file__), os.pardir))
sys.path.append(parent_path)
sys.path.insert(0, 'main_menu_folder/')
import main_menu as mm
sys.path.remove("main_menu_folder/")
sys.path.insert(0, 'checkers_folder/')
import feature_testing as ft


def mock_function(*args, **kwargs):
    """
    Mocks a function with any arguments
    """
    return True


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

    @patch("builtins.input", side_effect=["wrong", "1"])
    @patch("feature_testing.set_up_board", mock_function)
    def test_go_to_feature_testing(self, mock_input):
        self.assertEqual(ft.go_to_feature_testing(), "single jump")

    @patch("builtins.input", lambda _: "r")
    @patch("main_menu.main_menu_screen", mock_function)
    def test_go_to_feature_testing_return(self):
        self.assertEqual(ft.go_to_feature_testing(), "return_to_main_menu")

    def test_validate_ask_feature_testing(self):
        self.assertEqual(ft.validate_ask_feature_testing("1"), "single jump")
        self.assertEqual(ft.validate_ask_feature_testing("2"), "double jump")
        self.assertEqual(ft.validate_ask_feature_testing("3"), "triple jump")
        self.assertEqual(
            ft.validate_ask_feature_testing("4"), "quintuple jump")
        self.assertEqual(ft.validate_ask_feature_testing("5"), "king")
        self.assertEqual(ft.validate_ask_feature_testing("6"), "jump to king")
        self.assertEqual(ft.validate_ask_feature_testing("r"), "return")
        self.assertEqual(ft.validate_ask_feature_testing("wrong"), False)

    @patch("main_menu.start_checkers_game", mock_function)
    def test_set_up_board(self):
        self.assertEqual(ft.set_up_board("singe jump"), "set_up_board")


if __name__ == "__main__":
    unittest.main()
