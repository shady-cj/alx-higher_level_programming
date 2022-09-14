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


### 2. Size validation

- Task: Write a class Square that defines a square by: (based on 1-square.py)
* Private instance attribute: size
* Instantiation with optional size: def __init__(self, size=0):
size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
if size is less than 0, raise a ValueError exception with the message size must be >= 
- Files: 2-square.py, 2-main.py

**USAGE**
```
guillaume@ubuntu:~/0x06$ cat 2-main.py
#!/usr/bin/python3
Square = __import__('2-square').Square

my_square_1 = Square(3)
print(type(my_square_1))
print(my_square_1.__dict__)

my_square_2 = Square()
print(type(my_square_2))
print(my_square_2.__dict__)

try:
    print(my_square_1.size)
except Exception as e:
    print(e)

try:
    print(my_square_1.__size)
except Exception as e:
    print(e)

try:
    my_square_3 = Square("3")
    print(type(my_square_3))
    print(my_square_3.__dict__)
except Exception as e:
    print(e)

try:
    my_square_4 = Square(-89)
    print(type(my_square_4))
    print(my_square_4.__dict__)
except Exception as e:
    print(e)

guillaume@ubuntu:~/0x06$ ./2-main.py
<class '2-square.Square'>
{'_Square__size': 3}
<class '2-square.Square'>
{'_Square__size': 0}
'Square' object has no attribute 'size'
'Square' object has no attribute '__size'
size must be an integer
size must be >= 0
guillaume@ubuntu:~/0x06$
```


### 3. Area of a square

- Task: Write a class Square that defines a square by: (based on 2-square.py)
* Private instance attribute: size:
property def size(self): to retrieve it
property setter def size(self, value): to set it:
size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
if size is less than 0, raise a ValueError exception with the message size must be >= 0
* Instantiation with optional size: def __init__(self, size=0):

* Public instance method: def area(self): that returns the current square area
- Files: 3-square.py, 3-main.py

**USAGE**

```
guillaume@ubuntu:~/0x06$ cat 3-main.py
#!/usr/bin/python3
Square = __import__('3-square').Square

my_square_1 = Square(3)
print("Area: {}".format(my_square_1.area()))

try:
    print(my_square_1.size)
except Exception as e:
    print(e)

try:
    print(my_square_1.__size)
except Exception as e:
    print(e)

my_square_2 = Square(5)
print("Area: {}".format(my_square_2.area()))

guillaume@ubuntu:~/0x06$ ./3-main.py
Area: 9
'Square' object has no attribute 'size'
'Square' object has no attribute '__size'
Area: 25
guillaume@ubuntu:~/0x06$
```


### 4. Access and update private attribute

- Task: Write a class Square that defines a square by: (based on 3-square.py)

* Private instance attribute: size:
property def size(self): to retrieve it
property setter def size(self, value): to set it:
size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
if size is less than 0, raise a ValueError exception with the message size must be >= 0
* Instantiation with optional size: def __init__(self, size=0):
* Public instance method: def area(self): that returns the current square area

- Files: 4-square.py, 4-main.py


**USAGE**

```
#!/usr/bin/python3
Square = __import__('4-square').Square

my_square = Square(89)
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

my_square.size = 3
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

try:
    my_square.size = "5 feet"
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))
except Exception as e:
    print(e)
```

### 5. Printing a square

- Task: Write a class Square that defines a square by: (based on 4-square.py)

* Private instance attribute: size:
property def size(self): to retrieve it
property setter def size(self, value): to set it:
size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
if size is less than 0, raise a ValueError exception with the message size must be >= 0
* Instantiation with optional size: def __init__(self, size=0):
* Public instance method: def area(self): that returns the current square area
* Public instance method: def my_print(self): that prints in stdout the square with the character #:
if size is equal to 0, print an empty line


- Files: 5-square.py, 5-main.py


**USAGE**


```
guillaume@ubuntu:~/0x06$ cat 5-main.py
#!/usr/bin/python3
Square = __import__('5-square').Square

my_square = Square(3)
my_square.my_print()

print("--")

my_square.size = 10
my_square.my_print()

print("--")

my_square.size = 0
my_square.my_print()

print("--")

guillaume@ubuntu:~/0x06$ ./5-main.py
###
###
###
--
##########
##########
##########
##########
##########
##########
##########
##########
##########
##########
--

--
guillaume@ubuntu:~/0x06$
```


### 6. Coordinates of a square

- Task: Write a class Square that defines a square by: (based on 5-square.py)

* Private instance attribute: size:
- property def size(self): to retrieve it
- property setter def size(self, value): to set it:
  _size must be an integer, otherwise raise a TypeError exception with the message size must be an integerr_
