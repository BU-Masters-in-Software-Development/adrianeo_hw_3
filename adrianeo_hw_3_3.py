"""
Adrian Ortiz
Class: CS 521 - Spring 1
Date: 02-04-2024
Homework Problem # 3_3
This program requires input validation where the user is prompted to enter
a three-digit number. The number must be in ascending order and without
duplicates. The implementation involves loops for repeated prompting, and
conditionals to check the validity of the input.
"""

while True:
    number = input("Enter a three-digit number: ")

    # Check if the input has exactly three digits
    if len(number) != 3:
        print("Invalid input: The number must have exactly three digits. "
              "Please try again."
              )
        continue

    # Check if the input is a digit
    if not number.isdigit():
        print(
            "Invalid input: The number must be a numeric value. Please try again."
            )
        continue

    # Check if the digits are in ascending order
    if number != ''.join(sorted(number)):
        print(
            "Invalid input: The digits must be in ascending order. Please try again"
            )
        continue

    # Check if the digits are unique
    if len(set(number)) != 3:
        print("Invalid input: The digits must be unique. Please try again.")
        continue

    print("Valid number entered.")
    break

""" Output:
Enter a three-digit number: 1234
Invalid input: The number must have exactly three digits. Please try again.
Enter a three-digit number: abc
Invalid input: The number must be a numeric value. Please try again.
Enter a three-digit number: 321
Invalid input: The digits must be in ascending order. Please try again
Enter a three-digit number: 111
Invalid input: The digits must be unique. Please try again.
Enter a three-digit number: 123
Valid number entered.
"""
