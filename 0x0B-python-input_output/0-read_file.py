#!/usr/bin/python3

"""
This module contains a function that reads a file
"""


def read_file(filename=""):
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
