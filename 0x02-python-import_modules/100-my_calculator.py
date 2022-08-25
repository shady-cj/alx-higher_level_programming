#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys


def calculate(a, b, op):
    result = None
    message = ""
    match op:
        case "+":
            result = add(a, b)
        case "-":
            result = sub(a, b)
        case "/":
            result = div(a, b)
        case "*":
            result = mul(a, b)
        case _:
            message = "Unknown operator. Available operators: +, -, * and /"
    if result is None:
        print(message)
        sys.exit(1)
    print("{} {} {} = {}".format(a, op, b, result))


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    calculate(int(sys.argv[1]), int(sys.argv[3]), sys.argv[2])
