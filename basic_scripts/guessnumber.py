# Author: Nicholas Eby
# Created: 4.26.2023
# Title: Python Challenge 7: Guess Number
# Purpose: 7. Write a Python program that generates a random number at or between 1 and 100 and asks the user to guess the number.

import random

rand_num = random.randint(1, 100)

user_input = -1

while rand_num != user_input:
    user_input = int(input("Guess a number at or between 1 and 100: "))
    if user_input > rand_num:
        print("Guess a little lower...")
    elif user_input < rand_num:
        print("Guess a little higher...")
    else:
        print("You guessed it!")