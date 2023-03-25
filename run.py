import sys
import os
parent_path = os.path\
    .abspath(os.path.join(os.path.dirname(__file__), os.pardir))
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
