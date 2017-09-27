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
    """takes a number of inches and converts it to cm before returning as a float"""
    cm = inches * 2.54
    return cm
```
---
## Creating a function

```python
def inches_to_cm(inches):
    """takes a number of inches and converts it to cm before returning as a float"""
    cm = inches * 2.54
    return cm
```

1. ```def``` tells Python we're creating a function
2. ```inches_to_cm``` is the name of the function, which we use to *call* it
3. ```()``` is where arguments go
4. ```inches``` is an argument being *passed into* the function
5. ```:``` indicates that we're about to create a *block of code*. Indentation on subsequent lines indicates that they belong to that block
6. ```"""takes a number...as a float"""``` is a docstring, and indicates what the function does. Used by Python's internal help/documentation system
7. ```    cm = inches * 2.54``` creates a variable with a value calculated using the value that was passed in
8. ```    return cm``` will exit the function (because of ```return``` and make the value of ```cm``` the function's output 