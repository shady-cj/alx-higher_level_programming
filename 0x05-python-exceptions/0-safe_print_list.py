#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    for index in range(x):
        try:
            print(my_list[index], end="")
        except IndexError:
            index -= 1
            break
    print("")
    try:
        return (index + 1)
    except NameError:
        return (0)
