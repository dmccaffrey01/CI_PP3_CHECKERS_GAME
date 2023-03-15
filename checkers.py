""" 
This is the main file for the game. It will be responsible for handling user input
and displaying the current game state 
"""

import checkers_engine as check_eng
from run import cls, new_line
import colorama
from colorama import Fore, Back, Style
import time
import smart_move_finder as smf

def start_game():
    """ 
    Start the checkers game
    """
    
    game_state = check_eng.GameState()
    """
    player_one = 0 # If a human is playing, this will be 0, if an AI is playing this will be 1, 2, or 3, this represents AI difficulty

    player_two = 1 # If a human is playing, this will be 0, if an AI is playing this will be 1, 2, or 3, this represents AI difficulty

    start_game_loop(game_state, player_one, player_two)
    """
    display_boardn(game_state)

def start_game_loop(game_state, p1, p2):
    """ 
    Starts the basic game loop
    Asks player to pick a piece to move from movable pieces
    When player has picked a piece
    Asks player to pick a move from available moves
    Moves that piece the player picked
    Moves on to the other players go
    """
    moves = 0
    game_over = False
    while not game_over:
        color = game_state.color_go
        human_turn = (color == "black" and not p1) or (color == "white" and not p2)
        
        movable_pieces = game_state.get_movable_pieces(color)
        if not movable_pieces or moves >= 1000:
            game_over = True
            winner = check_winner(game_state, moves)
            print(winner)
            print("Total Moves: " + str(moves))
        else:
            selecting_move = True 
            while selecting_move and human_turn:
                selected_piece = select_piece(game_state, movable_pieces, color)
                
                selected_move = select_move(game_state, selected_piece, color)

                if selected_move != "return":
                    game_state.move_piece(selected_piece, selected_move[0], selected_move[1], color)
                    selecting_move = False

            if not human_turn:
                available_moves = game_state.find_all_available_moves(color)

                ai_move = smf.find_best_move(game_state, available_moves, p1 if game_state.color_go == "black" else p2)

                game_state.move_piece(ai_move[0], ai_move[1], ai_move[2], ai_move[3])
            
            display_board(game_state)
            
            #time.sleep(2)
            
            game_state.change_color_go()
            
            moves += 1

def display_board(game_state):
    """ 
    Prints the board state to the console
    """
    cls()
    board_state = game_state.board
    board_rows = game_state.BOARD_ROWS
    board_cols = " ".join(game_state.BOARD_COLS)
    odd_row = True
    for x, r in zip(board_state, board_rows):
        row = x
        if odd_row:
            print(r + " " + Back.RED + row[0] + " " + Back.YELLOW + row[1] + " " + Back.RED + row[2] + " " + Back.YELLOW + row[3] + " " + Back.RED + row[4] + " " + Back.YELLOW + row[5] + " " + Back.RED + row[6] + " " + Back.YELLOW + row[7] + " ")
            odd_row = False
        else:
            print(r + " " + Back.YELLOW + row[0] + " " + Back.RED + row[1] + " " + Back.YELLOW + row[2] + " " + Back.RED + row[3] + " " + Back.YELLOW + row[4] + " " + Back.RED + row[5] + " " + Back.YELLOW + row[6] + " " + Back.RED + row[7]+ " ")
            odd_row = True
    
    print("  " + board_cols)

def display_boardn(game_state):
    """
    Prints out the board state 
    """
    global col_index, icons
    icons = []
    cls()
    board_state = game_state.board
    rows = game_state.BOARD_ROWS
    cols = game_state.BOARD_COLS
    col_index = -1
    odd_row = True
    for r, row_index in zip(rows, range(8)):
        for i in range(5):
            print(format_board_line(board_state, r, i, row_index))
            col_index = -1   
    print(Style.DIM + Fore.BLUE + format_cols_line(cols))
    
def format_board_line(board_state, r, i, row_index):
    """
    Formats a line for a row of the board
    Returns an f string with colors and correct pieces 
    """
    if int(r) % 2 == 0:
        if i == 2:
            return f"{Style.DIM + ' ' * 7 + Fore.BLUE + r + ' ' * 2 + yellow_square() + red_square(board_state, i, row_index) + yellow_square() + red_square(board_state, i, row_index) + yellow_square() + red_square(board_state, i, row_index) + yellow_square() + red_square(board_state, i, row_index)}"
        else:
            return f"{Style.DIM + ' ' * 10 + yellow_square() + red_square(board_state, i, row_index) + yellow_square() + red_square(board_state, i, row_index) + yellow_square() + red_square(board_state, i, row_index) + yellow_square() + red_square(board_state, i, row_index)}"
    else:
        if i == 2:
            return f"{Style.DIM + ' ' * 7 + Fore.BLUE + r + ' ' * 2 + red_square(board_state, i, row_index) + yellow_square() + red_square(board_state, i, row_index) + yellow_square() + red_square(board_state, i, row_index) + yellow_square() + red_square(board_state, i, row_index) + yellow_square()}"
        else:
            return f"{Style.DIM + ' ' * 10 + red_square(board_state, i, row_index) + yellow_square() + red_square(board_state, i, row_index) + yellow_square() + red_square(board_state, i, row_index) + yellow_square() + red_square(board_state, i, row_index) + yellow_square()}"

