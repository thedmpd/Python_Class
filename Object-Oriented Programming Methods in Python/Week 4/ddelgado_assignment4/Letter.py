'''
* Program #: Letter Class Assigment 4
* Programmer: Diogo M Delgado
* Due: 7/25/2016
* CS 3A, summer 2016
* Description: Create a program that defines a class Letter which
    initializes a letter object with attributes such as author, receiver and
    add new line so that it can be continuously written one line at a time.
'''

class Letter:
    
    #initiate with author, receiver #
    def __init__(self, letterFrom, letterTo):
        if (type(letterFrom) == str):
            self.__letterFrom = letterFrom
        else:
            return TypeError
        if (type(letterTo) == str):
            self.__letterTo = letterTo
        else:
            return TypeError
        self.__body = ""

    #method to add a line to body
    def addLine(self, line):
        self.__body = self.__body + "\n" + line

    #method to return all text of letter
    def getText(self):
        return "Dear " + self.__letterTo + ":" + \
               "\n" + self.__body + \
               "\n\n" + "Sincerely," + \
               "\n\n" + self.__letterFrom
               
        
    

    
