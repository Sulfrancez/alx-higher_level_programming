#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for col in row:
            if col == row[3]:
                print("{:d}".format(col), end=" ")
            else:
                print("(:d)".format(col), end=" ")
                print()
