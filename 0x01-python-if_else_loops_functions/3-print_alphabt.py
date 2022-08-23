#!/usr/bin/python3

for alpha in range(ord('a'), ord('z')):
    if chr(alpha) == 'e' or chr(alpha) == 'q':
        continue
    print("{}".format(chr(alpha)), end="")
