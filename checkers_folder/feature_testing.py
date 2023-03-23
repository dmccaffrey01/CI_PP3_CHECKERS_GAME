import colorama
from colorama import Fore, Back, Style
import os
import time
import sys
# Get the parent path of the current script
parent_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
# Add the parent path to the system path
sys.path.append(parent_path)
sys.path.insert(0, 'main_menu_folder/')
import main_menu as mm
import display

#Initialize colorama
colorama.init(autoreset=True)

board_states = {
    "empty": [
            ["x", "_", "x", "_", "x", "_", "x", "_"],
            ["_", "x", "_", "x", "_", "x", "_", "x"],
            ["x", "_", "x", "_", "x", "_", "x", "_"],
            ["_", "x", "_", "x", "_", "x", "_", "x"],
            ["x", "_", "x", "_", "x", "_", "x", "_"],
            ["_", "x", "_", "x", "_", "x", "_", "x"],
            ["x", "_", "x", "_", "x", "_", "x", "_"],
            ["_", "x", "_", "x", "_", "x", "_", "x"]
        ],

    "full": [
            ["x", "w", "x", "w", "x", "w", "x", "w"],
            ["w", "x", "w", "x", "w", "x", "w", "x"],
            ["x", "w", "x", "w", "x", "w", "x", "w"],
            ["_", "x", "_", "x", "_", "x", "_", "x"],
            ["x", "_", "x", "_", "x", "_", "x", "_"],
            ["b", "x", "b", "x", "b", "x", "b", "x"],
            ["x", "b", "x", "b", "x", "b", "x", "b"],
            ["b", "x", "b", "x", "b", "x", "b", "x"]
        ],

    "single jump": [
            ["x", "W", "x", "_", "x", "_", "x", "W"],
            ["_", "x", "_", "x", "_", "x", "_", "x"],
            ["x", "_", "x", "W", "x", "W", "x", "_"],
            ["_", "x", "_", "x", "B", "x", "_", "x"],
            ["x", "_", "x", "W", "x", "W", "x", "_"],
            ["_", "x", "_", "x", "_", "x", "_", "x"],
            ["x", "W", "x", "_", "x", "_", "x", "W"],
            ["W", "x", "_", "x", "_", "x", "_", "x"]
        ],

    "double jump": [
            ["x", "_", "x", "_", "x", "_", "x", "_"],
            ["_", "x", "_", "x", "_", "x", "_", "x"],
            ["x", "_", "x", "_", "x", "_", "x", "_"],
            ["_", "x", "_", "x", "_", "x", "_", "x"],
            ["x", "_", "x", "_", "x", "w", "x", "_"],
            ["w", "x", "_", "x", "_", "x", "_", "x"],
            ["x", "_", "x", "w", "x", "_", "x", "_"],
            ["b", "x", "b", "x", "_", "x", "_", "x"]
        ],
    
    "triple jump": [
            ["x", "_", "x", "_", "x", "_", "x", "_"],
            ["_", "x", "_", "x", "_", "x", "_", "x"],
            ["x", "_", "x", "_", "x", "w", "x", "_"],
            ["_", "x", "_", "x", "_", "x", "_", "x"],
            ["x", "_", "x", "_", "x", "w", "x", "_"],
            ["w", "x", "_", "x", "_", "x", "_", "x"],
            ["x", "_", "x", "w", "x", "_", "x", "_"],
            ["b", "x", "b", "x", "_", "x", "_", "x"]
        ],

    "quintuple jump": [
            ["x", "_", "x", "_", "x", "_", "x", "_"],
            ["_", "x", "_", "x", "_", "x", "_", "x"],
            ["x", "_", "x", "w", "x", "w", "x", "_"],
            ["_", "x", "_", "x", "_", "x", "_", "x"],
            ["x", "w", "x", "_", "x", "w", "x", "_"],
            ["_", "x", "_", "x", "_", "x", "_", "x"],
            ["x", "_", "x", "w", "x", "_", "x", "_"],
            ["b", "x", "B", "x", "_", "x", "_", "x"]
        ],

    "king": [
            ["x", "_", "x", "B", "x", "_", "x", "w"],
            ["_", "x", "_", "x", "b", "x", "_", "x"],
            ["x", "_", "x", "_", "x", "_", "x", "_"],
            ["_", "x", "_", "x", "_", "x", "_", "x"],
            ["x", "_", "x", "_", "x", "_", "x", "_"],
            ["_", "x", "_", "x", "_", "x", "_", "x"],
            ["x", "_", "x", "_", "x", "_", "x", "_"],
            ["_", "x", "_", "x", "_", "x", "_", "x"]
        ],

    "jump to king": [
            ["x", "_", "x", "_", "x", "_", "x", "w"],
            ["_", "x", "_", "x", "W", "x", "_", "x"],
            ["x", "_", "x", "_", "x", "_", "x", "_"],
            ["_", "x", "_", "x", "w", "x", "_", "x"],
            ["x", "_", "x", "_", "x", "b", "x", "_"],
            ["_", "x", "_", "x", "_", "x", "_", "x"],
            ["x", "_", "x", "_", "x", "_", "x", "_"],
            ["_", "x", "_", "x", "_", "x", "_", "x"]
        ],

    "test board 1": [
            ["x", "_", "x", "_", "x", "_", "x", "_"],
            ["_", "x", "w", "x", "_", "x", "_", "x"],
            ["x", "_", "x", "b", "x", "_", "x", "_"],
            ["_", "x", "_", "x", "_", "x", "_", "x"],
            ["x", "_", "x", "_", "x", "_", "x", "_"],
            ["_", "x", "_", "x", "w", "x", "_", "x"],
            ["x", "_", "x", "b", "x", "_", "x", "_"],
            ["_", "x", "_", "x", "_", "x", "_", "x"]
        ],

    "test board 2": [
            ["x", "_", "x", "_", "x", "_", "x", "w"],
            ["_", "x", "_", "x", "_", "x", "_", "x"],
            ["x", "_", "x", "_", "x", "_", "x", "_"],
            ["_", "x", "_", "x", "w", "x", "_", "x"],
            ["x", "_", "x", "b", "x", "_", "x", "_"],
            ["_", "x", "_", "x", "_", "x", "_", "x"],
            ["x", "_", "x", "_", "x", "_", "x", "_"],
            ["_", "x", "_", "x", "_", "x", "B", "x"]
        ],

    "test board 3": [
            ["x", "W", "x", "w", "x", "_", "x", "w"],
            ["_", "x", "_", "x", "_", "x", "_", "x"],
            ["x", "_", "x", "_", "x", "_", "x", "_"],
            ["_", "x", "_", "x", "W", "x", "_", "x"],
            ["x", "_", "x", "B", "x", "_", "x", "_"],
            ["_", "x", "_", "x", "_", "x", "_", "x"],
            ["x", "_", "x", "_", "x", "_", "x", "_"],
            ["b", "x", "B", "x", "_", "x", "_", "x"]
        ],

        "test board 4": [
            ["x", "_", "x", "_", "x", "_", "x", "w"],
            ["b", "x", "_", "x", "w", "x", "_", "x"],
            ["x", "_", "x", "b", "x", "_", "x", "_"],
            ["_", "x", "_", "x", "_", "x", "_", "x"],
            ["x", "_", "x", "_", "x", "_", "x", "_"],
            ["_", "x", "_", "x", "_", "x", "_", "x"],
            ["x", "_", "x", "_", "x", "_", "x", "_"],
            ["_", "x", "_", "x", "_", "x", "_", "x"]
        ],

        "test_get_available_moves_black": [
            ["x", "_", "x", "B", "x", "_", "x", "B"],
            ["_", "x", "_", "x", "_", "x", "_", "x"],
            ["x", "_", "x", "_", "x", "_", "x", "B"],
            ["_", "x", "_", "x", "B", "x", "_", "x"],
            ["x", "_", "x", "_", "x", "_", "x", "_"],
            ["B", "x", "_", "x", "_", "x", "_", "x"],
            ["x", "_", "x", "_", "x", "_", "x", "_"],
            ["b", "x", "_", "x", "B", "x", "_", "x"]
        ],

        "test_get_available_moves_white": [
            ["x", "_", "x", "W", "x", "_", "x", "w"],
            ["_", "x", "_", "x", "_", "x", "_", "x"],
            ["x", "_", "x", "_", "x", "_", "x", "W"],
            ["_", "x", "_", "x", "W", "x", "_", "x"],
            ["x", "_", "x", "_", "x", "_", "x", "_"],
            ["W", "x", "_", "x", "_", "x", "_", "x"],
            ["x", "_", "x", "_", "x", "_", "x", "_"],
            ["W", "x", "_", "x", "W", "x", "_", "x"]
        ],

        "test_check_kings_jumps_black": [
            ["x", "_", "x", "B", "x", "_", "x", "_"],
            ["_", "x", "_", "x", "_", "x", "_", "x"],
            ["x", "_", "x", "_", "x", "_", "x", "_"],
            ["_", "x", "_", "x", "_", "x", "_", "x"],
            ["x", "_", "x", "_", "x", "B", "x", "_"],
            ["_", "x", "b", "x", "_", "x", "_", "x"],
            ["x", "_", "x", "_", "x", "_", "x", "_"],
            ["_", "x", "_", "x", "B", "x", "_", "x"]
        ],

        "test_check_kings_jumps_white": [
            ["x", "_", "x", "W", "x", "_", "x", "_"],
            ["_", "x", "_", "x", "_", "x", "_", "x"],
            ["x", "_", "x", "_", "x", "_", "x", "_"],
            ["_", "x", "_", "x", "_", "x", "_", "x"],
            ["x", "_", "x", "_", "x", "W", "x", "_"],
            ["_", "x", "w", "x", "_", "x", "_", "x"],
            ["x", "_", "x", "_", "x", "_", "x", "_"],
            ["_", "x", "_", "x", "W", "x", "_", "x"]
        ],

        "test_check_ipnk": [
            ["x", "_", "x", "b", "x", "B", "x", "_"],
            ["_", "x", "_", "x", "_", "x", "_", "x"],
            ["x", "_", "x", "b", "x", "_", "x", "_"],
            ["_", "x", "_", "x", "_", "x", "_", "x"],
            ["x", "_", "x", "_", "x", "_", "x", "_"],
            ["_", "x", "w", "x", "_", "x", "_", "x"],
            ["x", "_", "x", "_", "x", "_", "x", "_"],
            ["_", "x", "w", "x", "W", "x", "_", "x"]
        ],

        "test_check_jump": [
            ["x", "_", "x", "_", "x", "_", "x", "w"],
            ["w", "x", "_", "x", "w", "x", "_", "x"],
            ["x", "_", "x", "_", "x", "w", "x", "_"],
            ["_", "x", "_", "x", "_", "x", "b", "x"],
            ["x", "b", "x", "_", "x", "_", "x", "_"],
            ["_", "x", "_", "x", "_", "x", "w", "x"],
            ["x", "_", "x", "_", "x", "_", "x", "b"],
            ["_", "x", "_", "x", "b", "x", "_", "x"]
        ],
}

