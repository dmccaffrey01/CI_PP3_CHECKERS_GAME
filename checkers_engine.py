""" 
This file is responsible for storing all the information about the current state of the chess game.
It will also be responsible for determining the valid moves at the current state.
"""

class GameState():
    """ 
    Creates an instance of the game state
    """
    def __init__(self):
        # board is an 8x8 2d list, each element of the list has 1 character.
        # Characters w and b represtent pieces white or black
        # Character x represents an empty space that cannot be moved into
        # Character _ represents an empty space that can be moved into
        self.board = [
            ["x", "w", "x", "w", "x", "w", "x", "w"],
            ["w", "x", "w", "x", "w", "x", "w", "x"],
            ["x", "w", "x", "w", "x", "w", "x", "w"],
            ["_", "x", "_", "x", "_", "x", "_", "x"],
            ["x", "_", "x", "_", "x", "_", "x", "_"],
            ["b", "x", "b", "x", "b", "x", "b", "x"],
            ["x", "b", "x", "b", "x", "b", "x", "b"],
            ["b", "x", "b", "x", "b", "x", "b", "x"]
        ]

        self.BOARD_ROWS = ["A", "B", "C", "D", "E", "F", "G", "H"]
        self.BOARD_COLS = ["1", "2", "3", "4", "5", "6", "7", "8"]

    def get_movable_pieces(self):
        """
        Finds out the movable pieces on the board
        Returns pieces in a list 
        """
        movable_pieces = self.get_all_players_pieces()
        movable_pieces = self.eliminate_immovable_pieces(movable_pieces)
        
        return movable_pieces


    def get_all_players_pieces(self):
        """
        Finds all the players pieces
        """
        movable_pieces = []
        i = 0
        j = 0
        for x in self.board:
            for y in x:
                if y == "b":
                    piece = self.format_piece(i, j)
                    movable_pieces.append(piece)

                j += 1

            i += 1
            j = 0

        return movable_pieces

    def eliminate_immovable_pieces(self, pieces):
        """ 
        Find all the movable and immovable pieces by finding available moves
        Take out the immovable and return a list
        """
        movable_pieces = []

        for piece in pieces:
            if self.find_available_moves(piece):
                movable_pieces.append(piece)

    def find_available_moves(self, piece):
        """ 
        Finds a piecs available moves
        Returns a list of positions where the piece can move
        Returns an empty string if no moves available
        """
        piece_index = self.get_index_of_piece(piece)
        

    def format_piece(self, r, c):
        """ 
        Formats a piece in the form A1
        Where A represents the row and 1 represents the column
        Ranges from (A to H) and (1 - 8)
        """
        row =  chr(65 + r)
        col = str(c + 1)
        return f"{row + col}"

    def get_index_of_piece(self, piece):
        """ 
        Finds the index of the piece in the board
        Returns it as an array where row is first and col is second
        """
        split_row_col = list(piece)
        row = self.BOARD_ROWS.index(split_row_col[0])
        col = self.BOARD_COLS.index(split_row_col[1])
        return [row, col]