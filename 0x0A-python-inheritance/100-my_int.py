#!/usr/bin/python3
"""
implementing myint that inherits from int
"""

class MyInt(int):
    def __eq__(self, other):
        return self.real != other
    def __ne__(self, other):
        return self.real == other
