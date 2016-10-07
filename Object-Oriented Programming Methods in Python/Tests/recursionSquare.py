"""

##
# Compute the area of a rectangle recursively.
#
## A class to represent a rectangle.
# 
class Rectangle :
    ## Construct a new rectangle.
    # @param w the widht of the rectangle
    # @param h the height of the rectangle
    #
    def __init__(self, w, h) :
        self._width = w
        self._height = h
    ## Compute the area of the rectangle recursively.
    # @return the area of the rectangle
    #
    def area(self):
        if (self._width == 1):
            return (self._height)
        else:
            sR = Rectangle(self._width - 1, self._height)
            smallerArea = sR.area()
            return self._height + smallerArea

 


def main() :
# Demonstrate that the area is computed correctly.
    r = Rectangle(20, 25)
    print(r.area())
    print("Expected: 500")
# Call the main function.
main()



def find(text, string):
    if len(string) > len(text):
        return False
    for i in range(len(string)):
        if text[i] != string[i]:
            return find(text[1:], string)
    return True

print(find("Mississippi", "sip"))
print(find("HelloWorld", "Love"))
print(find("HelloWorld", "Hell"))

values = []
values.append("Hydrogen")
values.append("Helium")
values.append("Lithium")

print(values)



values = [1, 2, 3]
values = values * 4
print(values)

hello = dict
hello = { 1 : 'January', 2 : 'February', 3 : 'March' }

print(hello[1])

hello["Ravi"] = 'chocolate'
hello["Ravi"] = 'strawberries'
print(hello)



list1 = [1, 3, 2, 4, 5, 2, 1, 0]

print(list1[:-2])
print(list1[-8:2])
print(list1[0])
print(list1[4:6])
print(list1[:2])



list1 = [1, 2, 3]
list2 = []
for element in list1:
 list2.append(element) 
list1 = [4, 5, 6]
print(list2)

fruit = {"Apple": "Green", "Banana": "Yellow"}
fruit["Plum"] = "Purple"
if "Appley" in fruit :
    print(fruit)

days = {}
days["February"] = [28, 29]
print(days)

pets = {}
pets["Snowball"] = {77, 4.5, "Cat"}
pets["Spike"] = {132, 23.1, "Dog"}

print(pets)

class PhoneNumber :
  
   def __init__(self, lName, phone = "215-555-1212") :
      self._name = lName
      self._phone = phone

   def getName(self):
      return self._name

   def getPhone(self):
      return self._phone

Jones = PhoneNumber("Jones")
print(Jones.getName(), Jones.getPhone())

class Contact :
   def __init__(self, name, phone=""):
      self._name = name
      self._phone = phone

   def getName(self) :
      return self._name

   def setName(self, new_name) :
      self._name = new_name

   def getPhone(self) :
      return self._phone

   def setPhone(self, new_phone) :
      self._phone = new_phone

p1 = Contact("Bob", "555-123-4567")
p2 = Contact("Joe", "555-000-0000")
p1.setName(p2.getName())

print(p1.getPhone())

aList = [123, 'xyz', 'zara', 'abc', 'xyz', 'xyz'];

aList.remove('xyz');
print("List : ", aList)
aList.remove('abc');
print("List : ", aList)

def double(hello = []):
    temp = []
    temp = hello * 2
    return temp

print(double(aList))

nList = [123, 4, 434, 54, 56, 322 ,343421, 67, 77]

def remove_evens(nList = []):
    temp = []
    for i in range(len(nList)):
        if (nList[i] % 2 == 1):
            temp.append(nList[i])
    return temp            


print(remove_evens(nList))
"""
"""
def main():
    courses = {
        'CS101': 3004,
        'CS102': 4501,
        'CS103': 6755,
        'NT110': 1244,
        'CM241': 1411
        }
    userInput = input("Enter a course: ")
    if userInput in courses:
        print(str(userInput) + " is in room " + str(courses[userInput]))
    else:
        print("That class was not found")

main()
"""
"""
def len(string = ""):
    if (string == ""):
        return 0
    else:
        return 1 + len(string[1:])



print(len("he;llo"))
"""
class Register:
    #initiate the register to set all values to 0
    def __init__(self):
        self.__setCount = 0
        self.__setTally = 0

    #process the vehicles
    def ProcessCar(self, car):
        self.__setCount += car
        self.__setTally += (car * 1)

    def ProcessTruck(self, truck):
        self.__setCount += truck
        self.__setTally = self.__setTally + (truck * 2)

    #get the tally and count numbers
    def getCount(self):
        return self.__setCount

    def getTally(self):
        return self.__setTally

    #setCount and setTally methods in case of the need to reset
    def setTally(self, monies):
        self.__setTally = monies

    def setCount(self, count):
        self.__setCount = count

def main():
    register = Register()

    userInput = input(str("Enter type of vehicle (car/truck): "))
    while (userInput != 'N'):
        if userInput == 'car':
            register.ProcessCar(1)
        elif userInput == 'truck':
            register.ProcessCar(1)
        else:
            print("Vehicle did not match our records.")
        print("Number of vehicles: " + str(register.getCount()))
        print("Money Collected: ", '{:2,.2f}'.format(register.getTally()))
        userInput = input("Do you want to enter more vehicles (Y/N)? ")
        if userInput != 'N':
            userInput = input(str("Enter type of vehicle (car/truck): "))

main()

















































