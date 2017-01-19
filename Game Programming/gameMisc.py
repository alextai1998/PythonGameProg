# Import the pygame library and initialise the game engine
import pygame
pygame.init()


def grid(window, color, sizeCell):
    """
    This function will draw out lines to form a grid
    :param window: Surface (pygame.display.set_mode(size))
    :param color: Color (INT, INT, INT)
    :param sizeCell: Int, size of the cells
    :return: None
    """
    # Horizontal Lines
    for y in range(701):
        pygame.draw.line(window, color, (0, 0 + y*sizeCell), (700, 0 + y*sizeCell))

    # Vertical Lines
    for x in range(501):
        pygame.draw.line(window, color, (0 + x*sizeCell, 0), (0+x*sizeCell, 500))


def snake(start_x, start_y):
    pygame.draw.rect(screen, red, (start_x, start_y, 19, 19), 0)


# Open a new window
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My First Game")

black = (0, 0, 0)
red = (255, 0, 0)


# The loop will carry on until the user exit the game
carryOn = True


# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

x = 1
y = 1


# -------- Main Program Loop -----------
while carryOn:
    # Event loop
    for event in pygame.event.get():  # User did something, this function returns a list
        if event.type == pygame.QUIT:  # If user clicked close
            carryOn = False  # Flag that we are done so we exit
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:  # Pressing x Key will quit the game
                carryOn = False  # Flag that we are done so we exit

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= 20
    if keys[pygame.K_RIGHT]:
        x += 20
    if keys[pygame.K_UP]:
        y -= 20
    if keys[pygame.K_DOWN]:
        y += 20
    else:
        x += 20

    # ---Game logic should go here---

    # ---Drawing code should go here---
    # First, clear the screen to WHITE.
    screen.fill((255, 255, 255))
    grid(screen, black, 20)
    snake(x, y)

    # Update the screen
    pygame.display.flip()

    # Limit to 60 frames per second
    clock.tick(10)


# Once we have exited the game loop we can stop the game engine:
pygame.quit()
