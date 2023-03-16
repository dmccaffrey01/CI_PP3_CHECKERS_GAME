import colorama
from colorama import Fore, Back, Style
import os
from run import welcome, cls, new_line, typewriter
import time
from email_validator import validate_email, EmailNotValidError
import gspread
from google.oauth2.service_account import Credentials
import checkers
import checkers_engine

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

def main_menu_screen():
    """
    Display the main menu screen
    The user can select between three options
    To start the game, to view the game rules or to view the leaderboard
    """
    welcome()
    print(Fore.YELLOW + "Choose between the 4 options (eg. 1, 2, 3 or 4):")
    options = "1) Play game\n2) View game rules\n3) View leaderboard\n4) Exit Game\n"
    option_selected = input(options)
    new_line()
    while True:
        if validate_main_menu_selection(option_selected):
            main_menu_selection(validate_main_menu_selection(option_selected))
            return validate_main_menu_selection(option_selected)
            break
        welcome()
        print(Fore.YELLOW + "Please input (1, one) or (2, two) or (3, three) or (4, four):")
        option_selected = input(options)
        new_line()

def validate_main_menu_selection(option):
    """
    Checks if the option is valid
    Returns number in int if valid or else returns false 
    """
    if option == "1" or option.lower() == "one":
        return 1
    elif option == "2" or option.lower() == "two":
        return 2
    elif option == "3" or option.lower() == "three":
        return 3
    elif option == "4" or option.lower() == "four":
        return 3
    else:
        return False

def main_menu_selection(option):
    """ 
    Choose the path of the option selected
    """
    if option == 1:
        get_num_players()
    elif option == 2:
        pass
    elif option == 3:
        go_to_leaderboard()
    elif option == 4:
        exit_game()

    return option

def get_num_players():
    """
    Get the number of players playing the game
    """
    try:
        welcome()
        print(Fore.YELLOW + "Enter r to return")
        print(Fore.YELLOW + "How many players?(1 or 2 or 0)")
        options = "1) One\n2) Two\n3) None (CPU vs CPU)\n"
        option_selected = input(options)
        new_line()
        while True:
            num = validate_num_players(option_selected)
            if num:
                if num == 3:
                    start_cpu_game(0)
                else:
                    log_in_players(num)
                return num
                break
            welcome()
            print(Fore.YELLOW + "Please input (1, one) or (2, two) or (3, three):")
            option_selected = input(options)
            new_line()
    except:
        welcome()
        print(Fore.YELLOW + "Returning to main menu...")
        time.sleep(1)
        main_menu_screen()
           

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
    elif option == "3" or option.lower() == "three":
        return 3
    elif option == "r":
        return_to_main_menu()
        return 4
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
            return [self.name, self.email]
        else:
            self.add_player_to_database()
            return [self.name, self.email, self.total_games, self.wins, self.loses]

    def update_database_value(self, col, value, email):
        """
        Updates the name in the database 
        """
        if col == "name":
            col = 1
        elif col == "email":
            col = 2
        elif col == "total_games":
            col = 3
        elif col == "wins":
            col = 4
        elif col == "loses":
            col = 5
        
        row = WORKSHEET.col_values(2).index(email) + 1
        

        WORKSHEET.update_cell(row, col, value)
        return [row, col]

    def add_player_to_database(self):
        """
        Add player to the database
        """
        row = [self.name, self.email, self.total_games, self.wins, self.loses]
        WORKSHEET.append_row(row)
        return row

    def display_player_stats(self):
        """
        Displayer the players stats 
        """
        text = f"{Fore.CYAN + 'Name: ' + Fore.WHITE + self.name + Fore.CYAN + '   Email: ' + Fore.WHITE + self.email + Fore.CYAN + '   Total Games: ' + Fore.WHITE + str(self.total_games) + Fore.CYAN + '   Wins: ' + Fore.WHITE + str(self.wins) + Fore.CYAN + '   Loses: ' + Fore.WHITE + str(self.loses)}"
        return text
        
def start_cpu_game(num):
    """
    Starts a game cpu playing agains cpu if user selected 0 players 
    """
    cpu_difficulty_1 = ask_cpu_difficulty()
    cpu_difficulty_2 = ask_cpu_difficulty()
    start_checkers_game(cpu_difficulty_1, cpu_difficulty_2, num)
    return [cpu_difficulty_1, cpu_difficulty_2]

def log_in_players(num):
    """
    Asks the user for their name and if they have played before
    If they haven't then the program will register them
    If they have they will proceed to main menu
    Create a player instance of player class for each player
    """
    welcome()
    try:
        if num == 1 or num == 2:    
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

            if num == 1:
                cpu_difficulty = ask_cpu_difficulty()
                start_checkers_game(player1, cpu_difficulty, num)
                return [player1.display_player_stats()]

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
            
            start_checkers_game(player1, player2, num)
            return [player1.display_player_stats(), player2.display_player_stats()]  
    except:
        welcome()
        print(Fore.YELLOW + "Returning to main menu...")
        time.sleep(1)
        main_menu_screen()
        
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
        return_to_main_menu()
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
        name = input("Your Name: ")
        if name == "r":
            return_to_main_menu()
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
        if len(name) < 1 or len(name) > 12:
            new_line()
            print(Fore.RED + "Player name must be between 1 - 12 characters long.")
            print(Fore.RED + "Please try again.\n")
            new_line()

        elif not name.isalpha():
            new_line()
            print(Fore.RED + "Player name must only contain a-z or A-Z.\n")
            print(Fore.RED + "Please try again.")
            new_line()
                  
        else:
            return True
    except TypeError:
        return False

def return_to_main_menu():
    """ 
    Raises an exception
    """
    raise Exception("Return to main menu")

