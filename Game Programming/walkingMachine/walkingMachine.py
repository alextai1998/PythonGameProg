import pygame as pg
import sys

from pygame.locals import *

# --- Initialize the pygame library
pg.init()
# --- Set the size of the window
winSize = (800, 700)
window = pg.display.set_mode(winSize)
# --- Title
pg.display.set_caption('myExplorer')
# --- The clock will be used to control how fast the screen updates
clock = pg.time.Clock()

# --- Load images
wait = pg.image.load('wait.png')
downwalk1 = pg.image.load('down_walk_1.png')
downwalk2 = pg.image.load('down_walk_2.png')
upwalk1 = pg.image.load('up_walk_1.png')
upwalk2 = pg.image.load('up_walk_2.png')
rightwalk1 = pg.image.load('right_walk_1.png')
rightwalk2 = pg.image.load('right_walk_2.png')
leftwalk1 = pg.image.load('left_walk_1.png')
leftwalk2 = pg.image.load('left_walk_2.png')

# --- Scale the images
scaleWait = pg.transform.scale(wait, (99, 157))
scaleDWalk1 = pg.transform.scale(downwalk1, (99, 157))
scaleDWalk2 = pg.transform.scale(downwalk2, (99, 157))
scaleUWalk1 = pg.transform.scale(upwalk1, (99, 157))
scaleUWalk2 = pg.transform.scale(upwalk2, (99, 157))
scaleRWalk1 = pg.transform.scale(rightwalk1, (99, 157))
scaleRWalk2 = pg.transform.scale(rightwalk2, (99, 157))
scaleLWalk1 = pg.transform.scale(leftwalk1, (99, 157))
scaleLWalk2 = pg.transform.scale(leftwalk2, (99, 157))

# --- Dictionary for the character
felix = {
    'pos_y': int(winSize[1]/2),
    'pos_x': int(winSize[0]/2),
    'wait': scaleWait,
    'downwalk1': scaleDWalk1,
    'downwalk2': scaleDWalk2,
    'upwalk1': scaleUWalk1,
    'upwalk2': scaleUWalk2,
    'rightwalk1': scaleRWalk1,
    'rightwalk2': scaleRWalk2,
    'leftwalk1': scaleLWalk1,
    'leftwalk2': scaleLWalk2,
}

# --- Dictionary for the state machine
state = {'state': 'wait', 'param': {}, 'image': 'wait'}
walk = 10


# --- Game Loop
while True:
    for event in pg.event.get():
        if event.type is QUIT:
            pg.quit()
            sys.exit()
    keys = pg.key.get_pressed()

    window.fill((255, 255, 255))

    if state['state'] is 'wait':
        # --- Output ---
        state['image'] = 'wait'
        # --- Transition ---
        if keys[pg.K_DOWN]:
            state['state'] = 'dwalk'
            state['param'] = {'time': 0}
        elif keys[pg.K_UP]:
            state['state'] = 'uwalk'
            state['param'] = {'time': 0}
        elif keys[pg.K_RIGHT]:
            state['state'] = 'rwalk'
            state['param'] = {'time': 0}
        elif keys[pg.K_LEFT]:
            state['state'] = 'lwalk'
            state['param'] = {'time': 0}

    elif state['state'] is 'dwalk':
        # --- Output ---
        t = state['param']['time']
        n = t % 2 + 1
        state['image'] = 'downwalk' + str(n)
        felix['pos_y'] += walk
        # --- Transition ---
        if keys[pg.K_DOWN]:
            state['param']['time'] += 1
        else:
            state['state'] = 'wait'

    elif state['state'] is 'uwalk':
        # --- Output ---
        t = state['param']['time']
        n = t % 2 + 1
        state['image'] = 'upwalk' + str(n)
        felix['pos_y'] -= walk
        # --- Transition ---
        if keys[pg.K_UP]:
            state['param']['time'] += 1
        else:
            state['state'] = 'wait'

    elif state['state'] is 'rwalk':
        # --- Output ---
        t = state['param']['time']
        n = t % 2 + 1
        state['image'] = 'rightwalk' + str(n)
        felix['pos_x'] += walk
        # --- Transition ---
        if keys[pg.K_RIGHT]:
            state['param']['time'] += 1
        else:
            state['state'] = 'wait'

    elif state['state'] is 'lwalk':
        # --- Output ---
        t = state['param']['time']
        n = t % 2 + 1
        state['image'] = 'leftwalk' + str(n)
        felix['pos_x'] -= walk
        # --- Transition ---
        if keys[pg.K_LEFT]:
            state['state'] = 'lwalk'
            state['param']['time'] += 1
        else:
            state['state'] = 'wait'

    # --- Redrawing the character
    felix_rect = pg.Rect(felix['pos_x'], felix['pos_y'], 50, 50)
    image = state['image']
    window.blit(felix[image], felix_rect)

    # --- Go ahead and update the screen with what we've drawn.
    pg.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(10)
