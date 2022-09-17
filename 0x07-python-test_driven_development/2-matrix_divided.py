#!/usr/bin/python3

"""
 This module contains a function that divides all elements of a matrix.

    - Prototype: def matrix_divided(matrix, div):
    - matrix must be a list of lists of integers or floats,
        otherwise raise a TypeError exception with the message
        matrix must be a matrix (list of lists) of integers/floats
    - Each row of the matrix must be of the same size, otherwise
        raise a TypeError exception with the message Each row of
        the matrix must have the same size
    - div must be a number (integer or float), otherwise raise
        a TypeError exception with the message div must be a number
    - div can’t be equal to 0, otherwise raise a ZeroDivisionError
        exception with the message division by zero
    - All elements of the matrix should be divided by div,
        rounded to 2 decimal places
        Returns a new matrix
"""


def matrix_divided(matrix, div):
    """
    The function takes in a matrix and div validates the matrix
    and the div and performs division each element of the div and
    returns a new matrix of the result of each divisions
    """
    if type(matrix) == list and all([type(e) == list for e in matrix]):
        new_matrix = []
        length = None
        if type(div) not in (int, float):
            raise TypeError("div must be a number")
        if div == 0:
            raise ZeroDivisionError("division by zero")
        for row in matrix:
            new_row = []
            if length is None:
                length = len(row)
            elif length != len(row):
                raise TypeError("Each row of the matrix must\
 have the same size")
            for entry in row:
                if type(entry) not in (float, int):
                    raise TypeError("matrix must be a matrix (list of lists)\
 of integers/floats")
                new_row.append(round(entry / div, 2))
            new_matrix.append(new_row)
        return new_matrix

    else:
        raise TypeError("matrix must be a matrix (list of lists) of\
 integers/floats")
