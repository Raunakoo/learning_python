#######################################################
# Takes the user input, make sure it is a 4 letter word
#######################################################
i=5
while i>= 5:
    user_input=input("please enter a 4 letter word -->")
    i=len(user_input)

print(user_input)
    
###################################################
#reverse the number using
# subject[begin index: end index: step] 
#1.pass start position=-1
#2.keep the end position null as it is optional
#3.Start the stepping -1 from the end of the string
####################################################
user_input_reverse= user_input[-1: :-1] 

print("the reversed word is",user_input_reverse)

###################################################
# finds the letter a and converts it to lower case, 
# in case the user inputs a letter in uppercase
###################################################
if user_input.lower().find("a") > 0:
    print("letter a found")


else:
    print("the letter a is not in the word")
#######################
#length of word 
#####################
print("the length of your word is",len(user_input))

