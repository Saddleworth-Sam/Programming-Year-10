import math

#Program functions
def circleArea (radius,pi):
    #Area of a circle is pi (3.14)
    #times square o a radius
    area = pi * (radius * radius)
    return area

def areaRectangle(height, width):
    #Area of rectangle = height * width
    area = height * width
    return area

#Get a value for pi
pi = math.pi

print("SCIENTIFIC CALCULATOR")
print("-------------------------------------")
print("Press A to work out the area of a cirlce")
print("Press R to work out the area of a square/rectangle")


#Input user's choice
calculation = input("Enter your choice: ")

if calculation == "a" or calculation == "A":
    #User wants area of a circle
    #Input radius from user
    radius = float(input("Enter the radius of the cirlce: "))
    #Calculate area of cirlce
    area = circleArea(radius,pi)
    #Display on screen
    print("The area is: ", str(area))

if calculation == "r" or calculation == "R":
    #User wants area of a rectangle/square
    #Input height and width from user
    height = float(input("Enter the height of the rectangle: "))
    #Calculate area
    area = areaRectangle(height, width)
    #Display on screen
    print("The area is: ", str(area))

