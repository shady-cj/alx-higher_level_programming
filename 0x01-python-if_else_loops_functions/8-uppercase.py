#!/usr/bin/python3

def uppercase(str):
    new_str = ""
    for c in str:
        if ord(c) in list(range(ord('a'), ord('z') + 1)):
            c = chr(ord(c) - 32)
        new_str += c
    print(new_str)
