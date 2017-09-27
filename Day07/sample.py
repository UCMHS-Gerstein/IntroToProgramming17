import math

a = int(input('side a '))
b = int(input('side b '))

c = math.sqrt(a ** 2 + b ** 2)
print(f"The hypotenuse is {c}")
print(f"the hypotenuse is approximately {round(c)}")