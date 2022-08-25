#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    args = len(sys.argv) - 1
    sum = 0
    if (args == 0):
        print("{:d}".format(sum))
        sys.exit()
    i = 1
    while (i <= args):
        sum += int(sys.argv[i])
        i += 1
    print("{:d}".format(sum))
