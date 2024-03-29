#!/usr/bin/python3

# A prime can only be divided by 1 and itself
# 5 is a prime because it can only be divided by 1 and 5 = positive factor

# 6 is not a prime because it can be divided by 1, 2, 3 and itself

# Input max prime

# Use a for loop and check if modulus == 0 True
def is_prime(num):
    for i in range(2, num):
        if (num % i == 0):
            return False

    return True

# forming a list of prime numbers
def getPrimes(max_number):
    list_of_primes = []

    for num1 in range(2, max_number):
        if is_prime(num1):
            yield num1
            # list_of_primes.append(num1)
        
    # return list_of_primes 

# User input maximum number to be searched
max_num = int(input("Search for Primes up to : "))

# Calling the functions to check onthe maximum number
list_of_primes = getPrimes(max_num)

# A for loop to print out every value in the list_of_primes
for prime in list_of_primes:
    print(prime)
