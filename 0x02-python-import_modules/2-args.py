#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    args = len(sys.argv) - 1
    if (not args):
        print("{}".format("0 arguments."))
        sys.exit()

    print("{} {}:".format(args, "arguments" if args > 1
                          else "argument"))
    i = 1
    while (i <= args):
        print("{}: {}".format(i, sys.argv[i]))
        i += 1
