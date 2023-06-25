# Nicholas Eby
# June 23, 2023
# Battle of the Kights mini challenge

# Imports
import random
from knight import Knight
from helper_functions import game_loop, game_introduction, choose_mode
from constants import MODE_VALUES

if __name__ == "__main__":

    # Initialize Knights
    player1 = Knight(True)
    player2 = Knight(False)

    # Introduction
    print("Welcome to Battle of the Knights!")
    mode = choose_mode()

    if mode == MODE_VALUES["ONE_PLAYER"]:
        player1 = Knight(True)
        player2 = Knight(False)
    elif mode == MODE_VALUES["TWO_PLAYER"]:
        player1 = Knight(True)
        player2 = Knight(True)

    game_introduction(mode, player1, player2)

    game_loop(player1, player2)


    # game loop
    # if mode == MODES["ONE_PLAYER"]:
    #     game_loop_one_player(player1, player2)
    # elif mode == MODES["TWO_PLAYER"]:
    #     game_loop_two_player(player1, player2)
