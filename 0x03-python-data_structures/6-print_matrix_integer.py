#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for array in matrix:
        for j, i in enumerate(array):
            endstring = "" if j == (len(array) - 1) else " "
            print("{}".format(i), end=endstring)
        print("")
