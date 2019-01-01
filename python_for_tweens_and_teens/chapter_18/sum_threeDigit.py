sum = 0
for y in range(3):
    number = int(input("type a number to sum\n"))
    while number < 100 or number > 999:
        print("you have to type a three digit number\a")
        number = int(input("type a number\n"))
    sum = sum + number

print(sum)