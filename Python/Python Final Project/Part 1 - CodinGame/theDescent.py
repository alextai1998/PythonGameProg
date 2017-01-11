"""
This program finds the highest mountain out of a list of mountains.

The while loop represents the game.
Each iteration represents a turn of the game
where you are given inputs (the heights of the mountains)
and where you have to print an output (the index of the mountain to fire on)
The inputs you are given are automatically updated according to your last actions.
"""

# game loop
while True:

    heights = []  # generates a list first

    for i in range(8):  # iterate through 8 indices
        mountain_h = int(input())  # represents the height of one mountain.
        heights.append(mountain_h)  # append the data inputted by the game into the list
        hello = list(enumerate(heights))  # creates a list with heights and the index
        newList = [(v, k) for k, v in hello]  # switch the index with the heights
        newList.sort()  # sort the new list
        shootList = [v for k, v in newList]  # remove the heights to generate a list of indices

    print(shootList[7])  # The index of the mountain to fire on.
