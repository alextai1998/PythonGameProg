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


def drawY(branch, len, tur):
    if branch == 1:
        return
    else:
        tur.fd(len)
        tur.right(20)
        drawY(branch-1, len-10, tur)
        tur.left(40)
        drawY(branch-1, len-10, tur)
        tur.right(20)
        tur.back(len)

at.left(90)
at.fd(100)
drawY(7, 80, at)


# Close window with a click on the screen
myWin.exitonclick()
