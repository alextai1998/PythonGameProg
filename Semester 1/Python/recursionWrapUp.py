import turtle
import colorsys


###################Library##################


def drawcircle(x, y, radius, t):
    """
    :param x: The X coordinate of the initial position/starting point
    :param y: The Y coordinate of the initial position/starting point
    :param radius: The radius of the circle
    :param t: Turtle
    :return: None
    """
    moveturtle(x, y-radius)
    # pen color
    (r, g, b) = colorsys.hsv_to_rgb(float(radius) / 150, 1.0, 1.0)
    t.pencolor(r, g, b)
    # draw circle
    t.circle(radius)
    # return to the initial position
    moveturtle(x, y)
    # smaller circles
    if radius > 10:
        drawcircle(x-radius, y+radius, radius/2, t)
        drawcircle(x+radius, y-radius, radius/2, t)



def moveturtle(x, y):
    """
    This function sets the initial position/starting point of the turtle
    :param x: The X coordinate of the initial position/starting point
    :param y:The Y coordinate of the initial position/starting point
    :return: None
    """

    t.up()
    t.setposition(x, y)
    t.down()

    #######################################


t = turtle.Turtle()
t.pensize(2)
moveturtle(-50, 0)
myWin = turtle.Screen()
drawcircle(x=1, y=100, radius=90, t=t)
myWin.exitonclick()
