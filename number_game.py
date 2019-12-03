"""
Ask user to enter choices and  based on selection do it

P -  Print  the numbers. If list is empty then print "[]"
A - Add a new number to existing list 
M - Display Mean of numbers. If list is empty print MEan is 0
S - Disply smallest number in list
L - Display largest in list
Q- Quit
Any other entry Display Invalid selection
"""

# import statements

# import everything from math library
from math import *

# empty list to contain all the number inputs
numlst = []

# title
print("🎲🎲🎲🎲The Number Game🎲🎲🎲🎲")

# starting question
# asks if want to play or not
#.lower(), returns lowercased copy of string
startquestion = input("❓❓❓Do you want to start the game(y/n) ❓❓❓ ").lower()

#if statements for opening
if startquestion == "y":
    print("👏🎉Good, enjoy your time in the number game!👏🎉")
    #main function to be housed in here
    main_code()

elif startquestion == "n":
    print("👍👍👍Please try to play next time.👍👍👍")

else:
    print("❌ ❌ ❌ Sorry, that is invalid. Please input y/n. \
        try again. ❌ ❌ ❌")

def main_code():
    #All  of the main code goes here
    Print("This is the empty list you will start with")
    Print(numlst)