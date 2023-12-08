import csv

# Lists to store data
ids = []
students = []
marks = []

# Read the CSV file
with open("students.csv", mode="r") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row
    for row in reader:
        ids.append(row[0])
        students.append(row[1])
        marks.append(row[2])

# Print the data
for i in range(len(ids)):
    print(f"ID: {ids[i]}, Student: {students[i]}, Marks: {marks[i]}")


import pandas as pd

# Read the CSV file into a pandas DataFrame
data = pd.read_csv("students.csv", header=None, names=["id", "students", "marks"])

# Extract data into separate Series
ids = data["id"]
students = data["students"]
marks = data["marks"]

# Print the data
for i in range(len(ids)):
    print(f"ID: {ids[i]}, Student: {students[i]}, Marks: {marks[i]}")
