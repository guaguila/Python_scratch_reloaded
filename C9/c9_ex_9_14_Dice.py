#9-14. Dice: The module random contains functions that generate random numbers in a variety of ways. The function randint() returns an integer in the range you provide. The following code returns a number between 1 and 6:

#from random import randint
#x = randint(1, 6)

#Make a class Die with one attribute called sides, which has a default value of 6.
# Write a method called roll_die() that prints a random number between 1 and the number of sides the die has.

#Make a 6-sided die and roll it 10 times.
#Make a 10-sided die and a 20-sided die.

#Roll each die 10 times


from random import randint
"""Represents a dice that we can roll"""

class Dice():
    def __init__(self, sides = 6):
        self.sides = sides


    def roll_dice(self, times):
        print("\rThese are the results for a " + str(self.sides)
              + " sided dice rolling " + str(times) + " times:")
        format = []
        for i in range (times):
            random = randint(1, self.sides)
            format.append(random)
            #print ("\t" + str(random))
        print(str(format))
        print ("\t" + "This list has " + str(len(format)) + " elements"  + "\n")

#This is a variation that I did allowing the user to enter the qty of rolls.
#times = int(input ("Enter the number of rolls:"))


dice6 = Dice()
dice6.roll_dice(10)

dice10 = Dice(10)
dice10.roll_dice(10)

dice20 = Dice(20)
dice20.roll_dice(10)

