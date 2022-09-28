#!/usr/bin/python3


"""
A module that contains a function that appends
to the end of a file.
"""


def append_write(filename="", text=""):
    """
    Writing into filename that value ot text
    """
    num_of_char = 0
    with open(filename, "a", encoding="utf-8") as f:
        num_of_char = f.write(str(text))
    return num_of_char
