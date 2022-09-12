#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):

    index = 0
    for i in range(x):
        try:
            index += 1
            print("{:d}".format(my_list[i]), end="")
        except (TypeError, ValueError):
            index -= 1
    print("")
    try:
        return (index)
    except NameError:
        return (0)
