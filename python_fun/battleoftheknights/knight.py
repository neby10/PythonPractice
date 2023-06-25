# Nicholas Eby
# June 23, 2023
# Battle of the Kights: Knight Class

import random
from constants import NAMES, ACTIONS


# class Player():
#     def __init__(self) -> None:
#         self.health = 100
#         self.action = ""

#     def get_health(self):
#         return self.health

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
        self.last_actions = ["", ""]

    def get_valid_input(self, action_list, message) -> str:
        user_choice = ""
        while user_choice not in action_list:
            user_choice = input(message)
            user_choice = user_choice.upper()
        return user_choice

    def get_action_choice(self):
        if self.is_player:

            # make a copy of actions
            actions = list(ACTIONS)

            print("Player Turn: {}".format(self.name))

            # get valid input from user
            choice = self.get_valid_input(actions, "Choose 'a' to Attack, 'd' to Defend, or 'r' to Rest: ")

            # check for third action in a row
            if choice == self.last_actions[0] and choice == self.last_actions[1]:
                actions.remove(choice)
                choice = self.get_valid_input(actions, "You cannot enter the same action three times in a row. Please try another action.")

            # update action and last_actions
            self.action = choice
            self.last_actions[0], self.last_actions[1] = choice, self.last_actions[0]
        else:
            self.action = random.choice(ACTIONS)

    def get_defense(self) -> int:
        return random.randint(5, 10)

    def get_attack(self) -> int:
        return random.randint(5, 25)
    
    def apply_damage(self, damage) -> None:
        self.health -= damage

    def apply_rest(self) -> None:
        self.health += 10
        if self.health > 100:
            self.health = 100