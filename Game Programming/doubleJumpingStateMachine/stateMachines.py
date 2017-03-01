import pygame as pg
import sys

from pygame.locals import *

# initialize the pygame library
pg.init()
# sets the size of the window
winSize = (800, 700)
window = pg.display.set_mode(winSize)
# title
pg.display.set_caption('State Machines')
# The clock will be used to control how fast the screen updates
clock = pg.time.Clock()

#read images
walkLink = pg.image.load('waitlink.png')
jumpLink = pg.image.load('jumplink.jpg')
duckLink = pg.image.load('ducklink.jpg')
surfaceWait = pg.transform.scale(walkLink, (160, 200))
surfaceJump = pg.transform.scale(jumpLink, (160, 200))
surfaceDuck = pg.transform.scale(duckLink, (200, 200))
groundLevel = int(winSize[1]/2)

link = {'wait': surfaceWait,
        'jump': surfaceJump,
        'doubleJump': surfaceJump,
        'duck': surfaceDuck,
        'pos_x': int(winSize[0]/2),
        'pos_y': groundLevel,
        }
state = {'state': 'wait'}
jump = 100
gravity = 10

while True:  # main game loop
    for event in pg.event.get():
        if event.type is QUIT:
            pg.quit()
            sys.exit()
    keys = pg.key.get_pressed()

    window.fill((255, 255, 255))

    if state['state'] is 'wait':
        # -- output here
        jumpCount = 0
        # -- Transition code here
        if keys[pg.K_UP]:
            state['state'] = 'jump'
            link['pos_y'] -= 100
        elif keys[pg.K_a]:
            state['state'] = 'duck'

    elif state['state'] is 'jump':
        # -- output here
        link['pos_y'] += gravity
        # -- Transition code here
        if link['pos_y'] > groundLevel:
            link['pos_y'] = groundLevel
            state['state'] = 'wait'
        elif keys[pg.K_UP]:
            state['state'] = 'doubleJump'
            link['pos_y'] -= jump

    elif state['state'] is 'duck':
        # -- output here
        # -- Transition code here
        if keys[pg.K_a]:
            state['state'] = 'duck'
        else:
            state['state'] = 'wait'

    elif state['state'] is 'doubleJump':
        # -- output here
        link['pos_y'] += gravity
        # -- Transition code here
        if link['pos_y'] > groundLevel:
            link['pos_y'] = groundLevel
            state['state'] = 'wait'


    link_rect = pg.Rect(link['pos_x'], link['pos_y'], 50, 50)
    image = state['state']
    window.blit(link[image], link_rect)
    # --- Go ahead and update the screen with what we've drawn.
    pg.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(10)
