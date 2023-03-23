import unittest
from unittest.mock import patch
import colorama
from colorama import Fore, Back, Style
import os
import sys
import io
# Get the parent path of the current script
parent_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
# Add the parent path to the system path
sys.path.append(parent_path)
sys.path.insert(0, 'main_menu')
import main_menu as mm
import display
sys.path.remove('main_menu')
sys.path.insert(0, 'checkers')
import checkers as ch
import checkers_engine as ce
import feature_testing as ft
import smart_move_finder as smf
import math


#Initialize colorama
colorama.init(autoreset=True)

def mock_function(*args, **kwargs):
    """ 
    Mocks a function to return True
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
        self.test_gs = ce.GameState(ft.board_states["test board 2"])
        self.test_bs = ce.GameState(ft.board_states["test board 3"]).board
        self.black_available_moves = self.gs.find_all_available_moves("black")
        self.player2 = mm.Player("Pat", "pat@gmail.com", 12, 8, 4)
        self.player1 = mm.Player("John", "john@gmail.com", 10, 4, 6)

        # Disable time.sleep
        patcher1 = patch('time.sleep', return_value=None)
        patcher1.start()
        self.addCleanup(patcher1.stop)

        # Disable display.typewriter
        patcher2 = patch('display.typewriter', return_value=None)
        patcher2.start()
        self.addCleanup(patcher2.stop)
        
        # Disable print output
        self.saved_stdout = sys.stdout
        sys.stdout = io.StringIO()

    def tearDown(self):
        # Enable print output
        sys.stdout = self.saved_stdout

    @patch("checkers.start_game_loop", mock_function)
    def test_start_game(self):
        self.assertEqual(ch.start_game("player1", "player2", 2, "full"), [0, 0])
        self.assertEqual(ch.start_game("player1", 1, 1, "full"), [0, 1])
        self.assertEqual(ch.start_game(1, 1, 0, "full"), [1, 1])

    @patch("checkers.display_game_over", mock_function)
    @patch("builtins.input", lambda _: "1")
    def test_start_game_loop(self):
        self.assertEqual(ch.start_game_loop(self.test_gs, 0, 1, self.player1, 1, 1), "game over")

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

    def test_display_piece(self):
        self.assertEqual(ch.display_piece(self.test_bs, 1, 7, 0), f"{Back.BLACK + ' ' * 6}")
        self.assertEqual(ch.display_piece(self.test_bs, 1, 7, 2), f"{Back.BLACK + ' ' * 6}")
        self.assertEqual(ch.display_piece(self.test_bs, 2, 7, 2), f"{Back.BLACK + ' ' * 2 + Back.GREEN + ' ' * 2 + Back.BLACK + ' ' * 2}")
        self.assertEqual(ch.display_piece(self.test_bs, 1, 0, 3), f"{Back.WHITE + ' ' * 6}")
        self.assertEqual(ch.display_piece(self.test_bs, 1, 0, 1), f"{Back.WHITE + ' ' * 6}")
        self.assertEqual(ch.display_piece(self.test_bs, 2, 0, 1), f"{Back.WHITE + ' ' * 2 + Back.GREEN + ' ' * 2 + Back.WHITE + ' ' * 2}")
        self.assertEqual(ch.display_piece(self.test_bs, 2, 0, 5), f"{Back.RED + ' ' * 6}")

    def test_get_piece_icon(self):
        self.assertEqual(ch.get_piece_icon(self.test_bs, 7, 0), "b")
        self.assertEqual(ch.get_piece_icon(self.test_bs, 7, 2), "B")
        self.assertEqual(ch.get_piece_icon(self.test_bs, 0, 1), "W")
        self.assertEqual(ch.get_piece_icon(self.test_bs, 0, 3), "w")
        self.assertEqual(ch.get_piece_icon(self.test_bs, 0, 0), "x")
        self.assertEqual(ch.get_piece_icon(self.test_bs, 1, 0), "_")

    def test_fomrat_cols_line(self):
        self.assertEqual(ch.format_cols_line(self.gs.BOARD_COLS), f"{' ' * 10 + ' ' * 5 + 'A' + ' ' * 4 + ' ' * 5 + 'B' + ' ' * 4 + ' ' * 5 + 'C' + ' ' * 4 + ' ' * 5 + 'D' + ' ' * 4 + ' ' * 5 + 'E' + ' ' * 4 + ' ' * 5 + 'F' + ' ' * 4 + ' ' * 5 + 'G' + ' ' * 4 + ' ' * 5 + 'H' + ' ' * 4}")

    @patch("builtins.input", side_effect=["wrong", "1"])
    def test_select_piece_side(self, mock_input):
        self.assertEqual(ch.select_piece(self.gs, self.gs.get_movable_pieces("black"), "black"), "3A")

    @patch("builtins.input", lambda _: "1")
    def test_select_piece(self):
        self.assertEqual(ch.select_piece(self.gs, self.gs.get_movable_pieces("black"), "black"), "3A")

    def test_validate_selected_option(self):
        self.assertEqual(ch.validate_selected_option("1", "available_moves", self.black_available_moves), 1)
        self.assertEqual(ch.validate_selected_option("10", "available_moves", self.black_available_moves), False)
        self.assertEqual(ch.validate_selected_option("a", "available_moves", self.black_available_moves), False)
        self.assertEqual(ch.validate_selected_option("r", "available_moves", self.black_available_moves), "return")

    @patch("builtins.input", side_effect=["wrong", "1"])
    def test_select_move_side(self, mock_input):
        self.assertEqual(ch.select_move(self.gs, "3A", "black"), [["4B", "move"], 1])

    @patch("builtins.input", lambda _: "1")
    def test_select_move1(self):
        self.assertEqual(ch.select_move(self.gs, "3A", "black"), [["4B", "move"], 1])

    @patch("builtins.input", lambda _: "r")
    def test_select_move2(self):
        self.assertEqual(ch.select_move(self.gs, "3A", "black"), "return")

    def test_format_available_moves(self):
        self.assertEqual(ch.format_available_moves([["4B", "move", []], ["5C", "jump", ["4B"]]]), ["Move to: 4B", "Jump to: 5C"])

    @patch("checkers.ask_whats_next", mock_function)
    @patch("checkers.display_stats", mock_function)
    @patch("time.sleep", mock_function)
    def test_display_game_over(self):
        self.assertEqual(ch.display_game_over(self.gs, 1, 0, 0, self.player1, self.player2, 2), f"{' ' * 25}G A M E\n{' ' * 25}O V E R\n{' ' * 11}T H E   W I N N E R   I S   {'W H I T E'}\n{' ' * (5 + math.ceil((48-(33 + len('P A T')))/2))}C O N G R A T U L A T I O N S    {'P A T'}\n")

    def test_game_over(self):
        self.assertEqual(ch.game_over("white", "Pat"), f"{' ' * 25}G A M E\n{' ' * 25}O V E R\n{' ' * 11}T H E   W I N N E R   I S   {'W H I T E'}\n{' ' * (5 + math.ceil((48-(33 + len('P A T')))/2))}C O N G R A T U L A T I O N S    {'P A T'}\n")

    def test_display_stats(self):
        self.assertEqual(ch.display_stats(["cpu", "cpu"], 1), ["cpu", "cpu"])
        self.assertEqual(ch.display_stats(["p1", "p2"], 1), ["p1", "p2"])
        self.assertEqual(ch.display_stats(["p1", "cpu"], 1), ["p1", "cpu"])

    def test_update_player_stats(self):
        self.assertEqual(ch.update_player_stats("Black", 0, 0, self.player1, self.player2), [f"{Fore.CYAN + 'Name: ' + Fore.WHITE + self.player1.name + Fore.CYAN + '   Email: ' + Fore.WHITE + self.player1.email + Fore.CYAN + '   Total Games: ' + Fore.WHITE + str(self.player1.total_games) + Fore.CYAN + '   Wins: ' + Fore.WHITE + str(self.player1.wins) + Fore.CYAN + '   Loses: ' + Fore.WHITE + str(self.player1.loses)}", f"{Fore.CYAN + 'Name: ' + Fore.WHITE + self.player2.name + Fore.CYAN + '   Email: ' + Fore.WHITE + self.player2.email + Fore.CYAN + '   Total Games: ' + Fore.WHITE + str(self.player2.total_games) + Fore.CYAN + '   Wins: ' + Fore.WHITE + str(self.player2.wins) + Fore.CYAN + '   Loses: ' + Fore.WHITE + str(self.player2.loses)}"])
        self.assertEqual(ch.update_player_stats("Black", 0, 1, self.player1, 1), [f"{Fore.CYAN + 'Name: ' + Fore.WHITE + self.player1.name + Fore.CYAN + '   Email: ' + Fore.WHITE + self.player1.email + Fore.CYAN + '   Total Games: ' + Fore.WHITE + str(self.player1.total_games) + Fore.CYAN + '   Wins: ' + Fore.WHITE + str(self.player1.wins) + Fore.CYAN + '   Loses: ' + Fore.WHITE + str(self.player1.loses)}", "cpu"])
        self.assertEqual(ch.update_player_stats("Black", 1, 1, 1, 1), ["cpu", "cpu"])

    def test_check_winner(self):
        self.assertEqual(ch.check_winner(self.gs, 1000, "type", "p1", "p2", "player1", "player2"), "Draw")
        self.assertEqual(ch.check_winner(self.gs, 1, "color", "p1", "p2", "player1", "player2"), "White")
        self.assertEqual(ch.check_winner(self.gs, 1, "name", "p1", 0, "player1", self.player2), "Pat")
        self.assertEqual(ch.check_winner(self.gs, 1, "name", "p1", 1, "player1", self.player2), "CPU")
        self.assertEqual(ch.check_winner(self.test_gs, 1, "color", "p1", "p2", "player1", "player2"), "Black")
        self.assertEqual(ch.check_winner(self.test_gs, 1, "name", 0, "p2", self.player1, "player2"), "John")
        self.assertEqual(ch.check_winner(self.test_gs, 1, "name", 1, "p2", self.player1, "player2"), "CPU")

    @patch("checkers.after_game_selection", mock_function)
    @patch("builtins.input", side_effect=["wrong", "1"])
    def test_ask_whats_next(self, mock_input):
        self.assertEqual(ch.ask_whats_next("p1", "p2", "player1", "player2", "num"), 1)

    def test_validate_whats_next_input(self):
        self.assertEqual(ch.validate_whats_next_input("1"), 1)
        self.assertEqual(ch.validate_whats_next_input("2"), 2)
        self.assertEqual(ch.validate_whats_next_input("3"), 3)
        self.assertEqual(ch.validate_whats_next_input("4"), 4)
        self.assertEqual(ch.validate_whats_next_input("5"), False)

    @patch("checkers.start_game", mock_function)
    @patch("main_menu.raise_return_to_main_menu", mock_function)
    @patch("main_menu.exit_game", mock_function)
    @patch("leaderboard.go_to_leaderboard", mock_function)
    def test_after_game_selection(self):
        self.assertEqual(ch.after_game_selection(1, "player1", "player2", "num"), "start game")
        self.assertEqual(ch.after_game_selection(2, "player1", "player2", "num"), "return to main menu")
        self.assertEqual(ch.after_game_selection(3, "player1", "player2", "num"), "go to leaderboard")
        self.assertEqual(ch.after_game_selection(4, "player1", "player2", "num"), "exit game")

if __name__ == "__main__":
    unittest.main()