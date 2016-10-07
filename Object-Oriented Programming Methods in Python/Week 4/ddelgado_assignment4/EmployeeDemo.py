'''
* Program #: Employee Class DEMO Assigment 4
* Programmer: Diogo M Delgado
* Due: 7/25/2016
* CS 3A, summer 2016
* Description: Utilize the class Employee to create three employee objects
    and display their information.
'''

from Employee import Employee

#employee#1
employeeOne = Employee("Susan", "Meyers", 47899)
employeeOne.setJob("Vice President", "Accounting")

#employee#2
employeeTwo = Employee("Mark","Jones",39119)
employeeTwo.setJob("Programmer", "IT")

#employee#3
employeeThree = Employee("Joy","Rogers",81774)
employeeThree.setJob("Engineer","Manufacturing")

#printEmployees
print("Employee 1")
print("Name: ", employeeOne.getName())
print("ID number: ", employeeOne.getID())
print("Department: ", employeeOne.getDepartment())
print("Title: ", employeeOne.getJobTitle(), "\n")

print("Employee 2")
print("Name: ", employeeTwo.getName())
print("ID number: ", employeeTwo.getID())
print("Department: ", employeeTwo.getDepartment())
print("Title: ", employeeTwo.getJobTitle(), "\n")

print("Employee 3")
print("Name: ", employeeThree.getName())
print("ID number: ", employeeThree.getID())
print("Department: ", employeeThree.getDepartment())
print("Title: ", employeeThree.getJobTitle(), "\n")

#output
"""
>>> ================================ RESTART ================================
>>> 
Employee 1
Name:  Susan Meyers
ID number:  47899
Department:  Accounting
Title:  Vice President 

Employee 2
Name:  Mark Jones
ID number:  39119
Department:  IT
Title:  Programmer 

Employee 3
Name:  Joy Rogers
ID number:  81774
Department:  Manufacturing
Title:  Engineer 

>>> 
"""
