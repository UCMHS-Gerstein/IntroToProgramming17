<<<<<<< HEAD
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
=======
def respond_to_day(day):
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

respond_to_day(input("What day is it? ").lower())
>>>>>>> master
