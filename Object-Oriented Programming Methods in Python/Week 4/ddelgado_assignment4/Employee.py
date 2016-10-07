'''
* Program #: Employee Class Assigment 4
* Programmer: Diogo M Delgado
* Due: 7/25/2016
* CS 3A, summer 2016
* Description: Create a program that defines a class Employee which
    initializes an employee object with attributes such as name, ID number,
    department, and job title.
'''

class Employee:
    #initiate with First, Last name, ID #
    def __init__(self, firstName, lastName, idNumber):
        if (type(firstName) == str):
            self.__firstName = firstName
        else:
            return TypeError
        if (type(lastName) == str):
            self.__lastName = lastName
        else:
            return TypeError
        self.__id = idNumber

    #change name in cases of marriage or mispelling
    def changeName(self, firstName, lastName):
        if (type(firstName) == str):
            self.__firstName = firstName
        else:
            return TypeError
        if (type(lastName) == str):
            self.__lastName = lastName
        else:
            return TypeError

    #set the job title, and department
    def setJob(self, jobTitle, department):
        if (type(jobTitle) == str):
            self.__jobTitle = jobTitle
        else:
            return TypeError
        if (type(department) == str):
            self.__department = department
        else:
            return TypeError

    #return employee details
    def getName(self):
        name = (self.__firstName + " " + self.__lastName)
        return name

    def getID(self):
        return self.__id

    def getJobTitle(self):
        return self.__jobTitle

    def getDepartment(self):
        return self.__department
