#!/usr/bin/python3

import magic_calculation_102
def magic_calculation(a, b):
    add = magic_calculation_102.add
    sub = magic_calculation_102.sub

    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(i, c)
        return c
    else:
        return sub(a, b)



