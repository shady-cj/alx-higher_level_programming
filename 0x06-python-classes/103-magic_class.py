#!/usr/bin/python3
"""
assemblying a bytecode instruction into the actual python code
"""

import math


class MagicClass:

    """ The magic class that was disassembled """
    def __init__(self, radius=0):
        """ Intializing the MagicClass and validating the arg passed """
        self.__radius = 0

        if type(radius) != int and type(radius) != float:
            raise TypeError("radius must be a number")
        else:
            self.__radius = radius

    def area(self):
        """ Calculating the area of a circle from the given radius """
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """ Calculating the circumference of a circle from the given radius """
        return 2 * math.pi * self.__radius
