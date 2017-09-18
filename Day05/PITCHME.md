---
# Starting Python

Intro to Programming - Day 5
---
# Do Now

* Open up a terminal for Python 3
* Use the ```print()``` function to print 5 different things
* We'll have a quiz after everybody settles in
* Files and consoles you'll need: python3 interactive console, ```day05.py```, ```yourlastnameday05.py```
---
# Comments

```python
# This is a comment
# Comments let us include descriptions of what our code is doing
# We can also make other notes

# print "Hi, I'm a string" 10 times
for x in range(10):
    # Strings are a data type that stores text
    print("Hi, I'm a string")

print("Make a string by enclosing something in quotation marks")
# Single quotes work too
print('I am a string too!')
# Use whatever works best in a given situation
print("These double quotes don't mess with contractions.")
```
@[1-3, 5, 7, 11, 13]
@[6, 8, 10, 12, 14]
---
# Comments Are Important

* Make code easier to understand
* Communicate with others who need to use/edit your code
* Comment out line of code temporarily
* In class, you'll use them to show understanding of your own code
---
# Exercise

In a file called ```day05.py```, use the print function and place a comment describing it in the line above your print function
---
# Data Types

* Data has a variety of types
* For today: integer, float, string
+++
# Integer

* Whole number
* 3, 1000, -1, 42
* Abbreviated as **int**
+++
# Float

* Number with a decimal
* 5.0, 3.14159265359, -20.2
* Stands for **floating point number**
+++
# String

* Text
* Can use single quotes or double quotes

```python
print("Hi, I am a string")
print('I am also a string')
print("I usually use single quotes, but I'm using double quotes here because of the contraction")
print("Don't forget to close the quotes on your strings")
```
---
# Math and Numbers

```python
# Addition
print(1 + 2)

# Subtraction
print(3 - 20)

# Multiplication
print(21 * 2)

# Division
print(100 / 3)
```
---
# Exercise

Try using the following operators in an interactive console:

```+```, ```-```, ```*```, ```/```, ```%```, ```**```, ```<```, ```>```, ```<=```, ```>=```

To do this, open an iPython 3.6 console and see the results you get by putting these operators in between numbers. Python will use the correct order of operations.
---
# Printing

```python
# The print function takes one or more arguments

# We've already used the print function with one argument
print("I'm a string")

# The contents of the string will be evaluated before printing

# This will print 8, not 3 + 5
print(3 + 5)

# To print 3 + 5, use a string
print(3 + 5)

# We can provide multiple arguments, separated by commas
# Python will print each argument, separated by a space
print("What is 3 + 5?", 3 + 5)
```

There are other ways to combine multiple things into a single print function, but we'll get to those later
---
# Variables

* A variable is a name for a value
* pi refers to the value 3.14159265359
* ucmhs refers to this school
* Use short but descriptive names
+++
```python
# variables are created by assigning a value to them
# the two lines below are assignment statements
a = 5
b = 6

# python interprets a variable as equivalent to its value
# what will this print?
print(a * b)

# change the value of a variable with another assignment statement
a = 10

# you can assign a value based on other variables
c = a + b

# you can also assign a new value based on the existing value
c = c + 1
```
+++
What will this code do? In day05.py, try it out

```python
cats = 20
dogs = 10
unicorns = 0
total_animals = cats + dogs + unicorns  

print("There are", cats, "cats")
print("There are", dogs, "dogs")
print("There are", unicorns, "unicorns")
print("There are", total_animals, "animals")

```
---
# Class Exercise

* Create a file called ```yourlastnameday05.py```
* Please name it exactly as shown
* In the file, create a variable called inches and assign it a value
* Create a second variable called cm and use math and your first variable to assign it the number of cm your inches variable contains
* Use a print statement to tell me what both variables are.
* Remember to include comments
---
# Finished early?

* Open your python3 console
* type ```import math``` to import the math module
* use ```dir(math)``` to get a list of the functions contained in the math module, or use the following for nicer formatting:

```python
for item in dir(math):
    print(item)
```

Try the functions in the math module