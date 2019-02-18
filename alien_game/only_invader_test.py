import turtle as t
import tkinter as tk

t.bgcolor("blue")

'''Invader'''

invader = t.Turtle()

invader.shape("square")
invader.resizemode("user")
invader.shapesize(1,1)
invader.color('white')
invader.speed(0)
invader.penup()
invader.hideturtle()

tk.mainloop()