import sys
import os
# Get the parent path of the current script
parent_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
# Add the parent path to the system path
sys.path.append(parent_path)
sys.path.insert(0, 'main_menu_folder/')
import main_menu as mm 


def main():
    """
    Run all program functions
    """
    mm.main_menu_screen()

if __name__ == "__main__":
    main()
