---
# Object Oriented Programming

Intro to Programming - Day 30
---
# Classes

A construct that lets you organize your code better
---
# Libraries/Modules

* After importing, we can use variables and functions (methods) belonging to that module.
* The `math` module contains variables like pi and functions like `sin()`
+++
```python runnable
import math

print('Here are the variables and functions that belong to the math module.')
for x in dir(math):
    print(x, end=', ')
```