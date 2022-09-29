#!/usr/bin/python3

"""
A module that defines the student class
"""


class Student:
    """
    Defining public attributes and converting it to json
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is not None and type(attrs) == list:
            new_dict = {}
            for el in attrs:
                dict_val = self.__dict__.get(el)
                if dict_val is not None:
                    new_dict[el] = dict_val
            return new_dict
        return self.__dict__
