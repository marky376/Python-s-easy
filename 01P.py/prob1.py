#!/usr/bin/python3

# Problem : Receive miles and convert to kilometres
# kilometres = miles * 1.60934
# Enter Miles 5
# Print out 5 miles equals 8.04 kilometres

mile = float(input("Please enter number of miles to be converted: "))
kilom = round(mile * 1.6093, 2)

print("\n")
print(str(mile) + " miles equals to " + str(kilom) +  " kilometres ")

