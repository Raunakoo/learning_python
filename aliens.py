#importing modules
from turtle import *
from pynput.keyboard import Key, Controller
import random
import turtle as t
import time
import tkinter as tkinter

keyboard = Controller()
t.bgcolor("blue")

########################################
#Characters
########################################
'''Invader'''

invader = t.Turtle()

invader.shape("square")
invader.resizemode("user")
invader.shapesize(1,1)
invader.color('white')
invader.speed(0)
invader.penup()
invader.hideturtle()
