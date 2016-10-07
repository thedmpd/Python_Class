__author__ = 'Diogo Delgado'
"""
Tests both classes and the availability of the parent class's methods to its child. Will create a list of objects,
reiterate through the list and change each objects salary by calling the method giveRaise().
"""
from manager import Manager
from employee import Employee

employeeOne = Employee("John", "Smith", "7676762", 20100)
employeeTwo = Employee("Urah", "Quick", "89872", 10000)
managerOne = Manager("Raji", "Uruawa", "897282", 150000, "VP of Accounting", 908922)
managerTwo = Manager("Kool", "Aid Man", "9892861-2", 50000, "CEO", 1000002000)
employees = [employeeOne, employeeTwo, managerOne, managerTwo]

for eachEntry in employees:
    print(eachEntry)
    eachEntry.giveRaise(25)
    print(eachEntry)

"""
C:\Python34\python.exe -u C:\Program Files (x86)\JetBrains\PyCharm Community Edition 4.5.4\helpers\pydev\pydev_run_in_console.py 53813 53814 C:/Users/j/PycharmProjects/Homework/assignmentSeven.py
PyDev console: starting.
Running C:/Users/j/PycharmProjects/Homework/assignmentSeven.py
Employees Name: John Smith.
 Social: 7676762 | Salary: 20100
Employees Name: John Smith.
 Social: 7676762 | Salary: 25125.0
Employees Name: Urah Quick.
 Social: 89872 | Salary: 10000
Employees Name: Urah Quick.
 Social: 89872 | Salary: 12500.0
Employees Name: Raji Uruawa.
 Social: 897282 | Salary: 150000 Title: VP of Accounting | Annual Bonus: 908922.
Employees Name: Raji Uruawa.
 Social: 897282 | Salary: 187500.0 Title: VP of Accounting | Annual Bonus: 908922.
Employees Name: Kool Aid Man.
 Social: 9892861-2 | Salary: 50000 Title: CEO | Annual Bonus: 1000002000.
Employees Name: Kool Aid Man.
 Social: 9892861-2 | Salary: 62500.0 Title: CEO | Annual Bonus: 1000002000.

"""
