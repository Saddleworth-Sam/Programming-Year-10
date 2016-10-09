endLoop = 0#What endloop is
while endLoop == 0:#The start of a while loop, a while loop is a loop that carries on until a condition is met
    endCheck = input("Do you want it to stop? Y/N")#This is the condition
    if endCheck == 'y' or endCheck =='Y':#If the user has inputted the condition
        endLoop = 1#The loop ends
print ("I'm glad that's over with!")#When the loop ends