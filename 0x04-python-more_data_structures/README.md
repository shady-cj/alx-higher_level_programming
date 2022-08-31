# 0x04-python-more_data_structures

Learning more about data structures in python using dictionaries and other functions like map, reduce, filter.. etc..

## TASKS

### 0-square_matrix_simple.py
**0-square_matrix_simple.py** - A function that computes the square value of all integers of a 2 dimensional matrix.

**USAGE**

```
guillaume@ubuntu:~/0x04$ ./0-main.py
[[1, 4, 9], [16, 25, 36], [49, 64, 81]]
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
guillaume@ubuntu:~/0x04$
```


### 1-search_replace.py
**1-search_replace.py** - A function that replaces all occurrences of an element by another in a new list.

**USAGE**
```
guillaume@ubuntu:~/0x04$ ./1-main.py
[1, 89, 3, 4, 5, 4, 89, 1, 1, 4, 89]
[1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
guillaume@ubuntu:~/0x04$
```

### 2-uniq_add.py

**2-uniq_add.py** - A function that adds all unique integers in a list (only once for each integer).


**USAGE**
```
guillaume@ubuntu:~/0x04$ ./2-main.py
Result: 15
guillaume@ubuntu:~/0x04$
```


### 3-common_elements.py

**3-common_elements.py** - A function that returns a set of common elements in two sets.

**USAGE**

```
guillaume@ubuntu:~/0x04$ ./3-main.py
['C']
guillaume@ubuntu:~/0x04$
```


### 4-only_diff_elements.py

**4-only_diff_elements.py** - A function that returns a set of all elements present in only one set.

**USAGE**

```
guillaume@ubuntu:~/0x04$ cat 4-main.py
#!/usr/bin/python3
only_diff_elements = __import__('4-only_diff_elements').only_diff_elements

set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl" }
od_set = only_diff_elements(set_1, set_2)
print(sorted(list(od_set)))

guillaume@ubuntu:~/0x04$ ./4-main.py
['Bash', 'Javascript', 'Perl', 'Python', 'Ruby']
guillaume@ubuntu:~/0x04$
```


### 5-number_keys.py

**5-number_keys.py** - A function that returns the number of keys in a dictionary.


**USAGE**

```
guillaume@ubuntu:~/0x04$ cat 5-main.py
#!/usr/bin/python3
number_keys = __import__('5-number_keys').number_keys

a_dictionary = { 'language': "C", 'number': 13, 'track': "Low level" }
nb_keys = number_keys(a_dictionary)
print("Number of keys: {:d}".format(nb_keys))

guillaume@ubuntu:~/0x04$ ./5-main.py
Number of keys: 3
guillaume@ubuntu:~/0x04$ 
```


### 6-print_sorted_dictionary.py

**6-print_sorted_dictionary.py** - function that prints a dictionary by ordered keys. it involves sorting a dictionary


**USAGE**

```
guillaume@ubuntu:~/0x04$ cat 6-main.py
#!/usr/bin/python3
print_sorted_dictionary = __import__('6-print_sorted_dictionary').print_sorted_dictionary

a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3] }
print_sorted_dictionary(a_dictionary)

guillaume@ubuntu:~/0x04$ ./6-main.py
Number: 89
ids: [1, 2, 3]
language: C
track: Low level
guillaume@ubuntu:~/0x04$ 
```
