import math
import os
from random import randint
from collections import deque

import pygame
from pygame.locals import *

#base variables

FPS = 60

ANIMATION_SPEED = 0.18
wirth = 284*2
height = 512
##############################################################
# Creating class Bird or I am creating a Bird for my programme
###############################################################
class Bird(pygame.sprite.Sprite):
    #this represents the bird should be controlled by the player
    '''
    the bird can make it climb
    other wise it can sink(descends more quickly than it can climb
    it must pass through the pipe and between thepipe for every pipe passed one point scored
    x: bird x code
    y: bird y code
    msec_to_climb: Bird.CLIMB_DURATION
    CONSTATNT WIdth height sink_speed climb_speed   climb_DURATION
    '''
    
    WIDTH = HEIGHT = 50
    SINK_SPEED = 0.18
    CLIMB_SPEED = 0.3
    CLIMB_DURATION = 333.3
    # ##################################################### 
    # CLASS BIRD
    # Bird creates itself
    # ##################################################### 
    def __init__(self,x,y,msec_to_climb,images):
        '''
        :param x: bird x coordinate
        :param y: bird y coordinate

        :param msec_to_climb: number of miliseconds left to climb when the complete climb last
        :param images: images tupil contains image used by bird

        '''
        super(Bird,self) .__init__()
        self.x , self.y = x,y

        self.msec_to_climb = msec_to_climb
        self._img_wingup, self._img_wingdown = images
        self._mask_wingup = pygame.mask.from_surface(self._img_wingup)
        self._mask_wingdown = pygame.mask.from_surface(self._img_wingdown)

    ##################################################### 
    # CLASS BIRD
    # constionously update the bird during the game
    ##################################################### 
    def update(self, delta_frames = 1):
        '''Delta Frame is number of frames elapsed
         
        This function will use the cosine function to acheive a smooth climb

        ''' 

        if self.msec_to_climb > 0:
            frac_climb_done = 1-self.msec_to_climb / Bird.CLIMB_DURATION

            self.y -= (Bird.CLIMB_SPEED * frames_to_msec(delta_frames) \
            * (1-math.cos(frac_climb_done * math.pi)))

            self.msec_to_climb -= frames_to_msec(delta_frames)

        else:
            self.y += Bird.SINK_SPEED*frames_to_msec(delta_frames)
        
    ##################################################### 
    # CLASS BIRD
    #image of the bird
    ##################################################### 
    @property
    def image(self):
        '''
        this will decide wether 
        to return image 
        where the bird
        is pointing 
        upward or 
        where it is pointing 
        downward based on 
        pygame.time.getticks()

        '''
        if pygame.time.get_ticks() % 500 >= 250:
            return self._img_wingup

        else:
            return self._img_wingdown
    ##################################################### 
    # CLASS BIRD
    # rectangle
    ##################################################### 
    @property
    def rect(self):
        return Rect(self.x, self.y, Bird.WIDTH, Bird.HEIGHT)

    ##################################################### 
    # CLASS BIRD
    # mask defines that bird can flip wings go up or down
    ##################################################### 
    @property
    def mask(self):
        if pygame.time.get_ticks() % 500 >= 250:
            return self._mask_wingup
        else:
            return self._mask_wingdown

######################################################################################
# Create Pipe Pair obstacles for thegame
####################################################################################
class PipePair(pygame.sprite.Sprite):
    '''
    this represents obstacle for bird
    so pipe pair has top and bottom and only between the bird can pass
    Atrribute:
    x: -X position
    no y:0
    image
    mask
    top-pieces : number of pieces including in top pipe
    bottom pipe
    constant:
    WIDTH
    PIECE_HEIGHT
    ADD_INTERVAL
    '''

    WIDTH = 80
    PIECE_HEIGHT = 32
    ADD_INTERVAL = 3000

    # change accordingly

    def __init__(self, pipe_end_img, pipe_body_img):

        #Iniatilize a random pipe pair

        self.x = float(wirth - 1)
        self.score_counted= False
        self.image = pygame.Surface((PipePair.WIDTH, height),SRCALPHA)
        self.image.convert()
        self.image.fill((0,0,0,0))

        total_pipe_body_pieces = int((height -3*Bird.HEIGHT - 3* PipePair.PIECE_HEIGHT)/PipePair.PIECE_HEIGHT)

        self.bottom_pieces = randint(1,total_pipe_body_pieces)
        self.top_pieces = total_pipe_body_pieces - self.bottom_pieces

        for i in range(1,self.bottom_pieces + 1):

            piece_pos = (0, height - i * PipePair.PIECE_HEIGHT)

            self.image.blit(pipe_body_img, piece_pos)

        bottom_pipe_end_y = height - self.bottom_height_px
        bottom_end_pipe_pos = (0, bottom_pipe_end_y - PipePair.PIECE_HEIGHT)
        self.image.blit(pipe_end_img, bottom_end_pipe_pos)

        #top pipe

        for i in range(self.top_pieces):
            self.image.blit(pipe_body_img,(0, i * PipePair.PIECE_HEIGHT))

        total_pipe_end_x = self.top_height_px
        self.image.blit(pipe_end_img, (0,total_pipe_end_x))

        #compensenate for added end pipes

        self.top_pieces += 1
        self.bottom_pieces += 1

        #detect collision

        self.mask = pygame.mask.from_surface(self.image)


    @property
    def top_height_px(self):
        return self.top_pieces * PipePair.PIECE_HEIGHT


    @property
    def bottom_height_px(self):
        return self.bottom_pieces * PipePair.PIECE_HEIGHT

    
    @property
    def visible(self):
        return -PipePair.WIDTH < self.x < wirth
        #boolean type, return based on whether the pipepair screen is visible to player

    @property
    def rect(self):
        return Rect(self.x,0,PipePair.WIDTH, PipePair.PIECE_HEIGHT)

    def update(self, delta_frames = 1):

        self.x -= ANIMATION_SPEED * frames_to_msec(delta_frames)
        #DELTA FRAME IS NO OF FRAME ELAPSED 

    def collides_with(self,bird):
        return pygame.sprite.collide_mask(self,bird)
        #get if bird collides with pipe




