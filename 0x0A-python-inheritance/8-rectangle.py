#!/usr/bin/python3

""" A module that implements the Rectangle class
"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    a rectangle class that inherits from base geometry
    """

    def __init__(self, width, height):
        self.__height = self.integer_validator("height", height)
        self.__width = self.integer_validator("width", width)
