"""
 * Program: Book Order
 * Programmer: Diogo Delgado
 * Due: 7/5/2016
 * CS21A, summer 2016
 * Description: Create a program that takes in a book price and the amount of
      books. Calculate the total price given that tax is 7.5 % of the book price
      and add a $2.00 shipping charge per book and output that number.
"""

#global variables
bookPrice = 0.0
bookQuantity = 0
taxRate = 7.5 / 100
shippingCharge = 2.0
totalCost = 0.0

#get input from the user, make sure they are unable
# to give negative prices or qty
bookPrice = float(input("Enter the book price: "))
while (bookPrice <= 0):
    bookPrice = float(input("Please enter a number greater than 0: "))
bookQuantity = int(input("Enter the number of books: "))
while (bookQuantity <= 0):
    bookQuantity = int(input("Please enter a number greater than 0: "))

#calculate the tax
totalCost = ((bookPrice * bookQuantity) * taxRate)
#calculate the total cost
totalCost = totalCost + (bookPrice * bookQuantity) + (bookQuantity * shippingCharge)
#print total cost
print("The total cost of the order is " + str(round(totalCost,2)))


#program output
"""
>>> ================================ RESTART ================================
>>> 
Enter the book price: 32
Enter the number of books: 1
The total cost of the order is 36.4
>>> ================================ RESTART ================================
>>> 
Enter the book price: -122
Please enter a number greater than 0: 53
Enter the number of books: -12233300
Please enter a number greater than 0: 989
The total cost of the order is 58326.28
>>> ================================ RESTART ================================
>>> 
Enter the book price: 45.5
Enter the number of books: 2
The total cost of the order is 101.83
>>> 
"""
