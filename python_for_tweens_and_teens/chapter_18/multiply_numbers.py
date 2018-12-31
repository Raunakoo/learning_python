product = 1
N = int(input("type how many numbers to multiply\n\a"))
for x in range(N):
    number = int(input("Type number\n\a\a\a"))
    while number < 0:
        print("Type again, you typed a negative number")
        number = int(input("type how many postive numbers to multiply\n\a"))
    product *= number

print("the product is", product)