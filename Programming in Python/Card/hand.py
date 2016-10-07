__author__ = 'Diogo Delgado'
"""
Create a class Hand in its own module. One object of class Hand represents
a hand of cards and so one object stores a number of Card objects. For this
assignment you will submit three separate modules, one with the definition
of class Card, one with the definition of class Hand and one with the main
application that thoroughly tests class Hand.

class Hand must contain the following four methods:

1)   __init__(self, numCardsInHand) takes an integer as parameter and
initializes a Hand object with numCardsInHand Card objects inside it.
These Card objects are generated randomly. For simplicity, assume an
infinite number of decks of cards.

2)   bjValue(self) returns the blackjack value for the whole Hand of cards

3)   __str__(self) returns a string containing all the Cards in the Hand

4)   hitMe(self) adds one randomly generated Card to the Hand
"""

import card
import random

class Hand:
    handOfCards = []
    #create a new hand with a given amount of cards whose value is random
    def __init__(self, howManyCards):
        if (type(howManyCards) != int):
            raise TypeError()
        elif (howManyCards < 0):
            raise ValueError()
        else:
            self.handOfCards = []
            for cards in range(howManyCards):
                self.hitMe()

    #returns a string containing all the Cards in the Hand
    def __str__(self):
        hand = "This hand is made up of: "
        if (len(self.handOfCards) == 0):
            hand += "empty hand."
        else:
            for cards in self.handOfCards:
                hand += str(cards) + ", "
        return hand

    #adds one randomly generated Card to the Hand
    def hitMe(self):
        newCard = card.Card(random.randint(1,13), random.choice("dchs"))
        self.handOfCards.append(newCard)

    #returns the blackjack value for the whole Hand of cards
    def bjValue(self):
        handValue = 0
        for cards in self.handOfCards:
            handValue += cards.bjValue()
        return handValue




    
            
