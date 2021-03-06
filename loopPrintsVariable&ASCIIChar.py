'''
    Author: Mauricio Guzman
    Purpose: This python program will loop through the test string variable
    and print each individual character, in addition to its associated ASCII
DLLs
'''

# create a variable that stores a string
testString = 'Hello World'

# use the len() function to grab the length of the string
# have our loop var loop through the length of the string
# while looping - print each character's index position,
# also the character and its corresponding ASCII value
for c in range(len(testString)):
    print("The character at index position",c,"is: ", testString[c],
          "\nAnd its associated ASCII value is: ",ord(testString[c]),"\n")
    
#print(testString[0])

# write a loop that prints each character in the teststring variable
#for count in len(testString):
#print(len(testString))
    
