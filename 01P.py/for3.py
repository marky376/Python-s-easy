#!/usr/bin/python3
# Get the number of rows needed
rows = input("Enter number of rows: ")
# Convert into an integer
rows = int(rows)
# Get the  starting spaces for the top of the tree
spaces = rows - 1
# There is one hash to start that will be incremented
hashes = 1
# Save stump spaces till later
spaces_1 = rows - 1
# Make sure the right number of rows are printed
while rows != 0:

# Print the spaces
    for i in range(spaces):
        print(' ', end="")
# Print the hashes
    for i in range(hashes):
        print('#', end="")
# Newline after each row is printed
    print()
# That spaces is decremented by 1 each time
    spaces -= 1
# That hashes is incremented by 2 each time
    hashes += 2
# Decrement tree height each time to jump out of the loop
    rows -= 1
# Print the spaces before the stump and then hash
for i in range(spaces_1):
    print(' ', end="")

print("#")
