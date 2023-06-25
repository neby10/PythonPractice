# Author: Nicholas Eby
# Date Created: June 15, 2023
# The Monty Hall Problem

import random

# basic monty hall problem
def basic_monty_hall_problem(games, switch):
    wins = 0
    losses = 0
    correct_door_count = [0, 0, 0]
    guess_door_count = [0, 0, 0]
    goat_door_count = [0, 0, 0]

    for i in range(games):
        # choose random door as PRIZE door
        door_correct = random.randint(1, 3)
        # update totals
        if door_correct == 1:
            correct_door_count[0] += 1
        elif door_correct == 2:
            correct_door_count[1] += 1
        else:
            correct_door_count[2] += 1

        # choose random door as GUESS door
        door_guess = random.randint(1, 3)
        # update totals
        if door_guess == 1:
            guess_door_count[0] += 1
        elif door_guess == 2:
            guess_door_count[1] += 1
        else:
            guess_door_count[2] += 1

        # show door that is not PRIZE door and not GUESS door i.e the GOAT door
        ## NOTE: The GOAT door final tally will be skewed do to assining values left to right
        door_goat = 1
        if door_guess == 1 or door_correct == 1:
            door_goat = 2
            if door_guess == 2 or door_correct == 2:
                door_goat = 3

        # update totals
        if door_goat == 1:
            goat_door_count[0] += 1
        elif door_goat == 2:
            goat_door_count[1] += 1
        else:
            goat_door_count[2] += 1

        if switch:
            # switch
            if door_correct != door_guess:
                wins += 1
            else:
                losses += 1
        else:
            # stay
            if door_correct == door_guess:
                wins += 1
            else:
                losses += 1
                
    print("\n      Doors         {}".format([1, 2, 3]))
    print("Correct Door Count: {}".format(correct_door_count))
    print("Guess Door Count: {}".format(guess_door_count))
    print("Goat Door Count: {}\n".format(goat_door_count))
    return (wins, losses)


num_games = 10000
always_switch = True
total_wins, total_losses = basic_monty_hall_problem(num_games, always_switch)
print("Strategy: {}\nTotal Games: {}\nWins: {}\nLosses: {}\n".format(always_switch, num_games, total_wins, total_losses))