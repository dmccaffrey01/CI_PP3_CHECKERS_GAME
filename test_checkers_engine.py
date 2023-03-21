import unittest
from unittest.mock import patch
import checkers_engine as check_eng
import feature_testing as ft

class TestGameStateInit(unittest.TestCase):
    """
    Testing of the game state initialize
    """
    def setUp(self):
        self.test_game_state_1 = check_eng.GameState(ft.board_states["test board 1"])

    def test_board(self):
        self.assertEqual(self.test_game_state_1.board, ft.board_states["test board 1"])
        self.test_game_state_1.board = ft.board_states["full"]
        self.assertEqual(self.test_game_state_1.board, ft.board_states["full"])

    def test_board_rows_and_cols(self):
        self.assertEqual(self.test_game_state_1.BOARD_ROWS, ["8", "7", "6", "5", "4", "3", "2", "1"])
        self.assertEqual(self.test_game_state_1.BOARD_COLS, ["A", "B", "C", "D", "E", "F", "G", "H"])

    def test_color_go(self):
        self.assertEqual(self.test_game_state_1.color_go, "black")
        self.test_game_state_1.color_go = "white"
        self.assertEqual(self.test_game_state_1.color_go, "white")

    def test_black_to_move(self):
        self.assertEqual(self.test_game_state_1.black_to_move, True)
        self.test_game_state_1.black_to_move = False
        self.assertEqual(self.test_game_state_1.black_to_move, False)

    def test_original_piece_index(self):
        self.assertEqual(self.test_game_state_1.original_piece_index, [])
        self.test_game_state_1.original_piece_index = [1]
        self.assertEqual(self.test_game_state_1.original_piece_index, [1])

    def test_available_jumps_log(self):
        self.assertEqual(self.test_game_state_1.available_jumps_log, [])
        self.test_game_state_1.available_jumps_log = [1]
        self.assertEqual(self.test_game_state_1.available_jumps_log, [1])

    def test_jumped_pieces_log(self):
        self.assertEqual(self.test_game_state_1.jumped_pieces_log, [])
        self.test_game_state_1.jumped_pieces_log = [1]
        self.assertEqual(self.test_game_state_1.jumped_pieces_log, [1])

    def test_jump_count(self):
        self.assertEqual(self.test_game_state_1.jump_count, 0)
        self.test_game_state_1.jump_count = 1
        self.assertEqual(self.test_game_state_1.jump_count, 1)

    def test_available_jumps(self):
        self.assertEqual(self.test_game_state_1.available_jumps, [])
        self.test_game_state_1.available_jumps = [1]
        self.assertEqual(self.test_game_state_1.available_jumps, [1])

    def test_move_log(self):
        self.assertEqual(self.test_game_state_1.move_log, [])
        self.test_game_state_1.move_log = [1]
        self.assertEqual(self.test_game_state_1.move_log, [1])

    
class TestGameStateMoves(unittest.TestCase):
    """
    Testing of the game state finding moves 
    """
    def setUp(self):
        self.test_game_state_1 = check_eng.GameState(ft.board_states["test board 1"])

    def test_find_all_available_moves(self):
        self.assertEqual(self.test_game_state_1.find_all_available_moves("black"), [['6D', ['8B', 'jump', [['7C']]], 1, 'black'], ['6D', ['7E', 'move'], 2, 'black'], ['2D', ['4F', 'jump', [['3E']]], 1, 'black'], ['2D', ['3C', 'move'], 2, 'black']])
        self.assertEqual(self.test_game_state_1.find_all_available_moves("white"), [['7C', ['5E', 'jump', [['6D']]], 1, 'white'], ['7C', ['6B', 'move'], 2, 'white'], ['3E', ['1C', 'jump', [['2D']]], 1, 'white'], ['3E', ['2F', 'move'], 2, 'white']])

    def test_get_movalbe_pieces(self):
        self.assertEqual(self.test_game_state_1.get_movable_pieces("black"), ['6D', '2D'])
        self.assertEqual(self.test_game_state_1.get_movable_pieces("white"), ['7C', '3E'])

    def test_get_all_players_pieces(self):
        self.assertEqual(self.test_game_state_1.get_all_players_pieces("black"), ['6D', '2D'])
        self.assertEqual(self.test_game_state_1.get_all_players_pieces("white"), ['7C', '3E'])












if __name__ == "__main__":
    unittest.main()