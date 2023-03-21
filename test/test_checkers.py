import unittest
from unittest.mock import patch
import colorama
from colorama import Fore, Back, Style
import os
import sys
import io
import test_main_menu as tmm
# Get the parent path of the current script
parent_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
# Add the parent path to the system path
sys.path.append(parent_path)
import main_menu as mm
import checkers as ch
import checkers_engine as ce
import feature_testing as ft
import smart_move_finder as smf


#Initialize colorama
colorama.init(autoreset=True)

def mock_sgl(gs, p1, p2, pl1, pl2, n):
    """
    Mocks the start game loop function to return True 
    """
    return True

class MockGameState():
    """
    Mocks the game state class 
    """
    def __init__(self, board):
        self.color_go = "black"
        self.board = board

    def get_movable_pieces(self, color):
        """
        Returns empty string 
        """
        return []

def mock_dgo(arg1, arg2 ,arg3, arg4, arg5, arg6, arg7):
    """
    Mocks the display game over 
    """
    return True

def mock_dp(arg1, arg2 ,arg3, arg4):
    """
    Mocks the display piece 
    """
    return " "

class TestGameStart(unittest.TestCase):
    """
    Testing of the game state initialize
    """
    def setUp(self):
        self.gs = ce.GameState(ft.board_states["full"])
        self.bs = self.gs.board
        self.mgs = MockGameState("full")
        
        # Disable print output
        self.saved_stdout = sys.stdout
        sys.stdout = io.StringIO()

    def tearDown(self):
        # Enable print output
        sys.stdout = self.saved_stdout

    @patch("checkers.start_game_loop", mock_sgl)
    def test_start_game(self):
        self.assertEqual(ch.start_game("player1", "player2", 2, "full"), [0, 0])

    @patch("checkers.display_game_over", mock_dgo)
    def test_start_game_loop(self):
        self.assertEqual(ch.start_game_loop(self.mgs, 0, 1, mm.Player("John", "john@gmail.com", 10, 4, 6), 1, 1), "game over")

    def test_display_board(self):
        self.assertEqual(ch.display_board(self.gs), self.bs)

    @patch("checkers.display_piece", mock_dp)  
    def test_format_board_line(self):
        board_state = self.bs
        r = "8"
        i = 0
        row_index = 0
        self.assertEqual(ch.format_board_line(board_state, r, i, row_index), f"{Style.DIM + ' ' * 10 + ch.yellow_square() + ch.red_square(board_state, i, row_index) + ch.yellow_square() + ch.red_square(board_state, i, row_index) + ch.yellow_square() + ch.red_square(board_state, i, row_index) + ch.yellow_square() + ch.red_square(board_state, i, row_index)}")
        i = 2
        self.assertEqual(ch.format_board_line(board_state, r, i, row_index), f"{Style.DIM + ' ' * 7 + Fore.BLUE + r + ' ' * 2 + ch.yellow_square() + ch.red_square(board_state, i, row_index) + ch.yellow_square() + ch.red_square(board_state, i, row_index) + ch.yellow_square() + ch.red_square(board_state, i, row_index) + ch.yellow_square() + ch.red_square(board_state, i, row_index)}")
        r = "7"
        self.assertEqual(ch.format_board_line(board_state, r, i, row_index), f"{Style.DIM + ' ' * 7 + Fore.BLUE + r + ' ' * 2 + ch.red_square(board_state, i, row_index) + ch.yellow_square() + ch.red_square(board_state, i, row_index) + ch.yellow_square() + ch.red_square(board_state, i, row_index) + ch.yellow_square() + ch.red_square(board_state, i, row_index) + ch.yellow_square()}")
        i = 0
        self.assertEqual(ch.format_board_line(board_state, r, i, row_index), f"{Style.DIM + ' ' * 10 + ch.red_square(board_state, i, row_index) + ch.yellow_square() + ch.red_square(board_state, i, row_index) + ch.yellow_square() + ch.red_square(board_state, i, row_index) + ch.yellow_square() + ch.red_square(board_state, i, row_index) + ch.yellow_square()}")

    @patch("checkers.display_piece", mock_dp)   
    def test_red_square(self):
        self.assertEqual(ch.red_square(self.bs, 0, 0), f"{Back.RED + ' ' * 10}")
        self.assertEqual(ch.red_square(self.bs, 4, 0), f"{Back.RED + ' ' * 10}")
        self.assertEqual(ch.red_square(self.bs, 1, 0), f"{Back.RED + ' ' * 2 + ' ' + Back.RED + ' ' * 2}")

    def test_yellow_square(self):
        self.assertEqual(ch.yellow_square(), f"{Back.YELLOW + ' ' * 10}")

if __name__ == "__main__":
    unittest.main()