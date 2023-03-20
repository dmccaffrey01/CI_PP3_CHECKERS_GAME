import time
import os
import colorama
from colorama import Fore, Back, Style
import sys

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
    print(Fore.YELLOW + "=" * 80)
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

def typewriter(str):
    """
    Typewriter to print message out in unique way 
    """
    for c in str:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)