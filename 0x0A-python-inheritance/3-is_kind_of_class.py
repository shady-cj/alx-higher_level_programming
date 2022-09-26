#!/usr/bin/python3

"""A module that checks if an object is kind of the same 
object """


def is_kind_of_class(obj, a_class):
    if isinstance(obj, a_class):
        return True
    return False
