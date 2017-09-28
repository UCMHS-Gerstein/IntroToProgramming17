---
# Functions

Intro to Programming - Day 8
---
# Function

A reusable piece of code

```python
def say_hi_to(person):
    """says hello to the person given as an argument"""
    print(f"Hello, {person}. How are you today?")
```

```python
def inches_to_cm(inches):
    """takes a number of inches, converts it to cm, returns it as a float"""
    cm = inches * 2.54
    return cm
```
---
## Defining a function

```python
def inches_to_cm(inches):
    """takes a number of inches, converts it to cm, returns it as a float"""
    cm = inches * 2.54
    return cm
```

* ```def``` tells Python we're creating a function
* ```inches_to_cm``` is the name of the function, which we use to *call* it
* ```()``` is where arguments go
* ```inches``` is an argument being *passed into* the function
* ```:``` indicates that we're about to create a *block of code*
+++
```python
def inches_to_cm(inches):
    """takes a number of inches, converts it to cm, returns it as a float"""
    cm = inches * 2.54
    return cm
```

* ```"""takes a number...as a float"""``` is a docstring
* ```    cm = inches * 2.54``` creates a variable with a calculated value
* ```    return cm``` will exit the function (because of ```return```) and make the value of ```cm``` the function's output
---
# Snippets

Scroll down for function snippets
+++
```python
def say_hello():
    """Prints hello"""
    # insert code in here to print hello


# Print hello
say_hello()
```
+++
```python
def fifty():
    """Returns 50"""
    # insert code in here to return 50


# Should print 100
print(fifty() * 2)
```
+++
```python
def add_them_all(n1, n2, n3, n4, n5):
    """Returns sum of five numbers"""
    #insert code in here to return the sum of all 5 arguments


# Should print 111
print(add_them_all(1, 3, 5, 2, 100))
```
---
## Create a function from scratch

In day08.py, create a function called ```find_hypotenuse()``` with two parameters - **a** and **b**. This function should return the hypotenuse of a triangle with sides a and b. Make sure you call the function a few times and see if it works.

For square root, you can either use exponents or import the ```sqrt()``` function using the following line at the top of your program.

```python
from math import sqrt
```