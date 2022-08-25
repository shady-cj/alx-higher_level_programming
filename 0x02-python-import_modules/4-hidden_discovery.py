#!/usr/bin/python3
import hidden_4
for fn in dir(hidden_4):
    if (not fn.startswith("__")):
        print(fn)
