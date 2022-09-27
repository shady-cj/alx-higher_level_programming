#!/usr/bin/python3

"""
defining a base geometry class
"""


class BaseGeometry:
    """
    defining a base geometry class and a public method and
    an integer validator that
    raises an Exception
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        try:
            if type(value) != int:
                raise TypeError
            num = int(value)
        except (TypeError, ValueError):
            raise TypeError(f"{name} must be an integer") from None
        if num <= 0:
            raise ValueError(f"{name} must be greater than 0")
        return value
