#!/usr/bin/python3

"""
Defining a class that overwrites the setattr() method
"""


class LockedClass:
    """ Locked class overwrites the setattr() method and only allows
    setting new attribute if the name is "first_name"
    """
    def __setattr__(self, name, value):
        if name == "first_name":
            self.__dict__[name] = value
        else:
            raise AttributeError("'" + str(type(self).__name__) + "'"
                                 + " object has no attribute "
                                 + "'" + str(name) + "'")
