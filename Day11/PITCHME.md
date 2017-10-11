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
---
# Day 12 Classwork

* File: Day12.py
* 10 points for flowchart
* 15 points for code
+++
* Create code that will print out every number from 1 to 10000 except:
* Numbers divisible by both 3 and 11 will be replaced with "motorcycle"
* Numbers divisible by 3 (but not 11) will be replaced with "bicycle"
* Numbers divisible by 11 (but not 3) will be replaced with "car"
+++
* Your flowchart may be done on paper or computer
* Be careful that you depict loops and decisions
+++
## Code tips
* Theoretically, you could write this out without loops. Don't do it, or I'll make you go up to ten million
* You're going to need loops and conditional statements
+++
## Grading

Flowchart:

* 8 points for correctness
* 2 points for neatness

Code:

* 12 points for correctness
* 3 points for clear and well-documented code
