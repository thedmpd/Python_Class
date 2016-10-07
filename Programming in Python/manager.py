__author__ = 'Diogo Delgado'
"""
Inherits from class Employee the basic blocks of 4 instances, adds two more that are only relevant to the
Manager class such as the title and annual bonus compensation.
"""
from employee import Employee

class Manager(Employee):

    def __init__(self, firstName, lastName, socialSecurity, salary, title, annualBonus):
        Employee.__init__(self, firstName,lastName,socialSecurity,salary)
        self.title = title
        self.annualBonus = annualBonus

    def __str__(self):
        manager = Employee.__str__(self) + " Title: %s | Annual Bonus: %s." %(self.title, self.annualBonus)
        return manager

if (__name__ == "__main__"):
    managerOne = Manager("John", "Keey", "9189289", 1000, "Accounting Head", 1000)
    print(managerOne)
    managerOne.giveRaise(15)
    print(managerOne)

"""
C:\Python34\python.exe -u C:\Program Files (x86)\JetBrains\PyCharm Community Edition 4.5.4\helpers\pydev\pydev_run_in_console.py 53830 53831 C:/Users/j/PycharmProjects/Homework/manager.py
PyDev console: starting.
Running C:/Users/j/PycharmProjects/Homework/manager.py
Employees Name: John Keey.
 Social: 9189289 | Salary: 1000 Title: Accounting Head | Annual Bonus: 1000.
Employees Name: John Keey.
 Social: 9189289 | Salary: 1150.0 Title: Accounting Head | Annual Bonus: 1000.

"""
