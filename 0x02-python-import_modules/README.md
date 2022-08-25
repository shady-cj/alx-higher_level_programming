# 0x02-python-import_modules

This section visits the concept of python modules import and packages

## TASKS

### 0-add.py
**0-add.py** - A program that imports the function `def add(a, b):` from the file `add_0.py` and prints the result of the addition `1 + 2 = 3`

**USAGE**
```
guillaume@ubuntu:~/0x02$ ./0-add.py
1 + 2 = 3
```

### 1-calculation.py
**1-calculation.py** -  A program that imports functions from the file calculator_1.py, does some Maths, and prints the result.

**USAGE**
```
guillaume@ubuntu:~/0x02$ ./1-calculation.py
10 + 5 = 15
10 - 5 = 5
10 * 5 = 50
10 / 5 = 2
guillaume@ubuntu:~/0x02$
```

### 2-args.py
**2-args.py** -  A program that prints the number of and the list of its arguments.

**USAGE**
```
guillaume@ubuntu:~/0x02$ ./2-args.py
0 arguments.
guillaume@ubuntu:~/0x02$ ./2-args.py Hello
1 argument:
1: Hello
guillaume@ubuntu:~/0x02$ ./2-args.py Hello Welcome To The Best School
6 arguments:
1: Hello
2: Welcome
3: To
4: The
5: Best
6: School
guillaume@ubuntu:~/0x02$
```

### 3-infinite_add.py
**3-infinite_add.py** - A program that prints the result of the addition of all arguments

**USAGE**
```
guillaume@ubuntu:~/0x02$ ./3-infinite_add.py
0
guillaume@ubuntu:~/0x02$ ./3-infinite_add.py 79 10
89
guillaume@ubuntu:~/0x02$ ./3-infinite_add.py 79 10 -40 -300 89
-162
guillaume@ubuntu:~/0x02$
```

### 4-hidden_discovery.py
**4-hidden_discovery.py** -  a program that prints all the names defined by the compiled module `hidden_4.pyc` (please download it locally). This only works on python 3.8

**USAGE**
```
guillaume@ubuntu:~/0x02$ ./4-hidden_discovery.py | sort
my_secret_santa
print_hidden
print_school
guillaume@ubuntu:~/0x02$
```

### 5-variable_load.py
**5-variable_load.py** -  a program that imports the variable `a` from the file `variable_load_5.py` and prints its value.


### 100-my_calculator.py
**100-my_calculator.py** - a program that imports all functions from the file calculator_1.py and handles basic operations. from the command line.

**USAGE**
```
guillaume@ubuntu:~/0x02$ ./100-my_calculator.py ; echo $?
Usage: ./100-my_calculator.py <a> <operator> <b>
1
guillaume@ubuntu:~/0x02$ ./100-my_calculator.py 3 + 5 ; echo $?
3 + 5 = 8
0
guillaume@ubuntu:~/0x02$ ./100-my_calculator.py 3 H 5 ; echo $?
Unknown operator. Available operators: +, -, * and /
1
guillaume@ubuntu:~/0x02$
```


### 101-easy_print.py
**101-easy_print.py** - a program that prints `#pythoniscool`, followed by a new line, in the standard output with the use of print or eval or open or import sys

**USAGE**
```
guillaume@ubuntu:~/0x02$ ./101-easy_print.py
#pythoniscool
guillaume@ubuntu:~/0x02$
```

### 103-fast_alphabet.py
**103-fast_alphabet.py** -  a program that prints the alphabet in uppercase, followed by a new line.
without using:
* any loops
* any conditional statements
* str.join()
* any string literal
* any system calls
**USAGE**

```
guillaume@ubuntu:~/0x02$ ./103-fast_alphabet.py
ABCDEFGHIJKLMNOPQRSTUVWXYZ
guillaume@ubuntu:~/0x02$ wc -l 103-fast_alphabet.py
3 103-fast_alphabet.py
guillaume@ubuntu:~/0x02$
```
