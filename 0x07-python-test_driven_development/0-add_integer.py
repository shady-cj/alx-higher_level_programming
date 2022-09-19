#!/usr/bin/python3


"""
A module that contains just one function that adds two integers
  - Prototype: def add_integer(a, b=98):
  - a and b must be integers or floats, otherwise raise a
    TypeError exception with the message a must be an integer
    or b must be an integer
  - a and b must be first casted to integers if they are float
  Returns an integer: the addition of a and b
"""


def add_integer(a, b=98):
    """
    A function that takes two integers and adds the result
    and also validate the input
    >>> add_integer(1, 2)
    3
    """
    if all([type(a) in (float, int),
            type(b) in (float, int)]):
        a = int(a)
        b = int(b)

        return a + b

    else:
        if type(a) not in (float, int):
            raise TypeError("a must be an integer")
        if type(b) not in (float, int):
            raise TypeError("b must be an integer")
