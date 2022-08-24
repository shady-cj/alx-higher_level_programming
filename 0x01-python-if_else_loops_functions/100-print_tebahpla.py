#!/usr/bin/python3

for index in list(range(ord('z'), ord('a') - 1, -1)):
    print("{}".format(chr(index - 32) if index % 2 != 0 else chr(index)),
          end="")
