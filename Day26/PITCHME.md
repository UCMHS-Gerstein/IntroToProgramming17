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
#### Goal - count repetitions of each word in a text you choose

1. Learn to split text
2. Handle capitalization
3. Handle punctuation
4. Handle extra white space
5. Clean up code
6. Use code on your text
---
# Split

* Read through [the reference](https://docs.python.org/3/library/stdtypes.html?#str.split)
* You need to assign a string with multiple words to a variable. I've provided a Terry Pratchett quote as a sample

```python
s = "If you trust in yourself... and believe in your dreams... and follow your star... you'll still get beaten by people who spent their time working hard and learning things and weren't so lazy."
```

Can you split this into separate words?
---
# String module

We're going to use [the string module](https://docs.python.org/3/library/string.html) to do better text processing
---
# Longer quote

Create a file called `textprocessing.py` in your day26 directory. Create a variable called text containing the Neil Gaiman quote below.

"I hope that in this year to come, you make mistakes. Because if you are making mistakes, then you are making new things, trying new things, learning, living, pushing yourself, changing yourself, changing your world. You're doing things you've never done before, and more importantly, you're doing something." 
---
## Split the text

Use the .split() function to split the text and assign the list returned to a variable called split_text. Print the variable
+++
# How could we improve this?
---
## Sort the text

Print out a sorted copy of the text
---
## Matching text

Let's make the case match on everything. use `text.lowercase()`, which will return an all-lowercase version of `text`, and assign that to the variable `cleaned_text`
