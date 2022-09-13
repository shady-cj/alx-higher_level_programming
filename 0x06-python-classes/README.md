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


### 1. Square with size
- Task: Write a class Square that defines a square by: (based on 0-square.py)
- Files: 1-square.py, 1-main.py

**USAGE**
```
guillaume@ubuntu:~/0x06$ cat 1-main.py
#!/usr/bin/python3
Square = __import__('1-square').Square

my_square = Square(3)
print(type(my_square))
print(my_square.__dict__)

try:
    print(my_square.size)
except Exception as e:
    print(e)

try:
    print(my_square.__size)
except Exception as e:
    print(e)

guillaume@ubuntu:~/0x06$ ./1-main.py
<class '1-square.Square'>
{'_Square__size': 3}
'Square' object has no attribute 'size'
'Square' object has no attribute '__size'
guillaume@ubuntu:~/0x06$
```
