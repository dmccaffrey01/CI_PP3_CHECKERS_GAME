import unittest
from unittest.mock import patch
import os
import sys
# Get the parent path of the current script
parent_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
# Add the parent path to the system path
sys.path.append(parent_path)
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

    def test_eliminate_immovable_pieces(self):
        self.assertEqual(self.test_game_state_1.eliminate_immovable_pieces(['6D', '2D'], "black"), ['6D', '2D'])
        self.assertEqual(self.test_game_state_1.eliminate_immovable_pieces(['7C', '3E'], "white"), ['7C', '3E'])

    def test_find_available_moves(self):
        self.assertEqual(self.test_game_state_1.find_available_moves("6D", "black"), [['8B', 'jump', [['7C']]], ['7E', 'move']])
        self.assertEqual(self.test_game_state_1.find_available_moves("7C", "white"), [['5E', 'jump', [['6D']]], ['6B', 'move']])

    def test_format_piece(self):
        self.assertEqual(self.test_game_state_1.format_piece(2, 3), "6D")
        self.assertEqual(self.test_game_state_1.format_piece(1, 2), "7C")

    def test_format_row(self):
        self.assertEqual(self.test_game_state_1.format_row(0), "8")
        self.assertEqual(self.test_game_state_1.format_row(1), "7")
        self.assertEqual(self.test_game_state_1.format_row(2), "6")
        self.assertEqual(self.test_game_state_1.format_row(3), "5")
        self.assertEqual(self.test_game_state_1.format_row(4), "4")
        self.assertEqual(self.test_game_state_1.format_row(5), "3")
        self.assertEqual(self.test_game_state_1.format_row(6), "2")
        self.assertEqual(self.test_game_state_1.format_row(7), "1")

    def test_get_index_of_piece(self):
        self.assertEqual(self.test_game_state_1.get_index_of_piece("6D"), [2, 3])
        self.assertEqual(self.test_game_state_1.get_index_of_piece("7C"), [1, 2])

    def test_get_available_moves(self):
        self.assertEqual(self.test_game_state_1.get_available_moves([2,3], "black"), ["blocked", [1, 4]])
        self.assertEqual(self.test_game_state_1.get_available_moves([1,2], "white"), [[2, 1], "blocked"])

    def test_check_if_piece_on_edge_of_board(self):
        self.assertEqual(self.test_game_state_1.check_if_piece_on_edge_of_board([2, 3]), False)
        self.assertEqual(self.test_game_state_1.check_if_piece_on_edge_of_board([2, 0]), "Left")
        self.assertEqual(self.test_game_state_1.check_if_piece_on_edge_of_board([2, 7]), "Right")

    def test_check_if_piece_on_kings_edge(self):
        self.assertEqual(self.test_game_state_1.check_if_piece_on_kings_edge([2,3]), False)
        self.assertEqual(self.test_game_state_1.check_if_piece_on_kings_edge([0,3]), "Top")
        self.assertEqual(self.test_game_state_1.check_if_piece_on_kings_edge([7,3]), "Bottom")

    def test_get_diaganol(self):
        self.assertEqual(self.test_game_state_1.get_diaganol([2,3], "Left", "black"), [1, 2])
        self.assertEqual(self.test_game_state_1.get_diaganol([2,3], "Right", "black"), [1, 4])
        self.assertEqual(self.test_game_state_1.get_diaganol([2,3], "Left-King", "black"), [3, 2])
        self.assertEqual(self.test_game_state_1.get_diaganol([2,3], "Right-King", "black"), [3, 4])

    def test_check_if_diaganol_empty(self):
        self.assertEqual(self.test_game_state_1.check_if_diaganol_empty([1, 2]), "blocked")
        self.assertEqual(self.test_game_state_1.check_if_diaganol_empty([1, 4]), [1, 4])
        self.assertEqual(self.test_game_state_1.check_if_diaganol_empty([3, 2]), [3, 2])
        self.assertEqual(self.test_game_state_1.check_if_diaganol_empty([3, 4]), [3, 4])

    def test_format_available_moves(self):
        self.assertEqual(self.test_game_state_1.format_available_moves(["blocked", [1, 4]]), [["7E", "move"]])

