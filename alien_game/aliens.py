#importing modules
from turtle import *
from pynput.keyboard import Key, Controller
import random
import turtle as t
import time
import tkinter as tkinter

keyboard = Controller()

#Setting the background color as blue
t.bgcolor("blue")

########################################
'''Characters'''
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
##########################################
'''Alien'''

alien = t.Turtle()

alien.shape("circle")
alien.resizemode("user")
alien.shapesize(1,1)
alien.color("green")
alien.speed(0)
alien.penup()
alien.hideturtle()
##########################################
##########################################
'''Laser Beam'''

laser_beam = t.Turtle()

laser_beam.shape("square")
laser_beam.resizemode("user")
laser_beam.shapesize(0.25, 1.00)
laser_beam.color("red")
laser_beam.hideturtle()
##########################################
##########################################
##########################################

def space():
    keyboard.press(Key.space)

def up():
    if invader.heading()==0	or invader.heading()==180:
        invader.setheading(90)

def down():
    if invader.heading()==0	or invader.heading()==180:
        invader.setheading(270)

def left():
    if invader.heading()==90	or invader.heading()==270:
        invader.setheading(180)

def right():
    if invader.heading()==90	or invader.heading()==0:
        invader.setheading(0)

def enter():
    keyboard.press(Key.enter)

##########################################
##########################################
##########################################
'''Function to get game started'''

def start_game():
    game_on = False
    spacebar_turtle = t.Turtle()
    spacebar_turtle.color("red")
    spacebar_turtle.write("Press the Space Bar to start the game", align = "center" , 
                            font = ("helectiva", 20, "bold"))
    spacebar_turtle.hideturtle()
    ########Write if statement to check if user pressed spacebar#########

start_game()

##########################################
##########################################
'''Function to end the game(Use onward in code)'''
def over_game():
    exit()
    
##########################################
##########################################
##########################################
#checking if invader is outside window
def outside_window(invader):
    #This bug is a pylint error, or isn't really a bug
    left_wall= -t.window_width()/2	
    right_wall=t.window_width()/2
    top_wall=t.window_width()/2
    bottom_wall= -t.window_width()/2
    (x,y)=invader.pos()
    outside=\
	x<left_wall or \
	x>right_wall or \
	y<bottom_wall or \
	y>top_wall
    return outside
    ###########Include a function over_game################

def laser_hit_alien():
    '''problems with this code are not bugs, 
    but are the problem with Pylint, the debugger'''
    global laser_beam_position
    laser_beam_position = laser_beam.goto(laser_beam.position()[0], laser_beam.position()[1])
    global alien_position
    alien_position = alien.goto(alien.position()[0], alien.position()[1])
    global invader_position
    invader_position = invader.goto(invader.position()[0], alien.position()[1])
    #current score
    current_score = 0
    def laser_out_invader():
        if enter == True:




##########################################
#Keeps the screen up and is always at the end of the program
tkinter.mainloop()
##########################################

'''''''''''''''''''''''''''''''''''''''''
Code by Raunak Singh
'''''''''''''''''''''''''''''''''''''''''