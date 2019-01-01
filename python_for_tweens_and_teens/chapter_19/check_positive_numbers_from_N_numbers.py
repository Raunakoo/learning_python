N = int(input("How many integers do you wnat to enter\n"))
count = 0


for i in range(N):
    number = int(input("enter a positive or negative number\n"))
    if number > 0:
        count += 1 
    if count == N:
        print("All of the integers you entered are positive")
    if count == 0:
        print("All of the integers you entered are negative")

print("The number of postive integers you entered is", count)