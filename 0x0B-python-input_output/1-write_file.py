#!/usr/bin/python3


"""
A module that contains a function that writes
to a file.
"""


def write_file(filename="", text=""):
    num_of_char = 0
    with open(filename, "w", encoding="utf-8") as f:
        num_of_char = f.write(str(text))
    return num_of_char
