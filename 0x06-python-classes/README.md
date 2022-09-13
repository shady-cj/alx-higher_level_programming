# 0x06-python-classes

Understanding the concept of object oriented programming using class in python and also ubderstanding the various terminologies such as instance, objects, methods, class attributes, instance attributes, public, private and protected attributes.

## TASKS

### 0. My first square

- Task: Write an empty class Square that defines a square
- Files: 0-square.py, 0-main.py

**USAGE**

```
guillaume@ubuntu:~/0x06$ cat 0-main.py
#!/usr/bin/python3
Square = __import__('0-square').Square

my_square = Square()
print(type(my_square))
print(my_square.__dict__)

guillaume@ubuntu:~/0x06$ ./0-main.py
<class '0-square.Square'>
{}
guillaume@ubuntu:~/0x06$
```
