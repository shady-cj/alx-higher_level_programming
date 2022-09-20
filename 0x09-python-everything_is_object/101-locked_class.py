#!/usr/bin/python3

"""
Defining a class that restricts dynamically allocating memory
"""


class LockedClass:
    """ Locked class deines a __slot__ to limit the attributes that
    can be stored at every instance call
    """
    __slots__ = ["first_name"]
