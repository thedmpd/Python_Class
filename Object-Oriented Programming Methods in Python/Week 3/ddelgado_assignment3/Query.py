'''
* Program #: Query Assigment 3
* Programmer: Diogo M Delgado
* Due: 7/18/2016
* CS 3A, summer 2016
* Description: Create a program that defines a looks through one file to find
    a match for a phone number for the user in order to use the user's name to
    find their social. 
'''
#global Variables
phoneNumber = str(input("Enter the phone number (7 digits, with a dash): "))
dataList = []

#open data lists
inputFile = open("data1.txt", "r")
inputSocial = open("data2.txt", "r")
dataLine = inputFile.read().strip()
socialFile = inputSocial.read().strip()

#helper functions to find the data
def findInformation(dataLine, phoneNumber, socialFile):
    nameNumbers = dataLine.splitlines()
    separateNames = []
    i = 0
    j = 0
    while i < len(nameNumbers):
        holder = nameNumbers[i]
        holder = holder.split(',')
        holder[j + 1] = holder[j + 1].strip()
        if (phoneNumber in holder):
            separateNames.append(holder[j])
            print(phoneNumber, "is associated with", separateNames[j])
            findSocial(separateNames[j], socialFile)
            i = len(nameNumbers)
        elif ((len(separateNames) < 1) and (i + 1== len(nameNumbers))):
            print("No names match that number")
            i +=1;
        else:
            i += 1;

def findSocial(name, socialFile):
    socialNumbers = socialFile.splitlines()
    socialNames = []
    i = 0
    j = 0
    while i < len(socialNumbers):
        social = socialNumbers[i]
        social = social.split(',')
        social[j + 1] = social[j + 1].strip()
        if (name in social):
            socialNames.append(social[j + 1])
            print(socialNames[j], "is associated with", name)
            i = len(socialNumbers)
        elif ((len(socialNames) < 1) and (i + 1== len(socialNumbers))):
            print("Couldn't find a SSN for", name)
            i +=1;
        else:
            i += 1;

#main program
findInformation(dataLine, phoneNumber, socialFile)
inputSocial.close()
inputFile.close()

"""
>>> ================================ RESTART ================================
>>> 
Enter the phone number (7 digits, with a dash): 555-1234
555-1234 is associated with Bob
Couldn't find a SSN for Bob
>>> ================================ RESTART ================================
>>> 
Enter the phone number (7 digits, with a dash): 555-3456
555-3456 is associated with Mark
000000002 is associated with Mark
>>> ================================ RESTART ================================
>>> 
Enter the phone number (7 digits, with a dash): 000-1234
000-1234 is associated with Luke
000000003 is associated with Luke
>>> ================================ RESTART ================================
>>> 
Enter the phone number (7 digits, with a dash): 000-2345
000-2345 is associated with John
Couldn't find a SSN for John
>>> ================================ RESTART ================================
>>> 
Enter the phone number (7 digits, with a dash): 555-2345
555-2345 is associated with Matthew
000000001 is associated with Matthew
>>> ================================ RESTART ================================
>>> 
Enter the phone number (7 digits, with a dash): 2788-4903
No names match that number
>>> 
"""

