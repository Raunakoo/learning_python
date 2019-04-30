from math import sqrt  # Using math library in program

print("This program calculates if a given number is prime!")
# Asks for user input
number = float(input("Enter a number to see if it is prime or composite "))

# Find square root of A
sqroot_number = int(sqrt(number))
print("SQRT is",sqroot_number)
for i in range(2, sqroot_number+1):
    print("Value of i",i)
    print("Checking if number is prime or composite")
    if sqroot_number % i == 0:
        print("your number is composite")
        break
    else:
        print("your number is prime")

print("program is created by R. Singh")
