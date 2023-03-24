import colorama
from colorama import Fore, Back, Style
import os
import time
import gspread
from google.oauth2.service_account import Credentials
from operator import itemgetter
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

def go_to_leaderboard():
    """
    Display leader board
    Ask user to rank players by name, total games, wins and loses 
    """
    try:
        sort_type = 3
        viewing_leaderboard = True
        while viewing_leaderboard:
            display.cls()
            display_leaderboard_heading()
            display_leaderboard_ranks(sort_type)
            print(" ")
            print(" ")
            print(" ")
            sort_type = ask_user_to_sort_ranks()
            if sort_type == "return":
                viewing_leaderboard = False
                mm.raise_return_to_main_menu()
                return viewing_leaderboard
    except:
        return mm.return_to_main_menu()

def ask_user_to_sort_ranks():
    """
    Asks the user to sort the ranks
    3 choices, by wins, by games, by loses 
    """
    print(Fore.YELLOW + "What would you like the leaderboard to be sorted by?:")
    options = "1) Wins\n2) Total Games\n3) Loses\n4) Return to main menu\n"
    option_selected = input(options)
    while True:
        validated_option = validate_sort_ranks_input(option_selected)
        if validated_option:
            return validated_option
            break
        display.new_line()
        print(Fore.YELLOW + "Please input 1 or 2 or 3 for sort or (4 to return):")
        option_selected = input(options)

def validate_sort_ranks_input(option):
    """
    Checks if the option is valid
    Returns index of column in worksheet
    Valid options are 1, 2, 3, 4
    and if anything else it returns an error
    """
    if option == "1" or option.lower() == "one":
        return 3
    elif option == "2" or option.lower() == "two":
        return 2
    elif option == "3" or option.lower() == "three":
        return 4
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
    
    heading = f"{top_bottom_of_leaderboard() + empty_leaderboard_line() + leaderboard_headings() + empty_leaderboard_line() + top_bottom_of_leaderboard()}"
    print(heading, end="")
    return heading


def top_bottom_of_leaderboard():
    """ 
    Returns f string
    """
    return f"{' ' * 16 + Fore.YELLOW + '=' * 87}\n"

def empty_leaderboard_line():
    """ 
    Returns f string
    """
    return f"{' ' * 16 + Fore.YELLOW + '|' + Fore.YELLOW + '|' + ' ' * 15 + Fore.YELLOW + '|' + ' ' * 15 + Fore.YELLOW + '|' + ' ' * 17 + Fore.YELLOW + '|' + ' ' * 15 + Fore.YELLOW + '|' + ' ' * 17 + Fore.YELLOW + '|' + Fore.YELLOW + '|'}\n"

def leaderboard_headings():
    """ 
    Returns f string
    """
    return f"{' ' * 16 + Fore.YELLOW + '|' + Fore.YELLOW + '|' + ' ' * 4 + Fore.CYAN + 'R A N K' + ' ' * 4 + Fore.YELLOW + '|' + ' ' * 4 + Fore.CYAN + 'N A M E' + ' ' * 4 + Fore.YELLOW + '|' + ' ' * 4 + Fore.CYAN + 'G A M E S' + ' ' * 4 + Fore.YELLOW + '|' + ' ' * 4 + Fore.CYAN + 'W I N S' + ' ' * 4 + Fore.YELLOW + '|' + ' ' * 4 + Fore.CYAN + 'L O S E S' + ' ' * 4 + Fore.YELLOW + '|' + Fore.YELLOW + '|'}\n"
    
def display_leaderboard_ranks(sort_type):
    """
    Display the leaderboard depending on the type to rank 
    Sorts the leaderboard entries depending on what type
    """
    leaderboard_rows = []

    leaderboard_data = get_leaderboard_data()
    sorted_leaderboard_data = sort_leaderboard_data(leaderboard_data, sort_type)
    for i, row in zip(range(1, len(sorted_leaderboard_data)+1), sorted_leaderboard_data):
        print(f"{empty_leaderboard_line() + leaderboard_data_line(row, i) + empty_leaderboard_line() + top_bottom_of_leaderboard()}", end="")
        row.insert(0, i)
        leaderboard_rows.append(row)

    return leaderboard_rows

