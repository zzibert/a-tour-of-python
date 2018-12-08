def area(radius):
    return 3.142 * radius ** 2

def vol(area, length):
    return area * length

radius = int(input("enter a radius"))
length = int(input("enter a length!"))

print(vol(area(radius), length))
