"""
This program allows Thor to reach the coordinates of the light of power in a 2D field.

light_x: the X position of the light of power
light_y: the Y position of the light of power
initial_tx: Thor's starting X position
initial_ty: Thor's starting Y position
"""

light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

# Uses currentX and currentY to update every loop
currentX = initial_tx
currentY = initial_ty

# game loop
while True:
    NSDirection = ""
    EWDirection = ""

    remaining_turns = int(input())  # The remaining amount of turns Thor can move.

    if light_y > currentY:
        NSDirection += "S"
        currentY += 1
    elif light_y < currentY:
        NSDirection += "N"
        currentY -= 1
    if light_x > currentX:
        EWDirection += "E"
        currentX += 1
    elif light_x < currentX:
        EWDirection += "W"
        currentX -= 1

    print(NSDirection + EWDirection)  # A single line providing the move to be made: N NE E SE S SW W or NW
