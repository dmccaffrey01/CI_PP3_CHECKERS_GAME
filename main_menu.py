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
    def __init__(self, name, email, total_games, wins, loses):
        self.name = name
        self.email = email
        self.total_games = total_games
        self.wins = wins
        self.loses = loses

    def register_or_login_player(self):
        """
        Checks if player has registered
        If they have updates the players name
        If they haven't it adds them to the database 
        """
        if check_is_email_registered(self.email):
            self.update_database_value("name", self.name, self.email)
        else:
            self.add_player_to_database(self.name, self.email, self.total_games, self.wins, self.loses)

    def update_database_value(self, col, value, email):
        """
        Updates the name in the database 
        """
        if col == "name":
            col = 1
        elif col == "email":
            col = 2
        elif col == "totat_games":
            col = 3
        elif col == "wins":
            col = 4
        elif col == "loses":
            col = 5
        
        row = WORKSHEET.col_values(2).index(email) + 1

        WORKSHEET.update_cell(row, col, value)

    def add_player_to_database(self, name, email, totat_games, wins, loses):
        """
        Add player to the database
        """
        row = [name, email, totat_games, wins, loses]
        WORKSHEET.append_row(row)
        


def log_in_players(num):
    """
    Asks the user for their name and if they have played before
    If they haven't then the program will register them
    If they have they will proceed to main menu
    Create a player instance of player class for each player
    """
    welcome()
    try:
        global player1
        p1_registered = ask_registered("1")
        new_line()

        p1_name = ask_player_name("1")
        new_line()

        p1_email = validate_email_registered(ask_player_email(p1_name), p1_registered, p1_name)

        p1_total_games = get_worksheet_value(p1_email, "total_games")
        p1_wins = get_worksheet_value(p1_email, "wins")
        p1_loses = get_worksheet_value(p1_email, "loses")

        player1 = Player(p1_name, p1_email, p1_total_games, p1_wins, p1_loses)
        player1.register_or_login_player()

        if num == 2:
            global player2
            p2_registered = ask_registered("2")
            new_line()

            p2_name = ask_player_name("2")
            new_line()

            p2_email = validate_email_registered(ask_player_email(p2_name), p2_registered, p2_name)

            p2_total_games = get_worksheet_value(p2_email, "total_games")
            p2_wins = get_worksheet_value(p2_email, "wins")
            p2_loses = get_worksheet_value(p2_email, "loses")

            player2 = Player(p2_name, p2_email, p2_total_games, p2_wins, p2_loses)
            player2.register_or_login_player()
    except:
        welcome()
        print(e)
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
    while True:
        name = input()
        if name == "r":
            return_to_num_players()
            break
        if validate_user_name(name):
            break
    return name

def validate_user_name(name):
    """
    Check if name is valid
    Must be between 2 and 12 letters long and only using a-z A-Z
    """
    try:
        if len(name) < 2 or len(name) > 12:
            new_line()
            print(Fore.RED + "Player name must be between 2 - 12 characters long.")
            print(Fore.RED + "Please try again.\n")
            new_line()

        elif not name.isalpha():
            new_line()
            print(Fore.RED + "Player name must only contain a-z or A-Z.\n")
            print(Fore.RED + "Please try again.\n")
            new_line()
                  
        else:
            return True
    except TypeError:
        return False

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
        new_line()
        print(Fore.RED + "\n" + str(e))
        print(Fore.RED + "Please try again.\n")
        new_line()
        
def validate_email_registered(email, registered, name):
    """
    Registers new players email
    Checks if existing player email is correct
    Registers or trys again if email is incorrect
    Returns email
    """
    if not registered:
        if check_is_email_registered(email):
            return incorrect_email_input(name, registered, email)
        else:
            new_line()
            print(Fore.BLUE + "Registering...")
            new_line()
            return email
    else:
        if check_is_email_registered(email):
            new_line()
            print(Fore.BLUE + "Logging in...")
            new_line()
            return email
        else:
            return incorrect_email_input(name, registered, email)
       
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

def incorrect_email_input(name, registered, email):
    """
    Called when email entered does not match any email in database
    Prints error message
    Asks the user to try again or register as a new email
    Returns a new email
    """
    new_line()
    if registered:
        print(Fore.RED + "Email address not found on database")
        return ask_incorrect_email_question1(name, registered)
    else:
        print(Fore.RED + "Email address found on database")
        return ask_incorrect_email_question2(name, registered, email)

def ask_incorrect_email_question1(name, registered):
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
                new_line()
                print(Fore.BLUE + "Creating a new user")
                new_line()
                return validate_email_registered(ask_player_email(name), False, name)
            break
        new_line()
        print(Fore.YELLOW + "Please input 1 or 2 for have you an try again or register or (r to return):")
        option_selected = input(options)

def ask_incorrect_email_question2(name, registered, email):
    """
    Asks user to try entering their email again
    or to sign in as a that player
    """
    new_line()
    print(Fore.YELLOW + "What would you like to do:")
    options = "1) Try entering email again\n2) Sign in as that player\n"
    option_selected = input(options)
    while True:
        if validate_incorrect_email_input(option_selected):
            if validate_incorrect_email_input(option_selected) == 1:
                new_line()
                print(Fore.BLUE + "Try again")
                new_line()
                return validate_email_registered(ask_player_email(name), registered, name)
            elif validate_registered_input(option_selected) == 2:
                new_line()
                print(Fore.BLUE + "Logging in")
                new_line()
                return email
            break
        new_line()
        print(Fore.YELLOW + "Please input 1 or 2 for have you an try again or sign in or (r to return):")
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

def get_worksheet_value(email, type):
    """ 
    Get the players value at the type and return it
    If user has not registered return 0
    """
    email_col = WORKSHEET.col_values(2)
    
    if type == "total_games":
        type_col = WORKSHEET.col_values(3)
    elif type == "wins":
        type_col = WORKSHEET.col_values(4)
    elif type == "loses":
        type_col = WORKSHEET.col_values(5)
    else:
        return 0

    if email in email_col:
        return int(type_col[email_col.index(email)])
    else:
        return 0
