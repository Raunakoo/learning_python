#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import random
def esc(code):
    return f'\033[{code}m'

start = input("Do you want to start the flash card quiz?(y/n) ").lower()
print('\a')
if str(start) == "y":
    for d in range(25):
        Random_Number = random.randrange(1,26)
        print("What is the square of",Random_Number,"?")
        I = input("Enter your answer here: ")

        if int(I) == Random_Number**2:
            print(u"👏 👏 👏 👏 👏 👏 "+" You are correct "+ u" 👏 👏 👏 👏 👏 👏 👏 👏 ")
        else: 
            print(esc('31;1;4') + "you are wrong, the correct answer is", Random_Number**2)
            print(u"😊  😊  😊  😊  😊   😊"+"Do better next time:(")

    print("🍑🍑🍑🍑quiz end🍑🍑🍑🍑🍑")
else:
    print("bye, sorry you didn't want to do it:(")
    exit()