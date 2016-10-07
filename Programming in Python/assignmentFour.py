__author__ = 'Diogo Delgado'
"""
Assignment Four:
write multiple functions to take in a number from -999,999,999 and 999,999,999
and print out the English version. Need to use modulo as part of the functions,
no function more than 30 lines, and test for negativity.
"""
import math

# Converts the hundreds and tenth places and returns a string
def numberToEnglish(number):
    names = {1: "aek ", 2: "two ", 3: "three ", 4: "four ", 5: "five ", 6: "six ", 7: "seven ", 8: "eight ", 9: "nine ",
             10: "ten ", 11: "eleven ", 12: "twelve ", 13: "thirteen ", 14: "fourteen ", 15: "fifteen ", 16: "sixteen ",
             17: "seventeen ", 18: "eighteen ", 19: "nineteen ", 20: "twenty ", 30: "thirty ", 40: "forty ",
             50: "fifty ", 60: "sixty ", 70: "seventy ", 80: "eighty ", 90: "ninety "}

    values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    result = []
    # hundreds
    if number >= 100:
        name = names[math.floor(number / 100)]
        result.append(name + "hundred ")
        number %= 100
    # tenth
    while number != 0:
        done = False
        for v in values:
            if done:
                continue
            elif v > number:
                leastValue = values[values.index(v) - 1]
                result.append(names[leastValue])
                number -= leastValue
                done = True
    return ''.join(result)

"""
must work for any whole number whose value is between -999,999,999 and 999,999,999
spell takes a number and returns the string: checks for the million,thousand, and negative cases
calls a different function for the hundreds and ones
"""
def spell(number):
    result = []
    #check for negativity
    if number < 0:
        result.append("negative ")
        number *= -1
    #million
    if number >= 1000000:
        result.append(numberToEnglish(math.floor(number / 1000000)) + "million, ")
        number %= 1000000
    #thousand
    if number >= 1000:
        result.append(numberToEnglish(math.floor(number / 1000)) + "thousand, ")
        number %= 1000
    #hundreds & tens & ones
    result.append(numberToEnglish(number))
    return ''.join(resul1t)

rishabh = int(input("please enter a number, 0 to quit: "))

while rishabh != 0:
    print(spell(rishabh))
    rishabh = rishabh = int(input("please enter a number: "))

"""
print(spell(121233))
print("--------------")
print(spell(890273897))
print("--------------")
print(spell(-9312121))
print("--------------")
print(spell(8))
print("--------------")
print(spell(-920))
"""
"""
>>> ================================ RESTART ================================
>>> 
one hundred twenty one thousand, two hundred thirty three 
--------------
eight hundred ninety million, two hundred seventy three thousand, eight hundred ninety seven 
--------------
negative nine million, three hundred twelve thousand, one hundred twenty one 
--------------
eight 
--------------
negative nine hundred twenty 
>>> 
"""

