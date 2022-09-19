#!/usr/bin/python3


"""
A module that creates a simple Square class and instanstiate a
private size attribute
"""


class Square:
    """A simple Square class"""

    def __init__(self, size=None):
        """Initializes the class with a private attribute of size"""
        self.__size = size
