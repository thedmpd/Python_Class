##
# This module defines the car class.
#
##
# A car that tracks its fuel consumption as it is driven.
class Car:
## Constructs a new car with a given fuel efficiency.
# @param fuel_efficiency the fuel efficiency of the car
#
    def __init__(self, mpg):
        self.__mpg = mpg
        self.__fuel = 0
## Simulate driving the car.
# @param distance the distance the car is driven
    def drive(self, miles):
        self.__fuel = self.__fuel - (miles / self.__mpg)
## Get the amount of gas in the tank.
# @return the amount of gas in the tank
    def getGasLevel(self):
        return self.__fuel
## Add gas to the car's tank.
# @param amount the amount of gas to add
    def addGas(self, gallons):
        self.__fuel = self.__fuel + gallons
   

"""
##
# Demonstrate the car class.
#
from car import Car
myHybrid = Car(50) 
myHybrid.addGas(20)
myHybrid.drive(100)
print(myHybrid.getGasLevel())

#Output#
>>> ================================ RESTART ================================
>>> 
18.0
>>> 
"""
