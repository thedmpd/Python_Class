__author__ = 'Diogo Delgado'
"""
Creates a superclass of employees that will the parent of class Manager. It takes 4 instance variables, overwrites
the __str__(self) method, and defines the method giveRaise that will affect the object's salary when called.
"""
from functools import total_ordering
@total_ordering
class Employee:
    """
    specifies an object of class employee with the attributes: first and last Name, Social Security #, and Salary
    """

    def __init__(self, firstName, lastName, socialSecurity, salary):
        """
        creates one object of class Employee
        """
        self.firstName = firstName
        self.lastName = lastName
        self.socialSecurity = socialSecurity
        self.salary= salary

    def __str__(self):
        """
        converts the employee object's data into a formatted string
        """
        employee = "Employees Name: %s %s. \n Social: %s | Salary: %s" \
            % (self.firstName, self.lastName, self.socialSecurity, round(self.salary, 2))
        return employee

    def giveRaise(self,percentRaise):
        """
        this method will modify the object's salary by the percentage entered into it
        """
        percentRaise = float(percentRaise)
        self.salary = self.salary * (1 + (percentRaise / 100))

    def __eq__(self, other):
        """
        returns true in case of duplicate data based on first and last name
        """
        return ((self.firstName == other.firstName) and (self.lastName == other.lastName))
    
    def __lt__(self, other):
        """
        returns true when the object's last name is alphabetically less than the parameter object's last name.
        in the case that the last names are equal in weight, it checks the first names of both objects and returns
        true if the object's first name is less than the parameter object's first name, otherwise false is returned
        """
        if self.lastName.lower() < other.lastName.lower():
            return True
        elif self.lastName.lower() > other.lastName.lower():
            return False
        else:
            return (self.firstName.lower() < other.firstName.lower())

if (__name__ == "__main__"):
    employeeOne = Employee("Delta","Dirne","23444",100)
    print(employeeOne)
    employeeOne.giveRaise(10)
    print(employeeOne)
    employeeTwo = Employee("Argeh","Adrne","45443544",200)
    print(employeeTwo)
    employeeTwo.giveRaise(60)
    print(employeeTwo)
    print("duplicate data?")
    print(employeeOne.__eq__(employeeTwo))
    print(employeeOne.__eq__(employeeOne))
    print("Who is the first in the phonebook? Dirne or Adrne")
    print(employeeOne.__lt__(employeeTwo))
    print(employeeOne.lastName > employeeTwo.lastName)
    print(employeeOne.lastName < employeeTwo.lastName)
    print(employeeOne.lastName == employeeTwo.lastName)
    print("compare Dirne against himself")
    print(employeeOne.__lt__(employeeOne))
    print(employeeOne.lastName > employeeOne.lastName)
    print(employeeOne.lastName < employeeOne.lastName)
    print(employeeOne.lastName == employeeOne.lastName)
    #checking out the magic
    print("Employee.__doc__= " + Employee.__doc__)
    print("Employee.__init__.__doc__= " + Employee.__init__.__doc__)
    print("Employee.__str__= " + Employee.__str__.__doc__)
    print("Employee.giveRaise.__doc__= " + Employee.giveRaise.__doc__)
    print("Employee.__eq__.__doc__= " + Employee.__eq__.__doc__)
    print("Employee.__lt__.__doc__= " + Employee.__lt__.__doc__)


"""
C:\Python34\python.exe -u C:\Program Files (x86)\JetBrains\PyCharm Community Edition 4.5.4\helpers\pydev\pydev_run_in_console.py 60542 60543 C:/Users/j/PycharmProjects/Homework/employee.py
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
duplicate data?
False
True
Who is the first in the phonebook? Dirne or Adrne
False
True
False
False
compare Dirne against himself
False
False
False
True
Employee.__doc__=
    specifies an object of class employee with the attributes: first and last Name, Social Security #, and Salary

Employee.__init__.__doc__=
        creates one object of class Employee

Employee.__str__=
        converts the employee object's data into a formatted string

Employee.giveRaise.__doc__=
        this method will modify the object's salary by the percentage entered into it

Employee.__eq__.__doc__=
        returns true in case of duplicate data based on first and last name

Employee.__lt__.__doc__=
        returns true when the object's last name is alphabetically less than the parameter object's last name.
        in the case that the last names are equal in weight, it checks the first names of both objects and returns
        true if the object's first name is less than the parameter object's first name, otherwise false is returned

"""
