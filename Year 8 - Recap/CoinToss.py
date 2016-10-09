#This code tosses the coin

import random#This allows random.choice to work

def cointoss():

    options = ("heads", "tails")#These are the options
    result = random.choice(options)#This randomly chooses heads or tails 6 times
    print ("\n") #Print blank line
    print (result)#This prints what the result is
cointoss()#Tosses the coin (Heads or Tails)
cointoss()#Tosses the coin (Heads or Tails)
cointoss()#Tosses the coin (Heads or Tails)
cointoss()#Tosses the coin (Heads or Tails)
cointoss()#Tosses the coin (Heads or Tails)
cointoss()#Tosses the coin (Heads or Tails)


#This code rolls the dice

import time#This allows the code below to work
time.sleep (3)#Waits 2 seconds

import random#This allows random.choice to work

def diceroll():#This is here so diceroll prints 6 of the options

    options = ("1 2 3 4 5 6")#These are the options
    result = random.choice(options)#This randomly chooses numbers between 1 and 6, 6 times
    print ("\n")#This prints a blank line
    print (result)#This prints what the result is
diceroll()#Rolls dice (inputs a random number between 1-6)
diceroll()#Rolls dice (inputs a random number between 1-6)
diceroll()#Rolls dice (inputs a random number between 1-6)
diceroll()#Rolls dice (inputs a random number between 1-6)
diceroll()#Rolls dice (inputs a random number between 1-6)
diceroll()#Rolls dice (inputs a random number between 1-6)