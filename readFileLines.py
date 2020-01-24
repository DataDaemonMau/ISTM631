'''
    Author: Mauricio Guzman
    Program: A program that will count the number of lines in
    a file and return the total count
'''

# First open the file with read permissions/mode
f = open("myFile.txt","r")

# create a counter variable which will be incremented
lineCount = 0
# loop through each line in the file 
for line in f:
    # for each line add 1 to our line counter
    lineCount += 1
# Output the total count of lines that are in the file
print('The total number of lines in this file is: ',lineCount)
