# Author: Nicholas Eby
# Created: 4.27.2023
# Title: Python Challenge 27-29: CSV Bar Chart Using Matplotlib, JSON Pie Chart Using Matplotlib, XML Line Chart Using Matplotlib
# Purpose:
    # 27. Write a Python program that reads in a CSV file and creates a line chart of the data using matplotlib.
    # 28. Write a Python program that reads in a JSON file and creates a line chart of the data using matplotlib.
    # 29. Write a Python program that reads in an XML file and creates a bar chart of the data using matplotlib.

import matplotlib.pyplot as plt 
import csv
import json
from bs4 import BeautifulSoup

# Create a figure containing a single axes
fig, ax = plt.subplots() # subplots returns a tuple containing the Figure and Axes objects

# Plot data
ax.plot([0, 1, 2, 3, 4], [0, 5, 8, 2, 3])

# Show the graph through terminal
plt.show()

# # # # # # # # # # # # # # # # # # # # # # # #

# Challenge 27: CSV Bar Chart Using Matplotlib
# Create a figure containing a single axes
fig, ax = plt.subplots()

with open("practice.csv", "r") as file:
    # Create reader object
    csv_reader = csv.reader(file)

    # Skip Header
    next(csv_reader)

    # Create list of employees
    column = 8
    employees = [float(row[column]) for row in csv_reader]

    # Plot values
    ax.plot((range(len(employees))), employees)

    # Show Plot
    plt.show()

# # # # # # # # # # # # # # # # # # # # # # # #

# Challenge 28: JSON Pie Chart Using Matplotlib

fig, ax = plt.subplots()

with open("plotdata.json", "r") as file:
    data = json.load(file)

    grades = []
    for student in data['students']:
        student_grades = []
        for i in range(1, 11):
            student_grades.append(student[str(i)])
        grades.append(student_grades)

    for i in range(len(data['students'])):
        ax.plot(range(len(grades[i])), grades[i], label=str(data['students'][i]['name']))

    ax.legend()

    plt.show()

# # # # # # # # # # # # # # # # # # # # # # # #

# Challenge 29: XML Line Chart Using Matplotlib

with open("mydata.xml", "r") as file:
    contents = file.read()

    soup = BeautifulSoup(contents, "xml")

    names = soup.find_all('Name')
    names = [name.text for name in names]

    values = soup.find_all("Input")
    values = [float(value.text) for value in values]

fig, ax = plt.subplots()

# bar() function used to create a bar graph
plt.bar(names, values)

plt.title('Python Test Data')
plt.xlabel('Planets')
plt.ylabel('Numbers')

plt.show()

# Sort the names and values by name
# names, values = zip(*sorted(zip(names, values)))




