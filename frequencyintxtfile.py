# Author: Nicholas Eby
# Created: 4.26.2023
# Title: Python Challenge 9: Calculate Frequency in Txt File
# Purpose: 9. Write a Python program that reads in a text file and counts the frequency of each word in the file.

import string, re

# read file
file = open("test.txt", "r")
contents = file.read()
contents = contents.split()

# eliminate punctuation so all the words are only words
pattern = re.compile('[^\w\s]')
contents = [re.sub(pattern, '', word) for word in contents]

# add frequencies of words to a dictionary
my_dict = {}

for word in contents:
    word = word.lower()
    if word in my_dict:
        my_dict[word] += 1
    else:
        my_dict[word] = 1

# display to screen
print(my_dict)

# displaying specific words based on frequency
for item in my_dict:
    if my_dict[item] > 3:
        print(item, my_dict[item])

file.close()