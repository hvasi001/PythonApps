import csv

# Reading from a CSV file
with open('example.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

