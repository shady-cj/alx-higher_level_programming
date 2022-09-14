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
        if isinstance(size, int) or isinstance(size, float):
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an number")

    def area(self):
        """ Returns the area of the square """
        return self.__size * self.__size

    def __lt__(self, other):
        """ Overloading the less than operator """
        if self.area() < other.area():
            return True
        else:
            return False

    def __le__(self, other):
        """ Overloading the less than or equal to operator """
        if self.area() <= other.area():
            return True
        else:
            return False

    def __eq__(self, other):
        """ Overloading the equals to operator """
        if self.area() == other.area():
            return True
        else:
            return False

    def __ne__(self, other):
        """ Overloading the not equals to operator """
        if self.area() != other.area():
            return True
        else:
            return False

    def __gt__(self, other):
        """ Overloading the greater than operator """
        if self.area() > other.area():
            return True
        else:
            return False

    def __ge__(self, other):
        """ Overloading the greater than or equals to operator """
        if self.area() >= other.area():
            return True
        else:
            return False
