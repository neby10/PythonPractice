# developer: Nick Eby
# Date: April 18
# very sloppy but i think it works

import random, sys

def round_intro():
    print("     ____      ____      ____       ")
    print("    |    |    |    |    |    |      ")
    print("    |    |    |    |    |    |      ")
    print("    |____|    |____|    |____|      ")
    print("    Door 1    Door 2    Door 3      ")
    print("\n\nA prize is behind one of these doors. Your goal is to pick the correct door. Choose wisely.")

def door_1():
    print("You choose Door 1")
    print("     ____      ____      ____       ")
    print("    |    |    |    |    |    |      ")
    print(" -> |    | <- |    |    |    |      ")
    print("    |____|    |____|    |____|      ")
    print("    DOOR 1    Door 2    Door 3      ")

def door_2():
    print("You choose Door 2")
    print("     ____      ____      ____       ")
    print("    |    |    |    |    |    |      ")
    print("    |    | -> |    | <- |    |      ")
    print("    |____|    |____|    |____|      ")
    print("    Door 1    DOOR 2    Door 3      ")

def door_3():
    print("You choose Door 3")
    print("     ____      ____      ____       ")
    print("    |    |    |    |    |    |      ")
    print("    |    |    |    | -> |    | <-   ")
    print("    |____|    |____|    |____|      ")
    print("    Door 1    Door 2    DOOR 3      ")

def not_door_1():
    print("The correct door is NOT Door 1.")
    print("     ____      ____      ____       ")
    print("    | \/ |    |    |    |    |      ")
    print("    | /\ |    |    |    |    |      ")
    print("    |____|    |____|    |____|      ")
    print("    Door 1    Door 2    Door 3      ")

def not_door_2():
    print("The correct door is NOT Door 2.")
    print("     ____      ____      ____       ")
    print("    |    |    | \/ |    |    |      ")
    print("    |    |    | /\ |    |    |      ")
    print("    |____|    |____|    |____|      ")
    print("    Door 1    Door 2    Door 3      ")

def not_door_3():
    print("The correct door is NOT Door 3.")
    print("     ____      ____      ____       ")
    print("    |    |    |    |    | \/ |      ")
    print("    |    |    |    |    | /\ |      ")
    print("    |____|    |____|    |____|      ")
    print("    Door 1    Door 2    Door 3      ")

print("\n\nWelcome to")
print("_________          ___ ")
print("    |     |    |  |    ")
print("    |     |----|  |--  ")
print("    |     |    |  |___ ")
print("                       ")
print("                    ___             ______  \\  //        ")
print("        ||\  /||  ||   ||  ||\  ||    ||     \\//         ")
print("        || \/ ||  ||   ||  || \ ||    ||      ||          ")
print("        ||    ||  ||___||  ||  \||    ||      ||          ")
print("                         ____                           __             |    |           ")
print("           |||   |||  |||    |||  |||      |||         |  \   __  ___  |__  |   __      ")
print("           |||___|||  |||____|||  |||      |||         |__/ |/   |   | |  | |  |__| |\/|")
print("           |||   |||  |||    |||  |||      |||         |    |    |___| |__| |_ |___ |  |")
print("           |||   |||  |||    |||  |||_____ |||_____                                     ")
print("        /    _                  _____          ")
print("       /                  |   /\  |   __    __ ")
print("      /____  |  |\/| |  | |  |__| |  |  | |/   ")
print("          /  |  |  | |__| |_ |  | |  |__| |    ")
print("         /                                     ")
print("        /               With Python        \n\n")

stay_count = 0
switch_count = 0
win_count = 0
lose_count = 0

while True:
    round_intro()

    door_list = ["1", "2", "3"]
    correct_door = random.choice(door_list)
    incorrect_doors = door_list
    incorrect_doors.remove(correct_door)

    user_choice = "0"
    while user_choice not in ["1", "2", "3"]:
        user_choice = input("Type the number of the door that you are guessing and press enter: ")

    if user_choice == "1":
        door_1()
    elif user_choice == "2":
        door_2()
    elif user_choice == "3":
        door_3()

    print("Now I will reveal a door that is not the correct door.")

    wrong = 2
    right = 2

    if user_choice == correct_door:
        wrong_door = random.choice(incorrect_doors)
        incorrect_doors.remove(wrong_door)
        if wrong_door == "1":
            not_door_1()
        elif wrong_door == "2":
            not_door_2()
        elif wrong_door == "3":
            not_door_3()
        print("Would you like to stay with Door " + user_choice + ", or would you like to switch to Door " + incorrect_doors[0] + "?")
        print("If you would like to stay, press x then enter. If you would like to switch, press y then enter.")
        user_input = input(": ")
        if user_input == "x":
            print("You decide to stay with Door " + user_choice + ".")
            stay_count += 1
            win_count += 1
            right = 0
        elif user_input == "y":
            print("You decide to switch to Door " + incorrect_doors[0] + ".")
            switch_count += 1
            lose_count += 1
            wrong = 0
    elif user_choice in incorrect_doors:
        incorrect_doors.remove(user_choice)
        if "1" in incorrect_doors:
            not_door_1()
        elif "2" in incorrect_doors:
            not_door_2()
        elif "3" in incorrect_doors:
            not_door_3()
        print("Would you like to stay with Door " + user_choice + ", or would you like to switch to Door " + correct_door + "?")
        print("If you would like to stay, press x then enter. If you would like to switch, press y then enter. Press anything else to quit")
        user_input = input(": ")
        if user_input == "x":
            print("You decide to stay with Door " + user_choice + ".")
            stay_count += 1
            lose_count += 1
            wrong = 1
        elif user_input == "y":
            print("You decide to switch to Door " + correct_door + ".")
            switch_count += 1
            win_count += 1
            right = 1
        else:
            sys.exit()

    print("The correct door is...")
    print("DOOR {}".format(correct_door))
    print("  ")
    
    if wrong == 0:
        print("You were wrong. You should have stayed.")
    elif wrong == 1:
        print("You were wrong. You should have switched.")
    elif right == 0:
        print("You were right. Good choice to stay.")
    elif right == 1:
        print("You were right. Good choice to switch.")

    print("\nHere are your results:\n")
    print("Stay % = " + str((stay_count / (switch_count + stay_count)) * 100) + "%")
    print("Switch % = " + str((switch_count / (stay_count + switch_count)) * 100) + "%")
    print("Total Stays = " + str(stay_count))
    print("Total Switches = " + str(switch_count))
    print("  ")
    print("Win % = " + str((win_count / (lose_count + win_count)) * 100) + "%")
    print("Total Wins = " + str(win_count))
    print("Total Losses = " + str(lose_count))