# 0x01-python-if_else_loops_functions

Learning conditions and loops in python..

## TASKS

### 0-positive_or_negative.py

**0-positive_or_negative.py** - This program will assign a random signed number to the variable number each time it is executed. It prints whether the number stored in the variable number is positive or negative.

**USAGE**
```
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py
-4 is negative
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py
0 is zero
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py
-3 is negative
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py
-10 is negative
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py
10 is positive
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py
-5 is negative
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py
6 is positive
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py
7 is positive
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py
5 is positive
guillaume@ubuntu:~/0x01$
```

### 1-last_digit.py
**1-last_digit.py** - This program will assign a random signed number to the variable number each time it is executed. It prints the last digit of the number stored in the variable number.

**USAGE**
```
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of 4205 is 5 and is less than 6 and not 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of -626 is -6 and is less than 6 and not 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of 1144 is 4 and is less than 6 and not 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of -9200 is 0 and is 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of 5247 is 7 and is greater than 5
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of -9318 is -8 and is less than 6 and not 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of 3369 is 9 and is greater than 5
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of -5224 is -4 and is less than 6 and not 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of -4485 is -5 and is less than 6 and not 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of 3850 is 0 and is 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of 5169 is 9 and is greater than 5
guillaume@ubuntu:~/0x01$
```

### 2-print_alphabet.py
**2-print_alphabet.py** - The program that prints the ASCII alphabet, in lowercase, not followed by a new line.

**USAGE**
```
guillaume@ubuntu:~/0x01$ ./2-print_alphabet.py
abcdefghijklmnopqrstuvwxyzguillaume@ubuntu:~/0x01$
```

### 3-print_alphabt.py
**3-print_alphabt.py** - The program prints the ASCII alphabet, in lowercase, not followed by a new line. excluding 'q' and 'e'

**USAGE**
```
guillaume@ubuntu:~/0x01$ ./3-print_alphabt.py
abcdfghijklmnoprstuvwxyzguillaume@ubuntu:~/0x01$
```
### 4-print_hexa.py
**4-print_hexa.py** - The program prints all numbers from 0 to 98 in decimal and in hexadecimal.

**USAGE**
```
guillaume@ubuntu:~/0x01$ ./4-print_hexa.py
0 = 0x0
1 = 0x1
2 = 0x2
3 = 0x3
4 = 0x4
5 = 0x5
6 = 0x6
7 = 0x7
8 = 0x8
9 = 0x9
10 = 0xa
11 = 0xb
12 = 0xc
13 = 0xd
14 = 0xe
15 = 0xf
16 = 0x10
17 = 0x11
18 = 0x12
...
96 = 0x60
97 = 0x61
98 = 0x62
guillaume@ubuntu:~/0x01$
```

### 5-print_comb2.py
**5-print_comb2.py** - program that prints numbers from 0 to 99.
**USAGE**
```
guillaume@ubuntu:~/0x01$ ./5-print_comb2.py
00, 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99
guillaume@ubuntu:~/0x01$
```

### 6-print_comb3.py
**6-print_comb3.py** - A program that prints all possible different combinations of two digits.

**USAGE**
```
guillaume@ubuntu:~/0x01$ ./6-print_comb3.py
01, 02, 03, 04, 05, 06, 07, 08, 09, 12, 13, 14, 15, 16, 17, 18, 19, 23, 24, 25, 26, 27, 28, 29, 34, 35, 36, 37, 38, 39, 45, 46, 47, 48, 49, 56, 57, 58, 59, 67, 68, 69, 78, 79, 89
guillaume@ubuntu:~/0x01$
```

### 7-islower.py

**7-islower.py** - It contains  a function that checks for lowercase character.

**USAGE**
```
guillaume@ubuntu:~/0x01$ ./7-main.py
a is lower
H is upper
A is upper
3 is upper
g is lower
guillaume@ubuntu:~/0x01$
```


### 8-uppercase.py
**8-uppercase.py** - contains a function that prints a string in uppercase followed by a new line. similar to the str.upper() string method

**USAGE**
```
guillaume@ubuntu:~/0x01$ ./8-main.py
BEST
BEST SCHOOL 98 BATTERY STREET
guillaume@ubuntu:~/0x01$
```

