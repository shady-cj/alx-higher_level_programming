#!/usr/bin/python3

"""
This module defines a Rectangle class that defines private attributes
"""


class Rectangle:
    """
    The Rectangle class containing setters and getters to
    set and get the height and width of the rectangle
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
