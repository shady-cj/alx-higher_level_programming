# 0x08-python-more_classes

Deeper dive into classes, classmethod, staticmethods...

## TASKS

### 0. Simple rectangle

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


### 1. Real definition of a rectangle

- ***Task*** - Write a class Rectangle that defines a rectangle by: (based on 0-rectangle.py)

	- Private instance attribute: width:
	- property `def width(self):` to retrieve it
	- property setter def width(self, value): to set it:
	- width must be an integer, otherwise raise a TypeError exception with the message width must be an integer
	- if width is less than 0, raise a ValueError exception with the message width must be >= 0
	- Private instance attribute: height:
	- property `def height(self):` to retrieve it
	- property setter `def height(self, value):` to set it:
	- height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
	- if height is less than 0, raise a ValueError exception with the message height must be >= 0
	- Instantiation with optional width and height: `def __init__(self, width=0, height=0):`
- ***Files*** - 1-rectangle.py, 1-main.py

**USAGE**
```
guillaume@ubuntu:~/0x08$ cat 1-main.py
#!/usr/bin/python3
Rectangle = __import__('1-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print(my_rectangle.__dict__)

my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle.__dict__)

guillaume@ubuntu:~/0x08$ ./1-main.py
{'_Rectangle__height': 4, '_Rectangle__width': 2}
{'_Rectangle__height': 3, '_Rectangle__width': 10}
guillaume@ubuntu:~/0x08$ 
```

### 2. Area and Perimeter

- ***Task*** - Write a class Rectangle that defines a rectangle by: (based on 1-rectangle.py)

	- Private instance attribute: width:
		- property `def width(self):` to retrieve it
		- property setter def width(self, value): to set it:
			- width must be an integer, otherwise raise a TypeError exception with the message width must be an integer
			- if width is less than 0, raise a ValueError exception with the message width must be >= 0
	- Private instance attribute: height:
		- property `def height(self):` to retrieve it
		- property setter `def height(self, value):` to set it:
			- height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
			- if height is less than 0, raise a ValueError exception with the message height must be >= 0
	- Instantiation with optional width and height: def __init__(self, width=0, height=0):
	- Public instance method: def area(self): that returns the rectangle area
	- Public instance method: def perimeter(self): that returns the rectangle perimeter:
	- if width or height is equal to 0, perimeter is equal to 0

- ***Files*** - 2-rectangle.py, 2-main.py

**USAGE**

```
guillaume@ubuntu:~/0x08$ cat 2-main.py
#!/usr/bin/python3
Rectangle = __import__('2-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

print("--")

my_rectangle.width = 10
my_rectangle.height = 3
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

guillaume@ubuntu:~/0x08$ ./2-main.py
Area: 8 - Perimeter: 12
--
Area: 30 - Perimeter: 26
guillaume@ubuntu:~/0x08$
```

### 3. String representation

- ***Task*** - Write a class Rectangle that defines a rectangle by: (based on 2-rectangle.py)

	- Private instance attribute: width:
		- property `def width(self):` to retrieve it
		- property setter def width(self, value): to set it:
			- width must be an integer, otherwise raise a TypeError exception with the message width must be an integer
			- if width is less than 0, raise a ValueError exception with the message width must be >= 0
	- Private instance attribute: height:
		- property `def height(self):` to retrieve it
		- property setter `def height(self, value):` to set it:
			- height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
			- if height is less than 0, raise a ValueError exception with the message height must be >= 0
	- Instantiation with optional width and height: def __init__(self, width=0, height=0):
	- Public instance method: `def area(self):` that returns the rectangle area
	- Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
		- if width or height is equal to 0, perimeter is equal to 0
	- `print()` and `str()` should print the rectangle with the character #: (see example below)
		- if width or height is equal to 0, return an empty string
- ***Files*** - 3-rectangle.py, 3-main.py

**USAGE**

```
guillaume@ubuntu:~/0x08$ cat 3-main.py
#!/usr/bin/python3
Rectangle = __import__('3-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

print(str(my_rectangle))
print(repr(my_rectangle))

print("--")

my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle)
print(repr(my_rectangle))

guillaume@ubuntu:~/0x08$ ./3-main.py
Area: 8 - Perimeter: 12
##
##
##
##
<3-rectangle.Rectangle object at 0x7f92a75a2eb8>
--
##########
##########
##########
<3-rectangle.Rectangle object at 0x7f92a75a2eb8>
guillaume@ubuntu:~/0x08$
```
