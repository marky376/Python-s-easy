#!/usr/bin/python3

# Ask the user to input 2 values and store them in variables num1 num2

num1 = int(input("Please enter value for num1: "))
num2 = int(input("Please enter value for num2: "))

# Do some math with the given values for num1 and num2
# This is accompanied by assigning different variables here
add = num1 + num2 # add is the variable for addition
div = num1 / num2 # div is the variable for division
mul = num1 * num2 # mul is the variable for multiplication
sub = num1 - num2 # sub is the variable for subtraction
mod = num1 % num2 # mod is the variable for modulus

print("\n")
print("\n")
# Print out the output
#print(f"The sum of num1 and num2 is: {add}")
#print(f"The difference of num1 and num2 is: {sub}")
#print(f"The multiplication of num1 and num2 is: {mul}")
#print(f"The  division of num1 and num2 is: {div}")
#print(f"The modulus of num1 and num2 is: {mod}")

print("{} + {} = {}".format(num1, num2, add))
print("{} - {} = {}".format(num1, num2, sub))
print("{} * {} = {}".format(num1, num2, mul))
print("{} / {} = {}".format(num1, num2, div))
print("{} % {} = {}".format(num1, num2, mod))
