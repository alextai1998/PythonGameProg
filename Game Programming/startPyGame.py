import pygame as pg
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
    (a, b, c) = wormColor
    for i, c in enumerate(wormCoor):
        x = c['x'] * cellSize
        y = c['y'] * cellSize
        wormSegmentRect = pg.Rect(x, y, cellSize, cellSize)
        color = wormColor
        if i == 0:
            color = (155, 0, 0)
        elif i == 1:
            color = (190, 0, 00)
        pg.draw.rect(win, color, wormSegmentRect)


while True:  # main game loop
    for event in pg.event.get():
        if event.type is QUIT:
            pg.quit()
            sys.exit()

    if 'x' == 19 and direction is 'right':
        direction = 'down'
    elif 'x' == 0 and direction is 'left':
        direction = 'up'
    elif 'y' == 14 and direction is 'down':
        direction = 'left'
    elif 'y' == 0 and direction is 'up':
        direction = 'right'

    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT] and direction is not 'right':
        direction = 'left'
    if keys[pg.K_RIGHT] and direction is not 'left':
        direction = 'right'
    if keys[pg.K_UP] and direction is not 'down':
        direction = 'up'
    if keys[pg.K_DOWN] and direction is not 'up':
        direction = 'down'

    # Constraints
    if direction is 'right' and wormCoords[0]['x'] == winSize[0]/cellSize - 1:
        direction = 'down'
    if direction is 'down' and wormCoords[0]['y'] == winSize[1]/cellSize - 1:
        direction = 'left'
    if direction is 'up' and wormCoords[0]['y'] == 0:
        direction = 'right'
    if direction is 'left' and wormCoords[0]['x'] == 0:
        direction = 'up'

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
    drawWorm(window, wormCoords, cellSize, (225, 0, 0))

    # --- Go ahead and update the screen with what we've drawn.
    pg.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(10)
