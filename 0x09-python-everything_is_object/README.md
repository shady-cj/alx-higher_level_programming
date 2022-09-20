# 0x09-python-everything_is_object

This section dives deeper into python's objects, mutability, cloning, aliasing etc.

## TASKS

### 0. Who am I?

- ***Task*** - What function would you use to print the type of an object?

Write the name of the function in the file, without ()...
- ***Files*** - 0-answer.txt

### 1. Where are you?

- ***Task*** - How do you get the variable identifier (which is the memory address in the CPython implementation)?
- ***Files*** - 1-answer.txt


### 2. Right count

- ***Task*** - In the following code, do `a` and `b` point to the same object? Answer with Yes or No.
- ***Files*** - 2-answer.txt

**Sample**

```
>>> a = 89
>>> b = 100
```


### 3. Right count =
- ***Task*** - In the following code, do `a` and `b` point to the same object? Answer with Yes or No.

- ***Files*** - 3-answer.txt

**Sample**

```
>>> a = 89
>>> b = 89
```


### 4. Right count =

- ***Task*** - In the following code, do `a` and `b` point to the same object? Answer with Yes or No.
- ***Files*** - 4-answer.txt


**Sample**
```
>>> a = 89
>>> b = a
```

### 5. Right count =+

- ***Task*** - In the following code, do `a` and `b` point to the same object? Answer with Yes or No.
- ***Files*** - 5-answer.txt


**Sample**
```
>>> a = 89
>>> b = a + 1
```


### 6. Is equal

- ***Task*** - What do these 3 lines print?
- ***Files*** - 6-answer.txt

**Sample**
```
>>> s1 = "Best School"
>>> s2 = s1
>>> print(s1 == s2)
```


### 7. Is the same

- ***Task*** - What do these 3 lines print?
- ***Files*** - 7-answer.txt

**Sample**

```
>>> s1 = "Best"
>>> s2 = s1
>>> print(s1 is s2)
```


### 8. Is really equal

- ***Task*** - What do these 3 lines print?
- ***Files*** - 8-answer.txt

**Sample**

```
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 == s2)
```



### 9. Is really the same

- ***Task*** - What do these 3 lines print?
- ***Files*** - 9-answer.txt

**Sample**

```
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 is s2)
```

### 10. And with a list, is it equal

- ***Task*** - What do these 3 lines print?
- ***Files*** - 10-answer.txt

**Sample**

```
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 == l2)
```

### 11. And with a list, is it the same

- ***Task*** - What do these 3 lines print?
- ***Files*** - 11-answer.txt

**Sample**

```
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 is l2)
```

### 12. And with a list, is it really equal

- ***Task*** - What do these 3 lines print?
- ***Files*** - 12-answer.txt

**Sample**

```
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 == l2)
```

### 13. And with a list, is it really the same

- ***Task*** - What do these 3 lines print?
- ***Files*** - 13-answer.txt

**Sample**

```
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 is l2)
```

### 14. List append

- ***Task*** - What does this script print?
- ***Files*** - 14-answer.txt

**Sample**

```
l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)
```



### 15. List add

- ***Task*** - What does this script print?
- ***Files*** - 15-answer.txt

**Sample**

```
l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2)
```


### 16. Integer incrementation

- ***Task*** - What does this script print?
- ***Files*** - 16-answer.txt

**Sample**

```
def increment(n):
    n += 1

a = 1
increment(a)
print(a)
```


### 17. List incrementation

- ***Task*** - What does this script print?
- ***Files*** - 17-answer.txt

**Sample**

```
def increment(n):
    n.append(4)

l = [1, 2, 3]
increment(l)
print(l)
```

### 18. List assignation

- ***Task*** - What does this script print?
- ***Files*** - 18-answer.txt

**Sample**

```
def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)
```


### 19. Copy a list object

- ***Task*** - Write a function `def copy_list(l):` that returns a copy of a list.

	- The input list can contain any type of objects
	- Your file should be maximum 3-line long (no documentation needed)
	- You are not allowed to import any module

- ***Files*** - 19-copy_list.py, 19-main.py

**USAGE**

```
guillaume@ubuntu:~/0x09$ cat 19-main.py
#!/usr/bin/python3
copy_list = __import__('19-copy_list').copy_list

my_list = [1, 2, 3]
print(my_list)

new_list = copy_list(my_list)

print(my_list)
print(new_list)

print(new_list == my_list)
print(new_list is my_list)

guillaume@ubuntu:~/0x09$ ./19-main.py
[1, 2, 3]
[1, 2, 3]
[1, 2, 3]
True
False
guillaume@ubuntu:~/0x09$ wc -l 19-copy_list.py
3 19-copy_list.py
guillaume@ubuntu:~/0x09$
```


