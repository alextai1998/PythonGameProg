import pygame as pg
import sys
import random
import math

from pygame.locals import *

# --- Initialize the pygame library
pg.init()
# --- Set the size of the window
winSize = (1000, 875)
window = pg.display.set_mode(winSize)
# --- Title
pg.display.set_caption('Physics Machine')
# --- The clock will be used to control how fast the screen updates
clock = pg.time.Clock()


def draw_circles(particles):
    """
    Draws a circle with random size and position
    :return:
    """
    color = particles['color']
    size = particles['size']
    thickness = particles['thickness']
    x = particles['x']
    y = particles['y']
    pg.draw.circle(window, color, (int(x), int(y)), size, thickness)


def particle(x=10, y=10, size=15, color=(175,238,238), thickness=2, speed=0.5, angle=math.pi/2):
    """
    Creates a particle
    :param x:
    :param y:
    :param size:
    :param color:
    :param thickness:
    :param speed:
    :param angle:
    :return: dictionary
    """
    return {'x': x, 'y': y, 'size': size, 'color': color, 'thickness': thickness, 'speed': speed, 'angle': angle}


def new_particles(n=50):
    particles_list = []
    for i in range(n):
        size = random.randint(10, 60)
        x = random.randint(size, winSize[0] - size)
        y = random.randint(size, winSize[1] - size)
        speed = random.random()
        angle = random.uniform(0, math.pi*2)
        clr = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        particles_list.append(particle(x=x,
                                       y=y,
                                       size=size,
                                       speed=speed,
                                       angle=angle,
                                       color=clr))

    return particles_list


def add_vectors(vector1, vector2):
    """
    Function t add two vectors
    :param vector1: tuple (angle, mag)
    :param vector2: tuple (angle, mag)
    :return: vectors: tuple (angle, mag)
    """
    angle1, mag1 = vector1
    angle2, mag2 = vector2
    x = math.sin(angle1) * mag1 + math.sin(angle2) * mag2
    y = math.cos(angle1) * mag1 + math.cos(angle2) * mag2
    mag = math.hypot(x, y)  # --- Hypotenuse
    angle = 0.5 * math.pi - math.atan2(y, x)

    return angle, mag


def move(particle):
    """
    Move a particle by the speed and angle provided
    :param particle:
    :return:
    """
    angle = particle['angle']
    speed = particle['speed']

    particle['x'] += math.sin(angle) * speed
    particle['y'] -= math.sin(angle) * speed

    return particle


def bounce(particle):
    x = particle['x']
    y = particle['y']
    size = particle['size']
    angle = particle['angle']
    width = winSize[0]
    height = winSize[1]

    if x > width - size:  # --- Right wall reflection
        x = 2*(width - size) - x
        angle = -angle
    elif x < size:  # --- Left wall reflection
        x = 2*size - x
        angle = -angle

    if y > height - size:  # --- Upper wall reflection
        y = 2*(height - size) - y
        angle = math.pi - angle
    elif y < size:  # --- Lower wall reflection
        y = 2*size - y
        angle = math.pi - angle

    particle['x'] = x
    particle['y'] = y
    particle['angle'] = angle

    return particle


particles = new_particles(n=30)

while True: # --- Main game loop
    for event in pg.event.get():
        if event.type is QUIT:
            pg.quit()
            sys.exit()

    # --- Draw sprites
    window.fill((255, 255, 255))

    # --- For each particle
    for i in range(len(particles)):
        p = bounce(move(particles[i]))
        draw_circles(p)
        # --- Update after moving
        particles[i] = p

    # --- Go ahead and update the screen with what we've drawn.
    pg.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(50)
