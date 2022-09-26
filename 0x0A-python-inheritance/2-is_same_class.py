#!/usr/bin/python3

"""
A module that checks if an object is an instance of a class
"""


def is_same_class(obj, a_class):
    if type(obj) == a_class:
        return True
    return False
