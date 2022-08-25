#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    if len(sys.argv) != 4:
        print("{}".format("Usage: ./100-my_calculator.py <a> <operator> <b>"))
        sys.exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    op = sys.argv[2]
    result = None
    message = ""
    if op == "+":
        result = add(a, b)
    elif op == "-":
        result = sub(a, b)
    elif op == "/":
        result = div(a, b)
    elif op == "*":
        result = mul(a, b)
    else:
        message = "Unknown operator. Available operators: +, -, * and /"
    if result is None:
        print("{}".format(message))
        sys.exit(1)
    print("{:d} {} {:d} = {:d}".format(a, op, b, result))
