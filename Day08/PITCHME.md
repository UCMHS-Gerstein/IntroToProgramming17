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

- ```def``` tells Python we're creating a function
- ```inches_to_cm``` is the name of the function, which we use to *call* it |
- ```()``` is where arguments go |
- ```inches``` is an argument being *passed into* the function |
- ```:``` indicates that we're about to create a *block of code* |
+++
```python
def inches_to_cm(inches):
    """takes a number of inches, converts it to cm, returns it as a float"""
    cm = inches * 2.54
    return cm
```

- ```"""takes a number...as a float"""``` is a docstring
- ```    cm = inches * 2.54``` creates a variable with a calculated value |
- ```    return cm``` will exit the function (because of ```return```) and make the value of ```cm``` the function's output |