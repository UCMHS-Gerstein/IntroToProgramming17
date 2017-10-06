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
# Break

Takes you out of a block of code

```python
secret_word = 'alphabet'
while True:
    answer = input("guess the word >>> ").lower()
    print(f"You guessed {answer.upper()}")
    if answer == secret_word:
        print("You were right!")
        break
print("exiting the program now")
```
---    
# Class Exercise

* File: Day11.py
* Create 5 different while loops
* Make sure you include something that's counting repetitions
* Make sure you include something that will exit based on a user's input