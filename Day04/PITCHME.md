---
# Getting Started with PythonAnywhere

Intro to Programming - Day 4
---
# Do Now

Go to [PythonAnywhere](http://www.pythonanywhere.com) and sign up for an account

If you get an error *check your email before you try again*

Go to your account page and add me as your teacher under the **Teacher** tab

My username is jgerstein
---
# Account Page

![teacher](Day04/assets/teacher.PNG)
---
# Objectives

* Sign up for PythonAnywhere
* Perform basic command line operations
* Run code in interactive mode
---
# Vocabulary

* terminal/command line
* operator
* function
---
# Command Line Tools

* ```dir```
* ```ls```
* ```cd```
* ```mkdir```
* ```rm```
* ```touch```
* ```python3```
---
# Functions

* ```print()```
* ```help()```
* ```exit()```
---
# Command Line

* Open up a Bash console
* We're going to try using ```dir```, ```ls```, ```cd```, ```touch```, ```mkdir```, ```rm``` and ```mv```
---
# Interactive Python

* Open up an iPython 3.6 console
* Try doing simple calculations like ``` 3 + 5``` or ```1043 / 23```
* What happens with more advanced calculations?
+++
## Try some code:

```python
print('hello world')
```
---
# Text Editor

* Go to **Files** and create a file called ```hello.py```
* In that file, add some code and we'll look at ways to run it:

```python
print('hello world')
```
+++
## More Advanced Code

```python
import random

print("Generating a random number from 1 to 10")
print("...")
print("...")
print("...")
print(random.randint(1,10))
```
+++
## Making It More Efficient

```python
import random

print("Generating a random number from 1 to 10")
for x in range(100):
    print("...")
print(random.randint(1,10))
```
+++
## Getting Lots of Numbers

```python
import random

print("Generating 1000 random numbers")
for x in range(1000):
    print(random.randint(1,10))
```