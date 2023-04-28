# Author: Nicholas Eby
# Created: 4.25.2023
# Title: Python Challenge 5: Average
# Purpose: 5. Write a Python program that calculates the average of three numbers entered by the user.

def get_average(nums):
    sum = 0
    for i in range(3):
        sum += nums[i]
    return round(sum / len(nums), 2)

my_nums = []

for i in range(3):
    user_input = float(input("Please enter a number: "))
    my_nums.append(user_input)

print("The average of the numbers entered is " + str(get_average(my_nums)))

