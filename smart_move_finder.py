import random

PIECE_SCORES = {"b": 3, "w": -3, "B": 5, "W": -5}

def find_random_move(available_moves):
    """
    Picks and returns a random move
    """
    return available_moves[random.randint(0, len(available_moves) - 1)]

def find_best_move(game_state, all_available_moves):
    """
    Find the best move based on score of pieces 
    """
    turn_multiplier = 1 if game_state.color_go == "black" else -1
    max_score = -60
    best_move = None

    for player_move in all_available_moves:
        game_state.move_piece(selected_piece, selected_move[0], selected_move[1], color)
        score = turn_multiplier * score_the_pieces_on_board(game_state.board)
        if score > max_score:
            score = max_score
            best_move = player_move

    return best_move

def score_the_pieces_on_board(board):
    """
    Score the board based on pieces 
    """
    score = 0
    for row in board:
        for square in row:
            if square in PIECE_SCORES:
                score += PIECE_SCORES[square]

    return score