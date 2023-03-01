import colorama
from colorama import Fore, Back, Style
import os
from run import welcome, cls, new_line, update_num_players
import time
from email_validator import validate_email, EmailNotValidError
import gspread
from google.oauth2.service_account import Credentials

#Initialize colorama
colorama.init(autoreset=True)

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("CI_PP3_CHECKERS_GAME_DATABASE")
WORKSHEET = SHEET.worksheet("players")

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
    def __init__(self, name, email):
        self.name = name
        self.email = email
        


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
        new_line()
        p1_name = ask_player_name("1")
        new_line()
        p1_email = validate_email_registered(ask_player_email(p1_name), p1_registered, p1_name)
    except:
        welcome()
        print(Fore.YELLOW + "Returning to number of players...")
        time.sleep(1)
        update_num_players()

def ask_registered(num):
    """
    Ask the user if the player has been registered
    Returns true if they have
    Returns false if they have not
    """
    print(Fore.YELLOW + "Enter r to return")
    print(Fore.YELLOW + f"Has player {num} played before and have an existing account?")
    options = "1) Yes\n2) No\n"
    option_selected = input(options)
    while True:
        if validate_registered_input(option_selected):
            if validate_registered_input(option_selected) == 1:
                return True
            elif validate_registered_input(option_selected) == 2:
                return False
            break
        welcome()
        print(Fore.YELLOW + "Please input (1, y, yes) or (2, n, no) for have you an existing account or (r to return):")
        option_selected = input(options)

def validate_registered_input(option):
    """ 
    Checks if the input was 1,y,yes and returns 1
    if 2,n,no and returns 2
    if r it raise exception and returns to number of players
    """
    if option == "1" or option.lower() == "y" or option.lower() == "yes":
        return 1
    elif option == "2" or option.lower() == "n" or option.lower() == "no":
        return 2
    elif option.lower() == "r" or option.lower() == "return":
        return_to_num_players()
        return 3
    else:
        return False 

def ask_player_name(num):
    """
    Asks the user for their name
    Returns to number of players if input is r
    Returns name 
    """
    print(Fore.YELLOW + "Enter r to return")
    print(Fore.YELLOW + f"Enter name of player {num}:") 
    name = input()
    if name == "r":
        return_to_num_players()
    return name

def return_to_num_players():
    """ 
    Raises an exception
    """
    raise Exception("Return to number of players")

def ask_player_email(name):
    """
    Asks the user for their email
    Returns to number of players if r is pressed
    Checks if email is valid 
    """
    print(Fore.YELLOW + "Enter r to return")
    print(Fore.YELLOW + f"Enter email of {name}:") 
    while True:
        email = input()
        if email == "r":
            return_to_num_players()
            break
        if validate_user_email(email):
            break
    return email
            
def validate_user_email(email):
    """
    Check if email is valid
    Must be in form name@email.com
    """
    try:
        validate_email(email)
        return True
    except EmailNotValidError as e:
        print(Fore.RED + "\n" + str(e))
        print(Fore.RED + "Please try again.\n")
        
def validate_email_registered(email, registered, name):
    """
    Registers new players email
    Checks if existing player email is correct
    Registers or trys again if email is incorrect
    Returns email
    """
    if not registered:
        pass
    else:
        if check_is_email_registered(email):
            return email
        else:
            return incorrect_email_input(name, registered)
       
def check_is_email_registered(email):
    """
    Checks if the email entered is on the data base
    Returns true if it is and false if not
    """
    email_col = WORKSHEET.col_values(2)
    if email in email_col:
        return True
    else:
        return False

def incorrect_email_input(name, registered):
    """
    Called when email entered does not match any email in database
    Prints error message
    Asks the user to try again or register as a new email
    Returns a new email
    """
    new_line()
    print(Fore.RED + "Email address not found on database")
    return ask_incorrect_email_question(name, registered)

def ask_incorrect_email_question(name, registered):
    """
    Asks user to try entering their email again
    or to register as a new player
    """
    new_line()
    print(Fore.YELLOW + "What would you like to do:")
    options = "1) Try entering email again\n2) Register as new player\n"
    option_selected = input(options)
    while True:
        if validate_incorrect_email_input(option_selected):
            if validate_incorrect_email_input(option_selected) == 1:
                return validate_email_registered(ask_player_email(name), registered, name)
            elif validate_registered_input(option_selected) == 2:
                pass
            break
        new_line()
        print(Fore.YELLOW + "Please input 1 or 2 for have you an try again or register or (r to return):")
        option_selected = input(options)

def validate_incorrect_email_input(option):
    """ 
    Checks if the input is 1 or 2 or r
    Returns correct number for each case
    """
    if option == "1":
        return 1
    elif option == "2":
        return 2
    elif option.lower() == "r":
        return_to_num_players()
        return 3
    else:
        return False