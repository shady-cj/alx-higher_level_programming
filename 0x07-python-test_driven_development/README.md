# 0x07-python-test_driven_development

Learning about test driven development and different types of software testing some of which include

1. Functional Testing
2. Unit Testing
3. Integration Testing
4. Regression Testing
5. System Testing.
6. Non-Functional Testing: Load Testing(Performance and speed tests), Security Test.
7. Usability Testing
8. Portability Testing.. etc.

**NOTE**: MAKE SURE TO RUN `source ./python_path.sh` This will store the present path in the PYTHONPATH environment variable

## TASKS

### 0. Integers addition
- Task: Write a function that adds 2 integers.
- Files: 0-add_integer.py, tests/0-add_integer.txt, 0-main.py

**USAGE**
```
guillaume@ubuntu:~/0x07$ cat 0-main.py
#!/usr/bin/python3
add_integer = __import__('0-add_integer').add_integer

print(add_integer(1, 2))
print(add_integer(100, -2))
print(add_integer(2))
print(add_integer(100.3, -2))
try:
    print(add_integer(4, "School"))
except Exception as e:
    print(e)
try:
    print(add_integer(None))
except Exception as e:
    print(e)

guillaume@ubuntu:~/0x07$ ./0-main.py
3
98
100
98
b must be an integer
a must be an integer
guillaume@ubuntu:~/0x07$ python3 -m doctest -v ./tests/0-add_integer.txt | tail -2
19 passed and 0 failed.
Test passed.
guillaume@ubuntu:~/0x07$ python3 -c 'print(__import__("0-add_integer").__doc__)' | wc -l
9
guillaume@ubuntu:~/0x07$ python3 -c 'print(__import__("0-add_integer").add_integer.__doc__)' | wc -l
6
guillaume@ubuntu:~/0x07$
```
