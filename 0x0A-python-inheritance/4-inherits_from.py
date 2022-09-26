#!/usr/bin/python3

""" A module that checks a sub class """


def inherits_from(obj, a_class):
    """
    checks if obj is inherited from the class a_class and return True
    """
    if obj.__class__ == a_class:
        return False
    if issubclass(obj.__class__, a_class):
        return True
    return False
