'''
* Program #: AssignmentTwo_ExtraCredit_PIN
* Programmer: Diogo M Delgado
* Due: 7/11/2016
* CS 3A, summer 2016
* Description: Create an ATM like program that asks for the user's pin,
    and gives the user 3 tries before locking the card if the inputs are
    incorrect. The initial PIN is set as '1234'.
'''

#userPin
userPin = 1234
#exit condition: tracks user attempts and is the key to exit loop
userTries = 0

while (userTries < 3):
    #get user provided PIN attempt
    userAttempt = int(input("Enter your PIN: "))
    #check for correct or overAttempts
    if (userAttempt == userPin):
        print("Your PIN is correct.")
        userTries = 3
    elif ((userAttempt != userPin) and (userTries < 2)):
        print("Your PIN is incorrect.")
        userTries += 1
    else:
        print("Your bank card is blocked.")
        userTries += 1

    
"""
>>> ================================ RESTART ================================
>>> 
Enter your PIN: 3245
Your PIN is incorrect.
Enter your PIN: 2346
Your PIN is incorrect.
Enter your PIN: 2341
Your bank card is blocked.
>>> ================================ RESTART ================================
>>> 
Enter your PIN: 3131
Your PIN is incorrect.
Enter your PIN: 3245
Your PIN is incorrect.
Enter your PIN: 1234
Your PIN is correct.
>>> ================================ RESTART ================================
>>> 
Enter your PIN: 1234
Your PIN is correct.
>>> 
"""
