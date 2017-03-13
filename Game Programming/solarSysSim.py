import pygame as pg
import random
import math

# --- Definition of config variables
background_color = (0, 0, 0)
(width, height) = (400, 400)


class SolarSys:
    """
        Creates a particle object
    """
    num_particles = 0

    def __init__(self, x, y, size, color=(255, 255, 255), angle=math.pi/2, speed=1.0, mass=1.0):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.thickness = 0
        self.speed = speed
        self.angle = angle  # --- Going rightwards by default
        self.mass = mass  # mass of object
        SolarSys.num_particles += 1

    def attract(self, other):
        """
            gravitational force
        :param other: another particle to attract
        :return:
        """
        dx = (self.x-other.x)
        dy = (self.y-other.y)
        distance = math.hypot(dx, dy)
        force = 0.2*self.mass * other.mass / (distance ** 2)

        # --- Check for collision
        if distance < self.size + other.size:
            return True

        # --- Angle
        angle = math.atan2(dx, dy)

        # --- We use Newton's Law
        self.accelerate(angle + math.pi/2, force/self.mass)
        other.accelerate(angle - math.pi/2, force/other.mass)

    def accelerate(self, angle, speed):
        """
            accelerates the article by the given angle and speed
        :param angle:
        :param speed:
        :return:
        """
        self.angle, self.speed = add_vectors(self.angle, self.speed, angle, speed)

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
            self.angle = -math.pi - self.angle

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


def collide(p1, p2):
    """
        Combines two colliding particles into one bigger particle
    :param pi:
    :param p2:
    :return:
    """
    total_mass = p1.mass + p2.mass
    total_size = p1.size + p2.size

    # --- Position of the newly combined particle
    p1.x = (p1.x * p1.mass + p2.x * p2.mass) / total_mass
    p1.y = (p1.y * p1.mass + p2.y * p2.mass) / total_mass

    # ---
    (angle, speed) = add_vectors(p1.angle,
                                 p1.speed * p1.mass / total_mass,
                                 p2.angle,
                                 p2.speed * p2.mass / total_mass)
    p1.speed = speed
    p1.angle = angle
    p1.mass = total_mass
    p1.size = total_size
    p1.collided_with = p2


def calculate_size(mass):
    """
        Calcuclates the size of the particle given its mass
    :param mass:
    :return:
    """
    return 0.5 * mass ** 0.5

screen = pg.display.set_mode((width, height))
pg.display.set_caption('Particle simulator with OOP')

# --- number of particles
num_particles = 100
min_mass = 1
max_mass = 5
# --- list to store particles
set_particles = list()
# --- The clock will be used to control how fast the screen updates
clock = pg.time.Clock()

for i in range(num_particles):
    mass = min_mass + 0.5 * max_mass * random.random()
    # --- Calculate size
    size = int(calculate_size(mass))

    x = random.randint(size, width-size)
    y = random.randint(size, height-size)
    angle = random.uniform(0, math.pi * 2)

    set_particles.append(SolarSys(x=x,
                                  y=y,
                                  size=size,
                                  angle=angle,
                                  speed=0.0,
                                  mass=mass,
                                  color=(255,255,255))
                         )

running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill(background_color)

    particles_to_remove = []
    for i, p1 in enumerate(set_particles):

        for p2 in set_particles[i+1:]:
            if p1.attract(p2):
                collide(p1, p2)

        if p1.size > 5:
            # --- Yellow for sun
            p1.color = (255, 255, 0)

        if 'collided_with' in p1.__dict__:
            particles_to_remove.append(p1.collided_with)
            p1.size = calculate_size(p1.mass)
            del p1.__dict__['collided_with']

        p1.experience_drag(drag=0.5)
        p1.move()
        p1.draw(screen)

        for p in particles_to_remove:
            if p in set_particles:
                set_particles.remove(p)

    pg.display.flip()
    clock.tick(10)
