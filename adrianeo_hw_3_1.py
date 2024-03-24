"""
Adrian Ortiz
Class: CS 521 - Spring 1
Date: 02-04-2024
Homework Problem # 3_1
This program requires iterating through integers from 2 to 130 and
categorizing them as odd, even, squares, and cubes. It involves using
loops, conditionals, and mathematical operations. The implementation will
include counting occurrences in each category and displaying the results
according to the following example:
Checking numbers from 2 to 130
Odd (64): 3...129
Even (65): 2...130
Square (10):
[4, 9, 16, 25, 36, 49, 64, 81, 100, 121] Cube (4): [8, 27, 64, 125].
"""

# Count and categorize integers from 2 to 130
odd_count, even_count, square_count, cube_count = 0, 0, 0, 0
odd_numbers, even_numbers, square_numbers, cube_numbers = [], [], [], []

for num in range(2, 131):
    # Check if the number is even or odd and increment counters
    if num % 2 == 0:
        even_count += 1
        even_numbers.append(num)
    else:
        odd_count += 1
        odd_numbers.append(num)

    # Check if the number is a perfect square and increment counter
    if num ** 0.5 == int(num ** 0.5):
        square_count += 1
        square_numbers.append(num)

    # Check if the number is a perfect cube and increment counter
    if num ** (1/3) == int(num ** (1/3)):
        cube_count += 1
        cube_numbers.append(num)

# Combined print statement for all categories
results = (
    "Checking numbers from 2 to 130\n"
    f"Odd ({odd_count}): {odd_numbers[0]}...{odd_numbers[-1]}\n"
    f"Even ({even_count}): {even_numbers[0]}...{even_numbers[-1]}\n"
    f"Square ({square_count}): {square_numbers}\n"
    f"Cube ({cube_count}): {cube_numbers}"
)
print(results)

""" Output: 
    Checking numbers from 2 to 130
    Odd (64): 3...129
    Even (65): 2...130
    Square (10): [4, 9, 16, 25, 36, 49, 64, 81, 100, 121]
    Cube (2): [8, 27]
"""
