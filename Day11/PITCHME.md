---
# More Logic

Intro to Programming Day 11
---
# While loops

* Repeat something as long as a condition is true
* **while** some condition is true, **continue** doing this
* Remember to make sure you have exit conditions!
---
```python
secret_number = 8
guess = int(input("Pick a number"))
while guess != secret_number:
    guess = int(input("Try again! "))
print(f"You guessed the secret number! It was {secret_number}")
```
---
# Class Exercise

* Make 5 while loops