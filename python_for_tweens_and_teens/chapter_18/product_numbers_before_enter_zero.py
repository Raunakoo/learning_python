product = 1
print("Enter numerical values\
repeatedly, and then\
 when you want\
 to multiply the numbers\
 you enter 0\n")
user_input = int(input("Enter a number\n"))
end = int(input("press 0 if you want to end"))
while end != 0:
    user_input = int(input("enter\
     a number\n"))
    end = int(input("if you want to end press zero\n"))
    product = product * user_input
product = product * user_input
if end == 0:
    print(product)
    exit()