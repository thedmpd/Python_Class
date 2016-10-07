'''
* Program #: Teams from Assignment 5
* Programmer: Diogo M Delgado
* Due: 8/01/2016
* CS 3A, summer 2016
* Description: Given a txt file containing all the winners of the world
    series from 1903 to 2009, with the exception of 04 and 94 as no finals
    were held, open the file and input the contents into a list. Use the list
    to count the occurances of winners from that time period when a user asks
    for a teams trophy count.
'''
import os
#import file and check for validity
def main():    
    worldSeriesList = []
    worldSeriesList = listCreation(worldSeriesList)

    userInput = input("Enter the name of a team: ")
    wins = searchOccurrences(userInput, worldSeriesList)
    print("The " + str(userInput) + " won the world series "
          + str(wins) + " times between 1903 and 2009.")
    
#import file and check for validity, and create a list of values from text
def listCreation(lst):
    fileCheck = True
    fileName = input("Please enter the name of " +
                         "the file you'd like to use: ").strip()
    while (fileCheck):
        if(os.path.exists(fileName)):
            fileCheck = False
        else:
            print("File not found.")
            fileName = input("Please enter the name of " +
                         "the file you'd like to use: ").strip()

    infile = open(fileName, 'r')
    
    for line in infile:
        lst.append(line.lower().strip())
    return lst

#count the number of occurrences a team has during the time period
def searchOccurrences(teamName, lst):
    trophies = lst.count(teamName.lower())
    return trophies

#run the main
main()

"""
>>> ================================ RESTART ================================
>>> 
Please enter the name of the file you'd like to use.hey
File not found.
Please enter the name of the file you'd like to use.Wor
File not found.
Please enter the name of the file you'd like to use.WorldSeriesWinners.txt
Enter the name of a team: New York Giants
The New York Giants won the world series 5 times between 1903 and 2009.
>>> 
"""
