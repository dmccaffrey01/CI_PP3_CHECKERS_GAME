import time
import os
import colorama
from colorama import Fore, Back, Style
import main_menu as mm

#Initialize colorama
colorama.init(autoreset=True)


def cls():
    """
    Clear the console
    """
    os.system("cls" if os.name == "nt" else "clear")

def new_line():
    """
    Print '-' lines to separate messages
    """
    print(" ")
    print("- "*30)
    print(" ")

def welcome():
    """
    Display welcome screen
    """
    cls()
    print(Fore.BLUE + "Welcome to:")
    print(" ")
    print(Fore.RED + Style.BRIGHT + "  ____  __   __  _____   ____  __   ___ _____  ______   _______ ")
    print(Fore.GREEN + Style.BRIGHT + " / __ \|  | |  ||  ___| / __ \|  | /  /|  ___|/   _  \ |  _____|")
    print(Fore.RED + Style.BRIGHT + "| /  \/|  |_|  || |___ | /  \/|  |/  / | |___ |  |_| / | |_____ ")
    print(Fore.GREEN + Style.BRIGHT + "| |    |   _   ||  ___|| |    |     |  |  ___||     |  |_____  |")
    print(Fore.RED + Style.BRIGHT + "| \__/\|  | |  || |___ | \__/\|  |\  \ | |___ |  |\  \  _____| |")
    print(Fore.GREEN + Style.BRIGHT + " \____/|__| |__||_____| \____/|__| \__\|_____||__| \__\|_______|")
    print(" ")
    print(" ")
    print(Fore.BLUE + "                                            for 1 and 2 players")
    print(" ")
    print(" ")

def update_num_players():
    global num_players
    num_players = mm.get_num_players()
    return num_players

def main():
    """
    Run all program functions
    """
    # mm.main_menu_screen()
    mm.start_checkers_game("test")
    

if __name__ == "__main__":
    main()
