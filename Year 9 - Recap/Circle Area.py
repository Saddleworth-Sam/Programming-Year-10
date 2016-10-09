
import math#Allows pi.math.pi to work







pi = math.pi#This is what pi is


def circleArea(radius, pi):#This is what circlearea is
    #area of a circle is pi (3.14)
    #times square of radius
    area = pi * (radius * radius)#This is what area is
    return area#This prints what the area equals

calculator = input("Enter: calculator or 11 to find out the circle area.")#Allows the user to input a word or numbers
if calculator == "Circle" or calculator == "circle" or calculator == ("11"):#If the user input a valid variable
    print("\n")#Prints a blank line
    print("Type set to: Circle (Area)")#Tells the user what they are working out
    print("\n")#Prints a blank line
    radius = float(input("Enter the radius of the circle: "))#A Float is a decimal number
    area = circleArea(radius, pi)#This is what area is
    print("The area is: ", str(area))#str is a string and this prints The area is then what the area equals
else:#This is makes the code below print when the user inputs an invalid variable
    print("Enter 11 or calculator")#This prints when the user inputs an invalid variable

