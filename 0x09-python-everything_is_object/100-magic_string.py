#!/usr/bin/python3
def magic_string():
    magic_string.c = getattr(magic_string, "c", 0) + 1
    return ", ".join(["BestSchool" for _ in range(magic_string.c)])
