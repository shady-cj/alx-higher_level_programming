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
        """
        The constructor... inheriting from the parent class
        and also adding new attributes
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    def get_size(self):
        """
        defining getter on size attribute
        """
        return self.width

    def set_size(self, s):
        """
        defining setter on size
        """
        self.width = s
        self.height = s

    size = property(get_size, set_size)
