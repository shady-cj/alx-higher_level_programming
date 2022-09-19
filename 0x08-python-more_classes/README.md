# 0x08-python-more_classes

Deeper dive into classes, classmethod, staticmethods...

## TASKS

### 0x08-python-more_classes

- ***Task*** - Write an empty class `Rectangle` that defines a rectangle
- ***Files*** - 0-rectangle.py, 0-main.py

**USAGE**
```
guillaume@ubuntu:~/0x08$ cat 0-main.py
#!/usr/bin/python3
Rectangle = __import__('0-rectangle').Rectangle

my_rectangle = Rectangle()
print(type(my_rectangle))
print(my_rectangle.__dict__)

guillaume@ubuntu:~/0x08$ ./0-main.py
<class '0-rectangle.Rectangle'>
{}
guillaume@ubuntu:~/0x08$
```
