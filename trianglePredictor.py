'''
    Author: Mauricio Guzman
    Purpose: This program accepts the lengths of 3 sides of a triangle
    and then ouputs whether it is an equilateral triangle or not. 
'''

# Get the 3 sides of the triangle from the user:
sideA = int(input("Please enter length of side 1: "))
sideB = int(input("Please enter length of side 2: "))
sideC = int(input("Please enter length of side 3: "))

# Perform if/else checks to determine triangle type
if(sideA == sideB and sideB == sideC):
    print("The triangle is an equilateral triangle")
elif(sideA == sideB and sideB != sideC):
    print("The triangle is an isosceles triangle")
elif(sideA != sideB and sideB != sideC):
    print("The triangle is a scalene triangle")
else:
    print("Inputted values are undefined")
