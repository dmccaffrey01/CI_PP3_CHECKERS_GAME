import random

PIECE_SCORES = {"b": 3, "w": -3, "B": 5, "W": -5}

def find_best_move(game_state, available_moves, ai_difficulty):
    """
    Helper method that returns the next move
    Calls intial find move min max and returns next move
    """
    global next_move, search_depth
    next_move = None
    random.shuffle(available_moves)
    search_depth = set_search_depth(ai_difficulty)
    #find_move_nega_max(game_state, available_moves, search_depth, 1 if game_state.black_to_move else -1, game_state.color_go)
    if ai_difficulty == 1:
        find_random_move(game_state, available_moves)
    else:
        find_move_nega_max_alpha_beta(game_state, available_moves, search_depth, -60, 60, 1 if game_state.black_to_move else -1, game_state.color_go)
        if next_move == None:
            find_random_move(game_state, available_moves)
    return next_move

def find_random_move(game_state, available_moves):
    """
    Finds a random move to make 
    """
    global next_move
    next_move = available_moves[random.randint(0, len(available_moves) -1)]
    return next_move

#def find_move_nega_max(game_state, available_moves, depth, turn_multiplier, color):
    #""" 
    #Find a move based on min max algorithm
    #"""
    #global next_move, search_depth
    #if depth == 0:
        #return turn_multiplier * score_the_pieces_on_board(game_state.board)

    #max_score = -60 # Worst possible score
    #for move in available_moves:
        #game_state.move_piece(move[0], move[1], move[2], move[3])
        #next_moves = game_state.find_all_available_moves(get_opposite_color(color))
        #score = -find_move_nega_max(game_state, next_moves, depth - 1, -turn_multiplier, get_opposite_color(color))
        #if score > max_score:
            #max_score = score
            #if depth == search_depth:
                #next_move = move
        #game_state.undo_move()
    #return max_score 

def find_move_nega_max_alpha_beta(game_state, available_moves, depth, alpha, beta, turn_multiplier, color):
    """ 
    Find a move based on min max algorithm also using alpha beta pruning
    To help runtime and efficiency
    """
    global next_move, search_depth
    if depth == 0:
        return turn_multiplier * score_the_pieces_on_board(game_state.board)

    max_score = -60 # Worst possible score
    for move in available_moves:
        game_state.move_piece(move[0], move[1], move[2], move[3])
        next_moves = game_state.find_all_available_moves(get_opposite_color(color))
        score = -find_move_nega_max_alpha_beta(game_state, next_moves, depth - 1, -beta, -alpha, -turn_multiplier, get_opposite_color(color))
        if score > max_score:
            max_score = score
            if depth == search_depth:
                next_move = move
        game_state.undo_move()
        if max_score > alpha: #pruning happens
            alpha = max_score
        if alpha >= beta:
            break
    return max_score 

def set_search_depth(ai_difficulty):
    """
    Set the search depth depending on the AI difficulty 
    """
    if ai_difficulty == 2:
        search_depth = 2
    elif ai_difficulty == 3:
        search_depth = 4
    else:
        search_depth = 2
    
    return search_depth
    

def get_opposite_color(color):
    """ 
    Returns opposite color
    """
    if color == "white":
        return "black"
    elif color == "black":
        return "white"

def score_the_pieces_on_board(board):
    """
    Score the board based on pieces 
    A postive score is good for black
    A negative score is good for white
    """
    score = 0
    for row in board:
        for square in row:
            if square in PIECE_SCORES:
                score += PIECE_SCORES[square]

    return score