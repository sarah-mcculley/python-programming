import math

def calc_circumference(radius):
    circumference = 2 * math.pi * radius

    return circumference

def calc_area(radius):
   area = math.pi * radius * radius

   return area

print("To quit enter a negative value.")
radius = float(input("Give me a radius of your circle:"))

while radius >=0:
    x = calc_circumference(radius)
    y = calc_area(radius)

    print("The circumference is ", x)
    print(" The area is ", y)

    radius = float(input("Give me another radius:"))

