# importing functions
import random as ran

name = input("Type your name ")
first_three_letters = name[0:3]
number = str(ran.randrange(100, 999))

login = first_three_letters + number

print("your login is", login)
