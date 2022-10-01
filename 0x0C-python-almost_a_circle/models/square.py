#!/usr/bin/python3

"""
This modules a Square with all the necessary functionalities
and inherits from the Rectangle class
"""

from .rectangle import Rectangle



class Square(Rectangle):
    """
    Defining a Square class that inherits from
    Rectangle class
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
