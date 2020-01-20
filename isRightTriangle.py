'''
    Author: Mauricio Guzman
    Purpose: This program performs the Pythagorean theorem to determine
    if a triangle is a right triangle
'''

# Get the 3 sides of the triangle from the user:
sideA = int(input("Please enter length of side 1: "))
sideB = int(input("Please enter length of side 2: "))
sideC = int(input("Please enter length of side 3: "))

# Perform the Pythagorean theorem to determine if it is a right triangle
if((sideA*sideA + sideB*sideB == sideC*sideC) or (sideA*sideA + sideC*sideC == sideB*sideB) or (sideB*sideB + sideC*sideC == sideA*sideA)):
    print("This triangle is a right triangle")
else:
    print("This triangle is not a right triangle")

    
