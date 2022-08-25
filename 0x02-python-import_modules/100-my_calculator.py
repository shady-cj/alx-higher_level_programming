#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    if len(sys.argv) == 1 or len(sys.argv) > 4:
        print("{}".format("Usage: ./100-my_calculator.py <a> <operator> <b>"))
        sys.exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    op = sys.argv[2]
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
        print("{}".format(message))
        sys.exit(1)
    print("{:d} {} {:d} = {:d}".format(a, op, b, result))
