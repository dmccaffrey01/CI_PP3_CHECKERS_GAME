import unittest
from unittest.mock import patch
import os
import sys
import io
# Get the parent path of the current script
parent_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
# Add the parent path to the system path
sys.path.append(parent_path)
import smart_move_finder as smf
import checkers_engine as ce
import feature_testing as ft

def mock_random_move(arg1 ,arg2):
    """
    Mocks random move 
    """
    return 0

class TestSmartMoveFinder(unittest.TestCase):
    """ 
    Testing of the smart move finder functions
    """
    def setUp(self):
        self.gs = ce.GameState(ft.board_states["test board 4"])
        self.black_available_moves = self.gs.find_all_available_moves("black")

    @patch("random.randint", mock_random_move)
    def test_find_best_move(self):
        self.assertEqual(smf.find_best_move(self.gs, self.black_available_moves, 3), self.black_available_moves[1])
        self.assertEqual(smf.find_best_move(self.gs, self.black_available_moves, 1), self.black_available_moves[0])

    @patch("random.randint", mock_random_move)
    def test_find_random_move(self):
        self.assertEqual(smf.find_random_move(self.gs, self.black_available_moves), self.black_available_moves[0])
    
    def test_find_move_nega_max_alpha_beta(self):
        self.assertEqual(smf.find_move_nega_max_alpha_beta(self.gs, self.black_available_moves, 3, -60, 60, 1, "black"), 8)

    def test_set_search_depth(self):
        self.assertEqual(smf.set_search_depth(1), 2)
        self.assertEqual(smf.set_search_depth(2), 2)
        self.assertEqual(smf.set_search_depth(3), 4)

    def test_get_opposite_color(self):
        self.assertEqual(smf.get_opposite_color("black"), "white")
        self.assertEqual(smf.get_opposite_color("white"), "black")

    def test_score_the_pieces_on_board(self):
        self.assertEqual(smf.score_the_pieces_on_board(self.gs.board), 0)

if __name__ == "__main__":
    unittest.main()