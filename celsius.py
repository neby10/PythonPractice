# Author: Nicholas Eby
# Created: 4.25.2023
# Title: Python Challenge 6: Celsius
# Purpose: 6. Write a Python program that converts Celsius to Fahrenheit using user input for the temperature in Celsius.

temp = float(input("Please enter the temperature in Celsius: "))

print("The temperature in Fahrenheit is: ", round((temp * (9 / 5) + 32), 1))