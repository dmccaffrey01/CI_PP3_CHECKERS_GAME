""" 
This is the main file for the game. It will be responsible for handling user input
and displaying the current game state 
"""

import checkers_engine as check_eng
import display
import colorama
from colorama import Fore, Back, Style
import time
import smart_move_finder as smf
import main_menu as mm
import sys
import math
import leaderboard
import feature_testing as ft

def start_game(player1, player2, num, board_state):
    """ 
    Start the checkers game
    """
    game_state = check_eng.GameState(board_state)
    
    p1 = 0 # If a human is playing, this will be 0, if an AI is playing this will be 1, 2, or 3, this represents AI difficulty
    p2 = 0 # If a human is playing, this will be 0, if an AI is playing this will be 1, 2, or 3, this represents AI difficulty

    if num == 1:
        p1 = 0
        p2 = player2
    elif num == 2:
        p1 = 0
        p2 = 0
    else:
        p1 = player1
        p2 = player2

    start_game_loop(game_state, p1, p2, player1, player2, num)

    return [p1, p2]
    

def start_game_loop(game_state, p1, p2, player1, player2, num):
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
            display_game_over(game_state, moves, p1, p2, player1, player2, num)
            return "game over"
            
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
                
                time.sleep(0.2)

                game_state.move_piece(ai_move[0], ai_move[1], ai_move[2], ai_move[3])
            
            display_board(game_state)
            
            time.sleep(0.2)

            game_state.change_color_go()
            
            moves += 1

def display_board(game_state):
    """
    Prints out the board state 
    """
    global col_index, icons
    icons = []
    display.cls()
    board_state = game_state.board
    rows = game_state.BOARD_ROWS
    cols = game_state.BOARD_COLS
    col_index = -1
    for r, row_index in zip(rows, range(8)):
        for i in range(5):
            print(format_board_line(board_state, r, i, row_index))
            col_index = -1   
    print(Style.DIM + Fore.BLUE + format_cols_line(cols))

    return board_state
    
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

    display.new_line()

    print(Fore.YELLOW + "Choose a piece from the movable pieces eg.(1(F1) or 2(F2)...)")

    options = ""
    for piece, i in zip(movable_pieces, range(1, len(movable_pieces) + 1)):
        text = f"{i}) {piece}\n"
        options += text
    option_selected = input(options)
    display.new_line()
    while True:
        validated_option = validate_selected_option(option_selected, "movable_pieces", movable_pieces)
        if validated_option:
            return movable_pieces[validated_option - 1]
            break
        display_board(game_state)
        display.new_line() 
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

    display.new_line()

    print(Fore.YELLOW + "Choose a position to move to eg.(1(F1) or 2(F2)...)")
    print(Fore.YELLOW + "(Enter r to return to selecting a piece)")

    available_moves = game_state.find_available_moves(piece, color)

    formatted_moves = format_available_moves(available_moves)

    options = ""
    for move, i in zip(formatted_moves, range(1, len(formatted_moves) + 1)):
        text = f"{i}) {move}\n"
        options += text
    option_selected = input(options)
    display.new_line()
    while True:
        validated_option = validate_selected_option(option_selected, "available_moves", available_moves)
        if validated_option == "return":
            return "return"
            break
        elif validated_option:
            return [available_moves[validated_option - 1], validated_option]
            break
        display_board(game_state)
        display.new_line()
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

def display_game_over(game_state, moves, p1, p2, player1, player2, num):
    """
    Displays game over and winner
    Updates players wins, loses and games played
    Asks the user what to do next 
    """
    winner_color = check_winner(game_state, moves, "color", p1, p2, player1, player2)
    winner_name = check_winner(game_state, moves, "name", p1, p2, player1, player2)

    stats = update_player_stats(winner_color, p1, p2, player1, player2)

    display.cls()
    winning_message = game_over(winner_color, winner_name)
    time.sleep(3)
    display.cls()
    display_stats(stats, moves)
    time.sleep(2)
    display.new_line()
    ask_whats_next(p1, p2, player1, player2, num)

    return winning_message

