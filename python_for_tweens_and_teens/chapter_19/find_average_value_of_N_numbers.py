import math

total = 0
N = int(input("Type how many numbers you wnat to find the average of: "))

for i in range(N):
    number = int(input("type a number "))
    total = total + number

average = total/N
print("The average of your numbers is", average)