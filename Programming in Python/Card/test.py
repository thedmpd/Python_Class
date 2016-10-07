__author__ = 'Diogo Delgado'
"""
For this assignment you will submit three separate modules:
one with the main application that thoroughly tests class Hand.
The other two in separate files.
"""

import hand
import pickle
import json

#first two hands for bad values.
print("________________")
print("hand one- test for string value into __init__")
try:
    handOne = hand.Hand("assc")
    handOne.bjValue()
except TypeError:
    print("Please use an integer to denote how many cards you want.")
except ValueError:
    print("Please use a nonnegative integer.")

print("________________")
print("hand two- test for negative number into __init__")
try:
    handTwo = hand.Hand(-122)
    handTwo.bjValue()
except TypeError:
    print("Please use an integer to denote how many cards you want.")
except ValueError:
    print("Please use a nonnegative integer.")
    
#test for positive number of cards and then add one
print("________________")
print("hand three")
handThree = hand.Hand(5)
print("A hand with 5 cards.\n" + str(handThree))
print("The Blackjack value is: " + str(handThree.bjValue()))

#test for zero initial card and then add three
print("________________")
print("hand four")
handFour = hand.Hand(0)
print("A hand with 0 cards.\n" + str(handFour))
print("Let's add 3!")
for card in range(0,3):
    handFour.hitMe()
print(str(handFour))
print("The Blackjack value is: " + str(handFour.bjValue()))

#test for pickle initiating
print("________________")
print("hand four being saved into a pickle.")
pFile = open('pickledFiled', 'wb')
pickle.dump(handFour, pFile)
pFile.close()
#test for retrieval of pickled file
print("________________")
print("hand four information being used to create a new object, newPickleHand.")
loadedPickleFile = open('pickledFiled', 'rb')
newPickleHand = pickle.load(loadedPickleFile)
print(newPickleHand)
print("The Blackjack value is: " + str(newPickleHand.bjValue()))

#output
"""
>>> 
________________
hand one- test for string value into __init__
Please use an integer to denote how many cards you want.
________________
hand two- test for negative number into __init__
Please use a nonnegative integer.
________________
hand three
A hand with 5 cards.
This hand is made up of: 5 of Hearts, Queen of Spades, Queen of Diamonds, 4 of Clubs, 9 of Diamonds, 
The Blackjack value is: 38
________________
hand four
A hand with 0 cards.
This hand is made up of: empty hand.
Let's add 3!
This hand is made up of: Jack of Spades, 9 of Diamonds, 4 of Hearts, 
The Blackjack value is: 23
________________
hand four being saved into a pickle.
________________
hand four information being used to create a new object, newPickleHand.
This hand is made up of: Jack of Spades, 9 of Diamonds, 4 of Hearts, 
The Blackjack value is: 23
>>> 
"""

#attempt to get text file reading, data structure too complicated for json
#need to figure out new line of attack
"""
#create a file and save handFour into it.
print("________________")
print("hand four being saved into a file.")
handFourFile = open('handFourFile.text', 'w')
handFourJson = json.dumps(handFour.__dict__)
#handFourFile.writelines(line)
#handFourFile.write(str(handFour.bjValue()))
handFourFile.close()
#open handFourFile and create handFive from the information inside it.
print("________________")
print("hand five being created from handFourFile.")
handFive = hand.Hand(0)
handFourFile = open('handFourFile.text', 'r')
newList = []
for eachLine in handFourFile:
    newList.append(eachLine)
print(newList)
handFourFile.close()
print(str(handFive))
print(handFive.bjValue())
"""
