import colorama
from colorama import Fore, Back, Style
import os
import time
import sys
parent_path = os.path.abspath(os.path
                                .join(os.path.dirname(__file__), os.pardir))
sys.path.append(parent_path)
sys.path.insert(0, 'main_menu_folder/')
import display
import main_menu as mm

# Initialize colorama
colorama.init(autoreset=True)


def display_game_rules():
    """
    Displays the game rules
    """
    display.cls()
    for i in range(3):
        print(" ")

    print(f"{game_rules_heading() + game_rules_top_and_bottom_line()}" +
          f"{game_rules_empty_line() + format_game_rules_lines()}" +
          f"{game_rules_empty_line() + game_rules_top_and_bottom_line()}")

    if ask_user_to_exit_game_rules():
        return mm.return_to_main_menu()


def ask_user_to_exit_game_rules():
    """
    Asks the user to return to the main menu
    """
    print(Fore.YELLOW + "Press 1 or r to return to the main menu:")
    options = "1) Return to the main menu\n"
    option_selected = input(options)
    while True:
        validated_option = validate_exit_game_rules_input(option_selected)
        if validated_option:
            return validated_option
            break
        display.new_line()
        print(Fore.YELLOW + "Please input 1 or r:")
        option_selected = input(options)


def validate_exit_game_rules_input(option):
    """
    Validates if input is 1 or r
    """
    if option == "1" or option.lower() == "one" or option == "r":
        return "return"
    else:
        return False


def game_rules_heading():
    """
    Returns f string of game rules heading
    """
    return f"{' ' * 46 + Fore.CYAN + 'G A M E   R U L E S'}\n"


def get_game_rules_lines():
    """
    Returns the lines of strings in a list
    """
    file = open("game_rules.txt", "r")
    lines = file.readlines()
    formatted_lines = []
    for line in lines:
        formatted_lines.append(line.strip())

    file.close()
    return formatted_lines


def format_game_rules_lines():
    """
    Returns f string of lines put together
    """
    formatted_line = f""
    lines = get_game_rules_lines()
    for line in lines:
        formatted_line += format_game_rule_line(line)
    return formatted_line


def format_game_rule_line(line):
    """
    Return f string of line
    """
    if line == "nl":
        return game_rules_empty_line()
    else:
        return f"{game_rules_start_of_line() + Fore.WHITE + line}" \
               f"{+ ' ' * (100 - len(line)) + Fore.YELLOW + '|'}\n"


def game_rules_top_and_bottom_line():
    """
    Returns f string
    """
    return f"{' ' * 6 + Fore.YELLOW + '=' * 106}\n"


def game_rules_empty_line():
    """
    Returns f string
    """
    return f"{' ' * 6 + Fore.YELLOW + '|' + ' ' * 104 + Fore.YELLOW + '|'}\n"


def game_rules_start_of_line():
    """
    Returns f string
    """
    return f"{' ' * 6 + Fore.YELLOW + '|' + ' ' * 4}"
