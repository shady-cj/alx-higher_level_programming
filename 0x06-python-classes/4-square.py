#!/usr/bin/python3

"""A module that defines a Square class"""


class Square:
    """ A square class that takes a size as a argument """
    def __init__(self, size=0):
        """ Instantiate class and validate the size argument """
        self.size = size

    @property
    def size(self):
        """ The getter method for the size attribute """
        return self.__size

    @size.setter
    def size(self, size):
        """ The setter method to set the size attribute """
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """ Returns the area of the square """
        return self.__size * self.__size
