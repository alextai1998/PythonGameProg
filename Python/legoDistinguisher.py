import math as m
import numpy as np
import matplotlib.pyplot as plt


def dbeams(x, y):
    dx = x - 7
    dy = y - 4
    ans = dx**2 + dy**2
    result = m.sqrt(ans)
    return result


def dbrick(x, y):
    dx = x - 3
    dy = y - 5
    ans = dx**2 + dy**2
    result = m.sqrt(ans)
    return result

# Variable initialization
beamCounter = 0
brickCounter = 0

legos = np.loadtxt('Legos.txt', delimiter=',')  # Importing the text file that contains the points.

for x, y in legos:  # Steps through the pairs of points
    if dbeams(x, y) < dbrick(x, y):  # Compares the distance
        beamCounter += 1
        plt.scatter(x, y, color='blue')
    else:
        brickCounter += 1
        plt.scatter(x, y, color='red')

plt.scatter(7, 4, color='yellow')  # Prints the most representative brick/beam
plt.scatter(3, 5, color='black')  # Prints the most representative brick/beam

print("Number of beams: %r" % beamCounter)
print("Number of bricks: %r" % brickCounter)

plt.show()  # Shows the scatter plot
