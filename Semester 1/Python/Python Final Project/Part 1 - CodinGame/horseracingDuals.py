"""
This program, using a given number of strengths, identifies the two closest
strengths and shows their difference with an integer (≥ 0). ---> the minimum difference
"""

n = int(input())
horses = []

for i in range(n):
    pi = int(input())
    horses.append(pi)

horses.sort()
min_diff = None  # initialize into none

for i in range(0, n-1):  # iterates through all cases

    diff = int(abs(horses[i] - horses[i+1]))  # find difference

    if min_diff is None:
        min_diff = diff  # assigns if min_diff is empty
    elif diff < min_diff:
        min_diff = diff  # updates if diff is smaller than min_diff

print(min_diff)  # displays answer
