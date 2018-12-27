# importing modules
import tkinter as tk  # importing tkinter

# importing modules from tkinter library
import tkinter
from tkinter import messagebox
from tkinter import font
from tkinter import commondialog
# steps and structure of game
'''
1.user runs the program and opens calculator
2.user clicks any number from 0 to 9 on the keypad
3.the user clicks a operation(+,-,*,/)
4.the user clicks a second number 
5.user presses the equal sign to get his answer
'''
################################################################################
# notes:
#   step 2,3,4:
#       after done with code make sure the user clicks what he is supposed to
#   step 5:
#       display answer in alert box, and then top of the screen
################################################################################

# code for calculator

# create canvas to draw boxed and buttons
root = tk.Tk()
# define size of canvas
# root.geometry("width*height")
root.geometry("310x600")

# 1,2,3,4,5,6,7,,8,9, and 0 buttons on calculator

################################################################################
# text: text on button
# active background: background when button is under curser
# background: represented as bg the background of the buttons
# fg: foreground color or text color
# font: the font on the buttons label
################################################################################


class calculator:
    def __init__(self):

        self.bttn_clicks = 0

    def oneButton(self):
        if self.bttn_clicks == 0:
            self.num1 = 1
            print("Stored num1 with value", self.num1)
            self.bttn_clicks += 1
            print("number of clicks", str(self.bttn_clicks))

        elif self.bttn_clicks == 1:
            self.num2 = 1
            print("Stored num2 with value", self.num2)
            
            self.bttn_clicks += 1
            print("number of clicks", str(self.bttn_clicks))

    def twoButton(self):
        self.num2 = 2
        print("Button pressed is", self.num2)

        self.bttn_clicks += 1
        print(str(self.bttn_clicks))

#instantiate the class
calculator = calculator()

one = tk.Button(text="1", width=8, height=8,
                fg="deep sky blue", command=calculator.oneButton)
one.grid(row=1, column=1)

two = tk.Button(text="2", width=8, height=8,
                fg="deep sky blue", command=calculator.twoButton)
two.grid(row=1, column=2)
three = tk.Button(text="3", width=8, height=8, fg="deep sky blue")
three.grid(row=1, column=3)
four = tk.Button(text="4", width=8, height=8,  fg="deep sky blue")
four.grid(row=2, column=1)
five = tk.Button(text="5", width=8, height=8, fg="deep sky blue")
five.grid(row=2, column=2)
six = tk.Button(text="6", width=8, height=8, fg="deep sky blue")
six.grid(row=2, column=3)
seven = tk.Button(text="7", width=8, height=8, fg="deep sky blue")
seven.grid(row=3, column=1)
eight = tk.Button(text="8", width=8, height=8, fg="deep sky blue")
eight.grid(row=3, column=2)
nine = tk.Button(text="9", width=8, height=8, fg="deep sky blue")
nine.grid(row=3, column=3)
zero = tk.Button(text="0", width=8, height=8, fg="deep sky blue")
zero.grid(row=4, column=2)

# functions needed for program
# checks if button is pressed


def pressed(self, method):
    print("method:", method)
    for method in ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]:
        press = tk.Button(root, text=method,
                          command=lambda m=method: self.pressed(m))

# multiplacation,division,addition,subtraction buttons


# addition button
add_button = tk.Button(text="+", width=8, height=8, fg="deep sky blue")
add_button.grid(row=1, column=4)

# subtraction button
minus_button = tk.Button(text="-", width=8, height=8, fg="deep sky blue")
minus_button.grid(row=2, column=4)

# multiplacation button
multiplacation_button = tk.Button(
    text="*", width=8, height=8, fg="deep sky blue")
multiplacation_button.grid(row=3, column=4)

# division button
division_button = tk.Button(
    text="/", width=8, height=8, fg="deep sky blue")
division_button.grid(row=4, column=4)

root.mainloop()
