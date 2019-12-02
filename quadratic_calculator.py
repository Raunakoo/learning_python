import math

#Quadratic Equation - 0 = ax + b(x*x) + c
#Quadratic Formula - -b ± (b*b-4ac) t
    #to the 1/2 power divided by 2a

print("Starting Quadratic Calculator")

#############################################
#User Input
x = float(input("Enter value of x "))
y = float(input("Enter value of y "))
z = float(input("Enter value of z "))
print(x,y,z)
#############################################
#############################################
#It does the plus in the plus-minus operator
def quad_fm1(x,y,z):
    print("###In Quadratic function 1 Code###")
    #Dividend of formula
    Qdividend = (-y+(y*y-4*x*z)**0.5)
    #Divisor of formula
    Qdivisor = float(2*x)
    answer1 = Qdividend/Qdivisor
    
    print("answer1 equals", answer1)
    return answer1

quad_fm1(x,y,z)
#############################################
#############################################
#It does the minus in the plus-minus operator  
def quad_fm2(x,y,z):
    print("###In Quadratic function 2 Code###")
    #Dividend of formula
    Qdividend = (-y-(y*y-4*x*z)**0.5)
    #Divisor of formula
    Qdivisor = float(2*x)
    answer2 = Qdividend/Qdivisor
    print("answer2 equals", answer2)
    return answer2
    

quad_fm2(x,y,z)
#############################################
print("|exiting, have a nice day|")
#############################################