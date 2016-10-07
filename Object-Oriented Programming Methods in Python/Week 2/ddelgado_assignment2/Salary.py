'''
* Program #: AssignmentTwo_SalarySchedule
* Programmer: Diogo M Delgado
* Due: 7/11/2016
* CS 3A, summer 2016
* Description: Create a program that displays a salary schedule based on
    starting pay for teachers that earn a certain percentage of year-end
    salary increases and let the user dictate the length of years of such
    information to be displayed.
'''

#global variables
userSalary = float(input("Enter the starting salary: "))
userAnnualPercentUp = float(input("Enter the annual % increase: "))
yearsDisplay = int(input("Enter the number of years: "))
counter = 0

#value checks
while (userSalary <= 0):
    userSalary = float(input("Enter the starting salary greater than 0: "))

while (userAnnualPercentUp <= 0):
    userAnnualPercentUp = float(input("Enter the annual % increase greater than 0: "))

while (yearsDisplay <= 0):
    yearsDisplay = int(input("Enter the number of years greater than 0: "))

#calculate and display the table
print("Year    Salary")
print("--------------")
while (counter < yearsDisplay):
    if (counter == 0):
        print(" 1    ", ("%.2f" % userSalary))
    else:
        userSalary = (userSalary + (userSalary * (userAnnualPercentUp / 100)))
        if (counter < 9):
            print(" " + str(counter + 1) + "     " + str("%.2f" % userSalary))
        else:
            print((counter + 1), "   ", ("%.2f" % userSalary))
    counter += 1


"""
>>> ================================ RESTART ================================
>>> 
Enter the starting salary: 20439
Enter the annual % increase: 1
Enter the number of years: 20
Year    Salary
--------------
 1     20439.00
 2     20643.39
 3     20849.82
 4     21058.32
 5     21268.91
 6     21481.59
 7     21696.41
 8     21913.37
 9     22132.51
10     22353.83
11     22577.37
12     22803.15
13     23031.18
14     23261.49
15     23494.10
16     23729.04
17     23966.33
18     24206.00
19     24448.06
20     24692.54
>>> ================================ RESTART ================================
>>> 
Enter the starting salary: -1902
Enter the annual % increase: -12
Enter the number of years: -102
Enter the starting salary greater than 0: 1000
Enter the annual % increase greater than 0: 2
Enter the number of years greater than 0: 1
Year    Salary
--------------
 1     1000.00
>>> ================================ RESTART ================================
>>> 
Enter the starting salary: 45000
Enter the annual % increase: 3
Enter the number of years: 15
Year    Salary
--------------
 1     45000.00
 2     46350.00
 3     47740.50
 4     49172.71
 5     50647.90
 6     52167.33
 7     53732.35
 8     55344.32
 9     57004.65
10     58714.79
11     60476.24
12     62290.52
13     64159.24
14     66084.02
15     68066.54
>>> 
"""

