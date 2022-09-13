#!/usr/bin/python3

"""A module that defines a Square class"""


class Square:
    """ A square class that takes a size as a argument """
    def __init__(self, size=0):
        """ Instantiate class and validate the size argument """
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")
