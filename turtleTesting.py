import turtle

# Creates window
myWin = turtle.Screen()

# Creates a turtle
at = turtle.Turtle()


def drawSquare(sqrlen, turtle):
    """
    This function draws a square with turtle
    :param sqrlen: length of square
    :param turtle: the turtle itself
    :return:
    """
    if sqrlen < 5:
        return
    else:
        for i in range(4):
            turtle.forward(sqrlen)
            turtle.left(90)
        turtle.up()
        turtle.fd(5)
        turtle.left(90)
        turtle.fd(5)
        turtle.left(-90)
        turtle.down()
        drawSquare(sqrlen-10, turtle)

# drawSquare(100, at)

at.left(90)
at.fd(100)
at.left(45)
at.fd(50)
at.back(50)
at.right(90)
at.fd(50)
at.fd(50)
at.left(45)
at.fd(50)
at.back(50)
at.right(90)
at.fd(50)
at.fd(50)
at.left(45)
at.fd(50)
at.back(50)
at.right(90)
at.fd(50)
at.fd(50)
at.left(45)
at.fd(50)
at.back(50)
at.right(90)
at.fd(50)
at.fd(50)
at.left(45)
at.fd(50)
at.back(50)
at.right(90)
at.fd(50)

# Close window with a click on the screen
myWin.exitonclick()
