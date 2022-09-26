#!/usr/bin/python3

"""
defines square class
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    A square classs that inherits from rectangle class
    """

    def __init__(self, size):
        super().__init__(size, size)
        self.__size = size
