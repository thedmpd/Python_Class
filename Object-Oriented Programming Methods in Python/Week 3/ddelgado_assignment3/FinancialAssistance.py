'''
* Program #: Financial Assistance Assigment 3
* Programmer: Diogo M Delgado
* Due: 7/18/2016
* CS 3A, summer 2016
* Description: Create a program that defines a function that calculates the financial
    assistance for a family given two arguments, earnings and # of children.
    The formula is defined as:
    <20K in earnings = 2K per child;
    20K < earnings < 30K = 1.5K per child;
    30K < earnings <= 40K = 1K per child.
'''

#global variables
householdIncome = 0.0
numberChildren = 0
assistanceMonies = 0.0

def financialAssistance(income, children):
    monies = 0.0
    
    if (income < 20000):
        monies = 2000 * children
        return monies
    elif ((income < 30000) and (children > 1)):
        monies = 1500 * children
        return monies
    elif ((income <= 40000) and (children > 2)):
        monies = 1000 * children
        return monies
    else:
        return monies

while (householdIncome != -1):
    householdIncome = float(input("What is the household income (-1 to quit)?"))
    if (householdIncome != -1):
        numberChildren = int(input("How many children?"))
        assistanceMonies = financialAssistance(householdIncome, numberChildren)
        print("The assistance amount is $" + "{:,.2f}".format(assistanceMonies))

    
"""
>>> ================================ RESTART ================================
>>> 
What is the household income (-1 to quit)?24
How many children?3
The assistance amount is $6,000.00
What is the household income (-1 to quit)?35000
How many children?3
The assistance amount is $3,000.00
What is the household income (-1 to quit)?54000
How many children?2
The assistance amount is $0.00
What is the household income (-1 to quit)?18000
How many children?4
The assistance amount is $8,000.00
What is the household income (-1 to quit)?-9023
How many children?4
The assistance amount is $8,000.00
What is the household income (-1 to quit)?20000
How many children?1
The assistance amount is $0.00
What is the household income (-1 to quit)?20000
How many children?2
The assistance amount is $3,000.00
What is the household income (-1 to quit)?-1
>>> 
"""

        
