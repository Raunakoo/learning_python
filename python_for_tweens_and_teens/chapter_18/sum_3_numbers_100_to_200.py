sum = 0
N = int(input("How many numbers do you want to sum?\n"))
for y in range(N):
    number = int(input("Enter number from 100 to 200"))
    while number<100 or number>200:
        print("You didn't enter a number from 100 to 200")
        number = int(input("Please type again\n"))
    sum = sum + number

print(sum)