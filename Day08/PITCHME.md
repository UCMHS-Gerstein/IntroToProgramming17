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

1. ```def``` tells Python we're creating a function
2. ```inches_to_cm``` is the name of the function, which we use to *call* it |
3. ```()``` is where arguments go |
4. ```inches``` is an argument being *passed into* the function |
5. ```:``` indicates that we're about to create a *block of code* |
+++
```python
def inches_to_cm(inches):
    """takes a number of inches, converts it to cm, returns it as a float"""
    cm = inches * 2.54
    return cm
```

6. ```"""takes a number...as a float"""``` is a docstring
7. ```    cm = inches * 2.54``` creates a variable with a calculated value |
8. ```    return cm``` will exit the function (because of ```return```) and make the value of ```cm``` the function's output |