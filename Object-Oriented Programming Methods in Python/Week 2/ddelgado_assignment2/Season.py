'''
* Program #: AssignmentTwo_Season
* Programmer: Diogo M Delgado
* Due: 7/11/2016
* CS 3A, summer 2016
* Description: Create an algorithm that prints out the season depending on
   the month and date entered by the user.
'''

#globalVariables
userMonth = int(input("Enter the month as an integer: "))
userDay = int(input("Enter the day as an integer: "))
season = " "

#check for appropriate values
while ((userMonth <= 0) or (userMonth > 12)):
    userMonth = int(input("Enter an appropriate month as an integer(1-12): "))

while ((userDay <= 0) or (userDay  > 31)):
    userDay = int(input("Enter an appropriate day as an integer(1-31: "))

#determine the season
if ((userMonth > 0) and (userMonth < 4)):
    season = "Winter"
elif ((userMonth > 3) and (userMonth < 7)):
    season = "Spring"
elif ((userMonth > 6) and (userMonth < 10)):
    season = "Summer"
else:
    season = "Fall"

#determine season by looking at current season and day
if (((userMonth % 3) == 0) and (userDay >= 21)):
    if (season == "Winter"):
        season = "Spring"
    elif (season == "Spring"):
        season = "Summer"
    elif (season == "Summer"):
        season = "Fall"
    else:
        season = "Winter"

#output the result to the user
print("That day is in the ", season)

"""
>>> ================================ RESTART ================================
>>> 
Enter the month as an integer: 11
Enter the day as an integer: 21
That day is in the  Fall
>>> ================================ RESTART ================================
>>> 
Enter the month as an integer: 01
Enter the day as an integer: 2
That day is in the  Winter
>>> ================================ RESTART ================================
>>> 
Enter the month as an integer: -2
Enter the day as an integer: -21
Enter an appropriate month as an integer(1-12): 12
Enter an appropriate day as an integer(1-31: 31
That day is in the  Winter
>>> 
>>> ================================ RESTART ================================
>>> 
Enter the month as an integer: 04
Enter the day as an integer: 21
That day is in the  Spring
>>> ================================ RESTART ================================
>>> 
Enter the month as an integer: 7
Enter the day as an integer: 26
That day is in the  Summer
>>> 
"""
