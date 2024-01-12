#!/usr/bin/python3

# This program shows how to use the args AKA splat

# Obviously creating a function

def sumAll(*args):
    sum = 0

    for i in args:
        sum += i
        

