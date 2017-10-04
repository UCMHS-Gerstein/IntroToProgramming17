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

* Posted in [repo](https://github.com/UCMHS-Gerstein/IntroToProgramming17/blob/master/Day10/truthtables.md)
* We will go over in class
* Know the contents
* If unsure, you can use Python to check
---
## Try this code

Try different input values

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

Control the flow of your program

**if** the condition is true, **then** do something

```python
if True:
    print("If the logical test is true, this line shows up")
```
@[1]
@[2]
+++
# Multiple Ifs

You can have as many if statements as you want

```python
# stores an all-lowercase version of the user input in the name variable
# this means we don't have to worry about matching capitalization
name = input("Who are you? ").lower()

# These if statements will match for any capitalization of Wesley, Fred, and Hermione
if name == 'wesley':
    print('Shut up, Wesley.')
if name == 'fred':
    print('You\'re a cat. How are you typing this?')
if name == 'hermione':
    print('I didn\'t think they had computers at Hogwarts.')

# If the input didn't match, nothing happens
```
---
# Else

* else statements can be thought of as "otherwise"
* else statements don't have conditions
* else statement will run if the preceding if statement does not
* **if** the condition is true **then** do something. **otherwise** do the other thing.
+++
# Example

```python
# stores an all-lowercase version of the user input in the name variable
# this means we don't have to worry about matching capitalization
name = input("Who are you? ").lower()

# The if statement will match for any capitalization of Wesley
if name == 'wesley':
    print('Shut up, Wesley.')
# If the input is not some form of Wesley, the user is congratulated on not being Wesley Crusher
else:
    print('Congratulations on not being Wesley Crusher.')
```
---
# Else If (elif)

* elif statements can be thought of as "otherwise if"
* allows chaining of if statements
* elif will be checked if previous if and elif statement(s) did not run and will run if condition is true
* [if we reach this statement] **if** the condition is true **then** do something
+++
```python
# Take input and store it as all lowercase in day
day = input("What day is it? ").lower()

# respond to the day of the week
if day == "monday":
    print("Sorry, no sleeping in for you")
elif day == "tuesday":
    print("At least one day is over with, so you've got that going for you")
elif day == "wednesday":
    print("Halfway!")
elif day == "thursday":
    print("Happy Friday eve")
elif day == "friday":
    print("It's Friday!")
elif day == "saturday" or day == "sunday":
    print("Enjoy the weekend")  
else:
    print("Sorry, I don't know what you mean")
```
---
# Class exercise

File - day10.py

Create 10 if, elif, or else statements. Try to incorporate all of the symbols/keywords from slide 3

You can find my sample code [here](https://github.com/UCMHS-Gerstein/IntroToProgramming17/blob/master/Day10/sample.py)
