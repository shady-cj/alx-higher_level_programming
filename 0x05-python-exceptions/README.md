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