def get_leaderboard_data():
    """
    Gets the leaderboard data from the worksheet
    Returns a 2d list of worksheet rows
    Removes the first row
    """
    data = WORKSHEET.get_all_values()
    data.pop(0)
    return data

def sort_leaderboard_data(data, sort_type):
    """
    Sorts the data depending on sort type 
    """
    for row in data:
        for i in range(len(row)):
            if i == 2 or i == 3 or i == 4:
                row[i] = int(row[i])

    sorted_data = sorted(data, key=itemgetter(sort_type), reverse=True) if (sort_type == 2 or sort_type == 3) else sorted(data, key=itemgetter(sort_type))
    
    for row in data:
        for i in range(len(row)):
            if i == 2 or i == 3 or i == 4:
                row[i] = str(row[i])

    return sorted_data

def leaderboard_data_line(row, i):
    """
    Returns an f string of correct data put in for row of leaderboard 
    """
    rank = format_leaderboard_rank_and_wins_and_name(str(i), "rank")
    name = format_leaderboard_rank_and_wins_and_name(row[0], "name")
    games = format_leaderboard_games_and_loses(row[2])
    wins = format_leaderboard_rank_and_wins_and_name(row[3], "wins")
    loses = format_leaderboard_games_and_loses(row[4])
    return f"{' ' * 16 + Fore.YELLOW + '|' + Fore.YELLOW + '|' + rank + Fore.YELLOW + '|' + name + Fore.YELLOW + '|' + games + Fore.YELLOW + '|' + wins + Fore.YELLOW + '|' + loses + Fore.YELLOW + '|' + Fore.YELLOW + '|'}\n"

def format_leaderboard_rank_and_wins_and_name(str, type):
    """ 
    Correctly formats rank or wins to place in leaderboard
    """
    length = len(str)
    if length == 1:
        return f"{Fore.WHITE + ' ' * 7 + str + ' ' * 7}"
    elif length == 2:
        return f"{Fore.WHITE + ' ' * 6 + str[0] + ' ' + str[1] + ' ' * 6}"
    elif length == 3:
        return f"{Fore.WHITE + ' ' * 5 + str[0] + ' ' + str[1] + ' ' + str[2] + ' ' * 5}"
    elif length == 4:
        return f"{Fore.WHITE + ' ' * 4 + str[0] + ' ' + str[1] + ' ' + str[2] + ' ' + str[3] + ' ' * 4}"
    else:
        if type == "name":
            if length == 5:
                return f"{Fore.WHITE + ' ' * 3 + str[0] + ' ' + str[1] + ' ' + str[2] + ' ' + str[3] + ' ' + str[4] + ' ' * 3}"
            elif length == 6:
                return f"{Fore.WHITE + ' ' * 2 + str[0] + ' ' + str[1] + ' ' + str[2] + ' ' + str[3] + ' ' + str[4] + ' ' + str[5] + ' ' * 2}"
            else:
                return f"{Fore.WHITE + ' ' * 3 + str[0:5] + '... ' + ' ' * 3}" 
        else:
            return f"{Fore.WHITE + ' ' * 3 + '9 9 9 9 +' + ' ' * 3}"

def format_leaderboard_games_and_loses(str):
    """ 
    Correctly formats games or loses to place in leaderboard
    """
    length = len(str)
    if length == 1:
        return f"{Fore.WHITE + ' ' * 8 + str + ' ' * 8}"
    elif length == 2:
        return f"{Fore.WHITE + ' ' * 7 + str[0] + ' ' + str[1] + ' ' * 7}"
    elif length == 3:
        return f"{Fore.WHITE + ' ' * 6 + str[0] + ' ' + str[1] + ' ' + str[2] + ' ' * 6}"
    elif length == 4:
        return f"{Fore.WHITE + ' ' * 5 + str[0] + ' ' + str[1] + ' ' + str[2] + ' ' + str[3] + ' ' * 5}"
    else:
        return f"{Fore.WHITE + ' ' * 4 + '1 0 0 0 +' + ' ' * 4}"
