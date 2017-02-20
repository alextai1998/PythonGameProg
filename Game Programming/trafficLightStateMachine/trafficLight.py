import pygame as pg
import sys
from pygame.locals import *
import random


red = pg.image.load('redLight.png')
green = pg.image.load('greenLight.png')
yellow = pg.image.load('yellowLight.png')
off = pg.image.load('offLight.png')


# --- Initializes the pygame library
pg.init()

# --- The clock will be used to control how fast the screen updates
clock = pg.time.Clock()

# --- Sets the size of the window
winSize = (400, 300)
window = pg.display.set_mode(winSize)

# --- Initializes boolean variables
standby = True
start = True

state = {'state': 'off', 'counter': 0}

while True:  # off screen
    for event in pg.event.get():
        if event.type is QUIT:
            pg.quit()
            sys.exit()
    keys = pg.key.get_pressed()
    if keys[pg.K_SPACE]:
        state['state'] = 'red' if state['state'] is 'off' else 'off'

    window.fill((255, 255, 255))
    window.blit(off, (0, 0))

    if state['state'] is 'red':
        window.blit(red, (0, 0))
        # --- Transition Logic
        state['counter'] += 1
        if state['counter'] > 10:
            state['state'] = 'green'
            state['counter'] = 0
    elif state['state'] is 'green':
        window.blit(green, (0, 0))
        # --- Transition Logic
        state['counter'] += 1
        if state['counter'] > 10:
            state['state'] = 'yellow'
            state['counter'] = 0
    elif state['state'] is 'yellow':
        window.blit(yellow, (0, 0))
        # --- Transition Logic
        state['counter'] += 1
        if state['counter'] > 10:
            state['state'] = 'red'
            state['counter'] = 0

    # --- Go ahead and update the screen with what we've drawn.
    pg.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(20)
