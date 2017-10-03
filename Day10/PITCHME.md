---
# Logic

Intro to Programming Day 10
---
# Booleans

* Booleans are another data type
* **True** or **False**
---
# Logic

* ```and```, ```or```, ```not```
* ```<```, ```>```, ```<=```, ```>=```
* ```==```, ```!=```
* ```True```, ```False```
---
# Truth Tables

* Posted in [repo](\truthtables.md)
* We will go over in class
* Know the contents
* If unsure, you can use Python to check
---
# Try this code

Change your input values when you run it and see how it affects what's printed?

```python
hours_in_day = 24
hours_in_school = 7
hours_of_travel = int(input("How long do you travel for school? "))
hours_of_homework = int(input("How many hours of homework do you have? "))
time_left = hours_in_day - hours_in_school - hours_of_travel - hours_of_homework

if time_left == 12:
    print("Wow, exactly half your day is free time! As long as we count sleep as free time.")

if time_left > 10:
    print("It looks like you'll have time for plenty of sleep.")

if time_left < 8:
    print("Sorry, looks like you're not getting enough sleep tonight. :(")

if time_left <= 0:
    print("Wait, how are you going to accomplish all of this? There aren't enough hours in the day!")
```
+++
## How does it work?

* What did the code above do?
* How do you think an if statement works?
---
# If statements

* Control the flow of your program

```python
if True:
    print("If the logical test is true, this line shows up")
```
@[1]
@[2]