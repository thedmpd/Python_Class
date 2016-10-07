"""
 * Program: Large Letter
 * Programmer: Diogo Delgado
 * Due: 7/5/2016
 * CS21A, summer 2016
 * Description: Create a program that writes large letters with string literals.
    The letters should follow the same pattern and size as the following H:
    *   *
    *   *
    *****
    *   *
    *   *
    With this in mind, create a program that prints out 'HELLO' vertically.
"""

#variables that hold the declared letter format
largeLetterH = "*   *\n*   *\n*****\n*   *\n*   *"
largeLetterE = "*****\n*\n***\n*\n*****"
largeLetterL = "*\n*\n*\n*\n*****"
largeLetterO = " *** \n*   *\n*   *\n*   *\n *** "

#print the letters in a specified format with one space in between each letter
print(largeLetterH)
print("\n")
print(largeLetterE)
print("\n")
print(largeLetterL)
print("\n")
print(largeLetterL)
print("\n")
print(largeLetterO)

#program output
"""
>>> ================================ RESTART ================================
>>> 
*   *
*   *
*****
*   *
*   *


*****
*
***
*
*****


*
*
*
*
*****


*
*
*
*
*****


 *** 
*   *
*   *
*   *
 *** 
>>> 
"""
