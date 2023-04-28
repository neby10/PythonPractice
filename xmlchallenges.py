# Author: Nicholas Eby
# Created: 4.27.2023
# Title: Python Challenge 19-23: Print Values of Tag, Calculate Average, Find Max, Find Min, Create New XML With Selected
# Purpose:
    # 19. Write a Python program that reads in an XML file and prints the values of a specific tag.
    # 20. Write a Python program that reads in an XML file and calculates the average of a specific value.
    # 21. Write a Python program that reads in an XML file and finds the maximum value of a specific value.
    # 22. Write a Python program that reads in an XML file and finds the minimum value of a specific value.
    # 23. Write a Python program that reads in an XML file and creates a new XML file with only selected tags.

print("Welcome to XML Challenges Program\n")

import xml.etree.ElementTree as ET

# parse the XML file, .parse() returns an ElementTree object that can be used to access XML data
tree = ET.parse("myfile.xml")

# get root element
root = tree.getroot()

# .find() searches for the first occurrence of a tag among the immediate children of the current element
# .text returns the text content of an element
my_book = root.find('book')
first_author = my_book.find('author')
print(first_author.text)

# .findall() returns a list of all elements with a given tag name among the immediate children of the current element
for book in root.findall('book'):
    price = book.find('price')
    print(price.tag, price.text, end=" | ")
print()

# .get() returns the value of an attribute with a given name
for book in root.findall('book'):
    my_id = book.get('id')
    print(book.tag, my_id, end=" | ")
print()

# Challenge 19: Print values of a specific tag: 'publish_date'
for child in root:
    print(child.find('publish_date').text, end=" | ")
print()

# Challenge 20: Calculate the average of a specific value: 'price'
average_price = 0
num_items = 0
for child in root:
    average_price += float(child.find('price').text)
    num_items += 1
average_price /= num_items
print("Average price is $", round(average_price, 2))

# Challenge 21: Find the maximum of a specific value: 
xml_prices = []
for child in root:
    xml_prices.append(float(child.find('price').text))
print("Maximum price is $", max(xml_prices))

# Challenge 22: Find the minimum of a specfic value: 
print("Minimum price is $", min(xml_prices))

# Challenge 23: Create new XML file with only selected tags:
new_root = ET.Element('new_root')

for child in root:
    if child.tag in 'book':
        new_root.append(child)
    
new_tree = ET.ElementTree(new_root)
new_tree.write("myfilenew.xml")
print("File Successfully Written")