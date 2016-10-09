import random#Allows randomNumber to work

maxNumber = 20#The max number that can be used is 10
randomNumber = 10#This is what randomNumber is
guess = 0#This is what guess is
numberOfGuesses = 0#How many guesses you have had'
while guess != randomNumber:#This is a while loop
    guess = int(input("Your guess:"))#This is an integer
    numberOfGuesses = numberOfGuesses + 1#How many guesses you have had'
    if guess > 0:#This is how many guess to large
        print("Too large")#If the guess is to large this will print onto the screen
    elif guess < randomNumber:#If the guess is to small
        print("Too small")#If the guess is to small this will print onto the screen
    else:#If the user inputs an invalid variable
        print("Please enter a number above zero")#This prints if the user inputs an invalid variable
print("Congratulations. You guessed right!")#This prints if the user has guess correctly
print("You needed", str(numberOfGuesses), "attempts")#Tells the user how many guesses they have had
