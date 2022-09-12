# 0x05-python-exceptions

Learning about Python exceptions. Handling, raising errors.

## TASKS

### 0. Safe list printing
 
- Task: Write a function that prints x elements of a list.
- Files: 0-safe_print_list.py, 0-main.py

**USAGE**

```
guillaume@ubuntu:~/0x05$ ./0-main.py
12
nb_print: 2
12345
nb_print: 5
12345
nb_print: 5
guillaume@ubuntu:~/0x05$
```


### 1. Safe printing of an integers list

- Task: Write a function that prints an integer with `"{:d}".format().`
- Files: 1-safe_print_integer.py, 1-main.py

**USAGE**

```
guillaume@ubuntu:~/0x05$ ./1-main.py
89
-89
School is not an integer
```


### 2. Print and count integers

- Task: Write a function that prints the first x elements of a list and only integers.
- Files: 2-safe_print_list_integers.py, 2-main.py

**USAGE**

```
guillaume@ubuntu:~/0x05$ ./2-main.py
12
nb_print: 2
12345
nb_print: 5
12345Traceback (most recent call last):
  File "./2-main.py", line 14, in <module>
    nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
  File "/0x05/2-safe_print_list_integers.py", line 7, in safe_print_list_integers
    print("{:d}".format(my_list[i]), end="")
IndexError: list index out of range
guillaume@ubuntu:~/0x05$
```

### 3. Integers division with debug

- Task: Write a function that divides 2 integers and prints the result.
- Files: 3-safe_print_division.py, 3-main.py


**USAGE**
```
guillaume@ubuntu:~/0x05$ ./3-main.py
Inside result: 6.0
12 / 2 = 6.0
Inside result: None
12 / 0 = None
guillaume@ubuntu:~/0x05$
```

### 4. Divide a list

- Task: Write a function that divides element by element 2 lists.
- Files: 4-main.py, 4-list_division.py

**USAGE**
```
#!/usr/bin/python3
list_division = __import__('4-list_division').list_division

my_l_1 = [10, 8, 4]
my_l_2 = [2, 4, 4]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)

print("--")

my_l_1 = [10, 8, 4, 4]
my_l_2 = [2, 0, "H", 2, 7]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)

```


### 5. Raise exception

- Task: Write a function that raises a type exception.
- Files: 5-raise_exception.py, 5-main.py

**USAGE**
```
guillaume@ubuntu:~/0x05$ cat 5-main.py
#!/usr/bin/python3
raise_exception = __import__('5-raise_exception').raise_exception

try:
    raise_exception()
except TypeError as te:
    print("Exception raised")

guillaume@ubuntu:~/0x05$ ./5-main.py
Exception raised
guillaume@ubuntu:~/0x05$
```
