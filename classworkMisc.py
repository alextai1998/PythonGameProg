# def printPicnic(items, lwidth, rwidth):
#     """
#     Prints what to bring on a picnic.
#     :param items: dictionary
#     :param lwidth: int
#     :param rwidth: int
#     :return: None
#     """
#     print("PICNIC ITEMS".center(lwidth+rwidth, "-"))
#     for k, v in items.items():
#         print(k.ljust(lwidth, ".") + str(v).rjust(rwidth, "."))
#
#
# picnic = {"sandwiches": 4, "apples": 12, "cups": 4, "cookies": 8000}
# printPicnic(picnic, 12, 5)
# printPicnic(picnic, 20, 6)



# newList = []
# heights = [3,2,6,2,4,6,3]
# hello = list(enumerate(heights))
# print(hello)
# newList = [(v, k) for k,v in hello]
# print(newList)
# newList.sort()
# print(newList)
#
# shootList = [v for k,v in newList]
# print(shootList)




import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
# n = 6
# temps = ['42', '-5', '12', '21', '5', '24']
# smallestTemp = 5526

#
# if n == 0:
#     print(0)
# else:
#     for i in temps:
#         if abs(int(i)) == abs(smallestTemp):
#             smallestTemp = abs(int(i))
#         elif abs(int(i)) < abs(smallestTemp):
#             smallestTemp = int(i)
#
# print(temps)
#
# print(smallestTemp)
