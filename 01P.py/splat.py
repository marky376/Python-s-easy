#!/usr/bin/python3

# This program shows how to use the args AKA splat

# Obviously creating a function

def sum_all(*args):
    total = 0

    for i in args:
        total += i

    return sum


print("Sum :" + str((sumAll(1,2,3,4,5,6,7,8,9,10,11))))
