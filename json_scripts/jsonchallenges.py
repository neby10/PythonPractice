# Author: Nicholas Eby
# Created: 4.27.2023
# Title: Python Challenge 14-18: Print Values, Calculate Average, Find Max, Find Min, Create New JSON
# Purpose:
    # 14. Write a Python program that reads in a JSON file and prints the values of a specific key.
    # 15. Write a Python program that reads in a JSON file and calculates the average of a specific value.
    # 16. Write a Python program that reads in a JSON file and finds the maximum value of a specific value.
    # 17. Write a Python program that reads in a JSON file and finds the minimum value of a specific value.
    # 18. Write a Python program that reads in a JSON file and creates a new JSON file with only selected keys.

import json

print("Welcome to JSON Challenges Program\n")

with open("sample.json", "r") as input_file:
    data = json.load(input_file)

print(data, "\n")

# Challenge 14: Print value of a specific key: 'Pets'
print("Pets: ", data['Pets'])

# Challenge 15: Calculate average of a specific value: 'numbers'
print("Average of 'numbers' in data is:", (round(sum(data['numbers']) / len(data['numbers']), 2)))

# Challenge 16: Find max of a specific value: 'numbers'
print("Maximum of 'numbers' in data is:", max(data['numbers']))

# Challenge 17: Find min of a specific value: 'numbers'
print("Minimum of 'numbers' in data is:", min(data['numbers']))

# Challenge 18: Create a new JSON file with only selected keys
del data['tiger']
print("deleted key 'tiger'")
del data['Mobile']
print("deleted key 'Mobile'")
with open("sample2.json", "w") as output_file:
    json.dump(data, output_file)
    print("Output to 'sample2.json' was successful.")

