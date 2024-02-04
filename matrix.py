# A code that when run will display matrix of 1s and 0s in a random pattern

import random

def main():
    # Set the size of the matrix
    rows = 1000
    cols = 1000

    # Create a matrix of 1s and 0s
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(random.choice([0, 1]))
        matrix.append(row)

    # Display the matrix
    for row in matrix:
        print(row)

if __name__ == "__main__":
    main()

# The matrix is created using a list of lists. The outer list contains the rows of the matrix, and each row is a list of 1s and 0s. The random.choice function is used to randomly select a 0 or 1 for each element of the matrix. The matrix is then displayed by iterating over the rows and printing each one.