def go_to_feature_testing():
    """
    Ask the user what feature they would like to test
    """
    try:
        display.welcome()
        print(Fore.YELLOW + "Choose what board scenario you would like to test:")
        print(Fore.YELLOW + "(Enter r to return to main menu)")
        options = "1) Singe Jump\n2) Double jump\n3) Triple Jump\n4) Quintuple Jump\n5) King\n6) Jump To King\n"
        option_selected = input(options)
        display.new_line()
        while True:
            validated_option = validate_ask_feature_testing(option_selected)
            if validated_option:
                if validated_option == "return":
                    mm.raise_return_to_main_menu()
                else:
                    set_up_board(validated_option)
                return validated_option
            display.welcome()
            print(Fore.YELLOW + "Please input (1, one) or (2, two) or (3, three) or (4, four) or (5, five) or (6, six):")
            option_selected = input(options)
            display.new_line()
    except:
        return mm.return_to_main_menu()

def validate_ask_feature_testing(option):
    """
    Validate the option, returns number or return if valid
    And false if not valid 
    """
    if option == "1" or option.lower() == "one":
        return "single jump"
    elif option == "2" or option.lower() == "two":
        return "double jump"
    elif option == "3" or option.lower() == "three":
        return "triple jump"
    elif option == "4" or option.lower() == "four":
        return "quintuple jump"
    elif option == "5" or option.lower() == "five":
        return "king"
    elif option == "6" or option.lower() == "six":
        return "jump to king"
    elif option == "r":
        return "return"
    else:
        return False

def set_up_board(option):
    """
    Sets up the board with correct option to test
    Creates fake players to start the game
    Starts a checkers game with that board
    """
    test_player_1 = mm.Player("test_one", "testone@gmail.com", 0, 0, 0)
    test_player_2 = mm.Player("test_two", "testtwo@gmail.com", 0, 0, 0)
    mm.start_checkers_game(test_player_1, test_player_2, 2, option, True)
    return "set_up_board"


