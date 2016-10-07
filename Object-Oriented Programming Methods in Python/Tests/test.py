"""
def mystery(num1, num2) :
   result = num1 * num2
   return result

print(mystery(mystery(5, 3), mystery(5, 3)))

def squareArea(sideLength) :
   return sideLength ** 2

print(squareArea(3))
def drawShape(type) :
   length = len(type)
   if length == 0 :
      return
   if type == "triangle" :
      print("  *")
      print(" ***")
      print("*****")
drawShape("triangle")
def factorial(n) :
   result = 1
   for i in range(1, n + 1) :
     result = result * i
""""""
inputFile = open("quote.txt", "r")
char = inputFile.read(1)
while char != "" :
    print(char)
    char = inputFile.read(1)
inputFile.close()
"""
"""
infile = open(input(str("Please enter the name of the input file.")), "r")
outfile = open(input(str("Please enter the name of the output file.")), "w")

counter = 0
line = infile.readline()

while line != "" :
    counter += 1
    precedingLine = "/* " + str(counter) + " */ " + line
    outfile.write(precedingLine)
    line = infile.readline()

infile.close()
outfile.close()


num = int("45") * float("1.5")
print(num)

name = "Robert"
formalName = name.upper()
print(formalName)

def allDifferent(x,y,z):
    if((x == y) or (y == z) or (x ==z)):
        return False
    else:
        return True
def signOf(x):
    if (x == 0):
        return x
    elif (x > 0):
        x = 1
        return x
    else:
        x = -1
        return x
x = 0
z = '0'
y = "o"
print(signOf(x))
print(allDifferent(x, z, y))

def repeat(string, n, delim):
    holder = ""
    while(n > 0):
        holder += string
        n -= 1
        if (n > 0):
            holder += delim
    return holder

print(repeat("ho", 10, ", "))
"""
"""
floating = 123456.6543
print(" the va lue of this is %8.2f" % floating)
n = 8
sum = 0
for i in range(1, n) :
   if i % 2 == 0 :
      sum = sum + i
print(sum)
counter = 0
for i in range (-10, 11, 2) :
    counter += 1
    print(counter)
""""""
for i in range(0, 10) :
   print(i)
i = 0 
while i <= 10 :
   print(i)
   i = i + 1
j = 1
for i in  range(0, 10) :   
   while(j < 5) :
      print("Hello")
      if j == 2 : 
         j = 6
      j = j + 1
      print(j)
   print("switch  from inner to outer", i, "  ", j)
""""""
s = "Jonathan"
print(s.endswith("n"))
""""""
s = "hello World"
b = s[5:]
print(b)

for i in range(1, 200):
    if ((i % 2 == 0) and (i % 3 == 0)):
        print(i, " ")

i = 0
grades = 0.0
userCheck = True
userInput = input("Enter your grades from 0 to 100 or type stop to quit.")
while(userCheck):
    if(userInput == "stop" or userInput == "Stop"):
        userCheck = False
    else:
        grades = grades + userInput
        i += 1
        userInput = input("Enter your grades from 0 to 100 or type stop to quit.")
if(i > 1):
    average = grades / i
    print(average)

revenue = 98456
costs = 45000
profit = revenue - costs
print(profit)
"""
"""
def final_cost(cost, bool member):
    if (member):
        cost = cost - ((cost * (10/100)) + (cost * (5/100)))
    else:
        cost = cost - (cost * (5/100))
    return cost
""""""
futureValue = 0.0
presentValue = float(input("Enter the present value of the account in dollars: "))
monthlyInterest = float(input("Enter the monthly interest rate as a percentage: "))
numberMonths = int(input("Enter the number of months: "))

def find_future_value(presentValue, monthlyInterest, numberMonths):
    holder = 0.0
    monthlyInterest = monthlyInterest / 100
    holder = presentValue * ((1 + monthlyInterest) ** numberMonths)
    return holder

futureValue = find_future_value(presentValue, monthlyInterest, numberMonths)
print("The information for your account is: ")
print("Present value: $", "{:,}".format(presentValue))
print("Interest Rate: %", monthlyInterest)
print("After 3 months, the value of your account will be $", "{:,.2f}".format(futureValue))
"""
"""
def mysteryPrint(n) :
  if n == 0 :
    return 0
  else :
    return n + mysteryPrint(n - 1)

print(mysteryPrint(-4))
"""
def main() :
   recurse(3)

def recurse(n) :
   total = 0
   if n == 0 :
      return 0
   else : 
      total = 3 + recurse(n - 1)
      print(total)
   return total
     
main()

def mystery(n) :
   if n == 0 :
      return 0
   else :
      return n % 10 + mystery(n // 10)

print(mystery(-1))


