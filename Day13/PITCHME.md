---
# More Loops

Intro to Programming Day 13
---
# While Loop Review

Repeats something until the condition being checked is no longer true
+++
<iframe src="https://trinket.io/embed/blocks/9690aa5f90" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
+++
<iframe src="https://trinket.io/embed/blocks/b041f8aa6d" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
+++
<iframe src="https://trinket.io/embed/blocks/90c41717f0" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
---
# Vocab/functions

* Iteration
* ```range()```
* list
---
# For Loop

Used to loop a certain number of times, or for a set of values

```python
# Will repeat for every number from 0 through 99
for number in range(100):
    # print the current number
    print(number)
```
---
## For or While?

* Everything a for loop can do can be done with a while loop, although sometimes it would be much longer and more complex code
* Use **for** when you want a specific number of repetitions or when you want to go through a list of items
* Use **while** when you're checking for some other type of condition
---
### Anatomy of a for loop

```python
for number in range(10):
    print(number)
```

* Can be thought of as "for each item in this set of values, do something"
* Variable can be named any way you want, but it helps to be descriptive
* Variable does **not** need to be used in the loop