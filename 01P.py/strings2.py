#!/usr/bin/python3
'''
A program to convert strings given into an acronym
'''

# Ask  for a stirng
rand_string = str(input("Enter a string: "))

# Convert string to uppercase
rand_string = rand_string.upper()

# Convert string into a list
list_word = rand_string.split()
# Cycle through the list
for word in list_word:

    # Get the 1st letter of the word and eliminate the newline
    print(word[0], end="")
# Add a newline
print()
