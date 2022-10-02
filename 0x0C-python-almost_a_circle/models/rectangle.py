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
        with respect to the x and y axis
        """
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            for _ in range(self.x):
                print(" ", end="")
            for _ in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """
        overriding the __str__ method
        """
        dim = f"{self.width}" if type(self).__name__ != "Rectangle" else f"\
{self.width}/{self.height}"
        return f"[{type(self).__name__}] ({self.id}) {self.x}/{self.y} \
- {dim}"

    def update(self, *args, **kwargs):
        """
        Allowing updates on the class attributes
        """
        i = 0
        u_dict = {
                "id": 0,
                "width": 0,
                "height": 0,
                "x": 0,
                "y": 0
                }
        while i < len(args):
            if i == 0:
                self.id = args[i]
                u_dict["id"] += 1
            elif i == 1:
                self.width = args[i]
                u_dict["width"] += 1
            elif i == 2:
                self.height = args[i]
                u_dict["height"] += 1
            elif i == 3:
                self.x = args[i]
                u_dict["x"] += 1
            elif i == 4:
                self.y = args[i]
                u_dict["y"] += 1
            i += 1
        for k, v in kwargs.items():
            if u_dict[k] == 0:
                setattr(self, k, v)

    def to_dictionary(self):
        """
        Converting the Rectangle instance to
        dictionary
        """
        d = {
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y
            }

        return d
