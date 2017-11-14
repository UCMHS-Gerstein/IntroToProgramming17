---
# Dictionaries

Intro to Programming - Day 23
---
# How would you keep track of inventory?
+++
### Example

You're a (very small) art museum with 5 unique pieces of art. How can you store your inventory?
+++
```python
inventory = ['Starry Night', 'The Persistence of Memory', 'The Great Wave Off Kanagawa', 'The Scream', 'The Broken Column']

# Print list of inventory
for item in inventory:
    print(f" - {item}")
```
+++
### Handling multiples

What if you had duplicates of a few items?
+++
```python
inventory = ['apple', 'apple', 'orange', 'banana', 'banana', 'banana', 'chocolate', 'durian']

# print each item
for item in inventory:
    print(f" - {item}")
```
+++
### More multiples

What if you had a lot of duplicates?

5 apples, 3 potatoes, 2 bananas, 1 durian, 10 peppers

How could you keep track and make this easy to manage?
---
# Dictionaries

* Unordered set of key-value pairs
* Keys must be unique
* Values can be any type of data
+++
### When to use lists

* Position matters
* Don't need to link multiple pieces of information
+++
### When to use dictionaries

* Position doesn't matter
* Need to link information to unique keys
+++
### Example

```python
inventory = {'apples': 5, 'potatoes': 3, 'bananas': 2, 'durian': 1, 'peppers': 10}
```
---
# Working with Dictionaries

```python
sample_dict = {'key1': value1, 'key2': value2, 'key3': value3, ... , 'keyN': valueN}
```
+++
### Accessing items in a dict

* Unlike a list, there is no index - key-value pairs can be in any order
* Use the *key* to access the *value* associated with it

```python
inventory = {'apples': 5, 'potatoes': 3, 'bananas': 2, 'durian': 1, 'peppers': 10}

# Will return the value associated with the 'apples' key
inventory['apples']
```
+++
### Try it (not submitted)

Create a dictionary with at least 5 key value pairs. Try accessing the values associated with the keys

Can you figure out how you could modify the value associated with a key?
+++
### Modifying values

* Modifying values in a dict works a lot like modifying a list
* The code below will assign 200 as the value for the 'apples' key, creating the key if it doesn't already exist

```python
inventory['apples'] = 200
```
---
# Working with a whole dictionary
+++
# Generating lists

* Dictionaries are capable of generating lists of their keys and values

```python
inventory = {'apples': 5, 'potatoes': 3, 'bananas': 2, 'durian': 1, 'peppers': 10}

# Returns a list of keys
inventory.keys()

# Returns a list of values
inventory.values()

# Returns a list of keys AND values
inventory.items()
```
+++
```python
inventory = {'apples': 5, 'potatoes': 3, 'bananas': 2, 'durian': 1, 'peppers': 10}

for key, value in inventory.items():
    print(f"* {key} -- {value}")
```
+++
# Practice

We'll work on some examples together, and next class you'll have exercises in a repo similar to more-lists