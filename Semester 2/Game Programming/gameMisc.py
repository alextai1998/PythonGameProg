# Import the pygame library and initialise the game engine
import pygame
pygame.init()


def grid(window, color, cellSize, winSize):
    """
    This function will draw out lines to form a grid
    :param window: Surface (pygame.display.set_mode(size))
    :param color: Color (INT, INT, INT)
    :param sizeCell: Int, size of the cells
    :return: None
    """
    # Horizontal Lines
    for y in range(winSize[0]):
        pygame.draw.line(window, color, (0, 0 + y*cellSize), (700, 0 + y*cellSize))

    # Vertical Lines
    for x in range(winSize[1]):
        pygame.draw.line(window, color, (0 + x*cellSize, 0), (0+x*cellSize, 500))


def snake(window, snakeCoord, cellSize, snakeColor):
    pygame.draw.rect(screen, red, (snakeCoords[0]["x"]*cellSize, snakeCoords[0]["y"]*cellSize, 19, 19), 0)


# Open a new window
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My First Game")

black = (0, 0, 0)
red = (255, 0, 0)
cellSize = 20


# The loop will carry on until the user exit the game
carryOn = True


# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

direction = "right"
snakeCoords = [{"x": 5, "y": 5},
               {"x": 5, "y": 4},
               {"x": 5, "y": 3}]



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
        direction = "left"
    if keys[pygame.K_RIGHT]:
        direction = "right"
    if keys[pygame.K_UP]:
        direction = "up"
    if keys[pygame.K_DOWN]:
        direction = "down"

    if direction is "up":
        newHead = {"x": snakeCoords[0]["x"], "y": snakeCoords[0]["y"] - 1}
    elif direction is "down":
        newHead = {"x": snakeCoords[0]["x"], "y": snakeCoords[0]["y"] + 1}
    elif direction is "left":
        newHead = {"x": snakeCoords[0]["x"] - 1, "y": snakeCoords[0]["y"]}
    else:
        newHead = {"x": snakeCoords[0]["x"] + 1, "y": snakeCoords[0]["y"]}

    snakeCoords.insert(0, newHead)
    del snakeCoords[-1]

    # ---Game logic should go here---

    # ---Drawing code should go here---
    # First, clear the screen to WHITE.
    screen.fill((255, 255, 255))
    grid(screen, black, cellSize, size)
    snake(screen, snakeCoords, cellSize, (0, 155, 0))

    # Update the screen
    pygame.display.flip()

    # Limit to 60 frames per second
    clock.tick(2)


# Once we have exited the game loop we can stop the game engine:
pygame.quit()
