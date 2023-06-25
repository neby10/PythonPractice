# Author: Nicholas Eby
# Created: 4.26.2023
# Title: Python Challenge 8: Count Words in Txt File
# Purpose: 8. Write a Python program that reads in a text file and counts the number of words in the file.

print("Welcome to Count Words in Txt File Program")

with open("test.txt", "r") as f:
    my_file = f.read()

lines = my_file.split()
count1 = len(lines)
# print(lines)
print("test.txt is", count1, "words.")


file = open("test2.txt", "r")
contents = file.read()

contents = contents.split()
count2 = len(contents)
# print(contents)
print("test2.txt is", count2, "words.")

file.close()
