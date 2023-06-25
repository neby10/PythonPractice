# Author: Nicholas Eby
# Created: 4.25.2023
# Title: Python Challenge 3: Rectangle Area
# Purpose: 3. Write a Python program that calculates the area of a rectangle using user input for the length and width.

def get_rectangle_area(length, width):
    return length * width;

var_length = int(input("Enter the length of the rectangle: "))
var_width = int(input("Enter the width of the rectangle: "))

print("The area of the rectangle is " + str(get_rectangle_area(var_length, var_width)))

