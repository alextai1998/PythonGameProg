import pygame as pg
import random
import math

# --- Definition of config variables
background_color = (255, 255, 255)
(width, height) = (1000, 400)


class Particle:
    """
        Creates a particle object
    """
    num_particles = 0

    def __init__(self, x, y, size, angle=math.pi/2, speed=1.0):
        self.x = x
        self.y = y
        self.size = size
        self.color = (0, 55, 150)
        self.thickness = 1
        self.speed = speed
        self.angle = angle  # --- Going rightwards by default
        Particle.num_particles += 1

    def draw(self, screen):
        """
            Draws the particle on the screen
        :return: none
        """
        pg.draw.circle(screen,
                       self.color,
                       (int(self.x), int(self.y)),
                       self.size,
                       self.thickness
                       )

    def move(self):
        """
            Move the particle given the angle and speed
        :return: none
        """
        self.x += math.sin(self.angle) * self.speed
        self.y -= math.cos(self.angle) * self.speed

    def bounce(self, height, width):
        """
            Check for particles approaching the walls and bounce off them
        :return: none
        """

        if self.x > width - self.size:  # --- Right wall reflection
            self.x = 2 * (width - self.size) - self.x
            self.angle = -self.angle

        elif self.x < self.size:  # --- Left wall reflection
            self.x = 2 * self.size - self.x
            self.angle = -self.angle

        if self.y > height - self.size:  # --- Upper wall reflection
            self.y = 2 * (height - self.size) - self.y
            self.angle = math.pi - self.angle
        elif self.y < self.size:  # --- Lower wall reflection
            self.y = 2 * self.size - self.y
            self.angle = math.pi - self.angle

    def add_gravity(self, gravity):
        angle, speed = gravity
        self.angle, self.speed = add_vectors(self.angle, self.speed, angle, speed)

    def experience_drag(self, drag=0.9):
        self.speed *= drag


def add_vectors(angle1, length1, angle2, length2):
    """ Returns the sum of two vectors """

    x = math.sin(angle1) * length1 + math.sin(angle2) * length2
    y = math.cos(angle1) * length1 + math.sin(angle2) * length2

    angle = 0.5 * math.pi-math.atan2(y, x)
    length = math.hypot(x, y)
    return angle, length

screen = pg.display.set_mode((width, height))
pg.display.set_caption('Particle simulator with OOP')

# --- number of particles
num_particles = 100
min_size = 5
max_size = 10
gravity = (math.pi, 0.5)
# --- list to store particles
set_particles = list()

for i in range(num_particles):
    size = random.randint(min_size, max_size)
    x = random.randint(size, width-size)
    y = random.randint(size, height-size)
    angle = random.uniform(0, math.pi * 2)

    set_particles.append(Particle(x=x,
                                  y=y,
                                  size=size,
                                  angle=angle)
                         )

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill(background_color)

    # --- draw the particles
    for par in set_particles:
        par.add_gravity(gravity)
        par.experience_drag(drag=0.9999)
        par.move()
        par.bounce(height, width)
        par.draw(screen)

    pg.display.flip()
