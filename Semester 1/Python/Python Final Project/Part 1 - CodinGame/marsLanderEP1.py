"""
This program safely lands the "Mars Lander" shuttle, the landing ship which contains the Opportunity rover.
Mars Lander is guided by a program, and right now the failure rate for landing on the NASA simulator is unacceptable.
"""

surface_n = int(input())  # the number of points used to draw the surface of Mars.

for i in range(surface_n):
    # land_x: X coordinate of a surface point. (0 to 6999)
    # land_y: Y coordinate of a surface point. By linking all the points together
    # in a sequential fashion, you form the surface of Mars.
    land_x, land_y = [int(j) for j in input().split()]

# game loop
while True:
    # h_speed: the horizontal speed (in m/s), can be negative.
    # v_speed: the vertical speed (in m/s), can be negative.
    # fuel: the quantity of remaining fuel in liters.
    # rotate: the rotation angle in degrees (-90 to 90).
    # power: the thrust power (0 to 4).
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]

    if v_speed <= -40:  # simple condition
        print("0 4")  # increase speed
    else:
        print("0 0")  # decrease speed
