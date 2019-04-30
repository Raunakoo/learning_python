from math import *

print("This program creates the factorial of a number")

number = int(input("Enter a number "))
i = 1

print("1#########################!")

if number == 1:
    print("The factorial is 1")
    exit()



while number > i:
    factorial = number*i
    print("Now the number is changed to this factorial", factorial)
    i += 1
    print("This is the value of i", i)
    
print("Your factorial is", factorial)
    
