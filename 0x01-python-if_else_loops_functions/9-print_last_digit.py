#!/usr/bin/python3

def print_last_digit(number):
    sign_num = None
    if number >= 0:
        sign_num = 1
    else:
        sign_num = -1

    last_digit = (sign_num * number) % 10
    print("{}".format(last_digit), end="")
    return last_digit
