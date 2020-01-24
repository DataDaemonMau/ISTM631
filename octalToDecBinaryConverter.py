'''
    Author: Mauricio Guzman
    Purpose: A program used to convert octal to binary
    notation that continues to take input until the
    program is exited by the user.
'''

while True:
    print("To exit the program type in 'exit'")
    octal = input("Enter the number that is in Octal Format: ")

    # exit the program when user is done (closes shell)
    if(octal == 'exit'):
        exit();
    else:
        # First convert octal to decimal form
        decForm = int(octal, 8)
        print(decForm)
        # then convert decimal to binary form
        binForm = bin(decForm)
        print(binForm)
        print("The number",octal,"in Octal form is equal to: ",binForm, "in binary") 
