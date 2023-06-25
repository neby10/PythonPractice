# Nicholas Eby
# June 23, 2023
# Battle of the Kights: Helper functions

from constants import ACTION_VALUES, MODES

def choose_mode() -> str:
    mode = ""
    while mode not in MODES:
        mode = input("Please enter one of the following modes in order to play: {}:".format(MODES))
    return mode

def game_introduction(mode, player1, player2):
    if mode == "one":
        print("You are playing single player. You're name is {}. You're opponent's name is {}.".format(player1.name, player2.name))
    elif mode == "two":
        print("You are playing two player. You're name is {}. You're opponent's name is {}.".format(player1.name, player2.name))
    
    print("You can Attack, Defend, or Rest on each turn.")
    print("You cannot perform the same action more than twice in a row.")
    print("------------------------------")

def display_battle_scene(p1_action, p2_action) -> None:
    # top line
    if p1_action == ACTION_VALUES["ATTACK"]:
        print(" O  /", end="")
    elif p1_action == ACTION_VALUES["DEFEND"]:
        print(" O | ", end="")
    elif p1_action == ACTION_VALUES["REST"]:
        print(" O   ", end="")

    print("  ", end="")

    if p2_action == ACTION_VALUES["ATTACK"]:
        print("\\  O ")
    elif p2_action == ACTION_VALUES["DEFEND"]:
        print(" | O ")
    elif p2_action == ACTION_VALUES["REST"]:
        print("   O ")

    # middle line
    if p1_action == ACTION_VALUES["ATTACK"]:
        print("-+-/ ", end="")
    elif p1_action == ACTION_VALUES["DEFEND"]:
        print("-+-| ", end="")
    elif p1_action == ACTION_VALUES["REST"]:
        print("-+-  ", end="")

    print("  ", end="")

    if p2_action == ACTION_VALUES["ATTACK"]:
        print(" \-+-")
    elif p2_action == ACTION_VALUES["DEFEND"]:
        print(" |-+-")
    elif p2_action == ACTION_VALUES["REST"]:
        print("  -+-")

    # bottom line
    if p1_action == ACTION_VALUES["ATTACK"]:
        print("/ \\  ", end="")
    elif p1_action == ACTION_VALUES["DEFEND"]:
        print("/ \\| ", end="")
    elif p1_action == ACTION_VALUES["REST"]:
        print("/ \\  ", end="")

    print("  ", end="")

    if p2_action == ACTION_VALUES["ATTACK"]:
        print("  / \\")
    elif p2_action == ACTION_VALUES["DEFEND"]:
        print(" |/ \\")
    elif p2_action == ACTION_VALUES["REST"]:
        print("  / \\")

def display_end_scene(is_left_player) -> None:
    """Parameter: boolean value"""
    if is_left_player:
        print("\\O/         ")
        print(" +          ")
        print("/ \\    /-+-O")
    else:
        print("         \\O/")
        print("          + ")
        print("O-+-\\    / \\")

# Game Loops
# def game_loop_one_player(knight1, knight2) -> None:
#     print("Game Loop 1")
#     while True:
#         break

# def game_loop_two_player(knight1, knight2) -> None:
#     print("Game Loop 2")
#     while True:
#         knight1.get_action_choice()
#         knight2.get_action_choice()
#         print("Knight1 Choice: ", knight1.action)
#         print("Knight2 Choice: ", knight2.action)
#         break

def handle_action(knight1, knight2) -> None:
    # Attack > Rest, Rest > Defend, Defend > Attack
    if knight1.action == ACTION_VALUES['ATTACK'] and knight2.action == ACTION_VALUES['ATTACK']:
        knight1_melee = knight1.get_attack()
        knight2_melee = knight2.get_attack()
        knight1.apply_damage(knight2_melee)
        knight2.apply_damage(knight1_melee)
    elif knight1.action == ACTION_VALUES['DEFEND'] and knight2.action == ACTION_VALUES['DEFEND']:
        pass # do nothing
    elif knight1.action == ACTION_VALUES['REST'] and knight2.action == ACTION_VALUES['REST']:
        knight1.apply_rest()
        knight2.apply_rest()
    elif knight1.action == ACTION_VALUES['ATTACK'] and knight2.action == ACTION_VALUES['DEFEND']:
        # no damage dealt by attack but there is a counter attack
        counter_damage = knight2.get_defense()
        knight1.apply_damage(counter_damage)
    elif knight1.action == ACTION_VALUES['DEFEND'] and knight2.action == ACTION_VALUES['ATTACK']:
        counter_damage = knight1.get_defense()
        knight2.apply_damage(counter_damage)
    elif knight1.action == ACTION_VALUES['ATTACK'] and knight2.action == ACTION_VALUES['REST']:
        knight2.apply_rest()
        atk = knight1.get_attack()
        knight2.apply_damage(atk)
    elif knight1.action == ACTION_VALUES['REST'] and knight2.action == ACTION_VALUES['ATTACK']:
        knight1.apply_rest()
        atk = knight2.get_attack()
        knight1.apply_damage(atk)
    elif knight1.action == ACTION_VALUES['DEFEND'] and knight2.action == ACTION_VALUES['REST']:
        knight2.apply_rest()
    elif knight1.action == ACTION_VALUES['REST'] and knight2.action == ACTION_VALUES['DEFEND']:
        knight1.apply_rest()
    else:
        print("error")

def game_loop(knight1, knight2) -> None:
    while True:
        # get action each player
        knight1.get_action_choice()
        knight2.get_action_choice()
        print("Knight1: {} | Knight2: {}".format(knight1.action, knight2.action))

        # Display battle scene
        display_battle_scene(knight1.action, knight2.action)

        # handle action
        handle_action(knight1, knight2)
        
        # display results
        print("{} Health = {}".format(knight1.name, knight1.health))
        print("{} Health = {}".format(knight2.name, knight2.health))

        print("------------------------------")

        if knight1.health <= 0:
            print("{} dies. {} wins the game!".format(knight1.name, knight2.name))
            display_end_scene(False)
            break
        if knight2.health <= 0:
            print("{} dies. {} wins the game!".format(knight2.name, knight1.name))
            display_end_scene(True)
            break