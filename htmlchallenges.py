# Author: Nicholas Eby
# Created: 4.27.2023
# Title: Python Challenge 24-26: Print Specific Tag Value, Find All Links, Find All Images
# Purpose:
    # 24. Write a Python program that reads in an HTML file and prints the values of a specific tag.
    # 25. Write a Python program that reads in an HTML file and finds all links on the page.
    # 26. Write a Python program that reads in an HTML file and finds all images on the page.

print("Welcome to HTML Challenges Program\n")

from bs4 import BeautifulSoup

# open html file and read contents
with open("sample.html", "r") as file:
    contents = file.read()
    # print(contents)

    # creates a new BeautifulSoup object that can then be parsed using .find(), .prettify(), .find_all(), .get_text()
    soup = BeautifulSoup(contents, 'html.parser')
    print(soup.find_all('p'))


# Challenge 24: Print Specific Tag Value: p
paragraphs = soup.find_all('p')
print("PARAGRAPHS")
for paragraph in paragraphs:
    print(paragraph.text)

# Challenge 25: Find All Links
links = soup.find_all('a')
print("LINKS")
for link in links:
    print(link.text)

# Challenge 26: Find All Images
images = soup.find_all('img')
total_images = 0
for image in images:
    total_images += 1
print("\nTotal Images =", total_images)