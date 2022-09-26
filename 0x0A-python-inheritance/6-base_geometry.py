#!/usr/bin/python3

"""
defining a base geometry class
"""


class BaseGeometry:
    """
    defining a base geometry class and a public method that
    raises an Exception
    """
    def area(self):
        raise Exception("area() is not implemented")
