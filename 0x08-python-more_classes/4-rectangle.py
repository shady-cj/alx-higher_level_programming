#!/usr/bin/python3

"""
This module defines a Rectangle class that defines private attributes
and calculates its perimeter and area and prints the rectangle
"""


class Rectangle:
    """
    The Rectangle class containing setters and getters to
    set and get the height and width of the rectangle
    and also provides methods to calculates its perimeter
    and area as well as printing it
    """

    def __init__(self, width=0, height=0):
        """ Initializes the class with height and width"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """ A getter method that returns the width """
        return self.__width

    @property
    def height(self):
        """ A getter method that returns the heiggt """
        return self.__height

    @width.setter
    def width(self, w):
        """ A setter method that sets the width of the rectangle """
        if type(w) != int:
            raise TypeError("width must be an integer")
        if w < 0:
            raise ValueError("width must be >= 0")
        self.__width = w

    @height.setter
    def height(self, h):
        """ A setter method that sets the height of the rectangle """
        if type(h) != int:
            raise TypeError("height must be an integer")
        if h < 0:
            raise ValueError("height must be >= 0")
        self.__height = h

    def area(self):
        """ Returns the area """
        return self.width * self.height

    def perimeter(self):
        """ Returns the perimeter """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """ Returns the shape in a user friendly format"""
        rect = ""
        if self.width == 0 or self.height == 0:
            return rect
        for _ in range(self.height):
            for _ in range(self.width):
                rect += "#"
            rect += "\n"
        return rect[:-1]

    def __repr__(self):
        """ Defines the repr version of the class for each instance"""
        return "Rectangle({},{})".format(self.width, self.height)
