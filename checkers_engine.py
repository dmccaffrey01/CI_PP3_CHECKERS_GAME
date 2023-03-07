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

        return movable_pieces

    def find_available_moves(self, piece):
        """ 
        Finds a pieces available moves
        Checks if move is blocked or empty
        Formats the move into piece
        Returns a list of positions where the piece can move
        Returns an empty string if no moves available
        """
        piece_index = self.get_index_of_piece(piece)
        available_moves = self.format_available_moves(self.get_available_moves(piece_index))
        return available_moves
               
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
    
    def get_available_moves(self, piece_index):
        """ 
        Checks if the piece is on the edge
        Checks the pieces diagnols if it is empty
        Returns the diaganols indexs in a list if it is empty
        """
        if self.check_if_piece_on_edge_of_board(piece_index) == "Left":
            diagnol_right = self.get_diaganol(piece_index, "Right")
            return ["blocked", self.check_if_diaganol_empty(diagnol_right)]
        elif self.check_if_piece_on_edge_of_board(piece_index) == "Right":
            diagnol_left = self.get_diaganol(piece_index, "Left")
            return [self.check_if_diaganol_empty(diagnol_left), "blocked"]
        else:
            diagnol_left = self.get_diaganol(piece_index, "Left")
            diagnol_right = self.get_diaganol(piece_index, "Right")
            return [self.check_if_diaganol_empty(diagnol_left), self.check_if_diaganol_empty(diagnol_right)]

    def check_if_piece_on_edge_of_board(self, piece_index):
        """ 
        Finds out if the piece is on the edge of the board
        If it is return True, if not return False
        """
        if piece_index[1] == 0:
            return "Left"
        elif piece_index[1] == 7:
            return "Right"
        else:
            return False

    def get_diaganol(self, piece_index, diaganol):
        """ 
        Gets the index of the diaganol position either to the right or left
        Returns index in a list where row is first col is second
        """
        row = piece_index[0] - 1
        if diaganol == "Left":
            col = piece_index[1] - 1
        elif diaganol == "Right":
            col = piece_index[1] + 1
        return [row, col]

    def check_if_diaganol_empty(self, diaganol):
        """ 
        Checks if the diaganol is an empty space on the board
        Returns the diaganol if it space is empty
        or returns blocked if space is taken
        """
        if self.board[diaganol[0]][diaganol[1]] == "_":
            return diaganol
        else: 
            return "blocked"

    def format_available_moves(self, moves):
        """ 
        Formats the available moves
        Returns a list where blocked is replaced by empty
        And eligable moves are formatted correctly
        """
        available_moves = []
        for move in moves:
            if move != "blocked":
                available_move = self.format_piece(move[0], move[1])
                available_moves.append(available_move)
        return available_moves

    def move_piece(self, piece, new_position):
        """ 
        Moves the piece into the new postion on the board
        Removes the piece from its original postion on the board
        And places it into the empty space on the board
        """
        piece_index = self.get_index_of_piece(piece)
        new_position_index = self.get_index_of_piece(new_position)

        self.board[piece_index[0]][piece_index[1]] = "_"
        self.board[new_position_index[0]][new_position_index[1]] = "b"
    
