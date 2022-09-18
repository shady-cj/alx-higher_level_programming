#!/usr/bin/python3

"""
This module contains a function that prints a square
with the character #.

    - Prototype: def print_square(size):
    - size is the size length of the square
    - size must be an integer, otherwise raise a TypeError exception
        with the message size must be an integer
    - if size is less than 0, raise a ValueError exception
        with the message size must be >= 0
    - if size is a float and is less than 0, raise a TypeError
        exception with the message size must be an integer
"""


def print_square(size):
    """
    The function takes in a size as an argument which is the size
    of the square to print and also validates the size value.
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    for _ in range(size):
        for _ in range(size):
            print("#", end="")
        print()
