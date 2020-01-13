""" 
    Author: Mauricio Guzman
    Purpose: 
    This program performs income tax calculations based on
    the number of dependents entered by the user and observing
    a standard tax rate and standard deduction. 
"""
# Define program constants - variables where values won't change
taxRate = 0.20
standardDeduction = 10000
dependentDeduction = 3000

# Request the persons gross income 
grossIncome = float(input("Enter the gross income: "))

# Request the number of dependents that they have 
numDependents = int(input("Enter the number of dependents that you have: "))
#numDependents = 2

# Compute the taxable income using the following formula
taxableIncome = ((grossIncome - standardDeduction)-(dependentDeduction * numDependents))

# Find the total income tax based on the following formula
incomeTax = (taxableIncome * taxRate)

# Display their income tax
print("The income tax is $" + str(incomeTax))
