#!/usr/bin/python3

"""A module that defines a Square class"""


class Square:
    """ A square class that takes a size as a argument """
    def __init__(self, size=0, position=(0, 0)):
        """ Instantiate class and validate the size and position argument """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (isinstance(value, tuple) and len(value) == 2 and
                all([isinstance(i, int) and i >= 0 for i in value])):
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        """ prints in stdout the square with the character # """
        print(self.__str__())

    def area(self):
        """ Returns the area of the square """
        return self.__size * self.__size

    def __str__(self):
        """ The string representation of the class """
        my_print_string = ""
        if self.size != 0:
            for _ in range(self.position[1]):
                my_print_string += "\n"
            for _ in range(self.size):
                for _ in range(self.position[0]):
                    my_print_string += " "
                for _ in range(self.size):
                    my_print_string += "#"
                my_print_string += "\n"
        return my_print_string[:-1]
