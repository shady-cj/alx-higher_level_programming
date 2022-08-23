#!/usr/bin/python3

def fizzbuzz():
    for i in range(1, 101):
        value = None
        if (i % 3 == 0 and i % 5 == 0):
            value = "FizzBuzz"
        elif (i % 3 == 0):
            value = "Fizz"
        elif (i % 5 == 0):
            value = "Buzz"
        else:
            value = i
        print("{}".format(value), end=" ")
