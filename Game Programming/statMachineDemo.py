import pygame as pg, gameLib as gl
import sys
from pygame.locals import *

# Initialize the pygame library
pg.init()
# Sets the size of the window
winSize = (800, 700)
window = pg.display.set_mode(winSize)
# Title
pg.display.set_caption("State Machine")
# The clock will be used to control how fast the screen updates
clock = pg.time.Clock()

# -- read game images: sprites--
waitingLink = pg.image.load('waitlink.png')
jumpingLink = pg.image.load('jumplink.png')

# -- dictionary for character
character = {'name': 'link',
             'life': 100,
             'walk_sprite': waitingLink,
             'pos_x': 100,
             'pos_y': 100}

while True:

    ch = gl.getkey()
    print(ch + ' pressed')
    if ord(ch) is 27:
        pg.quit()
        sys.exit()

    window.fill((255, 255, 255))
    chr_rect = pg.Rect(character['pos_x'], character['pos_y'], 50, 50)
    # -- replace rect by image
    window.blit(character['walk_sprite'], chr_rect)

    # -- Go ahead and update screen
    pg.display.flip()

    # -- Limit to 60 frames per second
    clock.tick(10)
