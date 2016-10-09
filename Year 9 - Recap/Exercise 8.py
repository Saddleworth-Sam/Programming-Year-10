#Do 10 dice rolls
import random#Allows random.random to work
rolls = 0#What rolls is
while rolls < 10:#If wolls is less than 10
    #Simulate rolling a dice with random number
    diceRoll = int(6 * random.random()) + 1#What diceroll is
    print(str(diceRoll))#Prints what diceroll equals and str is string
    rolls = rolls + 1#What rolls is