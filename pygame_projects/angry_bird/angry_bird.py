##############################################
#importing modules needed for angry bird game
##############################################

import os
import sys

import math
import pygame

import time
current_path = os.getcwd
import pymunk as pm
from level import Level
from character import Bird

##############################################
#initalizing pygame
##############################################
print(os.getcwd())
pygame.init()

##############################################
#screen wirth = 650, screen length = 1200
##############################################

screen = pygame.display.set_mode((1200,650))

##############################################
#loading images needed for game
##############################################

##############################################
#loading angry bird sprite into pygame
#.convert_alpha removes the background
##############################################

redbird = pygame.image.load("../angry_bird/resources/images/red-bird3.png").convert_alpha()

##############################################
#loading background image
##############################################

background = pygame.image.load("../angry_bird/resources/images/background3.png").convert_alpha()

#####################################################
#loading sling image that will launch the angry bird
#####################################################

sling_image = pygame.image.load("../angry_bird/resources/images/sling-3.png").convert_alpha()

##############################################
#loading full_sprite.png
#../ means earch in one directory above from where I am
# I ran the program in angry_bird folder, 
# so ../ will search in Pygame_projects
# fro folder angry_bird
##############################################

full_sprite = pygame.image.load("../angry_bird/resources/images/full-sprite.png").convert_alpha()

##############################################
#choosing any pig #want to change later
##############################################

rect = pygame.Rect(181, 1050, 50, 50)

cropped = full_sprite.subsurface(rect).copy()

pig_image = pygame.transform.scale(cropped,(30,30))

#Clock

clock  = pygame.time.Clock()

running = True

#base for physics

space = pm.Space()
# syntax cange in python 3.6
# Tutir is using python 2.7
space.gravity=0.0,-700.0
space.gravity

#making important lists

pigs = []
birds = []
balls = []
polys = []
beams = []
columns = []
poly_points = []

#important variables

ball_number = 0
mouse_distance = 0
rope_length = 90
angle = 0
x_mouse = 0
y_mouse = 0

#count number of loops

count = 0

mouse_pressed = False
tl = 0

#time from the one bird to other

tick_to_next_circle = 10

