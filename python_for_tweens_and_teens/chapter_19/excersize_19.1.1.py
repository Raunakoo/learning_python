#Guess what will be displayed
#x input value is 1
x = int(input("input number"))

'''
range in for loop
(-3, 3, 2) 
creates pattern:
-3, -1, 1
'''
print("Value of x is",x)
#The loop will run three times
for i in range(-3, 3, 2): 
    x = x * 3 
    print("value of i and x is: ",i,x)