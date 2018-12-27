import random

########################
#asks input
########################

user_input=input("enter your last name--->")

##############################
#takes the first four letters
##############################

first_four=user_input[0:4]

print(first_four)

###################################################################
#makes a random three digit number
#random.randrange(start, stop[, step])
#Return a randomly selected element from range(start, stop, step).
#################################################################### 

three_numbers=str(random.randrange(100,1000))

print(three_numbers)

##################################################################################
#makes my login ID by concatenating the two variables first_four and three_numbers
##################################################################################

user_ID="This is your login Id",first_four+three_numbers

print(user_ID)