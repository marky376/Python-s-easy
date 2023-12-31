#!/usr/bin/python3

# Have the user enter their investment amount and expected interest
amount = input("Please enter the amount: ")
interest = input("Please enter the expected interest: ")
amount = float(amount)
interest = float(interest)
# Each year their investment will  increase by their investment + their investment * interest rate is
new_interest = ((interest * amount) + amount)
# Print out the eranings after a 10 year period
print("Your newly generated earnings is {:.2f}".format(new_interest))


