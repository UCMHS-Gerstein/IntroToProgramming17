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
