# Nicholas Eby
# June 23, 2023
# Battle of the Kights mini challenge


# TODO
    # Knight Class
        # methods, attributes
    # Knights display functions or methods images...
    # Game Loop
        # randomly choose action, player chooses action
        # Display battle scene
        # update health
        # display names and health
        # check for health at or below 0 for both players
            # call end game
        # repeat
    # End Game
        # end scene + winner

# Imports
import random
from constants import NAMES, ACTION_VALUES, ACTIONS

# Knight Class
class Knight:
    def __init__(self, is_player) -> None:
        if is_player:
            self.name = "Sir {} the {}".format(random.choice(NAMES["KNIGHT_FIRST_NAMES"]), random.choice(NAMES["KNIGHT_LAST_NAMES"]))
        else:
            self.name = "{} the {}".format(random.choice(NAMES["VILLAIN_FIRST_NAMES"]), random.choice(NAMES["VILLAIN_LAST_NAMES"]))

        self.health = 100
        self.action = ""
        self.is_player = is_player

    def get_action_choice(self):
        if self.is_player:
            user_choice = ""
            while user_choice.upper() not in ACTIONS:
                user_choice = input("Choose 'a' to Attack, 'd' to Defend, or 'r' to Rest: ")
            user_choice = user_choice.upper()
            self.action = user_choice
        else:
            self.action = random.choice(ACTIONS)

    def get_defense(self) -> int:
        return 0

    def get_attack(self) -> int:
        return random.randint(5, 25)
    
    def get_health(self) -> int:
        return self.health
    
    def apply_damage(self, damage) -> None:
        self.health -= damage

    def apply_rest(self) -> None:
        self.health += 10
        if self.health > 100:
            self.health = 100


# Initialize Game

# Game Loop
def game_loop(knight, villain):
    while True:
        # LATER DISPLAY FOR EACH ROUND

        # get action each player
        knight.get_action_choice()
        villain.get_action_choice()
        print("Knight Choice: ", knight.action)
        print("Villain Choice: ", villain.action)

        # handle action
        if knight.action == ACTION_VALUES['ATTACK'] and villain.action == ACTION_VALUES['ATTACK']:
            knight_melee = knight.get_attack()
            villain_melee = villain.get_attack()
            knight.apply_damage(villain_melee)
            villain.apply_damage(knight_melee)
        elif knight.action == ACTION_VALUES['DEFEND'] and villain.action == ACTION_VALUES['DEFEND']:
            pass # do nothing
        elif knight.action == ACTION_VALUES['REST'] and villain.action == ACTION_VALUES['REST']:
            knight.apply_rest()
            villain.apply_rest()
        elif knight.action == ACTION_VALUES['ATTACK'] and villain.action == ACTION_VALUES['DEFEND']:
            pass # do nothing
        elif knight.action == ACTION_VALUES['DEFEND'] and villain.action == ACTION_VALUES['ATTACK']:
            pass # do nothing
        elif knight.action == ACTION_VALUES['ATTACK'] and villain.action == ACTION_VALUES['REST']:
            villain.apply_rest()
            atk = knight.get_attack()
            villain.apply_damage(atk)
        elif knight.action == ACTION_VALUES['REST'] and villain.action == ACTION_VALUES['ATTACK']:
            knight.apply_rest()
            atk = villain.get_attack()
            knight.apply_damage(atk)
        elif knight.action == ACTION_VALUES['DEFEND'] and villain.action == ACTION_VALUES['REST']:
            villain.apply_rest()
        elif knight.action == ACTION_VALUES['REST'] and villain.action == ACTION_VALUES['DEFEND']:
            knight.apply_rest()
        else:
            print("error")
        

        # display results
        print("{} Health = {}".format(knight.name, knight.health))
        print("{} Health = {}".format(villain.name, villain.health))

        if knight.health <= 0:
            print("{} dies. {} wins the game!".format(knight.name, villain.name))
            break
        if villain.health <= 0:
            print("{} dies. {} wins the game!".format(villain.name, knight.name))
            break

        # next round

    

# End Game


if __name__ == "__main__":

    # Initialize Knights
    player1 = Knight(True)
    player2 = Knight(False)

    # Introduction
    print("Welcome to Battle of the Knights!")
    print("You are {}.".format(player1.name))
    print("You're opponent is {}.".format(player2.name))

    # game loop
    game_loop(player1, player2)