def game_over(winner_color, winner_name):
    """ 
    Print out game over
    """
    wc = winner_color.upper()
    wc = " ".join(list(wc))
    wn = winner_name.upper()
    wn = " ".join(list(wn))
    for i in range(5):
        print(" ")
    winning_message = f"{' ' * 25}G A M E\n{' ' * 25}O V E R\n{' ' * 11}T H E   W I N N E R   I S   {wc}\n{' ' * (5 + math.ceil((48-(33 + len(wn)))/2))}C O N G R A T U L A T I O N S    {wn}\n"
    display.typewriter(winning_message)
    return winning_message

def display_stats(stats, moves):
    """ 
    Displays the stats for that game
    """
    for i in range(5):
        print(" ")
    display.new_line()
    print(Fore.CYAN + f"Total Moves: " + Fore.WHITE + str(moves))
    display.new_line()
    if stats[0] != "cpu":
        print(stats[0])
        display.new_line()
    if stats[1] != "cpu":
        print(stats[1])

    return stats
    

def update_player_stats(winner, p1, p2, player1, player2):
    """
    Updates the players, wins, loses and total games played 
    """
    stats = []
    if p1 == 0:
        player1.total_games += 1
        player1.update_database_value("total_games", player1.total_games, player1.email)
        if winner == "Black":
            player1.wins += 1
            player1.update_database_value("wins", player1.wins, player1.email)
        elif winner == "White":
            player1.loses += 1
            player1.update_database_value("loses", player1.loses, player1.email)
        stats.append(player1.display_player_stats())
    else:
        stats.append("cpu")
    
    if p2 == 0:
        player2.total_games += 1
        player2.update_database_value("total_games", player2.total_games, player2.email)
        if winner == "White":
            player2.wins += 1
            player2.update_database_value("wins", player2.wins, player2.email)
        elif winner == "Black":
            player2.loses += 1
            player2.update_database_value("loses", player2.loses, player2.email)
        stats.append(player2.display_player_stats())
    else:
        stats.append("cpu")
    
    return stats
              
def check_winner(game_state, moves, type, p1, p2, player1, player2):
    """
    Checks who the winner is and formats a string to return 
    """
    if moves >= 1000:
        message = "Draw"
    elif smf.score_the_pieces_on_board(game_state.board) > 0:
        if type == "color":
            message = "Black"
        elif type == "name":
            if p1 == 0:
                message = player1.name
            else:
                message = "CPU"
    else:
        if type == "color":
            message = "White"
        elif type == "name":
            if p2 == 0:
                message = player2.name
            else:
                message = "CPU"
    return message

def ask_whats_next(p1, p2, player1, player2, num):
    """ 
    Ask the user what to do next
    Their options are play again
    Return to main menu
    View the leaderboards
    Or quit the application
    """
    print(Fore.YELLOW + "What would you like to do:")
    options = "1) Play Again\n2) Return to Main Menu\n3) View the Leaderboards\n4) Quit\n"
    option_selected = input(options)
    display.new_line()
    while True:
        option = validate_whats_next_input(option_selected)
        if option:
            after_game_selection(option, p1, p2, player1, player2, num)
            return option
            break
        display.new_line()
        print(Fore.YELLOW + "Please input 1, 2, 3 or 4(r to return):")
        option_selected = input(options)

def validate_whats_next_input(option):
    """
    Checks if the option is valid
    If it is a 1, 2, 3 or 4 it returns 1, 2, 3 or 4False
    and if anything else it returns an error
    """
    if option == "1" or option.lower() == "one":
        return 1
    elif option == "2" or option.lower() == "two" or option == "r":
        return 2
    elif option == "3" or option.lower() == "three":
        return 3
    elif option == "4" or option.lower() == "four":
        return 4
    else:
        return False

def after_game_selection(option, player1, player2, num):
    """ 
    Decide what the game does after game has been played
    """
    if option == 1:
        start_game(player1, player2, num)
        return "start game"
    elif option == 2:
        mm.return_to_main_menu()
        return "return to main menu"
    elif option == 3:
        leaderboard.go_to_leaderboard()
        return "go to leaderboard"
    else:
        mm.exit_game()
        return "exit game"