### 9-print_last_digit.py
**9-print_last_digit.py** - contains a function that prints the last digit of a number.

**USAGE**
```
guillaume@ubuntu:~/0x01$ ./9-main.py
8044
guillaume@ubuntu:~/0x01$
```

### 10-add.py
**10-add.py** - a file that contains a function that adds two integers and returns the result

**USAGE**
```
guillaume@ubuntu:~/0x01$ ./10-main.py
3
98
98
guillaume@ubuntu:~/0x01$ 
```

### 11-pow.py
**11-pow.py** - it contains a function that computes a to the power of b and return the value.

**USAGE**
```
guillaume@ubuntu:~/0x01$ ./11-main.py
4
9604
1
0.0001
-1024
guillaume@ubuntu:~/0x01$
```

### 12-fizzbuzz.py
**12-fizzbuzz.py** - Contains a function that prints the numbers from 1 to 100 separated by a space.

**USAGE**
```
guillaume@ubuntu:~/0x01$ ./12-main.py | cat -e
1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 17 Fizz 19 Buzz Fizz 22 23 Fizz Buzz 26 Fizz 28 29 FizzBuzz 31 32 Fizz 34 Buzz Fizz 37 38 Fizz Buzz 41 Fizz 43 44 FizzBuzz 46 47 Fizz 49 Buzz Fizz 52 53 Fizz Buzz 56 Fizz 58 59 FizzBuzz 61 62 Fizz 64 Buzz Fizz 67 68 Fizz Buzz 71 Fizz 73 74 FizzBuzz 76 77 Fizz 79 Buzz Fizz 82 83 Fizz Buzz 86 Fizz 88 89 FizzBuzz 91 92 Fizz 94 Buzz Fizz 97 98 Fizz Buzz $
guillaume@ubuntu:~/0x01$
```
### 13-insert_number.c
**13-insert_number.c** - function in C that inserts a number into a sorted singly linked list.


**USAGE**
```
carrie@ubuntu:0x01$ gcc -Wall -Werror -Wextra -pedantic -std=gnu89 13-main.c linked_lists.c 13-insert_number.c -o insert
carrie@ubuntu:0x01$ ./insert
0
1
2
3
4
98
402
1024
-----------------
0
1
2
3
4
27
98
402
1024
carrie@ubuntu:0x01$
```

### 100-print_tebahpla.py 

**100-print_tebahpla.py** - A program that prints the ASCII alphabet, in reverse order, alternating lowercase and uppercase (z in lowercase and Y in uppercase) , not followed by a new line.

**USAGE**
```
guillaume@ubuntu:~/0x01$ ./100-print_tebahpla.py
zYxWvUtSrQpOnMlKjIhGfEdCbAguillaume@ubuntu:~/0x01$
```

### 101-remove_char_at.py

**101-remove_char_at.py** - function that creates a copy of the string, removing the character at the position n (not the Python way, the “C array index”).


**USAGE**
```
guillaume@ubuntu:~/0x01$ ./101-main.py
Bes School
Chcago
 is fun!
School
Python
guillaume@ubuntu:~/0x01$
```

### 102-magic_calculation.py

**102-magic_calculation.py** - It Writes the Python function _def magic_calculation(a, b, c):_ that does exactly the same as the following Python bytecode:

**BYTECODE**
```
3           0 LOAD_FAST                0 (a)
              3 LOAD_FAST                1 (b)
              6 COMPARE_OP               0 (<)
              9 POP_JUMP_IF_FALSE       16

  4          12 LOAD_FAST                2 (c)
             15 RETURN_VALUE

  5     >>   16 LOAD_FAST                2 (c)
             19 LOAD_FAST                1 (b)
             22 COMPARE_OP               4 (>)
             25 POP_JUMP_IF_FALSE       36

  6          28 LOAD_FAST                0 (a)
             31 LOAD_FAST                1 (b)
             34 BINARY_ADD
             35 RETURN_VALUE

  7     >>   36 LOAD_FAST                0 (a)
             39 LOAD_FAST                1 (b)
             42 BINARY_MULTIPLY
             43 LOAD_FAST                2 (c)
             46 BINARY_SUBTRACT
             47 RETURN_VALUE
```
