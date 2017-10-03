def find_diameter(r):
    diam = 2 * r
    return diam

def find_diameter2():
    diam = 2 * float(input("radius? "))
    return diam

for radius in range(0:100000:17):
    print(find_diameter(radius))