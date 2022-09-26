#!/usr/bin/python3

"""
This module returns the attributes and methods of a class
"""


def lookup(obj):
    """
    Returns the list of the methods and attributes
    """
    return (list(dir(obj)))