def ask_player_email(name):
    """
    Asks the user for their email
    Returns to number of players if r is pressed
    Checks if email is valid 
    """
    print(Fore.YELLOW + "Enter r to return")
    print(Fore.YELLOW + f"Enter email of {name}:") 
    while True:
        email = input("Email: ")
        if email == "r":
            return_to_main_menu()
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
        return_to_main_menu()
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

def ask_cpu_difficulty():
    """
    Asks the user what level of difficulty to set the computer
    3 options beginner, novice, expert 
    """
    print(Fore.YELLOW + "What level of difficulty would you like the cpu to be?:")
    options = "1) Beginner\n2) Novice\n3) Expert\n"
    option_selected = input(options)
    while True:
        if validate_cpu_difficulty_input(option_selected):
            return validate_cpu_difficulty_input(option_selected)
            break
        new_line()
        print(Fore.YELLOW + "Please input 1 or 2 or 3 for cpu difficulty or (r to return):")
        option_selected = input(options)

def validate_cpu_difficulty_input(option):
    """
    Checks if the option is valid
    If it is a 1 or 2 it returns 1 or 2
    and if anything else it returns an error
    """
    if option == "1" or option.lower() == "one":
        return 1
    elif option == "2" or option.lower() == "two":
        return 2
    elif option == "3" or option.lower() == "three":
        return 3
    elif option == "r":
        return_to_main_menu()
        return 4
    else:
        return False

def start_checkers_game(player1, player2, num):
    """ 
    Starts the checkers game
    """
    checkers.start_game(player1, player2, num)

def go_to_leaderboard():
    """
    Display leader board
    Ask user to rank players by name, total games, wins and loses 
    """
    try:
        sort_type = "wins"
        viewing_leaderboard = True
        while viewing_leaderboard:
            cls()
            display_leaderboard_heading()
            display_leaderboard_ranks(sort_type)
            sort_type = ask_user_to_sort_ranks()
            if sort_type == "return":
                viewing_leaderboard = False
                return_to_main_menu()
    except:
        welcome()
        print(Fore.YELLOW + "Returning to main menu...")
        time.sleep(1)
        main_menu_screen()

def ask_user_to_sort_ranks():
    """
    Asks the user to sort the ranks
    3 choices, by wins, by games, by loses 
    """
    print(Fore.YELLOW + "What would you like the leaderboard to be sorted by?:")
    options = "1) Wins\n2) Total Games\n3) Loses\n4) Return to main menu"
    option_selected = input(options)
    while True:
        if validate_sort_ranks_input(option_selected):
            return validate_sort_ranks_input(option_selected)
            break
        new_line()
        print(Fore.YELLOW + "Please input 1 or 2 or 3 for cpu difficulty or (r to return):")
        option_selected = input(options)

def validate_sort_ranks_input(option):
    """
    Checks if the option is valid
    If it is a 1 or 2 it returns 1 or 2
    and if anything else it returns an error
    """
    if option == "1" or option.lower() == "one":
        return "wins"
    elif option == "2" or option.lower() == "two":
        return "games"
    elif option == "3" or option.lower() == "three":
        return "loses"
    elif option == "r" or option == "4":
        return "return"
    else:
        return False

def display_leaderboard_heading():
    """
    Displays the leaderboard heading 
    """
    for i in range(5):
        print(" ")
    
    print(top_bottom_of_leaderboard())
    print(empty_leaderboard_line())
    print(leaderboard_headings())
    print(empty_leaderboard_line())
    print(top_bottom_of_leaderboard())


def top_bottom_of_leaderboard():
    """ 
    Returns f string
    """
    return f"{' ' * 19 + Fore.YELLOW + '=' * 87}"

def empty_leaderboard_line():
    """ 
    Returns f string
    """
    return f"{' ' * 19 + Fore.YELLOW + '|' + Fore.YELLOW + '|' + ' ' * 15 + Fore.YELLOW + '|' + ' ' * 15 + Fore.YELLOW + '|' + ' ' * 17 + Fore.YELLOW + '|' + ' ' * 15 + Fore.YELLOW + '|' + ' ' * 17 + Fore.YELLOW + '|' + Fore.YELLOW + '|'}"

def leaderboard_headings():
    """ 
    Returns f string
    """
    return f"{' ' * 19 + Fore.YELLOW + '|' + Fore.YELLOW + '|' + ' ' * 4 + Fore.YELLOW + 'R A N K' + ' ' * 4 + Fore.YELLOW + '|' + ' ' * 4 + Fore.YELLOW + 'N A M E' + ' ' * 4 + Fore.YELLOW + '|' + ' ' * 4 + Fore.YELLOW + 'G A M E S' + ' ' * 4 + Fore.YELLOW + '|' + ' ' * 4 + Fore.YELLOW + 'W I N S' + ' ' * 4 + Fore.YELLOW + '|' + ' ' * 4 + Fore.YELLOW + 'L O S E S' + ' ' * 4 + Fore.YELLOW + '|' + Fore.YELLOW + '|'}"
    
def display_leaderboard_ranks(sort_type):
    """
    Display the leaderboard depending on the type to rank 
    Sorts the leaderboard entries depending on what type
    """
    leaderboard_data = get_leaderboard_data()
    sorted_leaderboard_data = sort_leaderboard_data(leaderboard_data, sort_type)
    

def get_leaderboard_data():
    """
    Gets the leaderboard data from the worksheet
    Returns a 2d list of worksheet rows
    """
    return WORKSHEET.get_all_values()

def exit_game():
    """ 
    System exits the game
    """
    typewriter(f"""{' ' * 24}T h a n k   y o u   f o r   p l a y i n g\t\n
    {' ' * 20}H a v e   a   g o o d   d a y !\t\n""")
    sys.exit()