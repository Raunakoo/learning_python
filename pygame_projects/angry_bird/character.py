##############################################
#importing modules for character.py
##############################################

import pymunk as pm

##############################################
#deal with vector in 2 dimension
##############################################

from pymunk import Vec2d

###################################################
#The Angry Bird or the main character of the game
###################################################

'''
space parameter contains the bird's body
'''

class Bird():

    def __init__(self,distance,angle,x,y,space):

        self.life = 20

        ##############################################
        #the weight of the bird is five
        #the weight should be as less as possible,
        #till if you keep it 20 you won't be able
        #to project the bird freely
        ##############################################

        
        mass = 5

        ########
        #radius
        ########

        radius = 12

        ################################################################################################
        #inertia: some thing will remain unchanged if not pushed or pulled, the resistance to something
        #moment_for_circle takes (mass, inner_radius, outer_radius, offset)
        ################################################################################################

        inertia = pm.moment_for_circle(mass, 0 , radius, (0,0))

        ##############################################
        #body of Angry Bird
        ##############################################

        body = pm.Body(mass, inertia)

        ##############################################
        #check for position of body
        ##############################################

        body.position = x,y

        ##############################################
        #what the bird should move by
        ##############################################

        power = distance * 53
        impulse = power * Vec2d(1,0)

        '''
        makes angle opposite
        '''

        angle =- angle

        body.apply_impulse_at_local_point(impulse.rotated(angle), (0,0) )

        ############################################################################################
        #the above code is adding local impulse to body as if applied from the body local point
        ############################################################################################

        ##############################################
        #the shape of the bird
        ##############################################

        shape = pm.Circle(body, radius, (0,0))

        #####################################################
        #elasticity is used for the bounce of the bird (0.95)
        #####################################################

        shape.elasticity = 0.95

        ##############################################
        # the friction of the bird
        ##############################################

        self.friction = 1

        ##############################################
        # below is user defined
        ##############################################

        shape_collision_type = 0

        space.add(body, shape)

        ##############################################
        #iniatilizing things
        ##############################################

        self.body = body
        self.shape = shape

##############################################
#the pig
##############################################

class Pig():

    '''
    space parameter creates
    body and shape of pig
    '''

    def __init__(self, x , y, space):

        ##############################################
        #no commenting, if question refer Bird class
        ##############################################

        self.life = 20
        mass = 5
        radius = 14

        inertia = pm.moment_for_circle(mass, 0, radius, (0,0))

        body = pm.Body(mass, inertia)
        shape = pm.circle(body, radius, (0,0))

        shape.elasticity = 0.95
        shape.friction = 1
        shape.collision_type = 1
        shape.add(body, shape)

        self.body = body
        self.shape = shape