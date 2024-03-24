"""
Adrian Ortiz
Class: CS 521 - Spring 1
Date: 02-04-2024
Homework Problem # 3_5
The program involves reading a file with student records, parsing each record
into a tuple, and storing these tuples in a list. The final output is a
printed list of all student records.
"""

# Read and store student records from a file
file_path = "cs521_3_5_input.txt"
student_records = []

# Open the file and read each line
with open(file_path, 'r') as file:
    for line in file:
        # Split each line into a tuple and add it to the list
        student_record = tuple(line.strip().split(','))
        student_records.append(student_record)

# Print the list of student records
print(student_records)

""" Output: 
    [('Adrian Ortiz', ' 14', ' 4.0'), 
    ('Ximena Ortiz', ' 22', ' 5.0'), 
    ('Emily Rodriguez', ' 19', ' 3.0'), 
    ('Gina Elise', ' 39', ' 2.5')]
"""
