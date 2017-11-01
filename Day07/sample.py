from math import sqrt

# sides of triangle
a = float(input("Side a: "))
b = float(input("Side b: "))

# calculate hypotenuse
c = sqrt(a ** 2 + b ** 2)

# display results
print(f"With sides of {a} and {b}, the hypotenuse is {c}")