---
# Text processing

Intro to Programming - Day 26
---
## Goals

* Review dictionaries
* Review functionaries
* Handle strings better
---
# Setup

In a Bash console, create a new directory called "Day26" using `mkdir Day26` and navigate into it using `cd Day26`
---
# Goal - count repetitions of each word in a text you choose

1. Learn to split text
2. Handle capitalization
3. Handle punctuation
4. Handle extra white space
5. Clean up code
6. Use code on your text
---
# Split

* Read through [the reference](https://docs.python.org/3/library/stdtypes.html?#str.split)
* In a Python 3 console, create a string containing "If you trust in yourself... and believe in your dreams... and follow your star... you'll still get beaten by people who spent their time working hard and learning things and weren't so lazy." and assign it to a variable called s

```python
s = "If you trust in yourself... and believe in your dreams... and follow your star... you'll still get beaten by people who spent their time working hard and learning things and weren't so lazy."
```

Can you split this into separate words?
+++
# String module

We're going to use [the string module](https://docs.python.org/3/library/string.html) to do better text processing
