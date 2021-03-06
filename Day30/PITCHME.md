---
# Object Oriented Programming

Intro to Programming - Day 30
---
# Classes

A construct that lets you organize your code better
---
## Libraries/Modules

* After importing, we can use variables and functions (methods) belonging to that module.
* The `math` module contains variables like pi and functions like `sin()`
+++
```python
import math

print('Here are the variables and functions that belong to the math module.')
for x in dir(math):
    print(x, end=', ')
```

```python
print(f"math.pi returns the value of pi. {math.pi}")
print(f"math.sin(math.pi) will return the sin of pi. {math.sin(math.pi)}")
```
---
## Dictionaries

Think about multiple dictionaries that are set up the same way

```python
maurice = {'name': 'Maurice', 'age': 9, 'species': 'cat', 'description': 'fluffy'}
fred = {'name': 'Fred', 'age': 17, 'species': 'cat', 'description': 'gigantic'}
aaron_purr = {'name': 'Aaron Purr', 'age': 2, 'species': 'cat', 'description': 'grey tabby'}
mayim = {'name': 'Mayim', 'age': 14, 'species': 'dog', 'description': 'short and round'}
rumi = {'name': 'Rumi', 'age': 3, 'species': 'dog', 'description': 'tall and thin'}
```
+++
Each of those dictionaries described a specific pet. How about a generic pet?

```python
generic_pet = {'name': name_string, 'age': integer_value, 'species': species_string, 'description': description_string}
```
---
## Classes

* A class is a template
* An object is an instance created from that template

```python
class Simple(object):
    """Simple is a barebones example of a class"""
    
    def __init__(self):
        """Initialize a new instance of the Simple class"""
        self.response = 'Hello'
```
+++
```python
class Simple(object):
    """Simple is a barebones example of a class"""
    
    def __init__(self):
        """Initialize a new instance of the Simple class"""
        self.response = 'Hello'

new_object = Simple()
print(new_object.response)
```
@[1-6]
@[8]
@[9]
---
## Pet class

```python
class Pet(object):
    """Pet object defines a pet"""
    
    def __init__(self, name, species):
        """name is pet's name, species is type of pet"""
        
        # Assign the parameters given in the function to the variables
        # belonging to the new Pet object being created
        self.name = name
        self.species = species

fred = Pet("Fred", "cat")
momo = Pet("Maurice", "cat")
mayim = Pet("Mayim", "dog")
```
@[1]
@[2]
@[4-5]
@[4-10]
@[12-14]
+++
```python
print(fred.name)
print(fred.species)
print('---')
print(momo.name)
print(momo.species)
print('---')
print(mayim.name)
print(mayim.species)
```
+++
What will this do?

```python
pets = []

while True:
    pets.append(Pet(input('Name?  '), input('Species?  ')))
    if input('Continue? Y/N  ').lower() == 'n':
        break

for pet in pets:
    print(f"{pet.name} is a {pet.species}")
```