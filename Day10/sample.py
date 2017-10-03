hours_in_day = 24
hours_in_school = 7
hours_of_travel = float(input("How long do you travel for school? "))
hours_of_homework = float(input("How many hours of homework do you have? "))
time_left = hours_in_day - hours_in_school - hours_of_travel - hours_of_homework

if time_left == 12:
    print("Wow, exactly half your day is free time! As long as we count sleep as free time.")

if time_left > 10:
    print("It looks like you'll have time for plenty of sleep.")

if time_left < 8:
    print("Sorry, looks like you're not getting enough sleep tonight. :(")

if time_left < 0:
    print("Wait, how are you going to accomplish all of this? There aren't enough hours in the day!")