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

    def get_movable_pieces(self):
        """
        Finds out the movable pieces on the board
        Returns pieces in a list 
        """
        movable_pieces = self.get_all_players_pieces()
        movable_pieces = self.eliminate_immovable_pieces(movable_pieces)
        
        return movable_pieces


    def get_all_players_pieces():
        """
        Finds all the players pieces
        """
        movable_pieces = []
        i = 0
        j = 0
        for x in self.board:
            for y in x:
                if y == "b":
                    piece = f"{i}{j}"
                    movable_pieces.append(piece)

                j += 1

            i += 1
            j = 0

        return movable_pieces
        