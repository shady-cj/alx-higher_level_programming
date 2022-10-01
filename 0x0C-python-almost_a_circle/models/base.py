#!/usr/bin/python3


"""
This module defines a base class
"""


class Base:

    """
    Defining the Base class with all the public
    and private attributes
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
