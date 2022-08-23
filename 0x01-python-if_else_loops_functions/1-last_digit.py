#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
sign_num = None
message = ""

if number >= 0:
    sign_num = 1
else:
    sign_num = -1

last_digit = (sign_num * number) % 10
last_digit = sign_num * last_digit

if last_digit > 5:
    message += "and is greater than 5"
elif last_digit == 0:
    message += "and is 0"
else:
    message += "and is less than 6 and not 0"

print(f"Last digit of {number} is {last_digit} {message}")

