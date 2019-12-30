#fix: print letter instructions after every user letter input

"""
The Number Game

Ask user to enter choices and  based on selection do it

P -  Print  the numbers. If list is empty then print "[]"
A - Add a new number to existing list 
M - Display Mean of numbers. If list is empty print Mean is 0
S - Disply smallest number in list
L - Display largest in list
Q - exit
Any other entry Display Invalid selection
"""

# import statements

# import everything from math library
from math import *

# empty list to contain all the number inputs
numlst = []

# title
print("🎲🎲🎲🎲The Number Game🎲🎲🎲🎲")

def usermenu():
    print(numlst)

    print("P -  Print  the numbers. If list is empty then print []")
    print("A - Add a new number to existing list")
    print("M - Display Mean of numbers. If list is empty print Mean is 0")
    print("S - Disply smallest number in list")
    print("L - Display largest in list")
    print("Q - exit")

#main code
def main_code(numlst):
    #All of the main code goes here
    print("This is the empty list you will start with")
    print(numlst)

    print("P -  Print  the numbers. If list is empty then print []")
    print("A - Add a new number to existing list")
    print("M - Display Mean of numbers. If list is empty print Mean is 0")
    print("S - Disply smallest number in list")
    print("L - Display largest in list")
    print("Q - exit")

    while True:
        mainq = input("Enter a letter from above ").upper()
        if mainq == "EXAMPLE":
            numlst = [1,2,3,4,5,6,7,8,9,10]
        elif mainq == "P":
            print(numlst)
        elif mainq == "A":
            addq = int(input("What number do you want to add to the list "))
            if addq>0 or addq==0 or addq<0:
                numlst.append(addq)
            else:
                print("not valid number to add to list")
                
        elif mainq == "M":
            if numlst == []:
                print("the mean is 0")
            else:
                def Average(numlst): 
                    return sum(numlst) / len(numlst)
                average = Average(numlst)
                print("the average of the list is", average)
        elif mainq == "S":
            numlst.sort()
            print(numlst[0])
        elif mainq == "L":
            print(max(numlst))
        elif mainq == "Q":
            lastq = input("Rate the game, good, very good, fine, or bad ")
            if lastq == "very good" or "good":
                print("thanks for liking the game")
            elif lastq == "fine":
                print("have agood day")
            else:
                exit()
            exit()
        else:
            print("try again, that's not valid input")
            main_code(numlst)

# starting question
# asks if want to play or not
#.lower(), returns lowercased copy of string
startquestion = input("❓❓❓Do you want to start the game(y/n) ❓❓❓ ").lower()

#if statements for opening
if startquestion == "y":
    print("👏🎉Good, enjoy your time in the number game!👏🎉")
    #main function to be housed in here
    main_code(numlst)

elif startquestion == "n":
    print("👍👍👍Please try to play next time.👍👍👍")

else:
    print("❌ ❌ ❌ Sorry, that is invalid. Please input y/n. \
        try again. ❌ ❌ ❌")

######Note: the example tryout list has these answers that should be used for testing in code######
'''
P(print) - [1,2,3,4,5,6,7,8,9,10]
A(add) - XXXXXXXXXXXXX
M(mean) - 5.5
S(smallest) - 1
L(largest) - 10
control c - quit
'''