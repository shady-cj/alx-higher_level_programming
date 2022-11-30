# 0x12-javascript-warm_up

Learning about Javascript..



## TASKS


### 0. First constant, first print

Write a script that prints “JavaScript is amazing”:

* You must create a constant variable called myVar with the value “JavaScript is amazing”
* You must use console.log(...) to print all output
* You are not allowed to use var

**File**: 0-javascript_is_amazing.js


```
guillaume@ubuntu:~/0x12$ ./0-javascript_is_amazing.js 
JavaScript is amazing
guillaume@ubuntu:~/0x12$ 
guillaume@ubuntu:~/0x12$ semistandard ./0-javascript_is_amazing.js 
guillaume@ubuntu:~/0x12$ 

```


### 1. 3 languages

Write a script that prints 3 lines:

* The first line: “C is fun”
* The second line: “Python is cool”
* The third line: “JavaScript is amazing”
* You must use console.log(...) to print all output
* You are not allowed to use var

**File** - 1-multi_languages.js 


```
guillaume@ubuntu:~/0x12$ ./1-multi_languages.js 
C is fun
Python is cool
JavaScript is amazing
guillaume@ubuntu:~/0x12$ 
```



### 2. Arguments


Write a script that prints a message depending of the number of arguments passed:

* If no arguments are passed to the script, print “No argument”
* If only one argument is passed to the script, print “Argument found”
* Otherwise, print “Arguments found”
* You must use console.log(...) to print all output
* You are not allowed to use var
* Reference: process.argv



```
guillaume@ubuntu:~/0x12$ ./2-arguments.js 
No argument
guillaume@ubuntu:~/0x12$ ./2-arguments.js Best
Argument found
guillaume@ubuntu:~/0x12$ ./2-arguments.js Best School
Arguments found
guillaume@ubuntu:~/0x12$ 
```


### 3. Value of my argument


Write a script that prints the first argument passed to it:

* If no arguments are passed to the script, print “No argument”
* You must use console.log(...) to print all output
* You are not allowed to use var
* You are not allowed to use length


**File** - 3-value_argument.js



```
guillaume@ubuntu:~/0x12$ ./3-value_argument.js 
No argument
guillaume@ubuntu:~/0x12$ ./3-value_argument.js School
School
guillaume@ubuntu:~/0x12$ 
```