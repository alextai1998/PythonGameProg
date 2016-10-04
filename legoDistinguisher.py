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

beamCounter = 0
brickCounter = 0

legos = np.loadtxt('Legos.txt', delimiter=',')

for x, y in legos:
    if dbeams(x, y) < dbrick(x, y):
        beamCounter += 1
    else:
        brickCounter += 1

print(beamCounter)
print(brickCounter)

for x, y in legos:
    plt.scatter(x, y, color='gray')

plt.show()
