password = "fish"#This is the condition
guess = ""#What guess is
while (password != guess):#A while loop is a loop that continues until the condion is met
    guess = input ("Enter password: ")#Allows the user to input a password
    if password == (guess):#If the guess is correct
        print ("You are Correct.")#This prints if the guess is correct
    else:#If not correct
        print ("Try again.") #This prints when the guess is not correct