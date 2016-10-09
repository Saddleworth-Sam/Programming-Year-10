# Import Libraries
import random#This allows random.randrange, randomly choose a positon for the ball

# Set flag variables
runAgain = 'y'#This allows the user to input y and it will run the game again
score = 0#Integer

#Loop until the user wants the program to end
while runAgain == "y":#sring
    #Initialise the cups and randomly place the ball
    cups = [0, 0, 0]#This is the position of the cup
    ballPosition = random.randrange(0, 2)#Integer
    cups[ballPosition] = 1#This is the position of the cup

    #Display the welcome screen and
    strScore = str(score)#str is a shortand version of String
    print("Guess where the ball is!")#String
    print("You score: " + strScore)#This prints what strScore equals

    #Get the cup choice from the user
    guess = input("Which cup is the ball in, cup A, B, or C?")#Allows the user to input where the cup is

    # Convert it to uppercase to make a validation eaisier
    guess = guess.upper()#What guess is

    # Chuck which cup they chose and convert this to the corresponding
    # position in our list. Use -1 for an invalid choice
    if guess == 'A':#This is an IF Statement
        guessPos = 0#This is the position of the cup
    elif guess == 'B':#Is the users guess is B
        guessPos = 1#This is the position of the cup
    elif guess == 'C':#If the users guess is A
        guessPos = 2#Tells the user how many guesses the user has had
    else:#If the user inputs an invalid variable
        guessPos = -1#This is the position of the cup
    # Check whether the ball is in that position
    if guessPos != -1:#This is the position of the cup
        if cups[guessPos] == 1:#This is the position of the cup
            # If so, increment the score and say well done
            print("Well Done! The was in Cup " + guess)#If the user guesses correctly
            score = score + 1#What score is
        else:#If the user guess incorrectly
            # If not, inform the user
            print("Bad luck. The ball wasn't in Cup " + guess)#This prints if the user guesses incorrectly
    else:#This prints if the user inputs an invalid choice
            #If they didn't type  A, B, or C, tell them!
            print("Invalid choice! Please pick A.B or C next time!")#Print, prints the purple writing on the screen

    # Ask the user if they wish to run the program again
    runAgain = input("Press y to go again.")#Allows the user to play again

    #Display their final score on exit
strScore = str(score)#What strScore is
print("Final Score: " + strScore)#Prints the users final score
input("Press enter to exit")#Input allows the user to press the Enter key to exit the game