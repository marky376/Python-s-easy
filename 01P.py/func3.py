#!/usr/bin/python3

# Solve for x 

# x + 4 = 9

# x will always be the 1st value received and you only 
#will deal with addition

# Receive the string and split the string into variables
def solve_eq(equation):
    x, add, num1, equal, num2 = equation.split()

    num1, num2 = int(num1), int(num2)


# Convert the strings into integers

# Convert the result into a string and join them to the string "X = "
    return "x = " + str(num2 - num1)

# print()
print(solve_eq("x + 4 = 9"))
