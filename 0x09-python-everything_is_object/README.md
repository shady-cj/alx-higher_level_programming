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
