"""
author: Diogo M Delgado

Lifetime Earnings 

Estimate how much a young worker will earn before retiring at age 65,
where the worker’s name, age, and starting salary are input by the user.
Assume the worker receives a 5% raise each year.

Name the source code file “Earnings.py”.
"""

#userInputs
userName = str(input("Enter your name: "))
userAge = int(input("Enter your age: "))
userSalary = int(input("Enter your starting salary: "))
#userLifetime monies
userEarnings = 0

#user will retire at 65, each year add 5% to userSalary
while (userAge < 65):
    userEarnings = (userEarnings + userSalary)
    userSalary = (userSalary + (userSalary * .05))
    userAge += 1

#print out total earnings at 65
print(userName + " will earn about $" + "{:,}".format(int(userEarnings)) + ".")
