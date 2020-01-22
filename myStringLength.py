'''
    Author: Mauricio Guzman
    Purpose: This program will ask the user for a string input,
    it will then loop through and output the reversed order of
    the entire string. 
'''

# Request user input for string to be entered
myString = input("Please enter the string you would like reversed: ")

# create array variable to house the reversedString variable
revString = []

# Find the length of the entered string and save to variable
stringLength = len(myString)

# loop through string length to reverse the string
while (stringLength > 0):
    # cycle in reverse order through string and save/add to revString var
    revString += myString[stringLength - 1]
    # decrement the stringLength to continue to loop through remaining chars
    stringLength = stringLength - 1
# print the reversed string    
print(revString) 
