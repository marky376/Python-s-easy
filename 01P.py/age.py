#!/usr/bin/python3

# Providing different output based on age
# 1 - 18 -> important
# 21 ,50 -> 65 -> Important
# All the others -> Not important

# Receive age  and store in a variable age

age = int(input("Please enter your age: "))

# If age is both greater than or equal to one and less than or equal to 18 -> Important
if age >= 1 and age <= 18:
    print("The birthday is very important")
elif age >= 21 and age <= 65:
    print("The birthday is very important")
else:
    print("The birthday is not important by the way")

# if age is both greater than or equal to 21 and less than or equal to 65 -> Important

# Produce output on screen
