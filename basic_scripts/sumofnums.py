# Author: Nicholas Eby
# Created: 4.25.2023
# Title: Python Challenge 4: Sum of Nums
# Purpose: 4. Write a Python program that calculates the sum of two numbers entered by the user.

def get_sum(nums):
    sum = 0
    for num in nums:
        sum += num
    return sum

my_nums = []

my_nums_length = int(input("Enter the quantity of integers you wish to add: "))

for i in range(my_nums_length):
    my_nums.append(int(input("Enter an integer: ")))

total = print("The sum total is " + str(get_sum(my_nums)))