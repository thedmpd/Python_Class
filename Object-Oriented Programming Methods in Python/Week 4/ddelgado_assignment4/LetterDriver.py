'''
* Program #: Letter Class Driver Assigment 4
* Programmer: Diogo M Delgado
* Due: 7/25/2016
* CS 3A, summer 2016
* Description: Create a program that uses the Letter class in order
    to create a letter with two lines and print it out.
'''

from Letter import Letter

johnLetter = Letter("Mary", "John")
johnLetter.addLine("I am sorry we must part.")
johnLetter.addLine("I wish you all the best.")

print(johnLetter.getText())

#output
"""
>>> ================================ RESTART ================================
>>> 
Dear John:

I am sorry we must part.
I wish you all the best.

Sincerely,

Mary
>>> 
"""
