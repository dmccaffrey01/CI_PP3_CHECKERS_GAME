import sys
import time
import os
import colorama
from colorama import Fore, Back, Style

#Initialize colorama
colorama.init(autoreset=True)

def welcome():
    """
    Display welcome screen
    """
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
    time.sleep(1)

def cls():
    """
    Clear the console
    """
    os.system("cls" if os.name == "nt" else "clear")

def main():
    """
    Run all program functions
    """
    welcome()
    

if __name__ == "__main__":
    main()