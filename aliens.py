#importing modules
from turtle import *
from pynput.keyboard import Key, Controller
import random
import turtle as t
import time
import tkinter as tkinter

keyboard = Controller()

####################################################
#background color
t.bgcolor("blue")
####################################################

####################################################
#characters of game
###############################
#Invader
invader = t.Turtle()

invader.shape("square")
invader.resizemode("user")
invader.shapesize(1,1)
invader.color('white')
invader.speed(0)
invader.penup()
invader.hideturtle()
################################

################################
#Alien
alien = t.Turtle()

alien.shape("circle")
alien.resizemode("user")
alien.shapesize(1,1)
alien.color("white")
alien.speed(0)
alien.penup()
alien.hideturtle()

laser_beam = t.Turtle()

laser_beam.shape("square")
laser_beam.resizemode("user")
laser_beam.shapesize(0.25, 0.25)
laser_beam.color("red")

current_score = 0
################################

####################################################

#check if the game has started
game_started = False
#tell the user to press the space bar to start the game
text_turtle1=t.Turtle()
text_turtle1.color('green')
text_turtle1.write('Press spacebar to start',align='right',\
	font=('helectiva',20,'bold'))
text_turtle1.hideturtle()

score_turtle=t.Turtle()
score_turtle.hideturtle()
score_turtle.speed(0)

####################################################
#game_over
def Game_over(name, score):
	
    invader.color('blue')
    alien.color('blue')
    text_turtle=t.Turtle()
    text_turtle.pendown()
    text_turtle.color('green')
    text_turtle.write('Game Over',align='center',\
                            font=('helectiva',20,'bold'))
    text_turtle.hideturtle()
        


####################################################

####################################################
#laser beam
'''
1.check where laser beam hits
2.check where alien hits
3.if alien and laser beam are on the same place and the user presses alt,
3.the alien should turn blue or dissapear
4.else continue
'''
def laser_hit_alien():
    global laser_beam
    laser_beam_position = laser_beam.goto(laser_beam.position()[0], laser_beam.position()[1]) 
    global alien_position
    alien_position = alien.goto(alien.position()[0], alien.position()[1])

    if laser_beam_position == alien_position \
        and keyboard.press(Key.enter) == True:
        print("in if statement checking if laser_beam has been used")
        current_score += 1
        #the alien has been killed
        alien.color("blue")

def invader_killed():
    print("invader killed")
    if laser_beam_position == alien_position and keyboard.press(Key.enter) == False:
        Game_over()

def space():
    print(game_started)
    text_turtle1.color("blue")

def start_game():
    global game_started
    if game_started:
        return
    game_started=True
    score_turtle.color('green')
    score_turtle.write('player score = '+str(current_score), font=\
            ('ariel',20,'bold'), align = "left")
    keyboard.press(Key.space)
    keyboard.release(Key.space)
    space()
    
    

        
    
start_game()


def outside_window(invader):
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

####################################################

####################################################
#keep the turtle screen from dissapearing
#always at the end
tkinter.mainloop()
####################################################