import math

def circle_area(radius):
    return math.pi * radius * radius
def rectangle_area(length, width):
    return length * width
def triangle_area(base, height):
    return (1/2) * base * height

while True:
    shape = input("\nPick a shape: circle (c), rectangle (r), triangle (t), quit (q): ")

    if shape == "c" or shape == "C":
        u_radius = float(input("\nEnter the radius: "))
        print("The area of the circle is: " +str(circle_area(u_radius)))
    
    elif shape == "r" or shape == "R":
        u_length = float(input("\nEnter the length: "))
        u_width = float(input("Enter the width: "))
        print("The area of the rectangle is: " +str(rectangle_area(u_length, u_width)))
    
    elif shape == "t" or shape == "T":
        u_base = float(input("\nEnter the base: "))
        u_height = float(input("Enter the height: "))
        print("The area of the triangle is: " +str(triangle_area(u_base, u_height)))
    
    elif shape == "q" or shape == "Q":
        break

    else:
        print("\nInvalid shape! Try again")