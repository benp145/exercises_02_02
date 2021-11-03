from math import pi

def room_sq_footage():
    width = input("Enter the width of room in feet: ")
    length = input("Enter the lenght of room in feet: ")
    sq_feet = int(width) * int(length)
    print(f"The room is {sq_feet} square feet.")

def circumference():
    radius = input("Enter the radius of circle: ")
    ci = 2 * int(radius) * pi
    print(f"The circumference of the circle is {ci}")