class TestGameStateJumps(unittest.TestCase):
    """
    Testing of the game state jumps functions 
    """
    def setUp(self):
        self.test_game_state_1 = check_eng.GameState(ft.board_states["test board 1"])
        self.test_game_state_1.original_piece_index = [2, 3]

    def test_get_available_jumps(self):
        self.assertEqual(self.test_game_state_1.get_available_jumps([2, 3], "black"), [[0, 1]])

    def test_check_kings_jumps(self):
        self.assertEqual(self.test_game_state_1.check_kings_jumps([2, 3], "Left", "black"), [[0, 1]])

    def test_get_direction(self):
        self.assertEqual(self.test_game_state_1.get_direction("Left"), ["Left", "Left-King"])
        self.assertEqual(self.test_game_state_1.get_direction("Right"), ["Right", "Right-King"])

    def test_get_jump(self):
        self.assertEqual(self.test_game_state_1.get_jump([2, 3], "Left", "black"), "Left")

    def test_check_jump(self):
        self.assertEqual(self.test_game_state_1.check_jump([1, 2], "Left", "black"), "success")
        self.assertEqual(self.test_game_state_1.check_jump([1, 4], "Right", "black"), "blocked")

    def test_check_if_diaganol_contains_opposite_color_piece(self):
        self.assertEqual(self.test_game_state_1.check_if_diaganol_contains_opposite_color_piece([1, 2], "black"), True)
        self.assertEqual(self.test_game_state_1.check_if_diaganol_contains_opposite_color_piece([2, 3], "white"), True)
        self.assertEqual(self.test_game_state_1.check_if_diaganol_contains_opposite_color_piece([1, 4], "black"), False)

    def test_format_available_jumps(self):
        self.assertEqual(self.test_game_state_1.format_available_jumps(), [])

class TestMovePiece(unittest.TestCase):
    """
    Testing of the move piece functions 
    """
    def setUp(self):
        self.test_game_state_1 = check_eng.GameState(ft.board_states["test board 1"])
        self.test_game_state_1.original_piece_index = [2, 3]
        self.test_game_state_1.move_piece("6D", ['8B', 'jump', [['7C']]], 1, "black")
        self.test_game_state_2 = check_eng.GameState(ft.board_states["test board 1"])
        self.test_game_state_2.original_piece_index = [2, 3]
        
    def test_move_piece(self):
        self.assertEqual(self.test_game_state_2.move_piece("6D", ['8B', 'jump', [['7C']]], 1, "black"), [0, 1])

    def test_move_board_icon(self):
        self.assertEqual(self.test_game_state_2.move_board_icon([2, 3], [0, 1], "black"), [0, 1])

    def test_check_if_move_was_jump(self):
        self.assertEqual(self.test_game_state_2.check_if_move_was_jump(['8B', 'jump', [['7C']]], 1, "black"), [["7C","w"]])
        self.assertEqual(self.test_game_state_2.check_if_move_was_jump(['7E', 'move', []], 2, "black"), "move")

    def test_check_if_piece_needs_kinged(self):
        self.assertEqual(self.test_game_state_2.check_if_piece_needs_kinged([0,1], "black"), "Kinged")
        self.assertEqual(self.test_game_state_2.check_if_piece_needs_kinged([2,3], "black"), "Not kinged")

    def test_king_piece(self):
        self.assertEqual(self.test_game_state_2.king_piece([2, 3], "black"), "B")

    def test_check_if_piece_is_kinged(self):
        self.assertEqual(self.test_game_state_2.move_piece("6D", ['8B', 'jump', [['7C']]], 1, "black"), [0, 1])
        self.assertEqual(self.test_game_state_2.check_if_piece_is_kinged([0, 1], "black"), True)
        self.assertEqual(self.test_game_state_2.check_if_piece_is_kinged([2,3], "black"), False)

    def test_remove_piece_from_board(self):
        self.assertEqual(self.test_game_state_2.remove_piece_from_board("7C"), "_")

    def test_delete_last_log(self):
        self.assertEqual(self.test_game_state_1.delete_last_log(), "deleted")

    def test_add_move_to_log(self):
        self.assertEqual(self.test_game_state_2.add_move_to_log("6D", ['8B', 'jump', [['7C']]], 1, [['7C', "w"]], "Kinged", "black"), [["6D", ['8B', 'jump', [['7C']]], 1, [['7C', "w"]], "Kinged", "black"]])

    def test_undo_move(self):
        self.assertEqual(self.test_game_state_1.move_log, [["6D", ['8B', 'jump', [['7C']]], 1, [['7C', "w"]], "Kinged", "black"]])
        self.assertEqual(self.test_game_state_1.undo_move(), [])

    def test_undo_king_piece(self):
        self.assertEqual(self.test_game_state_1.undo_king_piece([0, 1], "Kinged"), "Unkinged")
        self.assertEqual(self.test_game_state_1.undo_king_piece([0, 1], "Not kinged"), "Not kinged")

    def test_restore_jumped_pieces(self):
        self.assertEqual(self.test_game_state_1.restore_jumped_pieces([['7C', "w"]]), "w")

    def test_change_color_go(self):
        self.assertEqual(self.test_game_state_1.change_color_go(), "white")
        self.assertEqual(self.test_game_state_1.change_color_go(), "black")
    

if __name__ == "__main__":
    unittest.main()