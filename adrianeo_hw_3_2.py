"""
Adrian Ortiz
Class: CS 521 - Spring 1
Date: 02-04-2024
Homework Problem # 3_2
The task involves creating a docstring, converting it into a list of
sentences, and then using loops to count uppercase letters, lowercase letters,
digits, and punctuation in each sentence.
"""

# Analyze a docstring for uppercase, lowercase, digits, and punctuation
docstring = ("My first sentence is very generic... ",
             "My favorite phrase is LGI!!! ",
             "LGI stands for Let's Get It!!!")

# Import string module for punctuation characters
import string

# Initialize counters for each sentence
sentence_counters = []

# Process each sentence in the docstring
for index, sentence in enumerate(docstring, start=1):
    uppercase_count = sum(1 for count in sentence if count.isupper())
    lowercase_count = sum(1 for count in sentence if count.islower())
    digit_count = sum(1 for count in sentence if count.isdigit())
    punctuation_count = sum(1 for count in sentence if count in
                            string.punctuation)

    # Append counts for the current sentence
    sentence_counters.append((index, uppercase_count, lowercase_count, digit_count, punctuation_count))

# Print the formatted header
print(f"{'#':<2} {'Upper':<8} {'Lower':<8} {'Digits':<8} {'Punct.':<8}")

# Print the separator
print("-" * 36)

# Print the counts for each sentence
for counter in sentence_counters:
    print(f"{counter[0]:<2} {counter[1]:<8} {counter[2]:<8} {counter[3]:<8} {counter[4]:<8}")


"""
Output:
    #  Upper    Lower    Digits   Punct.  
    ------------------------------------
    1  1        27       0        3       
    2  4        17       0        3       
    3  6        15       0        4       
"""
