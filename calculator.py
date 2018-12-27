# program must have 0 in user input boxes
# handle if 0 is passed for Division
# Input boxes should be lined up nicely
# output of calultor should be in another text box
# color the font on buttons in blue
# add 1,2,3,4,5,6,7,8,9 and dot and equal button keys for calculator


import tkinter as tk  # Python 3 import
from tkinter import messagebox

# create canvas to draw boxed and buttons
root = tk.Tk()
# define size of canvas
root.geometry("500x500")

# create the add function


def add():
    # get the first number input by the user
    number1Input = number1.get()
    # get the second number input by the user
    number2Input = number2.get()
    # add them and alert user the sum
    msg = messagebox.showinfo("Answer!", int(number1Input) + int(number2Input))


def subtract():
    number1Input = number1.get()
    number2Input = number2.get()
    msg = messagebox.showinfo("Answer!", int(number1Input) - int(number2Input))


def multiply():
    number1Input = number1.get()
    number2Input = number2.get()
    msg = messagebox.showinfo("Answer!", int(number1Input) * int(number2Input))


def division():
    number1Input = number1.get()
    number2Input = number2.get()
    msg = messagebox.showinfo("Answer!", int(number1Input) / int(number2Input))


# Create the label to show on canvas
my_label = tk.Label(root, text="number1")
# define where to position or show it on canvas
my_label.grid(row=0, column=0)
number1 = tk.Entry(root)
number1.grid(row=0, column=1)

my_label2 = tk.Label(root, text="number2")
my_label2.grid(row=10, column=10)
number2 = tk.Entry(root)
number2.grid(row=20, column=2)

my_button = tk.Button(root, text="ADD", command=add)
my_button.grid(row=1, column=1)
my_button = tk.Button(root, text="SUBTRACT", command=subtract)
my_button.grid(row=2, column=1)
my_button = tk.Button(root, text="Division", command=division)
my_button.grid(row=3, column=1)
my_button = tk.Button(root, text="MULTIPLY", command=multiply)
my_button.grid(row=4, column=1)

root.mainloop()
