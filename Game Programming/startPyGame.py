import pygame as pg, gameLib as gl
import sys
from pygame.locals import *

# initialize the pygame library
pg.init()
# sets the size of the window
winSize = (400, 300)
window = pg.display.set_mode(winSize)
cellSize = 20
# title
pg.display.set_caption('My first game')
# The clock will be used to control how fast the screen updates
clock = pg.time.Clock()
# Set start point.
wormCoords = [{'x': 5, 'y': 5},
              {'x': 5, 'y': 4},
              {'x': 5, 'y': 3}]

direction = 'right'


def drawGrid(win, winSize, cellSize, color):
    """
    Draws the grid for the game
    :param win: identifier of the window
    :param winSize: winSize (width,height)
    :param cellSize:
    :param color:
    """
    for x in range(0, winSize[0], cellSize):  # draw vertical lines
        pg.draw.line(win, color, (x, 0), (x, winSize[1]))
    for y in range(0, winSize[1], cellSize):  # draw horizontal lines
        pg.draw.line(win, color, (winSize[0], y), (0, y))


def drawWorm(win, wormCoor, cellSize, wormColor):
    for c in wormCoor:
        x = c['x'] * cellSize
        y = c['y'] * cellSize
        wormSegmentRect = pg.Rect(x, y, cellSize, cellSize)
        pg.draw.rect(win, wormColor, wormSegmentRect)


while True:  # main game loop

    ch = gl.getkey()
    if ord(ch) is 27:
        pg.quit()
        sys.exit()


    for event in pg.event.get():
        if event.type is QUIT:
            pg.quit()
            sys.exit()

    if ch == 'a':
        direction = 'left'
    if ch == 'd':
        direction = 'right'
    if ch == 'w':
        direction = 'up'
    if ch == 's':
        direction = 'down'

    if direction is 'up':
        newHead = {'x': wormCoords[0]['x'], 'y': wormCoords[0]['y'] - 1}
    elif direction is 'down':
        newHead = {'x': wormCoords[0]['x'], 'y': wormCoords[0]['y'] + 1}
    elif direction is 'left':
        newHead = {'x': wormCoords[0]['x'] - 1, 'y': wormCoords[0]['y']}
    else:
        newHead = {'x': wormCoords[0]['x'] + 1, 'y': wormCoords[0]['y']}

    wormCoords.insert(0, newHead)

    del wormCoords[-1]  # remove worm's tail segment

    window.fill((255, 255, 255))
    drawGrid(window, winSize, cellSize, (40, 40, 40))
    drawWorm(window, wormCoords, cellSize, (0, 155, 0))

    # --- Go ahead and update the screen with what we've drawn.
    pg.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(10)
