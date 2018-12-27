##########################
#imports math library
##########################

import math

#################################
#Asks the user to enter a number
#################################

n=int(input("please enter a number--->"))

########################################
#calculates the square root of a number
########################################

square_root=math.sqrt(n)
print(square_root)
'''
for i in range(2,int(square_root)+1):

    if n%i==0:
        print(n,"is composite")
        break

else:
    print(n,"is prime")    
''' 
i=2

while (i <= square_root):
    print("now i is ", i)
    if n%i==0:
        
        print("i is", i, " then " ,n,"is composite")
        break
    i=i+1

else:
    print("i is", i, " then " ,n,"is prime")
    
     
        