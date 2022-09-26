#!/usr/bin/python3

""" A module that checks a sub class """


def inherits_from(obj, a_class):
    """
    checks if obj is inherited from the class a_class and return True
    """
    if issubclass(obj, a_class):
        return True
    return False
