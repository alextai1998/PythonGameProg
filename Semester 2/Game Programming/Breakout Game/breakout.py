import pygame as pg
from pygame.locals import *
import sys
import random


class Breakout:
    def __init__(self):
        self.screen = pg.display.set_mode((800, 600))
        self.brick = []
        self.base = [[pg.Rect(300, 500, 20, 10), 120],
                     [pg.Rect(320, 500, 20, 10), 100],
                     [pg.Rect(340, 500, 20, 10), 80],
                     [pg.Rect(360, 500, 20, 10), 45]]
        self.ball = pg.Rect(300, 490, 10, 10)
        self.x_direction = -1
        self.y_direction = -1
        self.angle = 80
        self.speeds = {120: (-10, -3),
                       100: (-10, -8),
                       80: (10, -8),
                       45: (10, -3)}
        # --- Reverse the angles
        self.swap = {120: 45, 45: 120, 100: 80, 80: 100}

    def bricks(self):
        self.brick = []
        y = 60  # --- Position of starting y brick
        for i in range(200/20):
            x = 130  # --- Position of starting x brick
            for j in range(800/40-6):
                brick = pg.Rect(x, y, 25, 10)
                self.brick.append(brick)
                x += 40  # --- Width of brick
            y += 30  # --- Height of brick

    def ball_move(self):
        for i in range(2):
            speed = self.speeds[self.angle]
            movement = True
            if i:
                self.ball.x += speed[0] * self.x_direction
            else:
                self.ball.y += speed[1] * self.x_direction * self.y_direction
                movement = False
            if self.ball.x <= 0 or self.ball.x >= 800:
                self.angle = self.swap[self.angle]
                if self.ball.x <= 0:
                    self.ball.x = 1
                else:
                    self.ball.x = 799
            if self.ball.y <= 0:
                self.ball.y = 1
                self.y_direction *= -1

            # --- paddle-board reflection
            for base in self.base:
                if base[0].colliderect(self.ball):
                    self.angle = base[1]
                    self.x_direction = -1
                    self.y_direction = -1
                    break
            check = self.ball.collidelist(self.brick)

            if check != -1:
                brick = self.brick.pop(check)
                if movement:
                    self.x_direction *= -1
                self.y_direction *= -1
            if self.ball.y > 600:
                self.bricks()
                self.ball.x = self.base[1][0].x
                self.ball.y = 490
                self.y_direction = self.x_direction = -1

    def base_move(self):
        position = pg.mouse.get_pos()
        x = 0
        for p in self.base:
            p[0].x = position[0] + 20 * x
            x += 1

    def main(self):
        # --- The clock will be used to control how fast the screen updates
        clock = pg.time.Clock()

        self.bricks()

        # Loads start/end screens
        startscreen = pg.image.load('startscreen.jpg')

        # Initializes boolean variables
        standby = True
        start = True

        # --- Standby Mode
        while standby:
            # --- Display start screen
            self.screen.fill((0, 0, 0))
            self.screen.blit(startscreen, (0, 0))
            pg.display.flip()

            for event in pg.event.get():
                if event.type is MOUSEBUTTONDOWN:
                    standby = False
                elif event.type is QUIT:
                    pg.quit()
                    sys.exit()

        # --- Main game loop
        while start:
            # --- Window Caption
            pg.display.set_caption('Breakout!')

            # --- Limit to 60 frames per second
            clock.tick(60)

            for event in pg.event.get():
                if event.type == QUIT:
                    sys.exit()

            # --- Update positions of elements
            self.screen.fill((255, 255, 255))
            self.base_move()
            self.ball_move()

            # --- Drawing the bricks to break
            for brick in self.brick:
                pg.draw.rect(self.screen, (0, random.randint(120, 200), 0), brick)

            # --- Drawing the base to reflect
            for base in self.base:
                pg.draw.rect(self.screen, (220, 20, 60), base[0])

            # --- Drawing the ball to break with
            pg.draw.rect(self.screen, (0, 0, 0), self.ball)

            # --- Update the screen
            pg.display.flip()


# --- Run program
if __name__ == "__main__":
    Breakout().main()