### 20. Tuple or not?

- ***Task***
	```
	a = ()
	```
Is `a` a tuple? Answer with Yes or No.

- ***Files*** - 20-answer.txt



### 21. Tuple or not?

- ***Task***
	```
	a = (1, 2)
	```
Is `a` a tuple? Answer with Yes or No.

- ***Files*** - 21-answer.txt


### 22. Tuple or not?

- ***Task***
	```
	a = (1)
	```
Is `a` a tuple? Answer with Yes or No.

- ***Files*** - 22-answer.txt




### 23. Tuple or not?

- ***Task***
	```
	a = (1, )
	```
Is `a` a tuple? Answer with Yes or No.

- ***Files*** - 23-answer.txt



### 24. Who I am?

- ***Task*** - What does this script print?
- ***Files*** - 24-answer.txt

**Sample**

```
a = (1)
b = (1)
a is b
```

### 25. Tuple or not

- ***Task*** - What does this script print?
- ***Files*** - 25-answer.txt

**Sample**

```
a = (1, 2)
b = (1, 2)
a is b
```

### 26. Empty is not empty

- ***Task*** - What does this script print?
- ***Files*** - 26-answer.txt

**Sample**

```
a = ()
b = ()
a is b
```


### 27. Still the same?

- ***Task*** 
	```
	>>> id(a)
	139926795932424
	>>> a
	[1, 2, 3, 4]
	>>> a = a + [5]
	>>> id(a)
	```
Will the last line of this script print 139926795932424? Answer with Yes or No.

- ***Files*** - 27-answer.txt




### 28. Same or not?

- ***Task*** 
	```
	>>> a
	[1, 2, 3]
	>>> id (a)
	139926795932424
	>>> a += [4]
	>>> id(a)
	```
Will the last line of this script print 139926795932424? Answer with Yes or No.

- ***Files*** - 28-answer.txt



### 29. #pythonic

- ***Task*** - Write a function `magic_string()` that returns a string “BestSchool” n times the number of the iteration (see code):

	- Format: see example
	- Your file should be maximum 4-line long (no documentation needed)
	- You are not allowed to import any module

- ***Files*** - 100-magic_string.py, 100-main.py

**USAGE**

```
guillaume@ubuntu:~/0x09$ cat 100-main.py
#!/usr/bin/python3
magic_string = __import__('100-magic_string').magic_string

for i in range(10):
    print(magic_string())

guillaume@ubuntu:~/0x09$ ./100-main.py | cat -e
BestSchool$
BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool$
guillaume@ubuntu:~/0x09$ wc -l 100-magic_string.py
4 100-magic_string.py
guillaume@ubuntu:~/0x09$
```




### 30. Low memory cost

- ***Task*** - Write a `class LockedClass` with no class or object attribute, that prevents the user from dynamically creating new instance attributes, except if the new instance attribute is called first_name.

You are not allowed to import any module

- ***Files*** - 101-locked_class.py, 101-main.py
```
guillaume@ubuntu:~/0x09$ cat 101-main.py
#!/usr/bin/python3
LockedClass = __import__('101-locked_class').LockedClass

lc = LockedClass()
lc.first_name = "John"
try:
    lc.last_name = "Snow"
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

guillaume@ubuntu:~/0x09$ ./101-main.py
[AttributeError] 'LockedClass' object has no attribute 'last_name'
guillaume@ubuntu:~/0x09$
```


### 31. int 1/3

- ***Task*** - Assuming we are using a CPython implementation of Python3 with default options/configuration:

	- How many int objects are created by the execution of the first line of the script? (103-line1.txt)
	- How many int objects are created by the execution of the second line of the script (103-line2.txt)
- ***Files*** - 103-line1.txt, 103-line2.txt

**Sample**

```
julien@ubuntu:/python3$ cat int.py
a = 1
b = 1
julien@ubuntu:/python3$
```


### 32. int 2/3

- ***Task*** - Assuming we are using a CPython implementation of Python3 with default options/configuration:

	- How many int objects are created by the execution of the first line of the script? (`104-line1.txt`)
	- How many int objects are created by the execution of the second line of the script (`104-line2.txt`)
	- After the execution of line 3, is the int object pointed by a deleted? Answer with Yes or No (`104-line3.txt`)
	- After the execution of line 4, is the int object pointed by b deleted? Answer with Yes or No (`104-line4.txt`)
	- How many int objects are created by the execution of the last line of the script (`104-line5.txt`)

- ***Files*** - 104-line1.txt, 104-line2.txt, 104-line3.txt, 104-line4.txt, 104-line5.txt
