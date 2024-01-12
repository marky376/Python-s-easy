#!/usr/bin/python3
from math import pi
def get_area(shape):
    shape = shape.lower()

    if shape == "rectangle":
    
        rectangle_area()
    
    
    elif shape == "circle":
    
        circle_area()
    
    elif shape == "triangle":
    
        triangle_area()
    
    else:
        print("Please enter rectangle, square or triangle")

def rectangle_area():
    length = float(input("Please enter the length of the rectangle : "))
    
    width = float(input("Please enter the width of the rectangle : "))
    
    Area = length * width
    
    print(f"The area of the rectangle with {length} as the length and {width} as the width is {Area}")

def circle_area():

    radius = float(input("Please enter the radius of the circle : "))

    Area = radius * pi * radius

    print(f"The area of the circle with {radius} as the radius is {Area}")

def triangle_area():
    height = float(input("Please enter the height of the rectangle : "))
    base = float(input("Please enter the base of the triangle : "))


def main():
    shape_type = input("Get area for what shape? : ")

    get_area(shape_type)





main()
