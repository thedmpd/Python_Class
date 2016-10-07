__author__ = 'Diogo Delgado'
"""
Inherits from class Employee the basic blocks of 4 instances, adds two more that are only relevant to the
Manager class such as the title and annual bonus compensation.
"""
from employee import Employee
class Manager(Employee):
    """
    specifies an object of class Manager which is a subset of the class Employee thus containing all of the
    attributes from class Employee as well as the Manager specific attributes of title and annual bonus
    """

    def __init__(self, firstName, lastName, socialSecurity, salary, title, annualBonus):
        """
        creates an object of subclass Manager through inheritance from class Employee, initiating all attributes
        present in Employee along with title and annual bonus that is particulat to this subclass
        """
        Employee.__init__(self, firstName,lastName,socialSecurity,salary)
        self.title = title
        self.annualBonus = annualBonus

    def __str__(self):
        """
        takes a manager object and converts all the attributes as a formatted string
        """
        manager = Employee.__str__(self) + " Title: %s | Annual Bonus: %s." %(self.title, self.annualBonus)
        return manager

if (__name__ == "__main__"):
    managerOne = Manager("John", "Keey", "9189289", 1000, "Accounting Head", 1000)
    print(managerOne)
    managerOne.giveRaise(15)
    print(managerOne)
    managerTwo = Manager("John", "Aruh", "092037", 10000, "Operations Head", 1899)
    print(managerTwo)
    managerTwo.giveRaise(20)
    print(managerTwo)
    print("duplicate data?")
    print(managerOne.__eq__(managerTwo))
    print(managerOne.__eq__(managerOne))
    print("Who is the first in the phonebook? Keey or Aruh")
    print(managerOne.__lt__(managerTwo))
    print(managerOne.lastName > managerTwo.lastName)
    print(managerOne.lastName < managerTwo.lastName)
    print(managerOne.lastName == managerTwo.lastName)
    print("compare Keey against himself")
    print(managerOne.__lt__(managerOne))
    print(managerOne.lastName > managerOne.lastName)
    print(managerOne.lastName < managerOne.lastName)
    print(managerOne.lastName == managerOne.lastName)
    #check for the magic from Manager and Employee
    print("Manager.__doc__= " + Manager.__doc__)
    print("Manager.__init__.__doc__= " + Manager.__init__.__doc__)
    print("Manager.__str__.__doc__= " + Manager.__str__.__doc__)
    print("Employee.__doc__= " + Employee.__doc__)
    print("Employee.__init__.__doc__= " + Employee.__init__.__doc__)
    print("Employee.giveRaise.__doc__= " + Employee.giveRaise.__doc__)
    print("Employee.__str__.__doc__= " + Employee.__eq__.__doc__)
    print("Employee.__lt__.__doc__= " + Employee.__lt__.__doc__)
    print ("Employee.__str__.__doc__= " + Employee.__str__.__doc__)

"""
C:\Python34\python.exe -u C:\Program Files (x86)\JetBrains\PyCharm Community Edition 4.5.4\helpers\pydev\pydev_run_in_console.py 60551 60552 C:/Users/j/PycharmProjects/Homework/manager.py
PyDev console: starting.
Running C:/Users/j/PycharmProjects/Homework/manager.py
Employees Name: John Keey.
 Social: 9189289 | Salary: 1000 Title: Accounting Head | Annual Bonus: 1000.
Employees Name: John Keey.
 Social: 9189289 | Salary: 1150.0 Title: Accounting Head | Annual Bonus: 1000.
Employees Name: John Aruh.
 Social: 092037 | Salary: 10000 Title: Operations Head | Annual Bonus: 1899.
Employees Name: John Aruh.
 Social: 092037 | Salary: 12000.0 Title: Operations Head | Annual Bonus: 1899.
duplicate data?
False
True
Who is the first in the phonebook? Keey or Aruh
False
True
False
False
compare Keey against himself
False
False
False
True
Manager.__doc__=
    specifies an object of class Manager which is a subset of the class Employee thus containing all of the
    attributes from class Employee as well as the Manager specific attributes of title and annual bonus

Manager.__init__.__doc__=
        creates an object of subclass Manager through inheritance from class Employee, initiating all attributes
        present in Employee along with title and annual bonus that is particulat to this subclass

Manager.__str__.__doc__=
        takes a manager object and converts all the attributes as a formatted string

Employee.__doc__=
    specifies an object of class employee with the attributes: first and last Name, Social Security #, and Salary

Employee.__init__.__doc__=
        creates one object of class Employee

Employee.giveRaise.__doc__=
        this method will modify the object's salary by the percentage entered into it

Employee.__str__.__doc__=
        returns true in case of duplicate data based on first and last name

Employee.__lt__.__doc__=
        returns true when the object's last name is alphabetically less than the parameter object's last name.
        in the case that the last names are equal in weight, it checks the first names of both objects and returns
        true if the object's first name is less than the parameter object's first name, otherwise false is returned

Employee.__str__.__doc__=
        converts the employee object's data into a formatted string

"""
