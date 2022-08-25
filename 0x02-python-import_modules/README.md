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
