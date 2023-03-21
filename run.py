import main_menu as mm 
import checkers_engine as ce
import feature_testing as ft

def main():
    """
    Run all program functions
    """
    #mm.main_menu_screen()
    gs = ce.GameState(ft.board_states["test board 1"])
    print(gs.get_movable_pieces("white"))
    

if __name__ == "__main__":
    main()
