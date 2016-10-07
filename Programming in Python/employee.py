__author__ = 'Diogo Delgado'
"""
Creates a superclass of employees that will the parent of class Manager. It takes 4 instance variables, overwrites
the __str__(self) method, and defines the method giveRaise that will affect the object's salary when called.
"""
class Employee:

    def __init__(self, firstName, lastName, socialSecurity, salary):
        self.firstName = firstName
        self.lastName = lastName
        self.socialSecurity = socialSecurity
        self.salary= salary

    def __str__(self):
        employee = "Employees Name: %s %s. \n Social: %s | Salary: %s" \
            % (self.firstName, self.lastName, self.socialSecurity, round(self.salary, 2))
        return employee

    def giveRaise(self,percentRaise):
        percentRaise = float(percentRaise)
        self.salary = self.salary * (1 + (percentRaise / 100))

if (__name__ == "__main__"):
    employeeOne = Employee("Delta","Dirne","23444",100)
    print(employeeOne)
    employeeOne.giveRaise(10)
    print(employeeOne)
    employeeTwo = Employee("Argeh","Adrne","45443544",200)
    print(employeeTwo)
    employeeTwo.giveRaise(60)
    print(employeeTwo)

"""
C:\Python34\python.exe -u C:\Program Files (x86)\JetBrains\PyCharm Community Edition 4.5.4\helpers\pydev\pydev_run_in_console.py 53825 53826 C:/Users/j/PycharmProjects/Homework/employee.py
PyDev console: starting.
Running C:/Users/j/PycharmProjects/Homework/employee.py
Employees Name: Delta Dirne.
 Social: 23444 | Salary: 100
Employees Name: Delta Dirne.
 Social: 23444 | Salary: 110.0
Employees Name: Argeh Adrne.
 Social: 45443544 | Salary: 200
Employees Name: Argeh Adrne.
 Social: 45443544 | Salary: 320.0

"""
