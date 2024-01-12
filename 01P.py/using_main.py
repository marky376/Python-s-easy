#!/usr/bin/python3
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
    length = float(input("Please enter the length of the rectangle : ")
    width = float(input("Please enter the width of the rectangle : ")
    Area = length * width
    return Area

def main():
    shape_type = input("Get area for what shape? : ")

    get_area(shape_type)





main()
