"""
Adrian Ortiz
Class: CS 521 - Spring 1
Date: 02-04-2024
Homework Problem # 3_5
This task involves reading a specific file containing a 20-word sentence,
validating the word count, and then reformatting the sentence into four lines
with five words each.
"""

# Process and reformat a file containing a 20-word sentence
input_file = "cs521_3_4_input.txt"
output_file = "cs521_3_4_output.txt"

# Read the input file
with open(input_file, 'r') as file:
    sentence = file.read().strip()

# Split the sentence into words
words = sentence.split()
# Check if the sentence contains exactly 20 words
if len(words) != 20:
    print("Error: The sentence does not contain 20 words.")
else:
    # Reformat the sentence into 4 lines with 5 words each
    formatted_sentence = '\n'.join([' '.join(words[i:i+5]) for i in range(0, 20, 5)])
    # Write the formatted sentence to the output file
    with open(output_file, 'w') as file:
        file.write(formatted_sentence)
    print("File reformatted successfully.")

""" Output: 
    File reformatted successfully.
    Contents of cs521_3_4_output.txt:
    Adrian is going to get
    a Master's in Software Development
    from Boston Universities Metropolitan College.
    He loves his daughter Peanut.   
"""
