import colorama
from colorama import Fore, Back, Style
import os
from run import welcome, cls, new_line, update_num_players
import time

#Initialize colorama
colorama.init(autoreset=True)


def get_num_players():
    """
    Get the number of players playing the game
    """
    welcome()
    print(Fore.YELLOW + "How many players?(1 or 2)")
    options = "1) One\n2) Two\n"
    option_selected = input(options)
    new_line()
    while True:
        if validate_num_players(option_selected):
            log_in_players(validate_num_players(option_selected))
            return validate_num_players(option_selected)
            break
        welcome()
        print(Fore.YELLOW + "Please input (1, one) or (2, two):")
        option_selected = input(options)
        new_line()
           

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

class Player:
    """
    Create an instance of a player
    """
    def __init__(self, name, email, registered):
        self.name = name
        self.email = email
        self.registered = registered


def log_in_players(num):
    """
    Asks the user for their name and if they have played before
    If they haven't then the program will register them
    If they have they will proceed to main menu
    Create a player instance of player class for each player
    """
    welcome()
    try:
        p1_registered = ask_registered("1")
    except:
        welcome()
        print(Fore.YELLOW + "Returning to number of players...")
        time.sleep(1)
        update_num_players()

def ask_registered(num):
    print(Fore.YELLOW + f"Has player {num} played before and have an existing account?")
    options = "1) Yes\n2) No\n3) Return\n"
    option_selected = input(options)
    while True:
        if validate_registered_input(option_selected):
            if validate_registered_input(option_selected) == 1:
                return True
            elif validate_registered_input(option_selected) == 2:
                return False
            break
        welcome()
        print(Fore.YELLOW + "Please input (1, y, yes) or (2, n, no) or (3, r, return) for have you an existing account:")
        option_selected = input(options)
        new_line()

def validate_registered_input(option):
    if option == "1" or option.lower() == "y" or option.lower() == "yes":
        return 1
    if option == "2" or option.lower() == "n" or option.lower() == "no":
        return 2
    elif option == "3" or option.lower() == "r" or option.lower() == "return":
        raise Exception("Return to number of players")
        return 3
    else:
        return False 

def ask_player_name(num):
    print(Fore.YELLOW + f"Enter name of player {num}:") 
    return input()