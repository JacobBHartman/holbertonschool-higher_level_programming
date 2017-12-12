#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print("{:d}".format(matrix[i][j]), end="")
            if j == len(matrix[i]) - 1 and i != len(matrix) - 1:
                print()
            elif j == len(matrix[i]) - 1 and i == len(matrix) - 1:
                pass
            else:
                print(" ", end="")
    print()
