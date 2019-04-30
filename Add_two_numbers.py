print("This code adds two numbers that you input")

#################################################

#######User Input A#########
A = input("Enter a number, ")
try:
   val = int(A)
   print("Yes input string is an Integer.")
   print("Input number value is: ", val)
except ValueError:
    print("that wasn't a number")
    exit()

#######User Input B#########
B = input("Enter a number, ")
try:
   val = int(B)
   print("Yes input string is an Integer.")
   print("Input number value is: ", val)
except ValueError:
    print("that wasn't a number")
    exit()
####################################################

####Calling numbers int######
A = int(A)
B = int(B)
#############################

print("The sum of your numbers is", B+A)