def red_square(board_state, i, row_index):
    """
    Returns functions for red square in f string
    Consists of 10 letter width and 5 letter height 
    """
    global col_index
    col_index += 1
    if i == 0 or i == 4: 
        return f"{Back.RED + ' ' * 10}" 
    else:
        return f"{Back.RED + ' ' * 2 + display_piece(board_state, i, row_index, col_index) + Back.RED + ' ' * 2}"
    

def yellow_square():
    """ 
    Returns functions for yellow square in f string
    Consists of 10 letter width and 5 letter height
    """
    global col_index
    col_index += 1
    return f"{Back.YELLOW + ' ' * 10}"

def display_piece(board_state, i, row_index, col_index):
    """
    Displays the piece depending on its type and what line
    Consists of a 6 letter width and 3 letter height
    Kings have a green dot in the middle 
    """
    piece_icon = get_piece_icon(board_state, row_index, col_index)
    if piece_icon == "b":
        return f"{Back.BLACK + ' ' * 6}"
    elif piece_icon == "B":
        if i == 1 or i == 3:
            return f"{Back.BLACK + ' ' * 6}"
        else:
            return f"{Back.BLACK + ' ' * 2 + Back.GREEN + ' ' * 2 + Back.BLACK + ' ' * 2}"
    elif piece_icon == "w":
        return f"{Back.WHITE + ' ' * 6}"
    elif piece_icon == "W":
        if i == 1 or i == 3:
            return f"{Back.WHITE + ' ' * 6}"
        else:
            return f"{Back.WHITE + ' ' * 2 + Back.GREEN + ' ' * 2 + Back.WHITE + ' ' * 2}"
    else:
        return f"{Back.RED + ' ' * 6}"

def get_piece_icon(board_state, row_index, col_index):
    """
    Returns the pieces icon from the row and col indexes 
    """
    return board_state[row_index][col_index]

def format_cols_line(cols):
    """
    Returns cols line formatted correctly
    """
    new_cols = []   
    for col in cols:
        new_col = f"{' ' * 5 + col + ' ' * 4}"
        new_cols.append(new_col)
    cols_line = f"{' ' * 10 + ''.join(new_cols)}"
    return cols_line

def select_piece(game_state, movable_pieces, color):
    """
    Asks player to pick a piece to move from movable pieces
    Validates the option selected
    """
    display_board(game_state)

    new_line()

    print(Fore.YELLOW + "Choose a piece from the movable pieces eg.(1(F1) or 2(F2)...)")

    options = ""
    for piece, i in zip(movable_pieces, range(1, len(movable_pieces) + 1)):
        text = f"{i}) {piece}\n"
        options += text
    option_selected = input(options)
    new_line()
    while True:
        if validate_selected_option(option_selected, "movable_pieces", movable_pieces):
            return movable_pieces[validate_selected_option(option_selected, "movable_pieces", movable_pieces) - 1]
            break
        display_board(game_state)
        new_line() 
        print(Fore.YELLOW + f"Please input (1 - {len(movable_pieces)})")
        option_selected = input(options)
          

def validate_selected_option(option, type, list):
    """ 
    Checks if the option selected is a valid option
    Returns number of selected option if valid
    Or returns false if not valid
    """
    try:
        if option == "r" and type == "available_moves":
            return "return"
        option_selected = int(option)
        if option_selected >= 1 and option_selected <= len(list):
            return option_selected
        else:
            raise ValueError()
    except:
        return False

def select_move(game_state, piece, color):
    """
    Asks player to pick a board position for the selected piece to move to from available moves
    Validates the option selected
    """
    display_board(game_state)

    new_line()

    print(Fore.YELLOW + "Choose a position to move to eg.(1(F1) or 2(F2)...)")
    print(Fore.YELLOW + "(Enter r to return to selecting a piece)")

    available_moves = game_state.find_available_moves(piece, color)

    formatted_moves = format_available_moves(available_moves)

    options = ""
    for move, i in zip(formatted_moves, range(1, len(formatted_moves) + 1)):
        text = f"{i}) {move}\n"
        options += text
    option_selected = input(options)
    new_line()
    while True:
        if validate_selected_option(option_selected, "available_moves", available_moves) == "return":
            return "return"
            break
        elif validate_selected_option(option_selected, "available_moves", available_moves):
            return [available_moves[validate_selected_option(option_selected, "available_moves", available_moves) - 1], validate_selected_option(option_selected, "available_moves", available_moves)]
            break
        display_board(game_state)
        new_line()
        print(Fore.YELLOW + f"Please input (1 - {len(available_moves)})")
        option_selected = input(options)

def format_available_moves(moves):
    """ 
    Formats the available moves correctly to display to user
    """
    formatted_moves = []
    for move in moves:
        formatted_move = ""
        if move[1] == "move":
           formatted_move += "Move to: " + move[0]
        elif move[1] == "jump":
            formatted_move += "Jump to: " + move[0]
        formatted_moves.append(formatted_move)
    
    return formatted_moves
                
def check_winner(game_state, moves):
    """
    Checks who the winner is and formats a string to return 
    """
    if moves >= 1000:
        message = "There is no winner, it ended in a draw"
    elif smf.score_the_pieces_on_board(game_state.board) > 0:
        message = "Black is the winner"
    else:
        message = "White is the winner"
    return message




        
