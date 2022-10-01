#!/usr/bin/python3
from .base import Base

"""
This module contains the Rectangle class
that inherits from Base
"""


class Rectangle(Base):
    """
    Defining the Rectangle class
    and inheriting from the Base class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializer
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Getter on width
        """
        return self.__width

    @width.setter
    def width(self, w):
        """
        setter on width
        """
        Rectangle.validate(w, "width", "dim")
        self.__width = w

    @property
    def x(self):
        """
        getter on x
        """
        return self.__x

    @x.setter
    def x(self, x):
        """
        setter on x
        """
        Rectangle.validate(x, "x", "scale")
        self.__x = x

    @property
    def height(self):
        """
        getter on height
        """
        return self.__height

    @height.setter
    def height(self, h):
        """
        setter on height
        """
        Rectangle.validate(h, "height", "dim")
        self.__height = h

    @property
    def y(self):
        """
        getter on y
        """
        return self.__y

    @y.setter
    def y(self, y):
        """
        setter on y
        """
        Rectangle.validate(y, "y", "scale")
        self.__y = y

    @staticmethod
    def validate(v, name, t):
        """
        Helper staticmethod to validate inputs
        """
        if type(v) != int:
            raise TypeError(f"{name} must be an integer")
        if t == "dim" and v <= 0:
            raise ValueError(f"{name} must be > 0")
        if t == "scale" and v < 0:
            raise ValueError(f"{name} must be >= 0")

    def area(self):
        """
        Calculating the area of the rectangle
        """
        return self.width * self.height

    def display(self):
        """
        Printing out the rectangle with "#"
        """

        for _ in range(self.height):
            for _ in range(self.width):
                print("#", end="")
            print()
