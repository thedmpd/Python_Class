fibonacci = {1, 1, 2, 3, 5, 8}
primes = {2, 3, 5, 7, 11}
both = fibonacci.union(primes)
print(both)

fruit = set(["apple", "banana", "grapes", "kiwi"])
fruit2 = set(["apple", "banana", "grapes"])
fruit3 = set(["apple", "banana", "pears", "kiwi"])
if fruit2.issubset(fruit) : 
   print("fruit2 is a subset of fruit")
if fruit == fruit3 : 
   print("fruit and fruit3 are equal")
if fruit != fruit2 : 
   print("fruit and fruit2 are not equal") 

names = set(["Jane", "Joe", "Amy", "Lisa"])
names.add("Amber")
names.add("Zoe")
names.clear()
print(names)

names = set(["Jane", "Joe", "Amy", "Lisa"])
names.add("Amber")
names.add("Zoe")
names.discard("Jim")
print(names)

values = [1991, 1875, 1980, 1965, 2000]
values.sort()
print(values)

print(max(["Roland", "Kent", "Ravi", "Amy"]))

nums = [1, 2, 3, 4, 5]
nums2 = [5, 4, 3, 2, 1]
print(nums in nums2)

firstNames = ["Joe", "Jim", "Betsy", "Shelly"]
lastNames = states = ["Jones", "Patel", "Hicks", "Fisher"]
fullNames = firstNames + lastNames
print(fullNames)

states = ["Alaska", "Hawaii", "Florida", "Maine", "Ohio", "Florida"]
states.remove('Florida')
print(states)

states = ["Alaska", "Hawaii", "Florida", "Maine", "Ohio", "Florida"]
removedValue = states.pop(3)
print(removedValue)

states = ["Alaska", "Hawaii", "Florida", "Maine", "Ohio", "Florida"]
#indexValue = states.index("Pennsylvania")
#print(indexValue)

names = []
names.append("Amy")
names.append("Bob")
names.append("Peg")
names[0] = "Cy"
names.insert(0, "Ravi")
names.insert(4, "Savannah")

print(names)

values = [1.618, 2.71, 3.14]
#print(values[3])

prices = [10.00, 15.50, 13.25, 20.15]
values = prices
print(values)

for i in range(len(values)) :
   print(values[i])

for element in values : 
   print(element)
   
for i in range(1, len(values)) : 
   print(values[i])

somelist = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",  "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
for i in range(0, len(somelist), 2) :
   print(somelist[i], end = "")
   
holder = ""
for element in somelist:
    holder = holder + " " + str(element)
print(holder)

product = 1
for element in values:
    product = product * element

print(product)

a = [1, 4, 9, 16]
b = [9, 7, 4, 9, 11, 0]

def merge(a, b):
    size = max(len(a), len(b))
    i = 0

    newList = []
    if (size == len(a)):
        while (i < len(b)):
            newList.append(b[i])
            newList.append(a[i])
            i += 1
        while (i < len(a)):
            newList.append(a[i])
            i += 1
    else:
        while (i < len(a)):
            newList.append(a[i])
            newList.append(b[i])
            i += 1
        while (i < len(b)):
            newList.append(b[i])
            i += 1
    return newList

    
print(merge(a,b))
