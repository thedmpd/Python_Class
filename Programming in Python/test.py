import assignmentFive
import random
hand = 0
while (hand < 22):
    userInput = int(input("If you want to draw a card type 1, 2 to stay."))
    if userInput == 1:
        handOne = assignmentFive.Card(random.randint(1,13),"s")
        hand = hand + handOne.bjValue()
        print("your current hand is: ", hand)
    else:
        print("your final hand value was: ", hand)
        hand = 23
