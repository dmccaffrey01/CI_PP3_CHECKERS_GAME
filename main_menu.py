import colorama
from colorama import Fore, Back, Style
import os
from run import welcome, cls, new_line

def get_num_players():
    """
    Get the number of players playing the game
    """
    welcome()
    print(Fore.YELLOW + "How many players?(1 or 2)")
    options = "1) One\n2) Two\n"
    option_selcted = input(options)
    new_line()
    if validate_num_players(option_selcted):
        return validate_num_players(option_selcted)
    else:
        while True:
            welcome()
            print(Fore.YELLOW + "Please input 1 or 2:")
            option_selcted = input(options)
            new_line()
            if validate_num_players(option_selcted):
                return validate_num_players
                break

def validate_num_players(option):
    """
    Checks if the option is valid
    If it is a 1 or 2 it returns 1 or 2
    and if anything else it returns an error
    """
    if option == "1" or option.lower() == "one":
        return 1
    elif option == "2" or option.lower() == "two":
        return 2
    else:
        return False