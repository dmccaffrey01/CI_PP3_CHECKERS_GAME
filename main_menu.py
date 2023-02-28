import colorama
from colorama import Fore, Back, Style
import os
from run import welcome, cls, new_line, update_num_players, num_players

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
        print(Fore.YELLOW + "Please input 1 or 2:")
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
    def __init__(self, name, email, registered):
        self.name = name
        self.email = email
        self.registered = registered


def log_in_players():
    """
    Asks the user for their name and if they have played before
    If they haven't then the program will register them
    If they have they will proceed to main menu
    """
    ask_players_names(num_players)
    ask_existing_account(num_players)



def ask_existing_account():
    welcome()
    print(Fore.YELLOW + "Has player 1 played before and have an existing account?")
    options = "1) Yes\n2) No\n3) Return\n"
    option_selected = input(options)
    while True:
        if validate_existing_account_input(option_selected):
            break
        welcome()
        print(Fore.YELLOW + "Please input (1, y, yes) or (2, n, no) or (3, r, return) for have you an existing account:")
        option_selected = input(options)
        new_line()

def update_existing_account_status(bool):
    global existing_account_status
    existing_account_status = bool

def validate_existing_account_input(option):
    if option == "1" or option.lower() == "y" or option.lower() == "yes":
        update_existing_account_status(True)
        return True
    if option == "2" or option.lower() == "n" or option.lower() == "no":
        update_existing_account_status(False)
        return True
    elif option == "3" or option.lower() == "r" or option.lower() == "return":
        update_num_players()
        return True
    else:
        return False 