def load_images():
    '''__load images required for game and return dictionary of them__
    what should it return
    
    1.background
    2.bird-wingup
    3.bird_wingdown
    4.pipe_body
    5.pipe_end
    '''

    def load_images(img_file_name):
        '''return load it pygame image with filename'''
        '''(/images/)'''

        file_name = os.path.join(".","images", img_file_name)
        img = pygame.image.load(file_name)

        img.convert()
        return img

    return {
        
        "background" : load_images("background.png"),
        "pipe-end" : load_images("pipe_end.png"),
        "pipe-body" : load_images("pipe_body.png"),
        "bird-wingup" : load_images("bird_wing_up.png"),
        "bird-wingdown" : load_images("bird_wing_down.png"),
        

    }


def frames_to_msec(frame,fps= FPS):

    return 1000.0 * frame / fps
    #convert frame to ms in specified rate

def msec_to_frames(milliseconds,fps = FPS):
    '''

    milliseconds:how many millisecond to convert for frame 

    fps:rate to use for conversion
    :param milliseconds:
    :param fps
    :return:
    '''

    return fps * milliseconds / 1000.0


def main():
    '''__main flow of program__''' 
    print("Started the main")
    pygame.init()

    display_surface = pygame.display.set_mode((wirth, height))

    pygame.display.set_caption("Flappy Bird")

    clock = pygame.time.Clock()



    score_font = pygame.font.SysFont(None,32, bold = True )  #defualt font
    images = load_images()
    # Create a bird for the game using the BIRD class defined above
    bird = Bird(50, int(height/2 - Bird.HEIGHT/ 2),2, (images["bird-wingup"], images["bird-wingdown"]))
    pipes = deque()

    frame_clock = 0

    score = 0

    done = paused = False

    print("Outside the While loop")
    while not done:
        clock.tick(FPS)

        if not (paused or frame_clock % msec_to_frames(PipePair.ADD_INTERVAL)):
            pp  = PipePair(images["pipe-end"], images["pipe-body"])
            pipes.append(pp)

        #handle the user event
        for e in pygame.event.get():
            if e.type == QUIT or (e.type == KEYUP and e.key == K_ESCAPE):

                done =  True
                break
        
            elif e.type ==  KEYUP and e.key in (K_PAUSE, K_p):
            
                paused = not paused

            elif e.type == MOUSEBUTTONUP or (e.type == KEYUP and e.key in (K_UP, K_RETURN, K_SPACE)):

                bird.msec_to_climb = Bird.CLIMB_DURATION



        if paused:
            continue #don't draw anything

        #check for any collisions with PipePair

        pipe_collision = any(p.collides_with(bird)for p in pipes)


        if pipe_collision or 0 >= bird.y or bird.y >= height - Bird.HEIGHT:
            done = True

        for x in (0, wirth/2):
            display_surface.blit(images["background"], (x,0))

        while pipes and not pipes[0]. visible:
            pipes.popleft()

        for p in pipes:
            p.update()
            display_surface.blit(p.image, p.rect)

        bird.update()
        display_surface.blit(bird.image, bird.rect)

        # update and display score
        for p in pipes:
            if p.x + PipePair.WIDTH < bird.x and not p.score_counted:
                score += 1
                p.score_counted = True

        score_surface = score_font.render(str(score), True, (255, 255, 255))
        score_x = wirth/2 - score_surface.get_width()/2
        display_surface.blit(score_surface, (score_x, PipePair.PIECE_HEIGHT))
        print('Inside the while loop')

        pygame.display.flip()
        frame_clock += 1
    print('Game over! Score: %i' % score)

    pygame.quit()

if __name__ == "__main__":

    # If this module had been imported, __name__ would be 'flappybird'.
    # It was executed (e.g. by double-clicking the file), so call main.

    main()