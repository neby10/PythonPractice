# Author: Nicholas Eby
# Created: 4.26.2023
# Title: Python Challenge 10-13: Calculate Average, Calculate Max, Calculate Min, Create New CSV File
# Purpose:
    # 10. Write a Python program that reads in a CSV file and calculates the average of a specific column.
    # 11. Write a Python program that reads in a CSV file and finds the maximum value in a specific column.
    # 12. Write a Python program that reads in a CSV file and finds the minimum value in a specific column.
    # 13. Write a Python program that reads in a CSV file and creates a new CSV file with only selected columns.

import csv

print("Welcome to CSV Program\n")

with open("hundredthousand.csv", "r") as file:
    # create a CSV reader object
    csv_reader = csv.reader(file)

    # skip header
    next(csv_reader)

    # set to desired column
    column = 8

    # creates a list of all column values
    num_employees_list = [int(row[column]) for row in csv_reader]

    print("CSV STATISTICS")
    print(f"Average Employees: {sum(num_employees_list) / len(num_employees_list)}")
    print(f"Maximum Employees: {max(num_employees_list)}")
    print(f"Minimum Employees: {min(num_employees_list)}")



#  Create a new csv file using only selected columns

with open("hundredthousand.csv", "r") as input_file:
    # create reader object
    csv_reader = csv.reader(input_file)

    with open("test1.csv", "w") as output_file:
        # create writer object
        csv_writer = csv.writer(output_file)

        # iterate over each item to write to csv
        for row in csv_reader:
            selected_columns = [row[2], row[6], row[7], row[8]]
            csv_writer.writerow(selected_columns)
        
