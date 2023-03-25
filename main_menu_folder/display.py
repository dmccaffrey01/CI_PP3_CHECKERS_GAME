import time
import os
import colorama
from colorama import Fore, Back, Style
import sys

# Initialize colorama
colorama.init(autoreset=True)


def cls():
    """
    Clear the console
    """
    os.system("cls" if os.name == "nt" else "clear")
    return "clear"


def new_line():
    """
    Print '-' lines to separate messages
    """
    print(" ")
    print(Fore.YELLOW + "=" * 80)
    print(" ")
    return "new line"


def welcome():
    """
    Display welcome screen
    """
    cls()
    print("                            " +
          Fore.BLUE + "Welcome to:")
    print(" ")
    print("                            " +
          Fore.RED + r"  ____  __   __  _____   ____  __   ___ _____  " +
          "______   _______ ")
    print("                            " +
          Fore.GREEN + r" / __ \|  | |  ||  ___| / __ \|  | /  /|  ___|" +
          r"/   _  \ |  _____|")
    print("                            " +
          Fore.RED + r"| /  \/|  |_|  || |___ | /  \/|  |/  / | |___ |  " +
          r"|_| / | |_____ ")
    print("                            " +
          Fore.GREEN + r"| |    |   _   ||  ___|| |    |     |  |  " +
          r"___||     |  |_____  |")
    print("                            " +
          Fore.RED + r"| \__/\|  | |  || |___ | \__/\|  |\  \ | |___ |  " +
          r"|\  \  _____| |")
    print("                            " +
          Fore.GREEN + r" \____/|__| |__||_____| \____/|__| \__\|_____||__| " +
          r"\__\|_______|")
    print(" ")
    print(" ")
    print("                            " +
          Fore.BLUE + "                                            " +
          "for 1 and 2 players")
    print(" ")
    print(" ")
    return "welcome"


def typewriter(str):
    """
    Typewriter to print message out in unique way
    """
    for c in str:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.03)

    return "typewriter"
