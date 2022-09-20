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


