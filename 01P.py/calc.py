#!/usr/bin/python3

# Enter two values
num1 = input("Enter value for num1: ")
num2 = input("Enter value for num2: ")

print("Enter the operator to be used: ")
operator = input('Operator: ')

# store the user inout of two numbers and the operator
# convert strings into integers
num1 = int(num1)
num2 = int(num2)

# if + then we need to provide output based on addition
if operator == "+":
    add = num1 + num2
    print(add)
elif operator == "-":
    sub = num1 - num2
    print(sub)
elif operator == "/":
    div = num1 / num2
    print(div)
elif operator == "*":
    mul = num1 * num2
    print(mul)
else:
    mod = num1 % num2
    print(mod)
# if - then we need to provide output based on subtraction
# if * then we need to provide output based on multiplication
# if / then we need to provide output based on multiplication
