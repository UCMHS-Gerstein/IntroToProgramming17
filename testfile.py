import random

sides = int(input("how many sides to your die?  "))
throws = int(input("How many times should I throw it?  "))

results = {}

for x in range(throws):
    die = random.randint(1, sides)
    if die in results.keys():
        results[die] += 1
    else: 
        results[die] = 1

for k, v in results.items():
    print(k, ": ", v)

