cardSuit = {"hearts", "clubs", "diamonds", "spades"}

userCard = input("Name a card suit: ")
userCard = userCard.lower()

if (userCard in cardSuit):
    print("Congrats! You got it right.")
else:
    print("sorry that was not a valid suit.")