RED = (255,0,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
WHITE = (255,255,255)

#position before streching

sling_x, sling_y = 135, 450

#position after streching
#y position remains the same

sling2_x, sling2_y = 160, 450

score = 0

game_state = 0

bird_path = []

counter = 0

restart_counter = False
bonus_score_one = True

bold_font = pygame.font.SysFont("arial", 20, bold = True)

bold_font2 = pygame.font.SysFont("arial", 30, bold = True)

bold_font3 = pygame.font.SysFont("arial", 50, bold = True)

wall = False

##############################################################
#create motion of bird
##############################################################

#Static floor : the floor for game

static_body = pm.Body(body_type= pm.Body.STATIC)

'''
static body is segment where the body will be attached
A = (0.0, 060.0), or the first part inpoint
B = (1200.0, 060.0) or the second part inpoint
0.0 is the radius of the segment 
'''

static_lines = [pm.Segment(static_body, (0.0, 060.0), (1200.0, 060.0), 0.0)]

#switch second inpoint to first inpoint

static_lines1 = [pm.Segment(static_body,  (1200.0, 060.0), (1200.0, 800.0), 0.0)]

for line in static_lines:

    line.elasticity = 0.95
    line.friction = 1
    line.collision_type = 3

for line in static_lines1:

    line.elastisicity = 0.95
    line.friction = 1
    line.collision_type = 3

space.add(static_lines)


def to_pygame(p):

    #convert pymunk to pygame
    return int(p.x), int(-p.y + 600)

def vector(p0, p1):

    #return vecter out of points p0 and p1
    a = p1[0] - p1[0]
    b = p1[1] - p1[1]

    return[a,b]

def unit_vector(v):

    #calculate unit vector

    h = ((v[0]**2 + (v[1]**2)))**0.5

    if h == 0:

        #0 means intermediate ... so we assign another value
        h = 0.00000000000000\

    #unit vector formula: (vector v)/ (modulus(absolute value) of v)
    ua = v[0]/h
    ub = v[1]/h

    return (ua, ub)

#distance

def distance(x0, y0, x, y):

    #distance = square root of ((x-x0) squared + (y-y0) squared) 

    dx = x-x0
    dy = y-y0

    d = ((dx**2) + (dy**2))**0.5
    return d

def sling_action():
    # to change position of sling
    global mouse_distance
    global rope_length
    global angle
    global x_mouse
    global y_mouse

    #fix the bird to the sling rope

    v = vector((sling_x, sling_y, x_mouse, y_mouse))

    uv = unit_vector(v)


    uv1= uv[0]
    uv2 = uv[1]

    mouse_distance = distance(sling_x, sling_y, x_mouse, y_mouse)

    pu = (uv1 * rope_length + sling_x, uv2 *rope_length + sling_y)

    bigger_rope = 102

    x_redbird = x_mouse - 20
    y_redbird = y_mouse - 20

    if mouse_distance > rope_length:
        ############################################################
        #this code kept the sling in its original position
        #as in sling.png
        pux, puy = pu

        pux -= 20
        puy -= 20

        pul = pux, puy
        screen.blit(redbird, pul)

        ###########################################################

        pu2 = (uv1 * bigger_rope + sling_x, uv2 * bigger_rope + sling_y)

        pygame.draw.line(screen, (0,0,0), (sling2_x, sling2_y), pu2, 5)

        screen.blit(redbird, pul)

        pygame.draw.line(screen, (0,0,0, (sling_x, sling_y, pu2, 5)))\

    else:
        mouse_distance += 10

        # after you press mouse for bird_position
        pu3 = (uv1 * mouse_distance + sling_x, uv2 * mouse_distance + sling_y)

        pygame.draw.line(screen, (0,0,0), (sling2_x, sling2_y), pu3, 5)

        screen.blit(redbird(x_redbird, y_redbird))

        pygame.draw.line(screen, (0,0,0), (sling_x, sling_y), pu3, 5)

    #angle of impulse

    dy = y_mouse - sling_y

    dx = x_mouse - sling_x

    if dx == 0:

        dx = 0.000000000000001

    angle = math.atan((float(dy)/ dx))

level = Level(pigs, columns, beams, space)
level.number = 0
level.load_level()

while running:
    #Input handling
    for event in pygame.event.get():
        #######################################################################
        #quit the game when you press x 
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        #######################################################################
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_w:
            #toggle the wall
            if wall:
                space.remove(static_lines1)
                wall = False
            else:
                space.add(static_lines)
                wall = True

        elif event.type == pygame.KEYDOWN == pygame.K_s:
            space.gravity(0.0, -10.0)
            level.bool_space = True
        elif event.type == pygame.KEYDOWN == pygame.K_n:
            space.gravity(0.0, -700.0)
            level.bool_space = False
        #######################################################################
        #this code controls or interacts with the mouse
        if (pygame.mouse.get_pressed()[0] and x_mouse > 100 and \
                x_mouse < 250 and y_mouse > 370 and y_mouse < 550):
            mouse_pressed = True
        if (event.type == pygame.MOUSEBUTTONUP and \
                event.button == 1 and mouse_pressed):
            #release bird from here
            mouse_pressed = False
            if level.number_of_birds > 0:
                #minus the number of birds by 1
                level.number_of_birds -= 1
                #convert into seconds
                t1 = time.time()*1000
                #xo and yo are the maxium distance the bird can move
                xo = 154
                yo = 156  
                #make sure player doesn't break the rope
                if mouse_distance > rope_length:
                    mouse_distance = rope_length
                    #what to do if stretch is less than the maxium distance
                    if x_mouse < sling_x + 5:
                        #space is basically the body or shape of the bird
                        bird = Bird(mouse_distance, angle, xo, yo, space)
                        birds.append(bird)
                    else:
                        bird = Bird(-mouse_distance, angle, xo, yo, space)
                        birds.append(bird)
                    if level.number_of_birds == 0:
                        t2 = time.time
        #######################################################################

        