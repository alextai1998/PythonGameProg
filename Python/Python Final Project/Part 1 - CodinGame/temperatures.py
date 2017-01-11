"""
This program prints the temperature closest to 0 among input data. If two numbers are equally close to zero, positive
integer has to be considered closest to zero (for instance, if the temperatures are -5 and 5, then display 5).
"""

import sys

n = int(input())  # the number of temperatures to analyse
temps = input()  # the n temperatures expressed as integers ranging from -273 to 5526

temps = temps.split()  # splitting temps into a list
smallestTemp = 5526  # set benchmark as highest

if n == 0:
    smallestTemp = 0  # if there are no temperatures to analyze then display zer0
else:
    for i in temps:  # if there ARE temperatures to analyze then run through all of them
        if abs(int(i)) == abs(smallestTemp):
            if int(i) > smallestTemp:
                smallestTemp = int(i)  # update answer if applies
        elif abs(int(i)) < abs(smallestTemp):
            smallestTemp = int(i)  # update answer if applies

print(temps, file=sys.stderr)  # debugging

print(smallestTemp)  # display answer
