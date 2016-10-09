#General Elections

from random import randint

import time#Allows time.sleep(2) work

votes1 = (randint(1, 30000))#What votes1 is
votes2 = (randint(1, 30000))#What votes2 is
votes3 = (randint(1, 30000))#What votes3 is
votes4 = (randint(1, 30000))#What votes4 is

print("Presidential Election 2016")#Prints onto the screen
print("\n")#Prints a blank line
time.sleep(1)#Waits 1 second then prints the code below
print("Candidates: ")#Prints after one second
print("\n")#Prints a blank line
print("1.Barack Obama")#Who the user can vote for
print("2.David Cameron")#Who the user can vote for
print("3.Donald Trump")#Who the user can vote for
print("4.Hilary Clinton")#Who the user can vote for
print("\n")#Prints a blank line

president = input("Candidate: ")#Allows the user to input who they want to vote for
president = president.lower()#What president is

#Barack Obama
if president == ("barack obama") or president == ("obama") or president == ("barack") or president == ("1"):#If the user inputs 1 or Barrack obama
    print("You chose: Barack Obama")#THis prints if the user chose Barrack obama
    print("\n")#Prints a blank line
#Checks if you want to continue
    obamacheck = input("Do you wish to continue? Y/N: ")#Allows the user to input if they want to continue
    obamacheck = obamacheck.lower()#What obamacheck is
    #checks if the user has entered yes or y
    if obamacheck == ("y") or obamacheck == ("yes"):#If obamacheck is y or Y
        print("Vote processed.")#Prints after inputted y or Y
        print("Barack Obama's current votes: ", + votes1+1)#[rints how many votes Barrck obama has had
        time.sleep(1)#Waits one second then prints the code below
        print("\n")#Prints a blank line
        print("General Election 2016 Finished!")#Prints when they have voted
        print("\n")#Prints a blank line
        print("Here are the candidates with their votes: ")#Prints the mount of votes each candidate got
        print("Barack Obama: ", + votes1+1)#Prints how many votes Barrack obama got including the users vote
        print("David Cameron: ", + votes2)#Prints how many votes David Cameron got
        print("Donald Trump: ", + votes3)#Prints how many votes Donald Trump got
        print("Hilary Clinton: ", + votes4)#Prints how many vote Hilary Clinto got
    else:#If the user inputs N
        print("Vote cancelled.")#This Prints if the user has inputted N

#David Cameron
elif president == ("david cameron") or president == ("cameron") or president == ("david") or president == ("2"):#If the user inputted David Cameron
    print("You chose: David Cameron")#Prints who the user wants to vote for
    print("\n")#prints a blank line
#Checks if you want to continue
    davidcheck = input("Do you wish to continue? Y/N: ")#Allows the user to input Y or N
    davidcheck = davidcheck.lower()#What davidcheck is
    #checks if the user has entered yes or y
    if davidcheck == ("y") or davidcheck == ("yes"):#If the user inputs y or Y
        print("Vote processed.")#Prints if the user inputs y or Y
        print("David Cameron's current votes: ", + votes2+1)#Prints how many votes David Cameron has had
        time.sleep(1)#Waits 1 second until the next code is printed
        print("\n")#Prints a blank line
        print("General Election 2016 Finished!")#Prints when they have voted
        print("\n")#Prints a blank line
        print("Here are the candidates with their votes: ")#Prints how many votes each candidate got
        print("Barack Obama: ", + votes1)#Prints how many votes Barrack obama got
        print("David Cameron: ", + votes2+1)#Prints how many votes David Cameron got including the users vote
        print("Donald Trump: ", + votes3)#Prints how many votes Donald Trump got
        print("Hilary Clinton: ", + votes4)#Prints how many votes Hilary Clinton got
    else:#If the user inputs N
        print("Vote cancelled.")#This Prints if the user has inputted N

#Donald Trump
elif president == ("donald trump") or president == ("trump") or president == ("donald") or president == ("3"):#If the user inputs Donald Trump
    print("You chose: Donald Trump")#Prins who the user has voted for
    print("\n")#Prints a blank line
#Checks if you wish to continue
    trumpcheck = input("Do you wish to continue? Y/N: ")#Allows the user to input Y or N
    trumpcheck = trumpcheck.lower()#What trumpcheck is
    #checks if the user has entered yes or y
    if trumpcheck == ("y") or trumpcheck == ("yes"):#If the user inputs y or yes
        print("Vote processed.")#Prints when the user inputs y or yes
        print("Donald Trump's current votes: ", + votes3+1)#prints Donald Trumps current votes
        time.sleep(1)#Waits 1 second then prints the code below
        print("\n")#Prints a blank line
        print("General Election 2016 Finished!")#Prints when the user has voted
        print("\n")#Prints a blank line
        print("Here are the candidates with their votes: ")#Prints how many votes each candidate has got
        print("Barack Obama: ", + votes1)#Prints how many votes Barrack obama got
        print("David Cameron: ", + votes2)#Prints how many votes David Cameron got
        print("Donald Trump: ", + votes3+1)#Prints how many votes Donald Trump got including the users vote
        print("Hilary Clinton: ", + votes4)#Prints how many votes Hilary Clinton got
    else:#If the user inputs N
        print("Vote cancelled.")#This Prints if the user has inputted N

#Hilary Clinton
elif president == ("hilary clinton") or president == ("clinton") or president == ("hilary") or president == ("4"):
    print("You chose: Hilary Clinton")#Prins who the user has voted for
    print("\n")#Prints a blank line
#Checks if you wish to continue
    hilarycheck = input("Do you wish to continue? Y/N: ")#Allows the user to input Y or N
    hilarycheck = hilarycheck.lower()#What hilarycheck is
    #checks if the user has entered yes or y
    if hilarycheck == ("y") or hilarycheck == ("yes"):#If the user inputs y or yes
        print("Vote processed.")#Prints when the user inputs y or yes
        print("Hilary Clinton's current votes: ", + votes4+1)#Prints hilary clintons current votes
        time.sleep(1)#Waits 1 second then prints the code below
        print("\n")#Prints a blank line
        print("General Election 2016 Finished!")#Prints when the user has voted
        print("\n")#Prints a blank line
        print("Here are the candidates with their votes: ")#Prints how many votes each candidate has got
        print("Barack Obama: ", + votes1)#Prints how many votes Barrack obama got
        print("David Cameron: ", + votes2)#Prints how many votes David Cameron got
        print("Donald Trump: ", + votes3)#Prints how many votes Donald Trump got
        print("Hilary Clinton: ", + votes4+1)#Prints how many votes Hilary Clinton got including the users vote
    else:#If the user inputs N
        print("Vote cancelled.")#This Prints if the user has inputted N
#if candidate doesn't exist print this
else:#If the user inputs an invalid variable
    print("Please enter a valid candidate.")#This Prints if the user has inputted an invald variable