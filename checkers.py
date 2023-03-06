""" 
This is the main file for the game. It will be responsible for handling user input
and displaying the current game state 
"""

import checkers_engine as check_eng

def start_game():
    """ 
    Start the checkers game
    """
    game_state = check_eng.GameState()

    display_board(game_state)

    movable_pieces = game_state.get_movable_pieces()

    print(movable_pieces)


def display_board(game_state):
    """ 
    Prints the board state to the console
    """
    board_state = game_state.board

    for x in board_state:
        row = " ".join(x)
        print(row)
