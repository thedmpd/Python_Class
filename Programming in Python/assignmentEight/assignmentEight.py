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
managerTwo = Manager("Kool", "Aid-Man", "9892861-2", 50000, "CEO", 1000002000)
managerThree = Manager("Ashley", "Aa", "8964732", 5090903, "CTO", 10009289)
employees = [employeeOne, employeeTwo, managerOne, managerTwo, managerThree]

for eachEntry in employees:
    print(eachEntry)

employees = sorted(employees)
print("---------------All employees have been sorted.----------------------------")

for eachEntry in employees:
    print(eachEntry)

print("comparison of Aa vs Aid-Man")
print(managerThree.__lt__(managerTwo))
print(managerThree.lastName > managerTwo.lastName)
print(managerThree.lastName < managerTwo.lastName)
print(managerThree.lastName == managerTwo.lastName)
print(managerThree.__eq__(managerTwo))
print("comparison of Aa vs As")
print(managerThree.__lt__(managerThree))
print(managerThree.lastName > managerThree.lastName)
print(managerThree.lastName < managerThree.lastName)
print(managerThree.lastName == managerThree.lastName)
print(managerThree.__eq__(managerThree))
print("Employee vs Manager")
print(employeeOne.__lt__(managerOne))
print(employeeOne.lastName > managerOne.lastName)
print(employeeOne.lastName < managerOne.lastName)
print(employeeOne.lastName == managerOne.lastName)
print(employeeOne.__eq__(managerOne))
print("\n\n Documentation:")
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
C:\Python34\python.exe -u C:\Program Files (x86)\JetBrains\PyCharm Community Edition 4.5.4\helpers\pydev\pydev_run_in_console.py 51138 51139 C:/Users/j/PycharmProjects/Homework/assignmentSeven.py
PyDev console: starting.
Running C:/Users/j/PycharmProjects/Homework/assignmentSeven.py
Employees Name: John Smith.
 Social: 7676762 | Salary: 20100
Employees Name: Urah Quick.
 Social: 89872 | Salary: 10000
Employees Name: Raji Uruawa.
 Social: 897282 | Salary: 150000 Title: VP of Accounting | Annual Bonus: 908922.
Employees Name: Kool Aid-Man.
 Social: 9892861-2 | Salary: 50000 Title: CEO | Annual Bonus: 1000002000.
Employees Name: Ashley Aa.
 Social: 8964732 | Salary: 5090903 Title: CTO | Annual Bonus: 10009289.
---------------All employees have been sorted.----------------------------
Employees Name: Ashley Aa.
 Social: 8964732 | Salary: 5090903 Title: CTO | Annual Bonus: 10009289.
Employees Name: Kool Aid-Man.
 Social: 9892861-2 | Salary: 50000 Title: CEO | Annual Bonus: 1000002000.
Employees Name: Urah Quick.
 Social: 89872 | Salary: 10000
Employees Name: John Smith.
 Social: 7676762 | Salary: 20100
Employees Name: Raji Uruawa.
 Social: 897282 | Salary: 150000 Title: VP of Accounting | Annual Bonus: 908922.
comparison of Aa vs Aid-Man
True
False
True
False
False
comparison of Aa vs As
False
False
False
True
True
Employee vs Manager
True
False
True
False
False


 Documentation:
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
