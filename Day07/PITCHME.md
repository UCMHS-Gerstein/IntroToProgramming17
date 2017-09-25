---
# Taking user input

Intro to Programming - Day 5
---
# Files

Create day07madlibs.py. Copy the contents of day06story.py into the new file.
---
# Important terms

* return
* prompt
+++
## Return

* Functions **return** a value
* Output of a function
* If nothing is deliberately returned, functions return a 'NoneType' object
+++
## Prompt

* Message indicating that the user should do something
---
# Functions

* ```input()```
* ```type()```
* ```str()```
* ```int()```
* ```float()```
+++
## input()

* prompts user for input and returns that input as a string
* takes a string as an optional argument and uses that as the prompt

```python
color = input("what is your favorite color? ")

print(f"{color} is a great color!")
```
+++
## type()

* takes a single value as a required argument and returns that value's **data type**

```python
print("5 is", type(5))
print("5.0 is", type(5.0))
print("five is a", type('five'))
```
+++
## int(), str(), float()

* all three are conversion functions
* takes a single value as an input and returns it converted into the specified type

```python
    print(type(5))
    print(float(5))
    print(type(float(5)))
```
---
# Classwork

In day07.py, convert your story to use the ```input()``` function to get responses from a user. Test it on your classmates