__author__ = 'Diogo Delgado'
"""
Define a class where one object of the class represents a playing card.
"""
class Card:
    suitName = {'d': 'Diamonds', 'c': 'Clubs', 'h': 'Hearts', 's': 'Spades', 'n': 'Nothing'}
    valueName = {1: 'Ace', 11: 'Jack', 12: 'Queen', 13: 'King'}
    """
    rank is a number in the range 1-13 indicating the ranks Ace through King,
    and suit is a single character "d" "c", "h", or "s" indicating the suit
    (diamonds, clubs, hearts, or spades).
    Create the corresponding card by initiating it if given proper values, otherwise create throwaway.
    """
    def __init__(self, rank, suit):
        #rank check
        if (type(rank) != int):
            raise TypeError()
        elif ((rank < 1) or (rank > 13)):
            raise ValueError()
        else:
            self.rank = rank
        #suit check
        if (type(suit) != str):
            raise TypeError()
        elif (suit not in Card.suitName):
            raise ValueError()
        else:
            self.suit = suit

    #Returns the rank of the card
    def getRank(self):
        return self.rank
    
    #Returns the suit of the card
    def getSuit(self):
        return self.suit
    
    #Returns the Blackjack value of a card. Ace counts as 1,
    #face cards count as 10.
    def bjValue(self):
        if self.rank > 10:
            return 10
        else:
            return self.rank
        
    #Returns a string that names the card. For example. "Ace of Spades".
    def __str__(self):
        if self.getRank() in Card.valueName:  # if valueDict has key
            rank = Card.valueName[self.getRank()]
        else:
            rank = self.getRank()
        return str(rank) + " of " + Card.suitName[self.getSuit()]


if (__name__ == "__main__"):
    #test correct values
    print("________________")
    print("hand one")
    try:
        handOne = Card(3, 'c')
        handOne.bjValue()
    except TypeError:
        print("That card value does not exist. Please choose from 1-13.")
    except ValueError:
        print("Please input a number value for the card from 1-13.")
    try:
        handOne = Card(3, 'c')
        print(handOne)
    except TypeError:
        print("Please choose one of the four suits.")
    except ValueError:
        print("Please input a character denoting one of the four suits.")

    #test false values(both)
    print("________________")
    print("hand two")
    try:
        handTwo = Card('c', 7)
        handTwo.bjValue()
    except TypeError:
        print("That card value does not exist. Please choose from 1-13.")
    except ValueError:
        print("Please input a number value for the card from 1-13.")
    try:
        handTwo = Card('c', 7)
        print(handTwo)
    except TypeError:
        print("Please choose one of the four suits.")
    except ValueError:
        print("Please input a character denoting one of the four suits.")
    #test false values(suits)
    print("________________")        
    print("hand three")
    try:
        handThree = Card(7, 7)
        handThree.bjValue()
    except ValueError:
        print("That card value does not exist. Please choose from 1-13.")
    except TypeError:
        print("Please input a number value for the card from 1-13.")
    try:
        handThree = Card(7, 7)
        print(handThree)
    except ValueError:
        print("Please choose one of the four suits.")
    except TypeError:
        print("Please input a character denoting one of the four suits.")
    #test false values(value)
    print("________________")
    print("hand four")
    try:
        handFour = Card('c', 'd')
        handFour.bjValue()
    except ValueError:
        print("That card value does not exist. Please choose from 1-13.")
    except TypeError:
        print("Please input a number value for the card from 1-13.")
    try:
        handFour = Card('c', 'd')
        print(handFour)
    except ValueError:
        print("Please choose one of the four suits.")
    except TypeError:
        print("Please input a character denoting one of the four suits.")

    # Valid Inputs and Face card check
    handOne = Card(7, "h")
    print(handOne)
    print("BlackJack: ", handOne.bjValue())
    print("________________")
      
    handTwo = Card(11, "s")
    print(handTwo)
    print("BlackJack: ", handTwo.bjValue())
    print("________________")

    handThree = Card(13, "h")
    print(handThree)
    print("BlackJack: ", handThree.bjValue())
    print("________________")

    handFour = Card(9, "h")
    print(handFour)
    print("BlackJack: ", handFour.bjValue())
    print("________________")

"""
>>> 
________________
hand one
3 of Clubs
________________
hand two
That card value does not exist. Please choose from 1-13.
Please choose one of the four suits.
________________
hand three
Please input a number value for the card from 1-13.
Please input a character denoting one of the four suits.
________________
hand four
Please input a number value for the card from 1-13.
Please input a character denoting one of the four suits.
7 of Hearts
BlackJack:  7
________________
Jack of Spades
BlackJack:  10
________________
King of Hearts
BlackJack:  10
________________
9 of Hearts
BlackJack:  9
________________
"""