_if size is less than 0, raise a ValueError exception with the message size must be >= 0_
* Private instance attribute: position:
- property def position(self): to retrieve it
- property setter def position(self, value): to set it:
_position must be a tuple of 2 positive integers, otherwise raise a TypeError exception with the message position must be a tuple of 2 positive integers_
* Instantiation with optional size and optional position: def __init__(self, size=0, position=(0, 0)):
* Public instance method: def area(self): that returns the current square area
* Public instance method: def my_print(self): that prints in stdout the square with the character #:
- if size is equal to 0, print an empty line
- position should be use by using space - Don’t fill lines by spaces when position[1] > 0


- Files: 6-square.py, 6-main.py

**USAGE**

```
guillaume@ubuntu:~/0x06$ cat 6-main.py
#!/usr/bin/python3
Square = __import__('6-square').Square

my_square_1 = Square(3)
my_square_1.my_print()

print("--")

my_square_2 = Square(3, (1, 1))
my_square_2.my_print()

print("--")

my_square_3 = Square(3, (3, 0))
my_square_3.my_print()

print("--")

guillaume@ubuntu:~/0x06$ ./6-main.py | tr " " "_" | cat -e
###$
###$
###$
--$
$
_###$
_###$
_###$
--$
___###$
___###$
___###$
--$
guillaume@ubuntu:~/0x06$
```

### 7. Singly linked list

- Task: create Singly Linked List using The Node class and the Singly List class
- Files: 100-singly_linked_list.py, 100-main.py

**USAGE**
```
guillaume@ubuntu:~/0x06$ cat 100-main.py
#!/usr/bin/python3
SinglyLinkedList = __import__('100-singly_linked_list').SinglyLinkedList

sll = SinglyLinkedList()
sll.sorted_insert(2)
sll.sorted_insert(5)
sll.sorted_insert(3)
sll.sorted_insert(10)
sll.sorted_insert(1)
sll.sorted_insert(-4)
sll.sorted_insert(-3)
sll.sorted_insert(4)
sll.sorted_insert(5)
sll.sorted_insert(12)
sll.sorted_insert(3)
print(sll)

guillaume@ubuntu:~/0x06$ ./100-main.py
-4
-3
1
2
3
3
4
5
5
10
12
guillaume@ubuntu:~/0x06$
```


### 8. Print Square instance

- Task: Write a class Square that defines a square by: (based on 5-square.py)

* Private instance attribute: size:
- property def size(self): to retrieve it
- property setter def size(self, value): to set it:
  _size must be an integer, otherwise raise a TypeError exception with the message size must be an integerr_
_if size is less than 0, raise a ValueError exception with the message size must be >= 0_
* Private instance attribute: position:
- property def position(self): to retrieve it
- property setter def position(self, value): to set it:
_position must be a tuple of 2 positive integers, otherwise raise a TypeError exception with the message position must be a tuple of 2 positive integers_
* Instantiation with optional size and optional position: def __init__(self, size=0, position=(0, 0)):
* Public instance method: `def area(self):` that returns the current square area
* Public instance method: `def my_print(self):` that prints in stdout the square with the character #:
- if size is equal to 0, print an empty line
- position should be use by using space - Don’t fill lines by spaces when position[1] > 0
- Printing a `Square` instance should have the same behavior as `my_print()`

- Files: 101-square.py, 101-main.py

**USAGE**

```
guillaume@ubuntu:~/0x06$ cat 101-main.py
#!/usr/bin/python3
Square = __import__('101-square').Square

my_square = Square(5, (0, 0))
print(my_square)

print("--")

my_square = Square(5, (4, 1))
print(my_square)

guillaume@ubuntu:~/0x06$ ./101-main.py | tr " " "_" | cat -e
#####$
#####$
#####$
#####$
#####$
--$
$
____#####$
____#####$
____#####$
____#####$
____#####$
guillaume@ubuntu:~/0x06$
```


### 9. Compare 2 squares

- Task: based on `4-square.py` extend the class `Square` to make sure the Square instance can answer to comparators: ==, !=, >, >=, < and <= based on the square area

- Files: 102-square.py, 102-main.py

**USAGE**

```
guillaume@ubuntu:~/0x06$ cat 102-main.py
#!/usr/bin/python3
Square = __import__('102-square').Square

s_5 = Square(5)
s_6 = Square(6)

if s_5 < s_6:
    print("Square 5 < Square 6")
if s_5 <= s_6:
    print("Square 5 <= Square 6")
if s_5 == s_6:
    print("Square 5 == Square 6")
if s_5 != s_6:
    print("Square 5 != Square 6")
if s_5 > s_6:
    print("Square 5 > Square 6")
if s_5 >= s_6:
    print("Square 5 >= Square 6")

guillaume@ubuntu:~/0x06$ ./102-main.py
Square 5 < Square 6
Square 5 <= Square 6
Square 5 != Square 6
guillaume@ubuntu:~/0x06$
```
